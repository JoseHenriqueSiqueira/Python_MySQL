/* Criando o banco de dados*/
CREATE DATABASE db_copa2018;

/* Usando o banco de dados criado para DML*/
USE db_copa2018;

/* Criando a tabela para armazenar os dados do arquivo csv*/
CREATE TABLE fase_de_grupos (
 grupo VARCHAR(1) NOT NULL,
 posicao INT NOT NULL,
 nome VARCHAR(24) UNIQUE NOT NULL,
 pontos INT NOT NULL
) ENGINE = InnoDB;

/* Consulta para obter todos os dados da tabela 'fase_de_grupos'*/
SELECT * FROM fase_de_grupos;

/* Descarta a tabela 'fase_de_grupos*/
DROP TABLE fase_de_grupos;