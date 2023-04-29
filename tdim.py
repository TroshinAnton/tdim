import json
import codecs

print(
'''
████████╗██████╗░██╗███╗░░░███╗
╚══██╔══╝██╔══██╗██║████╗░████║
░░░██║░░░██║░░██║██║██╔████╔██║
░░░██║░░░██║░░██║██║██║╚██╔╝██║
░░░██║░░░██████╔╝██║██║░╚═╝░██║
░░░╚═╝░░░╚═════╝░╚═╝╚═╝░░░░░╚═╝
версия 0.2\n
''')


file = codecs.open("result.json", "r", "utf_8_sig" )
text = file.read()
file.close()

baza = json.loads(text)

it = 0

for person in baza['chats']['list']:
    try:
        print(it, person['name'])
        it += 1
    except KeyError as e:
        it += 1
        continue

select = int(input("Введи номер диалога: "))
cnt_of_messages = 0
cnt_of_words = 0
cnt_of_stickers = 0
cnt_of_letters = 0

for i in baza['chats']['list'][select]['messages']:
    try:
        cnt_of_stickers += i['media_type'] == 'sticker'
    except KeyError:
        pass
    
    cnt_of_words += i['text'].count(' ')
    if i['text'] != '':
        cnt_of_words += 1
    cnt_of_messages += 1
    cnt_of_letters += len(i['text'])
    
print('\n!!!!!!!!!!!!!!')
print("Количество сообщений:", cnt_of_messages)
print("Количество символов:", cnt_of_letters)
print("Количество слов:", cnt_of_words)
print("Количество стикеров:", cnt_of_stickers)
print('!!!!!!!!!!!!!!')
input('Нажми Enter для выхода')