import pyodbc

# Estabelecer a conexão com o SQL Server no contêiner do Docker
conn = pyodbc.connect(
    "DSN=finance;"
    "UID=SA;"
    "PWD=root-100;"
)


# Criar um cursor para executar consultas
cursor = conn.cursor()


# Variáveis com valores a serem usados nos comandos SQL
name = "test%"
table = "purchase_category"
column = "category_name"
condition = f"{column} = 'test%'"


# Comandos SQL
insert = f"INSERT INTO moneys.{table} ({column}) VALUES ('{name}');"
select = f"SELECT * FROM moneys.{table};"
update = f"UPDATE moneys.{table} SET {column} = '{name}' WHERE {condition};"
delete = f"DELETE FROM moneys.{table} WHERE {column} LIKE ('{name}');"


# Executando os comandos SQL criados
command = 'insert'

if command == 'insert':
    cursor.execute(insert)
    conn.commit()
elif command == 'update':
    cursor.execute(update)
    conn.commit()
elif command == 'delete':
    cursor.execute(delete)
    conn.commit()

resultado = cursor.execute(select)


# Ler os resultados da consulta
for row in resultado.fetchall():
    print(row)

# Fechar o cursor e a conexão
cursor.close()
conn.close()
