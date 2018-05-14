from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.base_request import *
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.txt_io import *
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.adjust_string import adjust_string
from time import sleep
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.adjust_string import *

"""
这是天天基金查询统计功能简化的函数

\\匹配Daily_running是Daily_running的出导入py\\

参数1：filepath：文件路径（str）格式
    基金数值为6位连续字符串，本函数自动切割

返回值：0：vield——日增长率-float()
        1：upper_less_1_list——涨幅0-1之间基金-[]
        2：lower_less_1_list——跌幅0-1之间基金-[]
        3：upper_than_1_list——涨幅过1基金-[]
        4：lower_than_1_list——跌幅过1基金-[]
        5：upper_than_2_list——涨幅过2基金-[]
        6：lower_than_2_list——得福过2基金-[]

"""

def fund_static_main(filepath):
    # 读取部分
    read_file_request = read_file(filepath)

    # 寄存部分
    fund_code_list = []  # 基金代码列表——A
    fund_info_dict = {}  # 基金数据字典——B
    vield = 0.0
    # 涨跌基金字典{}
    upper_less_1 = [] # 增长在1内基金——C
    lower_less_1 = []  # 下跌在1内基金——D
    upper_than_1 = []  # 大于1的基金——E
    lower_than_1 = []  # 小于1的基金——F
    upper_than_2 = []  # 大于2的基金——G
    lower_than_2 = []  # 小于2的基金——H
    # 执行部分
    for i in range(int(len(read_file_request) / 6)):  # 制作基金代码列表——A
        c = read_file_request[i * 6:i * 6 + 6]
        fund_code_list.append(c)



    for i in range(len(fund_code_list)):  # 制作基金字典——B
        a = request_part(fund_code_list[i])
        fund_name = made_date(a)[0]
        fund_rate = made_date(a)[1]
        veild = made_date(a)[2]
        fund_date = made_date(a)[3]
        knock_together = "{'" + fund_code_list[
            i] + "':{'fund_name':'" + fund_name + "','fund_rate':'" + fund_rate + "','veild':'" + veild + "','fund_date':'" + fund_date + "'}}"
        knock_together = eval(str(knock_together))
        fund_info_dict.update(knock_together)


    for i in range(len(fund_code_list)):  # 筛选不同涨跌——CDEFGH
        vield = vield + float(fund_info_dict[fund_code_list[i]]['veild'])  # ——
        present_fund_code = fund_code_list[i]
        present_fund_info = fund_info_dict[present_fund_code]
        final_string = out_put_string(present_fund_code,present_fund_info)
        if_code = float(present_fund_info['veild'])
        if 0 <= if_code < 1:
            upper_less_1.append(final_string)
        if -1 < if_code < 0:
            lower_less_1.append(final_string)
        if if_code >= 1:
            upper_than_1.append(final_string)
        if if_code <= -1:
            lower_than_1.append(final_string)
        if if_code >= 2:
            upper_than_2.append(final_string)
        if if_code <= -2:
            lower_than_2.append(final_string)


    vield = round(vield/len(fund_code_list),2)


    return vield, upper_less_1, lower_less_1, upper_than_1,lower_than_1, upper_than_2, lower_than_2

def request_part(code):
    sleep(0.1)
    a = base_request('http://fundgz.1234567.com.cn/js/'+code+'.js?rt=1463558676006')
    return a

def read_file(filepath):
    rep = read_file_inline(filepath)
    return rep

def made_date(back_date):
    a = back_date
    fund_name = adjust_string(a[a.find('name') + 7:a.find('jzrq') - 3], 19, ' ')  # 名称
    fund_rate = a[a.find('gszzl') + 8:a.find('gztime') - 3] + '%'  # 增长值
    veild=a[a.find('gszzl') + 8:a.find('gztime') - 3]
    fund_date = a[a.find('gztime') + 17:a.find('"});') - 6]
    return fund_name,fund_rate,veild,fund_date

def out_put_string(present_fund_code,present_fund_info):
    out_put = str(present_fund_info['fund_name']) + ' ' + '估值收益率为： ' + adjust_string(present_fund_info['fund_rate'], 7,\
    ' ') + '   (' + str(present_fund_code) + ')'
    return out_put

def single_fund_date(code):
    a = request_part(code)
    a = made_date(a)
    return a


if __name__ == '__main__':
    print()