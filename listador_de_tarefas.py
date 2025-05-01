import datetime
import os
import json

# git add -> adicionar aquivo para commit
# git commit -m "<message>" -> commitar de fato nova versão com modificações

data = datetime.datetime.now()
ze = 0

listatitulos = []
listadesc = []

with open("meus_dados.json" "w") as arquivo:
    json.dump(listatitulos)
    json.dump(listadesc)

with open("meus_dados.json" "r") as arquivo2:
    listatitulos.append(json.load(arquivo2))
    listadesc.append(json.load(arquivo2))

while ze == 0:

    os.system('cls')

    print('-=-' * 20)
    print('LISTADOR DE TAREFAS')
    print('-=-' * 20)
    print("""
    """)
    print("(1) listar nova tarefa "
          "(2) verificar tarefas"
          "(3) fechar o programa"
          )

    user_input = (input("Selecione uma opção acima: ")).strip()

    if user_input == '1':
        titulo = input('Título: ').title().strip()
        tarefa = input('digite sua tarefa: ').strip()
        td = input('digite enter para voltar ao programa: ')
        listatitulos.append(titulo)
        listadesc.append(tarefa)
        with open("meus_dados.json", "w") as arquivo:
            object_json = json.dumps(listatitulos, indent=4)
            object_json2 = json.dumps(listadesc, indent=4)



    elif user_input == '2':
        for index, t in enumerate(listatitulos, start=0):
            print('[', index, ']', t, "| data da tarefa listada: ", data.strftime("%d-%m-%Y às %H : %M : %S"), '[TAREFA PENDENTE]')

    elif user_input== '3':
        ze = 1

    else:
        print('[ OPÇÃO NÃO LISTADA VOLTANDO AO PROGRAMA ]')
        print('...'*39)
