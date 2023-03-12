import mysql.connector
from mysql.connector import errorcode
from config import HOST, USER, PASSWORD, DBNAME

class BaseDAO():

    def _connection(self) -> mysql.connector.CMySQLConnection:
        '''
            Method responsible for making the connection with the MySQL database.\n   
            Returns instance of CMySQLConnection.\n
            :return: CMySQLConnection instance
        '''
        try:
            # Establishes a connection with the database
            return mysql.connector.connect(host = HOST, user = USER, password = PASSWORD, database = DBNAME)
        except mysql.connector.Error as err:
            # Handles possible errors that may occur while connecting to the database
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise Exception("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise Exception("Database does not exist")
            else:
                raise Exception(err)
            
    def _execDML(self, sql:str, params:list = None) -> None:
        '''
            Method responsible for performing Data Manipulation Language operations (Insert, Update, and Delete).\n   
            :param sql: SQL statement to execute.
            :param params: List of values to be inserted into the SQL statement.
            :return: None
        '''
        cnx = self._connection()
        cursor = cnx.cursor()
        try:
            # If there is only one parameter, it needs to be passed as a tuple.
            if len(params) == 1:
                cursor.execute(sql, (params[0],))
            else:
                cursor.execute(sql, params)
        except mysql.connector.Error as err:
            print(err)
        finally:
            # Commit the changes to the database, close the cursor, and close the connection.
            cnx.commit()
            cursor.close()
            cnx.close()
    
    def _execQUERY(self, sql:str, params:list = None) -> list[tuple]:
        '''
            Method responsible for doing SQL query. (SELECT).\n
            Returns list of tuples.\n
            :param sql: str - the SQL query to be executed
            :param params: list - list of parameters to be used in the query
            :return: list[tuple] - the data retrieved from the query in a list of tuples
        '''
        cnx = self._connection()
        cursor = cnx.cursor()
        try:
            # If there is only one parameter, it needs to be passed as a tuple.
            if len(params) == 1:
                cursor.execute(sql, (params[0],))
            else:
                for param in params:
                    cursor.execute(sql, param)
            data = cursor.fetchall()
        except mysql.connector.Error as err:
            print(err)
        finally:
            # Commit the changes to the database, close the cursor, close the connection and return data.
            cnx.commit()
            cursor.close()
            cnx.close()
            return data