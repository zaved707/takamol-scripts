import pyperclip
from tkinter import Tk, Label, Entry, Button
from tkcalendar import Calendar

def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Text copied to clipboard:")
    print(text)

def set_custom_date():
    def set_date():
        selected_date = cal.get_date()
        original_text = f"{selected_date} SECOND SESSION (03:30) EVALUATION FORM SCAN AND PROFILE PICTURES PDF"
        copy_to_clipboard(original_text)
        root.destroy()

    root = Tk()
    root.title("Set Custom Date")

    label = Label(root, text="Select Custom Date:")
    label.pack()

    cal = Calendar(root, selectmode="day", date_pattern="dd.mm.yyyy")
    cal.pack()

    confirm_button = Button(root, text="Confirm", command=set_date)
    confirm_button.pack()

    root.mainloop()

if __name__ == "__main__":
    set_custom_date()
