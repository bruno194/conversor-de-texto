import PySimpleGUI as sg
import random

sg.theme('SystemDefaultForReal')
def principal():
    estilo = [
        [sg.Text('SUGESTÃO DE SENHA')],
        [sg.Button('gerar senha')],
        [sg.Text(size=(30,10), key='converter')],
        [sg.Button('sair')]
    ]
    janela = sg.Window('-GERADOR DE SENHA-').layout(estilo)
    while True:
        evento, valores = janela.read()
        cores = random.choice(['green','red', 'black', 'blue'])
        a = ['a','B','b','A','C','c','d','D','#','@','#','$','%','¨','&','*','(','1','2','3','4','5','6','7','8','9','e','f','E','F','G','H','I','g','h','i']
        computador = random.choices(a, k=8)
        newpas = ' '.join(computador)
        if evento == sg.WINDOW_CLOSED or evento == 'sair':
            break
        if evento == 'gerar senha':
            janela['converter'].update(f'{newpas}', text_color=cores)

principal()