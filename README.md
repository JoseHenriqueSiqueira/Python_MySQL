# Python_MySQL
Este repositório demonstra como conectar o MySQL com o Python de forma segura e simples. O exemplo utiliza dois bancos de dados: um simples, referente a Copa do Mundo 2018, e outro mais complexo, referente a uma livraria. O repositório também ensina como obter dados de um arquivo CSV e inseri-los dentro do banco MySQL. Para testar os métodos de insert, update, delete e select, há pastas com arquivos CSV para cada banco. A pasta da Copa do Mundo 2018 contém apenas um arquivo CSV, pois o banco é simples e contém apenas uma tabela. Já a pasta do banco complexo (Livraria) contém vários arquivos CSV, pois o banco possui quatro tabelas. Para testar de forma eficiente o banco Livraria, foi desenvolvido um script que gera dados ilimitados para as tabelas e os converte em uma planilha CSV. Este repositório é útil para quem quer aprender como conectar o MySQL com o Python de forma segura e para quem deseja praticar a inserção e manipulação de dados em bancos de dados MySQL.

## Images
### BaseDAO.py
[BaseDAO](/src/Base.py)<br>
<img src="/images/base.png?raw=true">

### DB_LIVRARIA
[Livraria_ScriptSQL](/src/Livraria/db_livraria_ScriptSQL.sql)<br>
<img src="/images/livraria_sql.png?raw=true">

### DB_COPA2018
[Copa2018_ScriptSQL](/src/Copa2018/copa2018_ScriptSQL.sql)<br>
<img src="/images/copa_sql.png">

## Requirements
[mysql.connector](https://pypi.org/project/mysql-connector-python/)<br>
[csv](https://docs.python.org/3/library/csv.html)<br>
[numpy](https://numpy.org/)<br>
[faker](https://pypi.org/project/Faker/)

## Built With
[Python 3.11.X](https://www.python.org/)<br>
[MySQL](https://www.mysql.com/)


