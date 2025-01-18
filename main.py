import keyboard
import win32.win32gui as g
import ctypes

user32 = ctypes.WinDLL('user32', use_last_error=True)
ignore = False

def switch_ignroe():
    global ignore
    ignore = not ignore
    text = "ŝaltis"
    if ignore:
        text = "malŝaltis"
    handle = user32.GetForegroundWindow()
    g.MessageBox(handle, "Esperanta klavaro {0}".format(text), "Klavara informo", int('00000040', 16))
def break_program():
    handle = user32.GetForegroundWindow()
    g.MessageBox(handle, "Esperanta klavaro ekfinis verki!", "Klavaro informo", int('00000030', 16))
    exit(0)

def get_layout():
    curr_window = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
    klid = user32.GetKeyboardLayout(thread_id)
    lang_id = klid&1023#last 10 bits sign language id. 00000011_11111111 = 0x03FF = 1023
    return hex(lang_id)

prevSymb = '\0'

symbs = "gjuhcs"
symbMap = {'g':'ĝ', 'j':'ĵ', 'u': 'ŭ', 'h':'ĥ', 'c':'ĉ', 's':'ŝ'}

keyboard.add_hotkey('ctrl+alt+2', switch_ignroe)
#keyboard.add_hotkey('ctrl+alt+3', break_program)
while True:
    try:
        event = keyboard.read_event()
        lang_id = get_layout()

        if lang_id != '0x9': #0x9 is english keyboard
            continue
        
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
    except Exception as e:
        print(e)
        continue