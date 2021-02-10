def try_color(intentos):
    if intentos > 0:
        print(f'Te quedan {intentos} intentos')
        color = input(
            'De que color es la fruta que un bot esta pensando en este momento?\n')
        if str(color) != 'naranja':
            try_color(intentos - 1)
        else:
            print('correcto es naranja')
    else:
        print('lo siento perdiste')


try_color(3)