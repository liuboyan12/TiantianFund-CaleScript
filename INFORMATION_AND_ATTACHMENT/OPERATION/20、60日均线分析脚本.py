from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.txt_io import *
from ANALYTIC_FUNCTION.script.RiJunXianFenXi import *

if __name__ == '__main__':
    import os
    pwd = os.getcwd()
    pwd =pwd.replace(":\\",':\\\\')
    filepath_all = pwd+'\INFORMATION_AND_ATTACHMENT\基金文件\\'
    # print(filepath)
    filename = ['个人基金.txt','媳妇基金.txt']

    for i in filename:
        txt_path = filepath_all+i
        fundcode = read_file_inline(txt_path)
        fund_list=[]
        for i in range(int(len(fundcode)/6)):
            append_code = fundcode[i*6:i*6+6]
            fund_list.append(append_code)
        print(fund_list)
        for i in fund_list:
            print(i)
            while 1<2:
                try:
                    comprehensive_fundition(i,'2018-04-18')
                    break
                except Exception as e:
                    print(e)
                    continue