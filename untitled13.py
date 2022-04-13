#   input message
#   ввод сообщения
message = input("Input Your message here: ")
message_list=[ord(ch) for ch in message]
# print(message_list[3],' ',type(message_list[3]),' ',message_list[2]," ", message_list[2]^message_list[3],"    ",chr(message_list[2]^message_list[3]))
print(message_list)

#   input secret key
#   ввод ключа
key=input("Input Your Secret KEY here: ")
key_list=[ord(ch) for ch in key]
print(key_list)

# блок выравнивания размера ключа и сообщения
if len(message_list) < len(key_list):
    while len(message_list) < len(key_list):
        message_list.append(0)

if len(message_list) > len(key_list):
    while len(message_list) > len(key_list):
        key_list.append(0)

 #  блок вывода кодир. сообщ
secret_message = [] # пустой список под шифр
for i in range (0, len(message_list)): # перебор сообщения и ключа
    secret_message.append(message_list[i]^key_list[i]) # шифрование складыванием по модулю 2
print("-------secret message = ", secret_message) # вывод кодир. сообщ

 #  блок вывода декодир. сообщ
new_message = [] # пустой список под дешифр
for j in range (0, len(secret_message)): # перебор сообщения и ключа
    bbb = secret_message[j]^key_list[j]
    bbb = chr(bbb)
    new_message.append(bbb) # дешифрование складыванием по модулю 2
print("new message = ", new_message, sep="", end="") # вывод декодир. сообщ


