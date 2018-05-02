from  BASE_CONDITIONING_MODES_AND_FUCTIONS.txt_io import *
from BASE_CONDITIONING_MODES_AND_FUCTIONS.base_request import base_request

filepath = 'D:\\Python_Lib_local\基金计算\基金文件\关注基金列表.txt'
every_number = []
final_result = []
out_put = ''
a = read_file_inline(filepath)#读取到文件
sum_of_dict = int(len(a) / 6)#字典内容数量
for i in range(int(len(a) / 6)):#切分的6位代码放进字典里面
   cut_string = a[i * 6:i * 6 + 6]
   every_number.append(cut_string)

for i in range(len(every_number)):

    request_result = base_request('http://fundgz.1234567.com.cn/js/'+every_number[i]+'.js?rt=1463558676006')
    num_code = request_result.find(every_number[i])

    if num_code != -1:
        final_result.append(every_number[i])
for i in range(len(final_result)):
    out_put_string = final_result[i]
    out_put = str(out_put)+str(out_put_string)

out_put_inline(filepath,out_put)
