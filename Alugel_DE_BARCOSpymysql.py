import pymysql

con = pymysql.connect(db='Conexão com seu bdd', user='Usuario', passwd='Senha')

cursor = con.cursor()

cursor.execute('select * from Cliente')  ### Execuntando o comando para Percorer a tabela Cliente
print("Dados da tabela Cliente:")        ## Execuntando um print da tabela
for cliente in cursor.fetchall():        ### Percorrendo o conteudo da tabela
    print(cliente)

cursor.execute('select * from Barco')       ### Percorrer a tabela barco
print("\nDados da tabela Barco:")           ### Execuntando um print da tabela
for barco in cursor.fetchall():             ### Percorrendo a informação da tabela
    print(barco)

i_cliente_id = input("ID do Cliente: ")        ### Incerindo o conteudo das tabelas anteriores
i_barco_id =  input("ID do Barco: ")
i_data_inicio = input("Data de Inicio (YYYY-MM-DD): ")   ## Data em formato Americano por conta do bdd
i_data_termino = input("Data de Termino (YYYY-MM-DD): ")
i_valor_total = input("Insira o valor: ")            ## Valor em formato decimal, porque especificamos assim no bdd

cursor.execute("INSERT INTO Aluguel (cliente_id, barco_id, data_inicio, data_termino, valor_total) VALUES (%s, %s, %s, %s, %s)",
(i_cliente_id, i_barco_id, i_data_inicio, i_data_termino, i_valor_total))  ### Incerindo as informações na tabela aluguel

con.commit()  #Chamando a função commit( para aplicar a inserção) 

cursor.execute("select * from Aluguel")         ## Selecionando a tabela Aluguel para obter a informação
print("\nDados da tabela Aluguel após a inserção:")
for regs in cursor.fetchall():
    print(regs)

con.close()    ### Fechando a ligação com o banco de dados.


