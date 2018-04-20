from fundition_static_packaging.TianTianJiJinShuJuChuLi import *

"""
传入值
"""
def stock_list(fundcode):
    _date = singleness_fund_inquire(fundcode)
    # _stock_date =cut_stock_date(_date)
    _result = cut_stock_date(_date)
    return _result





if __name__ == '__main__':
    # _stock_list=stock_list('002001')
    # print(_stock_list)
    _stock_list = "['0008582', '0003332', '6011551', '0005682', '6038331', '6002761', '0020432', '0007862', '0009632', '6038161']"
