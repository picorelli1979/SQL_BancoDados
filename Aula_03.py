# AQUI INSERIMOS DADOS ATRAVES DE VARIAVEIS QUE DETERMINAMOS  
# NESTE CASO QUANDO DAMOS O INSERT INTO FAZEMOS UMA CONCATENAÇÃO DE VARIAVEIS

import sqlite3
 
id = 5
nome = 'Angelina Julie'
cargo = 'Garota de Programa'
email = 'Joana_machado@gmail.com'


banco = sqlite3.connect('Meu_Primeiro_Banco.db')
 
cursor = banco.cursor()

# PRESTAR ATENÇÃO NAS ASPAS : PRIMEIRO ASPAS SIMPLE, DEPOIS ASPAS DUPLAS, DEPOIS O SINAL DE + (PARA CONCATENAR)
cursor.execute("INSERT INTO Funcionarios VALUES('"+str(id)+"','"+nome+"','"+cargo+"','"+email+"')") 

banco.commit()



