class Repo :
    def __init__(self, db) :
        self.db = db

    def get(self, id) :
        try:
            cursor = self.db.cursor()
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (id,))
            result = cursor.fetchone()
            cursor.close()
            return result
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
            return result
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

