
in_file = open('c:/draft/inp.txt','r', encoding= 'utf-16')
out_file = open('c:/draft/out.txt','w+', encoding= 'utf-16')

key = 'mouse'
len_key = len(key)

with in_file as my_file:
    # итерация по строкам
    for line in my_file:
        len_str = (len(line)) #  длина строки
        # line   строка
        
        #   выраниваем ключ
        k=(len_str//len_key+1)
        s_key = key*k
        for i in range (0,len(line)):
            symb=line[i] #  один символ
            symb_key=s_key[i]
            enc_symb=ord(symb)^ord(symb_key)
            w_enc_symb=bin(enc_symb)
            a=str(w_enc_symb[2:])
            n=8-len(a)
            b='0'*n+a
            out_file.write(b +' ')
        out_file.write('\n')         
        

out_file.close()
in_file.close()