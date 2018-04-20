def read_file_inline(filepath):
    f = open(filepath)
    p=f.read()
    f.close()
    return p

def out_put_inline(q,fielpath='C:\\Users\Administrator\Desktop\out_put.txt'):
    f = open(fielpath,'w')
    f.write(str(q))
    f.close()