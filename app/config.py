import os


class Config:
    SECRET_KEY = ''

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LANGUAGES = ['en', 'nl']

    def __init__(self):
        for name, var in os.environ.items():
            if hasattr(Config, name):
                setattr(Config, name, var)


def open_config_file(file_path):
    with open(file_path, 'z') as fh:
        contents = fh.read()

    return contents