import PySimpleGUI as sg
from random import randint, sample,choice
sg.theme('DarkAmber')  # Add a touch of color
layout = [[sg.Text('Faça sua Escolha:')],
          [sg.Text('- QUINA\n- MEGA SENA\n- DUPLA SENA\n'
                   '- LOTOFÁCIL\n- LOTOMANIA\n- DIA DE SORTE')],
          [sg.Text('Escolha sua Loteria e Click OK para iniciar o Programa'), sg.InputOptionMenu(['QUINA', 'MEGA SENA', 'DUPLA SENA', 'LOTOFÁCIL', 'LOTOMANIA', 'DIA DE SORTE'])],
          [sg.Button('Ok'), sg.Button('Sair')]]
window = sg.Window('Números da Sorte - Jogos da CEF', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':  # Fecha janela se usuario clicar sair ou fechar janela.
        break
if values[0] == 'QUINA':
    opção, init, fim, qdezInit, qdezFim = 'QUINA', 0, 80, 5, 15
if values[0] == 'MEGA SENA':
    opção, init, fim, qdezInit, qdezFim = 'MEGA SENA', 1, 60, 6, 15
if values[0] == 'DUPLA SENA':
    opção, init, fim, qdezInit, qdezFim =   'DUPLA SENA', 1, 50, 6, 15
if values[0] == 'LOTOFÁCIL':
    opção, init, fim, qdezInit, qdezFim =   'LOTOFÁCIL', 1, 25, 15, 20
if values[0] == 'LOTOMANIA':
    opção, init, fim, qdezInit, qdezFim  =  'lOTOMANIA', 0, 99, 50, 50
if values[0] == 'DIA DE SORTE':
    opção, init, fim, qdezInit, qdezFim  =  'DIA DE SORTE', 1, 30, 7, 15

Meses = ('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'Maio'.upper(),
         'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO',
             'Novembro'.upper(), 'Dezembro'.upper())
mesecolhido = choice(Meses) # escolhe um mês dentre os meses da lista "Meses".
#window.close()

sg.theme('DarkTeal9')    #DarkAmber
layout = [[sg.Text(f' Muito bem! Você escolheu:\n\n =================== {opção} =====================\n')],
          [sg.Text(f'======= Esta Loteria opera com dezenas entre {init} e {fim} =======')],
          [sg.Text(f'Para esta Loteria Você pode fazer bilhetes de {qdezInit} até {qdezFim} dezenas ')],
          [sg.Text('Escolha aqui a qtde de Dezenas que Você quer Jogar ==> '), sg.InputOptionMenu(range(qdezInit,qdezFim+1))],
          [sg.Button('Gerar Bilhete'), sg.Button('Sair')]]

window = sg.Window('Números da Sorte - Jogos da CEF', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':  # Fecha janela se usuario clicar sair ou fechar janela.
        break
num = int(values[0])
dezenas = sorted(sample(range(init, fim), num))
if opção == 'DIA DE SORTE':
    opa = [sg.Text(f'=== MÊS DA SORTE!!! ==>  {mesecolhido}')]
else:
    opa = ''
sg.theme('DarkTeal9')    #DarkAmber
layout = [[sg.Text(f'=============== PARABÉNS!!!===========\n SUAS {num} DEZENAS PARA ===== {opção} ===== FORAM: ')],
          [sg.Text(f'DEZENAS SORTEADAS => {dezenas}')],
          opa,
          [sg.Button('Gerar Bilhete'), sg.Button('Sair')]]

window = sg.Window('Números da Sorte - Jogos da CEF', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':  # Fecha janela se usuario clicar sair ou fechar janela.
        break