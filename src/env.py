from dotenv import load_dotenv
import os

load_dotenv()

class DataBase():

    HOST = os.getenv('HOST')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DBNAME = os.getenv('DBNAME')

