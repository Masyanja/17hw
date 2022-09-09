# прописываем путь до базы
import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'test.db')  # абсолютный путь
    SQLALCHEMY_TRACK_MODIFICATIONS = False
