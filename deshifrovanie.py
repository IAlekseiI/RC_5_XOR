
in_file = open('c:/draft/out.txt','r', encoding= 'utf-16')
out_file = open('c:/draft/decr.txt','w+', encoding= 'utf-16')

print('введите ключ')
key = input()
len_key = len(key)

with in_file as my_file:
    # итерация по строкам
    for line in my_file:
        len_str = (len(line)) #  длина строки
        # line   строка
        print('\n')
        n_string=[]
        
        block=len_str
        for j in range(0,4):
            key=key[-1]+key[:-1]
            print('key = ',key)
            for i in range(0,(len(line)),block):
                print(line[i:(i+block)])
        
        for w in range(0,len(line), 9):
            k = len(line)//len_key+1
            n_key= key*k
            w_string=line[w:w+8]
            
            if w_string != '\n' and len(w_string)>=8:
                d_string = int(w_string, base = 2)
            #char=chr(d_string[w]^ord(n_key[w]))
               
            n_string.append(int(d_string))
        print(n_string)
        for i in range(0, len(n_string)):
            chunk = n_string[i]^ord(n_key[i])
            if chunk == 103 or chunk == 127:
                n = ' '    
            n=chr(chunk)
            if n != '103':
                out_file.write(n)

out_file.close()
in_file.close()


