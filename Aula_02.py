# AQUI IREMOS APRENDER A DELETAR UM DADO  

import sqlite3

# AQUI DIZEMOS QUE SE ESTIVER TUDO CERTO ELE EXECUTA ESSE BLOCO DE CODIGO

try:
    
    banco = sqlite3.connect('Meu_Primeiro_Banco.db')
    
    cursor = banco.cursor()

    cursor.execute('DELETE FROM Funcionarios WHERE id = 5')

    banco.commit()

    banco.close()
    print('OS DADOS FORAM REMOVIDOS COM SUCESSO !!!!')

# AQUI DIZEMOS QUE SE NÃO ESTIVER TUDO CERTO ELE EXECUTA A EXEÇÃO

except sqlite3.Error as error:
    print('[ERROR] ao Concluir:', error)






