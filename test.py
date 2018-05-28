from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.txt_io import *
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.adjust_string import *
filepath = 'C:\\Users\Administrator\Desktop\email.txt'
a = read_file_inline(filepath)
a = format_removeal(a)
# a = a.replace('.com','.com","')
# a = '["'+a[:-2]+"]".replace('"',"'")
a=eval(a)
print(len(a))