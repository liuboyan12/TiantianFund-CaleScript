'519697'
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import *

_dict = singleness_fund_inquire('519697')
_dict = cut_Data_ACWorthTrend(_dict)
a = eval(daily_line_dict_assembly_test(_dict, 20))
_list = list(a.keys())
print(type(_list))
print(type(a), a[_list[-1]])