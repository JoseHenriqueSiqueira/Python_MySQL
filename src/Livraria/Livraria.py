import sys
sys.path.append(r'./src')
from Base import BaseDAO
import csv

class tbl_Gerentes(BaseDAO):

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
            super()._execDML('INSERT INTO tbl_Gerentes (nome, cpf, rg, senha) VALUES ( %s, %s, %s, %s)', value)

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
        super()._execDML(f"UPDATE tbl_Gerentes SET nome = %s, cpf = %s, rg = %s, senha = %s WHERE {by} = %s", params)

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
            super()._execDML(f"DELETE FROM tbl_Gerentes WHERE {by} = %s", value)

    def get_cvs_data(self, table_path:str = r'src/Livraria/DadosCSV/Gerentes.csv') -> list[tuple]:
        '''
            Method responsible for getting values from a CSV file.
            Returns list of tuples.
            :return: list[tuple]
        '''
        with open (table_path,'r', encoding = 'utf-8') as file:
            data = []
            reader = csv.DictReader(file)
            for row in reader:
                data.append((row['NOME'], row['CPF'], row['RG'], row['SENHA']))
            return data

class tbl_Leitores(BaseDAO):        

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
            super()._execDML('INSERT INTO tbl_Leitores (nome, cpf, telefone, cep, numero) VALUES ( %s, %s, %s, %s,%s)', value)

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
        super()._execDML(f"UPDATE tbl_Leitores SET nome = %s, cpf = %s, telefone = %s, cep = %s, numero = %s WHERE {by} = %s", params)

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
            super()._execDML(f"DELETE FROM tbl_Leitores WHERE {by} = %s", value)

    def get_cvs_data(self, table_path:str = r'src/Livraria/DadosCSV/Leitores.csv') -> list[tuple]:
        '''
            Method responsible for getting values from a CSV file.
            Returns list of tuples.
            :return: list[tuple]
        '''
        with open (table_path,'r', encoding = 'utf-8') as file:
            data = []
            reader = csv.DictReader(file)
            for row in reader:
                data.append((row['NOME'], row['CPF'], row['TELEFONE'], row['CEP'], row['NUMERO']))
            return data

class tbl_Livros(BaseDAO):        

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
            super()._execDML('INSERT INTO tbl_Livros (nome, autor, genero, editora) VALUES ( %s, %s, %s, %s)', value)

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
        super()._execDML(f"UPDATE tbl_Livros SET nome = %s, autor = %s, genero = %s, editora = %s WHERE {by} = %s", params)

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
            super()._execDML(f"DELETE FROM tbl_Livros WHERE {by} = %s", value)

    def get_cvs_data(self, table_path:str = r'src/Livraria/DadosCSV/Livros.csv') -> list[tuple]:
        '''
            Method responsible for getting values from a CSV file.
            Returns list of tuples.
            :return: list[tuple]
        '''
        with open (table_path,'r', encoding = 'utf-8') as file:
            data = []
            reader = csv.DictReader(file)
            for row in reader:
                data.append((row['NOME'], row['AUTOR'], row['GENERO'], row['EDITORA']))
            return data


if __name__ == "__main__":

    print("Inserindo Gerentes...")
    gerentes = tbl_Gerentes()
    gerentes_data = gerentes.get_cvs_data()
    gerentes.insert_values(gerentes_data)

    print("Inserindo Leitores...")
    leitores = tbl_Leitores()
    leitores_data = leitores.get_cvs_data()
    leitores.insert_values(leitores_data)

    print("Inserindo Livros...")
    livros = tbl_Livros()
    livros_data = livros.get_cvs_data()
    livros.insert_values(livros_data)

    print("FIM")
