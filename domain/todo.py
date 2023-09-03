import uuid

class Todo:
    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.id = uuid.uuid4()

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_user_id(self):
        return self.user_id

    def get_id(self):
        return self.id

    def set_title(self, new_title):
        self.title = new_title

    def set_description(self, new_description):
        self.description = new_description

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}"
