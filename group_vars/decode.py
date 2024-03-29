from cryptography.fernet import Fernet
from datetime import datetime
import yaml

def load_key_from_file(file_path):
    """Load the encryption key from a file."""
    with open(file_path, 'rb') as file:
        return file.read()

def decrypt_data(file_path, key):
    """Decrypt data from a given file using the provided key."""
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data.decode()

def write_group_vars(decrypted_data, vars_file_path):
    # Load decrypted data into a YAML object
    data_dict = yaml.safe_load(decrypted_data)

    # Write the YAML object directly back into the file
    with open(vars_file_path, 'w') as file:
        yaml.safe_dump(data_dict, file, default_flow_style=False, allow_unicode=True, sort_keys=False)

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Vars written on {current_date}")

if __name__ == "__main__":
    secret_key_file_path = '../key.txt'
    key = load_key_from_file(secret_key_file_path)
    decrypted_data = decrypt_data("group_vars.yaml", key)

    vars_file_path = 'group_vars.yaml'
    write_group_vars(decrypted_data, vars_file_path)
