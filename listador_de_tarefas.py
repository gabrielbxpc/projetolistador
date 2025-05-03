import datetime
import os
import json

with open('data.json') as f:
    json_object0 = json.load(f)



# with open("data.json", 'w') as f:

ze = 0

dados = json_object0["l1"]

listaconc = json_object0["l2"]

datatowrite = {"l1": dados, "l2": listaconc}



while ze == 0:
    os.system('cls')

    print('-=-' * 20)
    print('LISTADOR DE TAREFAS')
    print('-=-' * 20)
    print("""
    """)
    print ("[1] cadastrar nova tarefa ")
    print ("[2] verificar tarefas")
    print("[3] verificar tarefas concluídas")
    print("[4] fechar o programa")
    print("""
    """)

    user_input = (input("Selecione uma opção acima: ")).strip()

    if user_input == '1':

        os.system('cls')

        data = datetime.datetime.now()
        data = data.strftime("%d/%m/%Y às %H : %M : %S")
        print("""
        """)
        titulo = input('Título: ').title().strip()
        tarefa = input('digite sua tarefa: ').strip()
        td = input('digite enter para voltar ao programa: ')
        dados.append({'nome': [titulo], 'desc': [tarefa], 'data': [data]})

    elif user_input == '2':

            os.system('cls')

            print('---' * 20)
            print("[1] verificar tarefas")
            print("[2] verificar tarefas por completo")
            print("[3] marcar tarefa como concluída")
            user_input0 = (input('digite uma das opções: '))
            if user_input0 == '1':
                for index, t in enumerate(dados, start=0):
                    print('[', index, ']', t['nome'],
                          '[TAREFA PENDENTE]')
                user_input3 = input('digite enter para voltar ao programa: ')
            elif user_input0 == '2':
                for index, t in enumerate(dados, start=0):
                    print('[', index, ']', t['nome'],
                          '[TAREFA PENDENTE]')
                user_input2 = int(input('selecione uma tarefa acima: '))
                print('Título: ', dados[0]['nome'][user_input2])
                print('Tarefa: ', dados[0]['desc'][user_input2])
                print("""data da tarefa listada: """, dados[0]['data'][user_input2])
                user_input3 = input('digite enter para voltar ao programa: ')
            elif user_input0 == '3':
                for index, t in enumerate(dados, start=0):
                    print('[', index, ']', t['nome'],
                          '[TAREFA PENDENTE]')
                user_input4 = int(input('selecione a tarefa para marcar como concluída: '))
                listaconc.append(dados[user_input4])
                del dados[user_input4]


            else:
                print('[ OPÇÃO NÃO LISTADA VOLTANDO AO PROGRAMA ]')
                print('...' * 39)

    elif user_input=='3':
        os.system('cls')
        for index, t in enumerate(listaconc, start=0):
            print('[', index, ']', t['nome'],
                  '[TAREFA CONCLUÍDA]')
        user_input5 = input('digite enter para voltar ao programa: ')
    elif user_input== '4':
        ze = 1

    else:
        print('[ OPÇÃO NÃO LISTADA VOLTANDO AO PROGRAMA ]')
        print('...'*39)

with open('data.json', 'w') as w:
    json.dump(datatowrite, w)

