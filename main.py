import json

print('Menu PUC')
print('(1) Estudante')

menues = int(input())


MenuOpcoes = '[{"id": "1", "tipo": "Estudante"}]'
Armazenar = '{"Dados": []}'

Menujson = json.loads(MenuOpcoes)
Armazenara = json.loads(Armazenar)

def Listarjson(file):
    f = open (file, "r")
    return json.loads(f.read())['Dados']


def incluir(tipo):
    nome = str(input("Nome do estudante: "))
    curso = str(input("Curso acadêmico: "))

    Armazenara["Dados"].append({"tipo": tipo, "nome": nome, "Curso": curso})

    for data in Listarjson('dados.json'):
       Armazenara["Dados"].append(data)


    with open('dados.json', 'w') as outfile:
        json.dump(Armazenara, outfile)

def Listar():

     for data in Listarjson('dados.json'):
       print(data)

def opcoes(tipo):
    menucoes = input("O que deseja? Incluir, Listar: ")
    if menucoes == "Incluir":
         incluir(tipo)
    elif menucoes == "Listar":
         Listar()
    else:
        print('Opção inválida')


for a in Menujson:
    if int(a['id']) == menues:
        opcoes(a['tipo'])
        break
    elif menues > len(Menujson):
        print('Nenhuma opção selecionada')
        break



