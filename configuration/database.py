import mysql.connector

class DatabaseConnection :
    def __init__(self):
        self.connection = self.__create_database_connection()

    def __create_database_connection(self):
        host = "localhost"  # Ganti dengan host MySQL Anda
        user = "root"   # Ganti dengan username MySQL Anda
        password = "password_root"  # Ganti dengan password MySQL Anda
        database = "py_project"  # Ganti dengan nama database yang ingin Anda gunakan

        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if connection.is_connected():
                print("Berhasil terhubung ke MySQL Server")
        except mysql.connector.Error as err:
            print(f"Kesalahan: {err}")
        return connection

    def close_database_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Koneksi database ditutup")
