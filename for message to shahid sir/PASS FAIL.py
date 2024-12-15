import pyperclip
from datetime import datetime

# Get the current date in the format 02.05.2024
current_date = datetime.now().strftime("%d.%m.%Y")

# Original text
original_text = '''TOTAL:-

PASS:-

FAIL:-
'''

# Copy the text to clipboard
pyperclip.copy(original_text)

# Notify the user
print("Text copied to clipboard:")
print(original_text)
