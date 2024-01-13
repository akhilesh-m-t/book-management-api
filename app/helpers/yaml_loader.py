import os
import yaml

current_directory = os.getcwd()
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
yaml_file_path = os.path.abspath(os.path.join(parent_directory, "config.yaml"))
print(yaml_file_path)
with open(yaml_file_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

DATABASE_URL = config["database"]["url"]
ALGORITHM = config["jwt"]["algorithm"]
ACCESS_SECRET_KEY = config["jwt"]["access_key_secret"]
REFRESH_SECRET_KEY = config["jwt"]["refresh_key_secret"]
ACCESS_SECRET_KEY_EXPIRES = config["jwt"]["access_token_expire_minutes"]
REFRESH_SECRET_KEY_EXPIRES = config["jwt"]["refresh_token_expire_minutes"]
