import keyboard
import win32.win32gui as g

ignore = False

def switch_ignroe():
    global ignore
    ignore = not ignore
    text = "ŝaltis"
    if ignore:
        text = "malŝaltis"
    g.MessageBox(None, "Esperanta klavaro {0}".format(text), "Klavara informo", int('00000040', 16))
def break_program():
    g.MessageBox(None, "Esperanta klavaro ekfinis verki!", "Klavaro informo", int('00000030', 16))
    exit(0)

prevSymb = '\0'

symbs = "gjuhcs"
symbMap = {'g':'ĝ', 'j':'ĵ', 'u': 'ŭ', 'h':'ĥ', 'c':'ĉ', 's':'ŝ'}

keyboard.add_hotkey('ctrl+2', switch_ignroe)
while True:
    
    event = keyboard.read_event()
    key = event.name

    isChanger = key.lower() == 'x'
    
    if event.event_type == 'down' or (key.__len__() > 1) or ignore:
        continue

    print('{0}, {1}, {2}, {3}'.format(prevSymb, key, isChanger, event.is_keypad))

    if isChanger and symbMap.__contains__(prevSymb.lower()):
        isUpper = prevSymb.isupper()
        keyboard.press_and_release('backspace')
        keyboard.press_and_release('backspace')
        newKey = symbMap[prevSymb.lower()]
        if isUpper:
            newKey = newKey.upper()
        keyboard.write(newKey)
        prevSymb = '\0'
    else:
        prevSymb = key 