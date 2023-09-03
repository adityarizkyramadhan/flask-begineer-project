from configuration.database import DatabaseConnection
from domain.user import User

class Repo :
    def __init__(self, db :DatabaseConnection) :
        self.db = db

    def get(self, id) :
        try:
            cursor = self.db.cursor()
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (id,))
            result = cursor.fetchone()
            cursor.close()
            user = User(result[1], result[2], result[3])
            user.set_id(result[0])
            return user
        except Exception as err:
            print(err)
            return False

    def get_all(self) :
        try:
            cursor = self.db.cursor()
            query = "SELECT * FROM users"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            users = []
            for row in result:
                user = User(row[1], row[2], row[3])
                user.set_id(row[0])
                users.append(user)
            return users
        except Exception as err:
            print(err)
            return False

    def create(self, user) :
        try:
            cursor = self.db.cursor()
            query = "INSERT INTO users (id, username, email, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (user.get_id(), user.get_username(), user.get_email(), user.get_password()))
            self.db.commit()
            cursor.close()
            return True
        except Exception as err:
            print(err)
            return False

    def get_by_email(self, email) :
        try:
            cursor = self.db.cursor()
            query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()
            user = User(result[1], result[2], result[3])
            user.set_id(result[0])
            return user
        except Exception as err:
            print(err)
            return False
