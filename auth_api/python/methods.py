import hashlib
import jwt
import mysql.connector

# Constants
JWT_SECRET = "my2w7wjd7yXF64FIADfJxNs1oupTGAuW"


class Token:
    def generate_token(self, received_username, received_password):
        # Get record from the database
        database = mysql.connector.connect(
            host="bootcamp-tht.sre.wize.mx",
            database="bootcamp_tht",
            user="secret",
            password="noPow3r",
        )
        cursor = database.cursor()

        query = "select password, salt, role from users where username = %s"

        cursor.execute(query, (received_username,))

        for (password, salt, role) in cursor:
            print(f"{received_username=}, {password=}, {salt=}, {role=}")

        cursor.close()
        database.close()

        # Generate the salted and hashed password
        salted_password = received_password + salt
        print(f"{salted_password=}")

        hashed_salted_password = hashlib.sha512(salted_password.encode()).hexdigest()

        print(f"{hashed_salted_password=}")

        if password != hashed_salted_password:
            # If invalid credentials return null value
            return

        # %% If valid createndials create JWT
        encoded_jwt = jwt.encode({"role": role}, JWT_SECRET, algorithm="HS256")
        print(f"{encoded_jwt=}")

        return encoded_jwt


class Restricted:
    def access_data(self, authorization):
        try:
            jwt.decode(authorization, JWT_SECRET, algorithms=["HS256"])
        except jwt.InvalidSignatureError:
            return "Invalid JWT"
        return "You are under protected data"
