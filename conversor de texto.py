import PySimpleGUI as sg

sg.theme('Topanga')
def programa():
    estilo = [
        [sg.Text('CONVERSOR-DE-TEXTO')],
        [sg.Input(key='vai-da-certo')],
        [sg.Button('maiúsculo'),
         sg.Button('minúsculo'),
         sg.Button('1° letra maiúscula'),
         sg.Button('1° letra minúscula')],
        [sg.Text(size=(30, 4), key='c')],
        [sg.Button('sair')]
    ]
    janela = sg.Window('CONVERSOR DE TEXTO').layout(estilo)
    while True:
        evento, valores = janela.read()
        if evento == sg.WINDOW_CLOSED or evento == 'sair':
            break
        a = list(valores['vai-da-certo'])
        try:
            mai = ''.join(a)
            b1 = mai.upper()
            min = ''.join(a)
            b2 = min.lower()
            mai2 = ''.join(a)
            b3 = mai2.capitalize()
            min2 = ''.join(a)
            b4 = min2[0].lower()
            resto = valores['vai-da-certo'][1:]
        except:
            janela['c'].update('erro, digite alguma coisa ',text_color='red')
        else:
            if evento == 'maiúsculo':
                janela['vai-da-certo'].update(b1)
            if evento == 'minúsculo':
                janela['vai-da-certo'].update(b2)
            if evento == '1° letra maiúscula':
                janela['vai-da-certo'].update(b3)
            if evento == '1° letra minúscula':
                janela['vai-da-certo'].update(f'{b4}{resto}')


programa()