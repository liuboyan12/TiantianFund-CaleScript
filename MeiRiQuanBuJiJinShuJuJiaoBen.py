from common_module_and_fuction.adjust_string import *
from fundition_static_packaging.TianTianfundition_static_module import *
from common_module_and_fuction. txt_io import *


if __name__ == '__main__':
    _list = read_file_inline('D:\\Python_Lib_Local\基金计算\基金文件\所有基金中可查询基金.txt')
    _list = eval(_list)
    print(_list)
    code_and_rate= []
    _string_final = ''

    for i in _list:
        # print(i)
        e = ''
        try:
            _return = request_part(i)
            _return = format_removeal(_return)
            rate = find_and_cut(_return, 'gszzl":"', '","gztime"')
            _string = "'" + str(i)+"'" + ':' + str(rate)
            _string_final = _string_final+','+_string
            print(_string_final)
        except Exception as e :
            if e!='':
                while_code = 0
                while(while_code<1):
                    try:
                        _return = request_part(i)
                        _return = format_removeal(_return)
                        rate = find_and_cut(_return, 'gszzl":"', '","gztime"')
                        _string = "'" + str(i) + "'" + ':' + str(rate)
                        _string_final = _string_final + ',' + _string
                    except Exception as e2:
                        pass
                    if_code = _string_final.find(i)
                    if if_code!=-1:
                        while_code = 2
                    else:
                        pass
        rate = round(float(_list.index(i)) / float(len(_list)) * 100, 3)
        print('完成率', rate, '%')
    _string_final = _string_final[1:]
    _string_final = _string_final[:-1]
    _string_final = '{'+_string_final+'}'
    _return = eval(_string_final)
    print(_string_final)
    print('输出文件')
    out_put_inline(_string_final)
