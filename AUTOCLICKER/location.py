import pyautogui
import keyboard
import time

def show_mouse_location():
    try:
        while True:
            x, y = pyautogui.position()
            position_str = f"Mouse position: x={x}, y={y}"
            print(position_str)
            if keyboard.is_pressed('x'):
                with open("coordinates.txt", "a") as file:
                    user_input = input("Enter a value: ")
                    file.write(f"{user_input}: {position_str}\n")
            elif keyboard.is_pressed('ctrl+q'):
                break
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    print("Press 'x' to save current coordinates with input.")
    print("Press 'Ctrl+q' to stop.")
    show_mouse_location()
