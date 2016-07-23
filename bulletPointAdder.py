#!/usr/bin/env python3
import pyperclip
text = pyperclip.paste()
splitText = text.split('\n')
for i in range(len(splitText)):
    splitText[i] = '* ' + splitText[i]
text = '\n'.join(splitText)
pyperclip.copy(text)
