"""
# 使用说明：python(3.x)
# adjust_string()函数，传入参数为：字符串（str）/总长半角位数（）/填充内容（半角str）
# 例如字符串'12345678啊'
# 如果需要截取8位长度，返回'12345678'
# 如果需要截取9位就会判断截取位最后一位是不是全角字符，如果是那么就不截取这个字符，补一个filler进去依然还是半角的9位
# 如果需要截取11位就会在后面补一个filler
"""
#裁剪函数传入字符串和裁切字符串长度（半角）
def adjust_string(string,digit,filler):
    strings=str(string)
    p=all_digit(string)[0]
    if p>digit:
        a=crop_string(string,digit,filler)
        return a
    if p<=digit:
        b=fill_string(strings,digit,filler)
        return b

#传入string，返回值为:全部位数，全角位数，半角位数
def all_digit(string):
    quanjiao = 0
    banjiao = 0
    for i in range(len(string)):
        p = string[i].encode('utf-8')
        q=len(p)
        if q == 3 :
            quanjiao=quanjiao+1
        if q == 1:
            banjiao=banjiao+1
        sum1 = quanjiao*2+banjiao
    return sum1,quanjiao,banjiao

#填充字符串(传入字符串，位数-半角）
def fill_string(string,digit=10,filler=' '):
    quanjiao=all_digit(string)[1]
    banjiao=all_digit(string)[2]
    digit=digit-quanjiao*2-banjiao
    string=string+digit*filler
    return  string

#裁切字符串（传入字符串，位数-半角）
def crop_string(string,digit=10,filler=' '):
         strs=''
         dig=digit
         for i in range(len(string)):
            p = string[i]
            o = p.encode('utf-8')
            q = len(o)
            if q == 3:
                dig = dig - 2
            if q == 1:
                dig = dig - 1
            if dig > 0:
                strs = strs + string[i]
            if dig == 0:
                strs = strs + string[i]
                break
            if dig < 0:
                strs = strs + filler
                break
         return strs

#传入参数为要切割的字符串strings，查找的起点字符串cut_point1,和结束字符串
def find_and_cut(strings,cut_point1,cut_point2):
    return_string1 = format_removeal(strings)
    cut_point1 = format_removeal(cut_point1)
    cut_point2 = format_removeal(cut_point2)
    integer1 = int(return_string1.find(cut_point1))
    integer1 = int(integer1)+int(len(cut_point1))
    integer2 = return_string1.find(cut_point2)
    return_string = return_string1[integer1:integer2]
    return return_string

#格式化字符串，去掉所有乱七八糟的东西
def format_removeal(strings):
    return_strings =strings.replace(" ","").replace("\t","").strip().replace('\n','').replace('\r','').replace('\f','').replace('\0','')
    return return_strings
