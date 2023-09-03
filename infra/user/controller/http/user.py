from infra.user.usecase.user import Usecase
from flask import Flask, request, request, jsonify
from domain.user import User

class Controller:
    def __init__(self, usecase: Usecase, app: Flask):
        self.usecase = usecase
        self.app = app

        # Menambahkan routing ke dalam kelas
        self.app.add_url_rule('/user/register', 'create_user', self.create_user, methods=['POST'])
        self.app.add_url_rule('/user/<string:user_id>', 'get_user', self.get_user, methods=['GET'])

    def create_user(self):
        # Ambil Input dari request
        try:
            data = request.get_json()
            if data is None:
                return jsonify({"error": "Invalid input"}), 400
            username = data["username"]
            email = data["email"]
            password = data["password"]
            user = User(username, email, password)
            isCreated = self.usecase.create(user)
            if isCreated == None :
                return jsonify({"error" : "Invalid input"}), 400
            if not isCreated :
                return jsonify({"error" : "data not created"}), 400
            return jsonify({"message" : "success register"}), 201
        except Exception as error :
            return jsonify({"error" : error}), 500



    def get_user(self, user_id):
        return jsonify({"user_id": user_id, "username": "example_user"})
