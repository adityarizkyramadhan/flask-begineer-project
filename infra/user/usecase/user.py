from infra.user.repo.mysql.user import Repo
from domain.user import User
import utils.util as util

class Usecase :
    def __init__(self, repository: Repo):
        self.repository = repository

    def get(self, id):
        if not util.is_valid_uuid(id):
            return False
        return self.repository.get(id)

    def get_all(self):
        return self.repository.get_all()

    def create(self, user : User):
        if not user.validate_not_empty():
            return None
        user.set_uuid()
        user.change_password(util.hash_password(user.get_password()))
        return self.repository.create(user)

    def login(self, email, password):
        user = self.repository.get_by_email(email)
        if user :
            if util.compare_password(password, user.get_password()) :
                return user
        return False
