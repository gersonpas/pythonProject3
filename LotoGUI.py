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

Meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
mesecolhido = choice(Meses) # escolhe um mês dentre os meses da lista "Meses".


#qdezenas = int(input(f'\033[0;33mEscolha um jogo entre {qdezInit} e {qdezFim} Dezenas\033[0;33m: '))

#window.close()

sg.theme('DarkTeal9')    #DarkAmber
layout = [[sg.Text(f' Muito bem! Você escolheu:\n\n =================== {opção} =====================\n')],
          [sg.Text(f'Escolha dezenas entre {init} e {fim}')],
          [sg.Text(f'Quantas dezenas quer Jogar? Entre {qdezInit} e {qdezFim} ')],
          [sg.Text('Escolha qtde de Dezenas'), sg.InputOptionMenu(range(qdezInit,qdezFim+1))],
          [sg.Button('Gerar Bilhete'), sg.Button('Sair')]]

window = sg.Window('Números da Sorte - Jogos da CEF', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':  # Fecha janela se usuario clicar sair ou fechar janela.
        break
num = int(values[0])
dezenas = sorted(sample(range(init, fim), num))
if opção == 'DIA DE SORTE':
    opa = [sg.Text(f'MÊS SORTEADO ==>  {mesecolhido}')]
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