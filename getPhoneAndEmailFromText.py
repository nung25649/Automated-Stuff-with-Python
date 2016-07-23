import pyperclip, re

text = str(pyperclip.paste())
phoneRegex = re.compile('''(
    (\d{3})     #first 3 digits
    (-|\s|\.)      #separator
    (\d{7}|(\d{3})(-|\s|\.)(\d{4})) #last 4 digits, separated or bunched
    )''', re.VERBOSE)
emailRegex = re.compile(r'(([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9-]+).([a-zA-Z.]+))')

matches = []
for num in phoneRegex.findall(text):
    if num[3][3] in ' .':
        matches.append(num[1] + '-' + num[3][:3] + '-' + num[3][4:])
    elif num[3][3] != '-':
        matches.append(num[1] + '-' + num[3][:3] + '-' + num[3][3:])
    else:
        matches.append(num[0])
for email in emailRegex.findall(text):
    matches.append(email[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('no email and phone number found')


