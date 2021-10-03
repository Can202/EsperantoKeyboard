import time
import keyboard

def main():
    
    keyboard.add_hotkey('alt+^+j', lambda: write("ĵ"))
    keyboard.add_hotkey('alt+^+c', lambda: write("ĉ"))
    keyboard.add_hotkey('alt+^+g', lambda: write("ĝ"))
    keyboard.add_hotkey('alt+^+h', lambda: write("ĥ"))
    keyboard.add_hotkey('alt+^+s', lambda: write("ŝ"))
    keyboard.add_hotkey('alt+^+h', lambda: write("ĥ"))
    keyboard.add_hotkey('alt+^+u', lambda: write("ŭ"))
    
    keyboard.add_hotkey('alt+shift+^+j', lambda: write("Ĵ"))
    keyboard.add_hotkey('alt+shift+^+c', lambda: write("Ĉ"))
    keyboard.add_hotkey('alt+shift+^+g', lambda: write("Ĝ"))
    keyboard.add_hotkey('alt+shift+^+h', lambda: write("Ĥ"))
    keyboard.add_hotkey('alt+shift+^+s', lambda: write("Ŝ"))
    keyboard.add_hotkey('alt+shift+^+h', lambda: write("Ĥ"))
    keyboard.add_hotkey('alt+shift+^+u', lambda: write("Ŭ"))
    keyboard.add_hotkey('alt+shift+s+q', byebye)
    while True:
        keyboard.wait()
def write(string):
    print(string)
    time.sleep(.15)
    keyboard.write(string)

def byebye():
    quit()
if __name__ == '__main__':
    main()