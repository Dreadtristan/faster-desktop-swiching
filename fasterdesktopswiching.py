import keyboard
while True:
    if keyboard.read_key() == "end":
        keyboard.press_and_release('ctrl+windows+right_arrow')
    if keyboard.read_key() == "home":
        keyboard.press_and_release('ctrl+windows+left_arrow')
