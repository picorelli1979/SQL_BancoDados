# NESTA AULA CRIAMOS O BANCO DE DADOS (MEU_PRIMEIRO_BANCO_DB) 
# CRIAMOS A TABELA DE FUNCIONARIOS 
# INSERIMOS VALORES NA TABELA 

# IMPORTAMOS A BIBLIOTECA DO SQLITE3
import sqlite3

# CRIAMOS A VARIAVEL BANCO E CRIAMOS A CONEXÃO COM SQLITE3 E DEMOS O NOME DO BANCO 
banco = sqlite3.connect('Meu_Primeiro_Banco.db')

# AQUI O CURSOR RECEBE TUDO QUE A VARIAVEL BANCO TEM E EXECUTA 
cursor = banco.cursor()

#================================================================
# AQUI CRIAMOS A TABELA DE FUNCIONARIOS
#================================================================

#cursor.execute('''CREATE TABLE Funcionarios(id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                                            nome VARCHAR(25) NOT NULL, 
#                                            cargo VARCHAR(30),
#                                            email VARCHAR(50))''')


#================================================================
# AQUI ABAIXO INSERIMOS  OS DADOS NA TABELA CRADA 
#================================================================

#cursor.execute('''INSERT INTO Funcionarios VALUES(?,?,?,?)''',
#               (1,'Fabricio Paim','Dev Junior','Fabricio001devenloper@gmail.com')) 

#cursor.execute('''INSERT INTO Funcionarios VALUES(?,?,?,?)''',
#               (2,'Jamile Catel','Empresaria','Jamile_catel@gmail.com'))

#cursor.execute('''INSERT INTO Funcionarios VALUES(?,?,?,?)''',
#              (3,'Micael Levi','Estudant','Micael_Levi2014@gmail.com'))

#cursor.execute('''INSERT INTO Funcionarios VALUES(?,?,?,?)''',
#              (4,'Rodrigo Martins','Motorista','Rodrigo14_martins@gmail.com'))

#cursor.execute('''INSERT INTO Funcionarios VALUES(?,?,?,?)''',
#              (5,'Luciano Garrincha','Jogador','Lu1000@gmail.com'))


#==================================================================
# AQUI ABAIXO ATUALIZAMOS OS DADOS 
#================================================================== 

query = '''UPDATE Funciorios SET nome = ? WHERE id = ?;''',('Kalleo Ravi',4)

cursor.execute(query)


#cursor.execute('''UPDATE Funcionarios SET cargo = ?  WHERE id = ?;''',
#              ( 'Advogado', 4))


# AQUI ESTAMOS CONCORDANDO COM O QUE FOI FEITO ACIMA, DAMOS UM COMMIT 
banco.commit()

# DAMOS UM COMANDO SQL E PEDIMOS PARA EXIBIR A TABELA DE FUNCIONARIOS 
cursor.execute("SELECT * FROM Funcionarios") 

# AQUI PRINTAMOS E PEDIMOS PARA PUXAR TODOS O DADOS DO CURSOR 
print(cursor.fetchall()) 