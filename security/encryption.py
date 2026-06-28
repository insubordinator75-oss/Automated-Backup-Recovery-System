from cryptography.fernet import Fernet



def generate_key():

    key = Fernet.generate_key()

    with open(
        "security/secret.key",
        "wb"
    ) as file:

        file.write(key)



def load_key():

    with open(
        "security/secret.key",
        "rb"
    ) as file:

        return file.read()



def encrypt_file(file_path):


    key = load_key()


    cipher = Fernet(key)


    with open(
        file_path,
        "rb"
    ) as file:

        data = file.read()



    encrypted_data = cipher.encrypt(
        data
    )


    with open(
        file_path,
        "wb"
    ) as file:

        file.write(
            encrypted_data
        )


    return True