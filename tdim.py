import json
import codecs
import sys

class TDIMError(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return self.err
        
print(
'''
████████╗██████╗░██╗███╗░░░███╗
╚══██╔══╝██╔══██╗██║████╗░████║
░░░██║░░░██║░░██║██║██╔████╔██║
░░░██║░░░██║░░██║██║██║╚██╔╝██║
░░░██║░░░██████╔╝██║██║░╚═╝░██║
░░░╚═╝░░░╚═════╝░╚═╝╚═╝░░░░░╚═╝
версия 0.2.2\n
''')

try:
    filename = 'result.json'
    if len(sys.argv) > 2 and sys.argv[1] == '--file':
        filename = sys.argv[2]
        
    file = codecs.open(filename, 'r', 'utf_8_sig')
    text = file.read()
    file.close()
except FileNotFoundError:
    raise TDIMError(f'JSON-файл {filename} не найден')

baza = json.loads(text)

it = 0

for person in baza['chats']['list']:
    try:
        print(it, person['name'])
        it += 1
    except KeyError:
        it += 1
        continue

select = int(input('Введи номер диалога: '))
cnt_of_messages = 0
cnt_of_words = 0
cnt_of_stickers = 0
cnt_of_letters = 0
cnt_of_select = 0

for i in baza['chats']['list'][select]['messages']:
    try:
        cnt_of_stickers += i['media_type'] == 'sticker'
    except KeyError: pass
    
    try:
        cnt_of_select += i['from'] == baza['chats']['list'][select]['name']
    except KeyError: pass
    
    cnt_of_words += i['text'].count(' ')
    if i['text'] != '':
        cnt_of_words += 1
    cnt_of_messages += 1
    cnt_of_letters += len(i['text'])
    
print('\n!!!!!!!!!!!!!!')
print('Количество сообщений:', cnt_of_messages)
print('Количество символов:', cnt_of_letters)
print('Количество слов:', cnt_of_words)
print('Количество стикеров:', cnt_of_stickers)
print("Сообщений от", baza['chats']['list'][select]['name'] + ':', cnt_of_select)
print("Сообщений от Вас:", cnt_of_messages - cnt_of_select)
print('!!!!!!!!!!!!!!')
input('Нажми Enter для выхода')

