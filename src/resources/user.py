import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class userRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username", type=str, required=True, help="this field can not be blank"
    )
    parser.add_argument(
        "password", type=str, required=True, help="password field can not be blank"
    )

    def post(self):
        data = userRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"message": "user:already exist"}, 400
        conn = sqlite3.connect("data.db")
        course = conn.cursor()
        create_user = "INSERT INTO users Values(NULL ,?,?)"
        course.execute(create_user, (data["username"], data["password"],))
        conn.commit()
        conn.close()
        return {"message": "user created successfully"}, 201
