from common_module_and_fuction.base_request import *
from common_module_and_fuction.adjust_string import *
from fundition_static_packaging.TianTianfundition_static_module import *
from common_module_and_fuction.put_txt_in_dictionary import *
"""
{'002001':——基金代码(fund_code)
	{
	'fund_name':'string',——基金名称
	'fund_in_date':'datetime',——买入日期
	'fund_vield_rate':——持有收益数组
			['datetime1':'value'],
	'fund_purchase':'value',——购买数量
	'fund_latest_price':'value'——最新价格
	}
}

{'002001':{'fund_name':'string','fund_in_date':'datetime','fund_vield_rate':['datetime1':'value'],'fund_purchase':'value','fund_latest_price':'value'}}

基金小项目
标准数据结构

脚本组成方式：【通过不同的位置拼接成为数据字典】
"""

# fund_code = input()
"""
函数零件部分
"""
#获取基金名称，传入基金代码，传出基金名称
def fund_name_get(fund_code):
    _string = base_request('http://fundgz.1234567.com.cn/js/'+fund_code+'.js?rt=1463558676006')
    _string = find_and_cut(_string,',"name":"','","jzrq"')
    _string = adjust_string(_string, 12, ' ')
    fund_name = _string

    return fund_name

def fund_in_date_get(fund_code):
    _string =  read_file_inline('D:\\Python_Lib_local\基金计算\基金文件\个人基金买入时间.txt')
    change_string = _string.replace(" ","").replace("\t","").strip().replace('\n','')
    _dict = eval(change_string)
    _keys = _dict.keys()
    _keys = list(_keys)
    _ifcode = 0
    try:
        a=_keys.index(fund_code)
    except Exception:
        _ifcode = 1
    if _ifcode==1:
        print('程序出错：输入fund_code,未在持有基金数据中')
    else:
        pass
    # print(a)

def fund_vield_rate_get():

    return

def fund_purchase_get():

    return

def fund_latest_price_get():

    return

"""
test
"""
from fundition_static_packaging.singleness_fund_inquire import *
from common_module_and_fuction.base_request import *
from common_module_and_fuction.adjust_string import *
from common_module_and_fuction.txt_io import *
import os
if __name__ == '__main__':
    read_file_inline('')