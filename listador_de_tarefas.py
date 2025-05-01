ze = 0

# alga = {"Título": [], "Tarefas": []}
listatitulos = []
listadesc = []

while ze == 0:

    print('-=-' * 20)
    print('LISTADOR DE TAREFAS')
    print('-=-' * 20)
    print(''

          '')
    print("(1) listar nova tarefa "
          "(2) verificar tarefas"
          "(3) excluir tarefas"
          "(4) fechar o programa")

    user_input = int(input("Selecione uma opção acima: "))

    if user_input == 1:
        titulo = input('Título: ').title()
        tarefa = input('digite sua tarefa: ')
        td = input('digite enter para voltar ao programa: ')
        listatitulos.append(titulo)
        listadesc.append(tarefa)

    if user_input == 2:
        for index, t in enumerate(listatitulos, start=0):
            print(index, t)