##############################################################
#                         CRIPT RC5XOR                       #
##############################################################


key = 'keys'# строковая переменная ключа, которую можно отредактировать
key_list=[ord(ch) for ch in key] #преобразование в список аскей кода


f_write = open('c:/draft/out.txt', 'w+',encoding='utf-8') #дополнительно вводим кодировку для корректной работы в линукс
with open('c:/draft/inp.txt', 'r') as f_read:
    # читаем файл по 4 байт
    chunk = f_read.read(4)
    
    while chunk:
        #print(chunk) #отладочный принт для вывода на экран
        key_chunk=[ord(ch) for ch in chunk] #построчное преобразование прочитанных символов в аскей код
        secret_chunk = [] #создание пустого скписка для последующей записи
        for i in range (len(key_chunk)): #цикл для побитового сложения ключа с сообщением
            secret_chunk.append(chr(key_list[i]^key_chunk[i])) 
            
        secret_message = (" ".join(map(str, secret_chunk))) #преобразование закодированного сообщения из списка в строку для последующей записи в выходной файл
        f_write.write(secret_message)
        chunk = f_read.read(4) #попытка прочитать очередные символы
f_write.close() #закрытие потока записи выходного файла


