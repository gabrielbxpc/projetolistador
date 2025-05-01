class Tarefa:
    def __init__(self, pendente = True):
        self.pendente = pendente




# git add -> adicionar aquivo para commit
# git commit -m "<message>" -> commitar de fato nova versão com modificações

ze = 0

# alga = {"Título": [], "Tarefas": []}
listatitulos = []
listadesc = []
listadata = []

while ze == 0:

    print('-=-' * 20)
    print('LISTADOR DE TAREFAS')
    print('-=-' * 20)
    print(''

          '')
    print("(1) listar nova tarefa "
          "(2) verificar tarefas"
          "(3) fechar o programa"
          )

    user_input = int(input("Selecione uma opção acima: "))

    if user_input == 1:
        titulo = input('Título: ').title().strip()
        tarefa = input('digite sua tarefa: ').strip()
        data = input('data que você está listando a tarefa: ').strip()
        td = input('digite enter para voltar ao programa: ')
        listatitulos.append(titulo)
        listadesc.append(tarefa)
        listadata.append(data)

    if user_input == 2:
        for index, t in enumerate(listatitulos, start=0):
            print(index, t, "(data da tarefa listada): ", listadata, '[TAREFA PENDENTE]')

    if user_input== 3:
        ze = 1

