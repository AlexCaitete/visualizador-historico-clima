import sqlite3

conexao = sqlite3.connect('historico_clima.db') #conectar ao banco desejado
cursor = conexao.cursor()   # conectar o nosso cursor para fazer as tarefas ao nosso banco de dados escolhido.

print('📂 Acessando Banco de dados...')
cursor.execute('SELECT * FROM consultas') #Comando SQL que seleciona tudo da tabela consultas

tudo = cursor.fetchall() #aqui ele executa uma função ja determinada pela biblioteca squile3 que é "pegar os resultados" e guarda na variavel TUDO

#AQUI É O CABEÇALHO QUE VAI APARECER NA TELA. OS :< SERVE PARA ALINHAR TODO O TEXTO A ESQUERDA E O Nº LOGO A POIS É O NÚMERO DE CARACTERES MÁXIMO DO TEXTO
print("\n📊 SEU HISTÓRICO DE CLIMA:")
print("=" * 75)
print(f'{"ID":<5} | {'CIDADE':<25} | {'TEMP':<10} | {'CONDICAO':<20} | {'DATA'}')
print("=" * 75)

#aqui começa o laço de repetição que vai gerar linha por linha como uma tupla. nas mesmas condições visuais do cabeçalho para que fique alinhado.
for linha in tudo:

    id_db = linha[0]
    cidade = linha[1]
    temp = linha[2]
    condicoes = linha[3]
    data =linha[4]
    print(f'{id_db:<5} | {cidade:<25} | {temp:<10} | {condicoes:<20} | {data}')
print("=" * 75)

#comando para fechar a conexção
conexao.close()
input('\nPressione ENTER para sair...')

