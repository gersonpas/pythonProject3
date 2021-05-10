import PySimpleGUI as sg
from random import randint, sample,choice
#sg.theme('DarkAmber')
sg.ChangeLookAndFeel('DarkAmber')

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]


layout = [[sg.Menu(menu_def, tearoff=True)],
          #[sg.Text('⇓⇓  FAÇA AQUI A SUA ESCOLHA  ⇓⇓')],
[sg.Text('⇓⇓  FAÇA AQUI A SUA ESCOLHA  ⇓⇓', size=(30, 1), justification='center', font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
          [sg.Text('-   QUINA\n-   MEGA SENA\n-   DUPLA SENA\n'
                   '-   LOTOFÁCIL\n-   LOTOMANIA\n-   DIA DE SORTE')],
          [sg.Text('  FAÇA AQUI SUA OPÇÃO     ⇒ ⇒ ⇒ '),

           sg.InputCombo(['QUINA', 'MEGA SENA', 'DUPLA SENA',
                    'LOTOFÁCIL', 'LOTOMANIA', 'DIA DE SORTE'], size=(15,1))],

          [sg.Text(' QUANTAS CARTELAS DESEJA FAZER     ⇒ ⇒ ⇒'), sg.InputCombo([1,2,3,4,5])],
          [sg.Button('Ok')]]
window = sg.Window('$ Acredite na Sua Sorte e Fique Rico $'.upper(), layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Ok':
        break
if values[1] == '':
    values[1] = 'QUINA'
if values[2] == '':
    values[2] = 1
qtdeBilhetes = int(values[2])
if values[1] == 'QUINA':
    opção, init, fim, qdezInit, qdezFim = 'QUINA', 0, 80, 5, 15
if values[1] == 'MEGA SENA':
    opção, init, fim, qdezInit, qdezFim = 'MEGA SENA', 1, 60, 6, 15
if values[1] == 'DUPLA SENA':
    opção, init, fim, qdezInit, qdezFim =   'DUPLA SENA', 1, 50, 6, 15
if values[1] == 'LOTOFÁCIL':
    opção, init, fim, qdezInit, qdezFim =   'LOTOFÁCIL', 1, 25, 15, 20
if values[1] == 'LOTOMANIA':
    opção, init, fim, qdezInit, qdezFim  =  'lOTOMANIA', 0, 99, 50, 50
if values[1] == 'DIA DE SORTE':
    opção, init, fim, qdezInit, qdezFim  =  'DIA DE SORTE', 1, 30, 7, 15
Meses = ('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'Maio'.upper(),
         'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO',
             'Novembro'.upper(), 'Dezembro'.upper())
mesecolhido = choice(Meses) # escolhe um mês dentre os meses da lista "Meses".
window.close()
sg.theme('DarkAmber')
layout = [[sg.Text(f' Muito bem! Você escolheu:\n\n =================== {opção} =====================\n'.upper())],
          [sg.Text(f'======= Esta Loteria opera com dezenas entre {init} e {fim} ======='.upper())],
          [sg.Text(f'Para esta Loteria Você pode fazer bilhetes de {qdezInit} até {qdezFim} dezenas '.upper())],
          [sg.Text('Escolha aqui a qtde de Dezenas que Você quer Jogar ==> '.upper()), sg.InputOptionMenu(range(qdezInit,qdezFim+1))],
          [sg.Button('Gerar Bilhete')],
          [sg.Menu(menu_def, tearoff=True)]]
window = sg.Window('Números da Sorte - Jogos da CEF'.upper(), layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Gerar Bilhete':  # Fecha janela se usuario clicar sair ou fechar janela.
        break
if values[0] == '':
    values[0] = qdezInit
num = int(values[0])
cont = 0
numSort = list()
opa = dict()
for cont in range(0,qtdeBilhetes):
    dezenas = sorted(sample(range(init, fim), num))
    numSort.append(dezenas)
    opa[cont] = [sg.Text(f'CARTELA {cont+1} :=> {numSort[cont]}')]
    cont += 1
if opção == 'DIA DE SORTE':
    ome = [sg.Text(f'$$$ :::  MÊS DA SORTE  :::  $$$  ⇒ ⇒ ⇒  {mesecolhido}')]
else:
    ome = ''
window.close()
sg.theme('DarkTeal9')    #DarkAmber
layout2 = [[sg.Text(f'===============  PARABÉNS!  ===========\n Veja abaixo suas  {qtdeBilhetes}  cartelas com  {num}  DEZENAS cada\n'
          f'\n           =======  {opção}  =======  '.upper())],
          opa.values(),
          ome,
          [sg.Text('    ')],
          [sg.Button('Nova Cartela'),sg.Button('Sobre o Programa'), sg.Button('Sair')],
           [sg.Menu(menu_def, tearoff=True)]]
window2 = sg.Window('AQUI OS SEUS NÚMEROS DA SORTE!!!', layout2)
while True:
    event, values = window2.read()
    if event == 'Nova Cartela':
        print('Próxima Cartela')
    if event == sg.WIN_CLOSED or event == 'Sair':  # Fecha janela se usuario clicar sair ou fechar janela.
        break
    if event == 'Sobre o Programa':
        break
#window.close()
sg.theme('DarkTeal9')    #DarkAmber
layout3 = [[sg.Text(" gerson pereira de araujo sobrinho".upper())],
           [sg.Text("Programador Java/Python")],
           [sg.Text('Programa Criando em Python 3.8 = V1.1 -  03/05/2021\nContatos: sobrinho.gerson@yahoo.com/')],
           [sg.Text("https://github.com/gersonpas/")],
           [sg.Button('Sair')],
           [sg.Menu(menu_def, tearoff=True)]]
window3 = sg.Window(' =======  sobre o autor  ======'.upper(), layout3)
while True:
    event, values = window3.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
         window3.close()
         break

