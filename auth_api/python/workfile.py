#%% [markdown]
# Workfile

#%% Imports
import hashlib
from jwt.exceptions import InvalidSignatureError
import mysql.connector
import jwt
from pprint import pprint

#%% Connect to the database
database = mysql.connector.connect(
    host="bootcamp-tht.sre.wize.mx",
    database="bootcamp_tht",
    user="secret",
    password="noPow3r",
)
cursor = database.cursor()

query = "select * from users where username = %s"

received_username = "noadmin"

cursor.execute(query, (received_username,))

for (username, password, salt, role) in cursor:
    print(f"{username=}, {password=}, {salt=}, {role=}")

cursor.close()
database.close()

# %% Calculate hashed and salted password
received_username = "noadmin"
received_password = "noPow3r"

salted_password = received_password + salt
print(f"{salted_password=}")

hashed_salted_password = hashlib.sha512(salted_password.encode()).hexdigest()

print(f"{hashed_salted_password=}")

print("Valid" if password == hashed_salted_password else "invalid")

# %% Create JWT
jwt_secret = "my2w7wjd7yXF64FIADfJxNs1oupTGAuW"

encoded_jwt = jwt.encode({"role": role}, jwt_secret, algorithm="HS256")

print(f"{encoded_jwt=}")

# %% Decrypting the token
decoded_role = jwt.decode(encoded_jwt, jwt_secret, algorithms=["HS256"])["role"]
pprint(f"{decoded_role=}")

# %% Detecting error
try:
    decoded_role = jwt.decode(encoded_jwt, "bad_secret", algorithms=["HS256"])["role"]
except jwt.InvalidSignatureError:
    print("Invalid JWT")

# %%
