from faker import Faker
import numpy as np
import csv

class Gerar_Dados():

    def _gerar_cpfs_aleatorios(self, quantidade: int = 1) -> list:
        # Cria um set para armazenar os CPFs gerados e garantir que não haja duplicatas
        cpfs = set()

        # Cria uma matriz numpy com os dígitos de 0 a 9
        digitos_base = np.arange(10)

        # Loop para gerar CPF's UNICOS até a quantidade passada como parâmetro pelo o usuário
        while len(cpfs) < quantidade:

            # Embaralha os dígitos e selecionar os 9 primeiros
            np.random.shuffle(digitos_base)
            digitos = digitos_base[:9]
            
            # Calcula o primeiro dígito verificador
            soma1 = np.sum(digitos * np.array([10, 9, 8, 7, 6, 5, 4, 3, 2]).reshape(1, -1), axis=1)
            resto1 = 11 - (soma1 % 11)
            primeiro_digito = np.where(resto1 > 9, 0, resto1)

            # Calcula o segundo dígito verificador
            digitos_com_verif1 = np.concatenate([digitos, primeiro_digito])
            soma2 = np.sum(digitos_com_verif1 * np.array([11, 10, 9, 8, 7, 6, 5, 4, 3, 2]).reshape(1, -1), axis=1)
            resto2 = 11 - (soma2 % 11)
            segundo_digito = np.where(resto2 > 9, 0, resto2)

            # Adiciona os dígitos verificadores e os dígitos para formar o CPF completo
            cpf_numeros = np.concatenate([digitos, primeiro_digito, segundo_digito])
            cpf_string = ''.join(map(str, cpf_numeros))
            
            cpfs.add(cpf_string)

        # Formatar os CPFs e retorna como uma lista
        cpfs_formatados = [cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:] for cpf in cpfs]
        return cpfs_formatados

    def _gerar_nomes_aleatorios(self, quantidade:int = 1) -> list:
        fake = Faker()
        nomes = []
        for _ in range(quantidade):
            nomes.append(fake.name()) 
        return nomes

    def _gerar_telefones_aleatorios(self, quantidade:int = 1) -> list:
        # Cria um conjunto vazio para armazenar os telefones gerados
        telefones = set()

        # Cria um array com os dígitos de 0 a 9 para serem usados na geração dos telefones
        digitos_base = np.arange(10)

        # Repete o processo de geração de telefones até atingir a quantidade desejada
        while len(telefones) < quantidade:
            # Gera um número aleatório de DDD entre 11 e 99
            ddd = np.random.randint(11, 100)

            # Embaralha os dígitos e seleciona os primeiros 9 para serem usados no número do telefone
            np.random.shuffle(digitos_base)
            digitos = digitos_base[:9]

            # Concatena o DDD com o restande do numero e transforma em uma String.
            telefone_numeros = np.concatenate([np.array([ddd]), digitos])
            telefone_string = ''.join(map(str, telefone_numeros))

            # Adiciona ao Conjunto
            telefones.add(telefone_string)
        
        # Adiciona a máscara aos telefones e retorna a lista
        telefones = ['(' + telefone[0:2] + ') ' + telefone[2:7] + '-' + telefone[7:] for telefone in telefones]

        return list(telefones)

    def _gerar_ceps_aleatorios(self, quantidade:int = 1) -> list:
        # Cria um conjunto vazio para armazenar os CEP'S gerados
        ceps = set()

        # Cria um array com os dígitos de 0 a 9 para serem usados na geração dos CEP'S
        digitos_base = np.arange(10)

        # Repete o processo de geração de CEP'S até atingir a quantidade desejada
        while len(ceps) < quantidade:
            # Embaralha os dígitos e seleciona os primeiros 8 para serem usados no número do cep
            np.random.shuffle(digitos_base)
            digitos = digitos_base[:8]

            # Transforma a array CEP'S em uma string
            ceps_string = ''.join(map(str, digitos))

            # Adiciona ao Conjunto
            ceps.add(ceps_string)

        # Adiciona a máscara aos CEP'S e retorna a lista
        ceps = [cep[0:5] + '-' + cep[5:] for cep in ceps]
        return ceps

    def _gerar_numeros_aleatorios(self, quantidade:int = 1) -> list:
        # Cria um conjunto vazio para armazenar os numeros residenciais gerados
        numeros_residenciais = set()

        # Cria um array com os dígitos de 0 a 9 para serem usados na geração dos numeros residenciais
        digitos_base = np.arange(10)

        # Repete o processo de geração de números residenciais até atingir a quantidade desejada
        while len(numeros_residenciais) < quantidade:
            # Gera um número aleatório entre 1 e 5, que será o tamanho do número residencial
            n = np.random.randint(2, 5)

            # Embaralha os dígitos e seleciona os primeiros 5 para serem usados no número residencial
            np.random.shuffle(digitos_base)
            digitos = digitos_base[:n]

            # Transforma a array em uma string
            numeros_string = ''.join(map(str, digitos))

            # Adiciona ao Conjunto
            numeros_residenciais.add(numeros_string)

        # Retorna o número aleatório como uma string
        return list(numeros_residenciais)

    def _gerar_livros_aleatorios(self, quantidade: int = 1) -> list:
        # Cria um conjunto vazio para armazenar os numeros residenciais gerados
        livros = set()
        # Cria um array com os dígitos de 0 a 9 para serem usados na geração dos numeros residenciais
        digitos_base = np.arange(10)
        # Repete o processo de geração de números residenciais até atingir a quantidade desejada
        while len(livros) < quantidade:
            n = np.random.randint(2, 5)
            # Embaralha os dígitos e seleciona os primeiros 2 para serem usados no número residencial
            np.random.shuffle(digitos_base)
            digitos = digitos_base[:n]
            # Transforma a array em uma string
            numeros_string = ''.join(map(str, digitos))
            # Adiciona ao Conjunto
            livros.add(numeros_string)
        livros = ['Livro_' + livro for livro in livros]
        # Retorna o número aleatório como uma string
        return list(livros)

    def _gerar_generos_aleatorios(self, quantidade: int = 1) -> list:
        generos = [
                    'Ficção Científica', 'Romance', 'Mistério', 'Aventura', 'História', 
                    'Fantasia', 'Terror', 'Suspense', 'Policial', 'Drama', 
                    'Comédia', 'Ação', 'Infantil', 'Autoajuda', 'Didático', 
                    'Biografia', 'Ensaio', 'Religião', 'Esporte', 'Gastronomia'
                    ]
        generos_lista = list()
        generos_lista = np.random.choice(generos, size=quantidade, replace=True)
        return generos_lista
    
    def _gerar_editoras_aleatorias(self, quantidade:int = 1) -> list:
        # gera uma array com números aleatórios de 10 a 99
        numeros_aleatorios = np.random.randint(10, 100, size=quantidade)
        # concatena cada número com a string "Editora_"
        editoras_aleatorias = ["Editora_" + str(num) for num in numeros_aleatorios]
        return editoras_aleatorias

    def _gerar_rg_aleatorios(self, quantidade:int = 1) -> list:
        rgs = set()
        digitos_base = np.arange(10)
        while len(rgs) < quantidade:
            np.random.shuffle(digitos_base)
            digitos = digitos_base[:8]
            cpf_string = ''.join(map(str, digitos))
            rgs.add(cpf_string)
        rgs_formatados = [rg[:2] + '.' + rg[2:5] + '.' + rg[5:8]for rg in rgs]
        return rgs_formatados

    def _gerar_senhas_aleatorias(self, quantidade: int = 1) -> list:
        chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        senhas = set()
        while len(senhas) < quantidade:
            password_length = np.random.randint(8, 21)
            password = ''.join(np.random.choice(chars, password_length))
            senhas.add(password)
        return list(senhas)

class Gerar_CSV(Gerar_Dados):

    def tbl_gerentes(self, quantidade:int = 1) -> None:
        nomes_aleatorios = self._gerar_nomes_aleatorios(quantidade)
        cpfs_aleatorios = self._gerar_cpfs_aleatorios(quantidade)
        rgs_aleatorios = self._gerar_rg_aleatorios(quantidade)
        senhas_aleatorias = self._gerar_senhas_aleatorias(quantidade)
        dados = list()
        for nome, cpf, rg, senha in zip(nomes_aleatorios, cpfs_aleatorios, rgs_aleatorios, senhas_aleatorias):
            dados.append((nome, cpf, rg, senha))
        with open('src/Livraria/DadosCSV/Gerentes.csv', 'w', newline='', encoding='utf-8') as file:
            leitores = csv.writer(file)
            leitores.writerow(['NOME','CPF','RG','SENHA'])
            for dado in dados:
                leitores.writerows([dado])

    def tbl_leitores(self, quantidade:int = 1) -> None:
        nomes_aleatorios = self._gerar_nomes_aleatorios(quantidade)
        cpf_aleatorios = self._gerar_cpfs_aleatorios(quantidade)
        telefones_aleatorios = self._gerar_telefones_aleatorios(quantidade)
        ceps_aleatorios = self._gerar_ceps_aleatorios(quantidade)
        numeros_aleatorios = self._gerar_numeros_aleatorios(quantidade)
        dados = list()
        for nome, cpf, telefone, cep, numero in zip(nomes_aleatorios, cpf_aleatorios, telefones_aleatorios, ceps_aleatorios, numeros_aleatorios):
            dados.append((nome, cpf, telefone, cep, numero))
        with open('src/Livraria/DadosCSV/Leitores.csv', 'w', newline='') as file:
            leitores = csv.writer(file)
            leitores.writerow(['NOME','CPF','TELEFONE','CEP','NUMERO'])
            for dado in dados:
                leitores.writerows([dado])

    def tbl_livros(self, quantidade:int = 1) -> None:
        nomes_aleatorios = self._gerar_nomes_aleatorios(quantidade)
        livros_aleatorios = self._gerar_livros_aleatorios(quantidade)
        generos_aleatorios = self._gerar_generos_aleatorios(quantidade)
        editoras_aleatorias = self._gerar_editoras_aleatorias(quantidade)
        dados = list()
        for autor, nome, genero, editora in zip(nomes_aleatorios, livros_aleatorios, generos_aleatorios, editoras_aleatorias):
            dados.append((nome, autor, genero, editora))
        with open('src/Livraria/DadosCSV/Livros.csv', 'w', newline='', encoding='utf-8') as file:
            leitores = csv.writer(file)
            leitores.writerow(['NOME','AUTOR','GENERO','EDITORA'])
            for dado in dados:
                leitores.writerows([dado])


cvs = Gerar_CSV()
cvs.tbl_gerentes(500)
cvs.tbl_leitores(500)
cvs.tbl_livros(100)