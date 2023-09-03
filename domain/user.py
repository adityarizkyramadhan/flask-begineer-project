import uuid

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


    def get_username(self):
        return self.username


    def set_uuid(self):
        self.id = uuid.uuid4()

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id.__str__()

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_email(self, new_email):
        self.email = new_email

    def change_password(self, new_password):
        self.password = new_password

    def validate_not_empty(self) -> bool:
        return self.username != "" and self.email != "" and self.password != ""

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"

