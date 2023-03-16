/*Criando o banco de dados*/
CREATE DATABASE db_livraria;

/*Utilizando o banco de dados criado*/
USE db_livraria;

/*Criando a tabela de gerentes*/
CREATE TABLE tbl_Gerentes
(
	id_gerente INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	nome VARCHAR (50) NOT NULL,
	cpf VARCHAR (20) UNIQUE NOT NULL,
	rg VARCHAR (20) UNIQUE NOT NULL,
	senha VARCHAR (20) NOT NULL
) ENGINE = InnoDB;

/*Criando a tabela de leitores*/
CREATE TABLE tbl_Leitores
(
	id_leitor INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	nome VARCHAR (50) NOT NULL,
	cpf VARCHAR (20) UNIQUE NOT NULL,
	telefone VARCHAR (20) UNIQUE NOT NULL,
	cep VARCHAR (20) NOT NULL,
	numero INT NOT NULL
) ENGINE = InnoDB;

/*Criando a tabela de livros*/
CREATE TABLE tbl_Livros
(
	id_livro INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	nome VARCHAR (50) NOT NULL,
	autor VARCHAR (50) NOT NULL,
	genero VARCHAR (50) NOT NULL,
	editora VARCHAR (20) NOT NULL
) ENGINE = InnoDB;

/*Criando a tabela de emprestimo*/
CREATE TABLE tbl_Emprestimos
(
	id_emprestimo INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	id_leitor INT UNIQUE NOT NULL,
	id_livro INT UNIQUE NOT NULL,
	data_emprestimo VARCHAR(20) NOT NULL DEFAULT (DATE_FORMAT(CURRENT_DATE(), '%d-%m-%Y')),
	data_entrega VARCHAR (20) NOT NULL DEFAULT (DATE_FORMAT(DATE_ADD(CURRENT_DATE(), INTERVAL 5 DAY), '%d-%m-%Y')),
	FOREIGN KEY (id_leitor) REFERENCES tbl_leitores(id_leitor),
	FOREIGN KEY (id_livro) REFERENCES tbl_livros(id_livro)
) ENGINE = InnoDB;

# COMANDO PARA DEBUG E TESTES #

/*Comando para mostrar informações sobre as tabelas*/
SHOW TABLE STATUS;

/*Comandos de inserção de dados*/
INSERT INTO tbl_Gerentes (nome, cpf, rg, senha) VALUES ('', '', '', '');
INSERT INTO tbl_Leitores (nome, cpf, telefone, cep, numero) VALUES ('', '', '', '', '');
INSERT INTO tbl_Livros (nome, autor, genero, editora) VALUES ('', '', '', '');
INSERT INTO tbl_Emprestimos (id_leitor, id_livro, data_emprestimo, data_entrega) VALUES ('', '', '', '');

/*Comandos para consultar todos os dados de uma tabela*/
SELECT * FROM tbl_Gerentes;
SELECT * FROM tbl_Leitores;
SELECT * FROM tbl_Livros;
SELECT * FROM tbl_Emprestimos;

/*Comando para remover todas as tabelas do banco de dados*/
DROP TABLES tbl_Emprestimos, tbl_Gerentes, tbl_Leitores, tbl_Livros;

/*Consulta personalizada da tabela emprestimo*/
SELECT tbl_Leitores.nome, tbl_Leitores.cpf, tbl_Livros.nome, tbl_Livros.genero FROM tbl_emprestimo 
JOIN tbl_Leitores ON tbl_emprestimo.id_leitor = tbl_Leitores.id_leitor
JOIN tbl_Livros ON tbl_emprestimo.id_livro = tbl_Livros.id_livro
WHERE tbl_emprestimo.id_emprestimo = '';