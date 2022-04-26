# encoding: iso-8859-1
DB_HOST = "localhost"
DB_PORT = "3306"
DB_USER = "root"
DB_PASSWORD = "urubu100"
DATABASE = "ALGAS"

# CREATE_QUERY = "CREATE TABLE IF NOT EXISTS dados (id INT PRIMARY KEY AUTO_INCREMENT,grau VARCHAR(15),turno VARCHAR(31),mensalidade VARCHAR(12),bolsa_integral_cotas DOUBLE(12,2),bolsa_integral_ampla INT,bolsa_parcial_cotas INT,bolsa_parcial_ampla INT,curso_busca VARCHAR(127),cidade_busca VARCHAR(31),uf_busca CHAR(2),universidade_nome VARCHAR(127),campus_nome VARCHAR(319),nome VARCHAR(127),nota_integral_ampla DOUBLE(12,2),nota_integral_cotas DOUBLE(12,2),nota_parcial_ampla DOUBLE(12,2),nota_parcial_cotas DOUBLE(12,2))"
CREATE_QUERY = "CREATE TABLE IF NOT EXISTS dados (id INT PRIMARY KEY AUTO_INCREMENT,curso VARCHAR(127),grau VARCHAR(15),turno VARCHAR(31),estado VARCHAR(31),mensalidade DOUBLE(12,2),bolsas INT)"
# INSERT_QUERY = "INSERT INTO dados (id, grau,turno,mensalidade,bolsa_integral_cotas,bolsa_integral_ampla,bolsa_parcial_cotas,bolsa_parcial_ampla,curso_busca,cidade_busca,uf_busca,universidade_nome,campus_nome,nome,nota_integral_ampla,nota_integral_cotas,nota_parcial_ampla,nota_parcial_cotas) VALUES (default, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_QUERY = "INSERT INTO dados (id,CURSO,GRAU,TURNO,ESTADO,MENSALIDADE,BOLSAS) VALUES (default,%s,%s,%s,%s,%s,%s)"
SELECT_QUERY = "SELECT * FROM dados"
DELETE_QUERY = "TRUNCATE dados"

# DROP_QUERY = "DROP TABLE dados"
