from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import *
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.TianTianfundition_static_module import *

if __name__ == '__main__':
    all_fund = all_fundcode_2_list()
    # print(all_fund)
    i = iter(all_fund)
    code_and_rate = []
    for x in i:
        try:
            _return = request_part(x)
        except Exception as e:
            if e != 'HTTP Error 404: Not Found':
                _return = format_removeal(_return)
                rate = find_and_cut(_return,'gszzl":"','","gztime"')
                # print('x',x)
                # print("rate",rate)
                _string = '['+str(x)+':'+"'"+str(rate)+"'"+']'
                # print(_string)
                code_and_rate.append(_string)
                print(code_and_rate)
            else:
                pass
    print(code_and_rate)