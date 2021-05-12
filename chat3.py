filename = '/Users/yuanke.tsai/Desktop/coding/chat/chat_file/chat3/3.txt'

lines = []
with open(filename, 'r', encoding='utf-8-sig') as file:
    for line in file:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    chat = s[1:]
    #print(time)
    print(name, chat)