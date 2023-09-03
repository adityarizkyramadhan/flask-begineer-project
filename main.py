from configuration.database import DatabaseConnection
from infra.user.repo.mysql.user import Repo
from domain.user import User

connection = DatabaseConnection()

# Make migration
# connection.connection.cursor().execute("CREATE TABLE users (id VARCHAR(255) PRIMARY KEY, username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")


repoUser = Repo(connection.connection)
