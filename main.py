from configuration.database import DatabaseConnection
from infra.user.repo.mysql.user import Repo as RepoUser
from infra.user.usecase.user import Usecase as UsecaseUser
from infra.user.controller.http.user import Controller as ControllerUser
from domain.user import User
from flask import Flask, request, request, jsonify
import json

connection = DatabaseConnection()

# Make migration
# connection.connection.cursor().execute("CREATE TABLE users (id VARCHAR(255) PRIMARY KEY, username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")

app = Flask(__name__)


repoUser = RepoUser(connection.connection)
usecaseUser = UsecaseUser(repoUser)
controllerUser = ControllerUser(usecaseUser, app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

