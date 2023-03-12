from Base import BaseDAO
import csv

class CopaDoMundo2018(BaseDAO):        

    def _params_type(self, method, params):
        '''
            Method responsible for checking if the parameters passed to a method have the expected types.
        '''
        expectations = {
            'update_values': {
                'by': str,
                'params': list
            },
            'delete_values': {
                'by': str,
                'params': list
            },
            'insert_values': {
                'data': list
            },
            'get_values_by': {
                'by': str,
                'value': str
            }
        }
        for param_name, expected_type in expectations[method].items():
            param_value = params.get(param_name)
            if not isinstance(param_value, expected_type):
                raise ValueError(f"Expected type of '{param_name}' is {expected_type.__name__}")

    def insert_values(self, data:list) -> None:
        '''
            Method responsible for inserting data into the database. (INSERT)\n   
            :param data: List of tuples that represents the data to be inserted
            :return: None
        '''
        # Check parameter type
        self._params_type('insert_values', {'data': data})
        for value in data:
            # Calling the parent method _execDML to execute the SQL stament and insert the data into the database
            super()._execDML('INSERT INTO fase_de_grupos VALUES (%s, %s, %s, %s)', value)

    def update_values(self, by:str, params:list) -> None:
        '''
            Method responsible for updating values in the database.
            :param by: str indicating the WHERE clause to be used
            :param params: list of values to be updated
            :return: None
        '''
        # Check parameter types
        self._params_type('update_values', {'by': by, 'params': params})
        # Calling the parent method _execDML to execute the SQL stament and update values into the database
        super()._execDML(f"UPDATE fase_de_grupos SET grupo = %s, posicao = %s, nome = %s, pontos = %s WHERE {by} = %s", params)

    def delete_values(self, by:str, params:list) -> None:
        '''
            Method responsible for delete values in the database.
            :param by: str indicating the WHERE clause to be used
            :param params: list of values to be deleted
            :return: None
        '''
        # Check parameter types
        self._params_type('delete_values', {'by': by, 'params': params})
        for value in params:
            # Calling the parent method _execDML to execute the SQL stament and delete values from the database
            super()._execDML(f"DELETE FROM fase_de_grupos WHERE {by} = %s", value)

    def get_values_by(self, by:str, value:str) -> list[tuple]:
        '''
            Method responsible for retrieving data from the database based on a specific field value.
            :param by: the field to search for.
            :param value: the value to search for in the field.
            :return: a list of tuples containing the query results.
        '''
        # Check parameter types
        self._params_type('get_values_by', {'by': by, 'value': value})
        # Calling the parent method _execQUERY to execute the SQL query
        return super()._execQUERY(f"SELECT * FROM fase_de_grupos WHERE {by} = %s", [value])
        
    def get_csv_values(self) -> list[tuple]:
        '''
            Method responsible for getting values from a CSV file.
            Returns list of tuples.
            :return: list[tuple]
        '''
        with open (r'src/Dados_Copa2018.csv','r', encoding = 'utf-8') as file:
            data = []
            reader = csv.DictReader(file)
            for row in reader:
                data.append((row['Grupo'], row['Posição'], row['Nome'], row['Pontos']))
            return data