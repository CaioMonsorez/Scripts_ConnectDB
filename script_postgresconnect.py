import psycopg2

#Criando uma conexao com o postgres

conn = psycopg2.connect(
  user = "user",
  password = "password",
  host = "XXX.XXX.XXX.XXX",
  port = 5432,
  database = "postgresdb_teste"
)

#Abre o arquivo que será inserido no banco de dados
with open ('qualquercsvcomdadosparaincluirnobanco.csv') as arq_open:
  csv = arq_open.readlines()


# abre um cursor com a conexao no banco de dados e insere todas as 
# linhas do arquivo csv que foi aberto acima, utilizando o separador definido

with conn.cursor() as cursor:
  cursos.copy_from(csv, 'stg_table', sep = '|') 
  conn.commit()