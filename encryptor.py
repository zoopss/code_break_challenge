import pyperclip

message = raw_input("Enter the message to be encrypted...")
i = len(message) - 1
translated = ''
translated1 = ""
translated2 = ""
while i >= 0 :
    if i % 2 == 0:
        translated1 = translated1 + message[i]

    elif i % 2 == 1:
        translated2 = translated2 + message[i]
    i = i-1

translated = translated2 + translated1
print translated
pyperclip.copy(translated)
