from flask import Flask
from flask_restx import Api, Resource, fields
from bson import ObjectId
from mongo_handler import client
from utils import is_valid_email

# initializing flask app
app = Flask(__name__)
api = Api(
    app,
    version="1.0",
    title="Users API",
    description="A CRUD API for a User Resource.",
)

ns = api.namespace("users", description="User operations")

# mongodb database and collection
db = client['users_db']
users_collection = db['users']

# user details model
user_model = api.model(
    "User",
    {
        "id": fields.String(readonly=True, description="The unique identifier of the user"),
        "name": fields.String(required=True, description="The name of the user"),
        "email": fields.String(required=True, description="The email address of the user"),
        "password": fields.String(required=True, description="The password of the user"),
    }
)


def abort_if_user_doesnt_exist(user_id):
    if not ObjectId.is_valid(user_id) or not users_collection.find_one({"_id": ObjectId(user_id)}):
        api.abort(404, "User {} doesn't exist".format(user_id))


# parser for request args
parser = api.parser()
parser.add_argument("name", type=str, required=True, help="The name of the user", location="form")
parser.add_argument("email", type=str, required=True, help="The email address of the user", location="form")
parser.add_argument("password", type=str, required=True, help="The password of the user", location="form")


# app routes
@ns.route("/<string:user_id>")
@api.doc(responses={404: "User not found"}, params={"user_id": "The unique identifier for the user"})
class User(Resource):
    """Show a single user item and lets you delete them"""

    @api.doc(description="user_id should be a valid MongoDB ObjectId")
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Fetch a given user"""
        abort_if_user_doesnt_exist(user_id)
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        user["id"] = str(user["_id"])
        del user["_id"]
        return user

    @api.doc(responses={204: "User deleted"})
    def delete(self, user_id):
        """Delete a given user"""
        abort_if_user_doesnt_exist(user_id)
        users_collection.delete_one({"_id": ObjectId(user_id)})
        return "", 204

    @api.doc(parser=parser)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Update a given user"""
        abort_if_user_doesnt_exist(user_id)
        args = parser.parse_args()
        if len(args['name']) == 0 or len(args['email']) == 0 or len(args['password']) == 0:
            api.abort(400, "Fields should not be empty")
        if not is_valid_email(args["email"]):
            api.abort(400, "Invalid email format")

        user = {
            "name": args["name"].strip(),
            "email": args["email"].strip(),
            "password": args["password"].strip(),
        }
        users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user})
        user["id"] = user_id
        return user


@ns.route("/")
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        users = users_collection.find()
        result = []
        for user in users:
            user["id"] = str(user["_id"])
            del user["_id"]
            result.append(user)
        return result

    @api.doc(parser=parser)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Create a user"""
        args = parser.parse_args()
        if len(args['name']) == 0 or len(args['email']) == 0 or len(args['password']) == 0:
            api.abort(400, "Fields should not be empty")
        if not is_valid_email(args["email"]):
            api.abort(400, "Invalid email format")

        user = {
            "name": args["name"].strip(),
            "email": args["email"].strip(),
            "password": args["password"].strip(),
        }
        result = users_collection.insert_one(user)
        user["id"] = str(result.inserted_id)
        return user, 201


# main method
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
