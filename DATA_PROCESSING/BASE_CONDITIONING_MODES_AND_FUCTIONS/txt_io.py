def read_file_inline(filepath,encoding = 'utf-8'):
    f = open(filepath,encoding=encoding)#),errors='ignore')
    p=f.read()
    f.close()
    return p

def out_put_inline(q,fielpath='C:\\Users\Administrator\Desktop\out_put.txt'):
    f = open(fielpath,'w',encoding='utf-8')
    f.write(str(q))
    f.close()