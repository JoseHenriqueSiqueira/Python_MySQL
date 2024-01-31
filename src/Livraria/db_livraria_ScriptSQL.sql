/*Criando o banco de dados*/
CREATE DATABASE livraria;

/*Utilizando o banco de dados criado*/
USE livraria;

/*Criando a tabela de gerentes*/
CREATE TABLE gerentes
(
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	nome VARCHAR (50) NOT NULL,
	cpf VARCHAR (20) UNIQUE NOT NULL,
	rg VARCHAR (20) UNIQUE NOT NULL,
	senha VARCHAR (20) NOT NULL
) ENGINE = InnoDB;

/*Criando a tabela de leitores*/
CREATE TABLE leitores
(
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	nome VARCHAR (50) NOT NULL,
	cpf VARCHAR (20) UNIQUE NOT NULL,
	telefone VARCHAR (20) UNIQUE NOT NULL,
	cep VARCHAR (20) NOT NULL,
	numero INT NOT NULL
) ENGINE = InnoDB;

/*Criando a tabela de livros*/
CREATE TABLE livros
(
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	nome VARCHAR (50) NOT NULL,
	autor VARCHAR (50) NOT NULL,
	genero VARCHAR (50) NOT NULL,
	editora VARCHAR (20) NOT NULL
) ENGINE = InnoDB;

/*Criando a tabela de emprestimo*/
CREATE TABLE emprestimos
(
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	id_leitor INT UNIQUE NOT NULL,
	id_livro INT UNIQUE NOT NULL,
	data_emprestimo VARCHAR(20) NOT NULL DEFAULT (DATE_FORMAT(CURRENT_DATE(), '%d-%m-%Y')),
	data_entrega VARCHAR (20) NOT NULL DEFAULT (DATE_FORMAT(DATE_ADD(CURRENT_DATE(), INTERVAL 5 DAY), '%d-%m-%Y')),
	FOREIGN KEY (id_leitor) REFERENCES leitores(id),
	FOREIGN KEY (id_livro) REFERENCES livros(id)
    
) ENGINE = InnoDB;