import time
import keyboard

def main():
    
    keyboard.add_hotkey('ctrl+alt+j', lambda: write("ĵ"))
    keyboard.add_hotkey('ctrl+alt+c', lambda: write("ĉ"))
    keyboard.add_hotkey('ctrl+alt+g', lambda: write("ĝ"))
    keyboard.add_hotkey('ctrl+alt+h', lambda: write("ĥ"))
    keyboard.add_hotkey('ctrl+alt+s', lambda: write("ŝ"))
    keyboard.add_hotkey('ctrl+alt+h', lambda: write("ĥ"))
    keyboard.add_hotkey('ctrl+alt+u', lambda: write("ŭ"))
    
    keyboard.add_hotkey('ctrl+alt+shift+j', lambda: write("Ĵ"))
    keyboard.add_hotkey('ctrl+alt+shift+c', lambda: write("Ĉ"))
    keyboard.add_hotkey('ctrl+alt+shift+g', lambda: write("Ĝ"))
    keyboard.add_hotkey('ctrl+alt+shift+h', lambda: write("Ĥ"))
    keyboard.add_hotkey('ctrl+alt+shift+s', lambda: write("Ŝ"))
    keyboard.add_hotkey('ctrl+alt+shift+h', lambda: write("Ĥ"))
    keyboard.add_hotkey('ctrl+shift+alt+u', lambda: write("Ŭ"))
    while True:
        keyboard.wait()
def write(string):
    print(string)
    time.sleep(.15)
    keyboard.write(string)
if __name__ == '__main__':
    main()