global info
info = dict()
info['titu'] = ''
info['but1'] = ''
info['but2'] = ''
info['re'] = ''
info['teste'] = False


def janela():
    import PySimpleGUI as sg
    sg.theme('DarkGrey9')
    layout = [[sg.Text("Digite uma temperatura com sua escala(K, F, C)")],
              [sg.Input(key='saida')],
              [sg.Button('OK'), sg.Button('Sair')],
              [sg.Text(size=(37, 1), visible=False, key='titul')],
              [sg.Button(visible=False, key='b1', size=(15, 1)), sg.Button(visible=False, key='b2', size=(15,1))],
              [sg.Text(size=(35, 2), visible=False, key='res', text_color='yellow', background_color='green')]]

    window = sg.Window('Conversor', layout)
    while True:
        event, valor = window.read()
        if event == 'b1':
            #window['resut'].update(visible=True)
            window['res'].update(f"Resultado:  \n    {conversor(valor['saida'], 1)}", visible=True)
        if event == 'b2':
            #window['resut'].update(visible=True)
            window['res'].update(f"Resultado:  \n    {conversor(valor['saida'], 2)}", visible=True)
        if event == 'OK':
            conversor(valor['saida'], 1)
            if not info['teste']:
                window['titul'].update(info['titu'], visible=True, text_color='white')
                window['b1'].update(info['but1'], visible=True)
                window['b2'].update(info['but2'], visible=True)
            else:
                window['res'].update("ERRO!!")
                window['b1'].update("ERRO!!")
                window['b2'].update("ERRO!!")
                window['titul'].update(f'Erro!! Digite a escala da temperatura Ex: 10c, 4f ,8k', text_color='red', visible=True)
        if event == sg.WIN_CLOSED or event == 'Sair':
            return "FIM"
    window.close(); del window


def conversor(t1, b):
    save = tip = ""
    t = str(t1)
    for i in t:
        if i.isnumeric():
            save += str(i)
        else:
            tip = str(i).upper()
    valor = int(save)
    if tip == "C":
        info['titu'] = 'De Celsius para qual unidade deseja converter?'
        info['but1'] = 'Fahrenheit'
        info['but2'] = 'Kelvin'
        info['teste'] = False
        return f'{valor}º Celsius para {CpraT(b, valor)}.'
    elif tip == "F":
        info['titu'] = 'De Fahrenheit pra qual unidade deseja converter?'
        info['but1'] = 'Celsius'
        info['but2'] = 'Kelvin'
        info['teste'] = False
        return f'{valor}º Fahrenheit para {FpraT(b, valor)}.'
    elif tip == "K":
        info['titu'] = 'De Kelvin pra qual unidade deseja converter?'
        info['but1'] = 'Celsius'
        info['but2'] = 'Fahrenheit'
        info['teste'] = False
        return f'{valor}º Kelvin para {KpraT(b, valor)}.'
    else:
        info['teste'] = True


def CpraT(x, c):
    r = 0
    if x == 1:
        r = (c * 9 / 5) + 32
        return f"Fahrenheit é {round(r, 1)}ºF"
    else:
        r = c + 273
        return f"Kelvin é {round(r, 1)}ºK"


def FpraT(x, c):
    r = 0
    if x == 1:
        r = (c - 32) * (5 / 9)
        return f"Celsius é {round(r, 1)}ºC"
    else:
        r = ((c - 32) * (5 / 9)) + 273.15
        return f"Kelvin é {round(r, 1)}ºK"


def KpraT(x, c):
    r = 0
    if x == 1:
        r = c - 273
        return f"Celsius é {round(r, 1)}ºC"
    else:
        r = (c - 273) * 9 / 5 + 32
        return f"Fahrenheit é {round(r, 1)}ºF"

