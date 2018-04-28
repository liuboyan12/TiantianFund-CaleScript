##
#时间转换模块，将时间转换为不同的模式
#
import datetime
import time

def str_2_datetime(str_yyyy_mm_dd):
    #输入string的时间格式为  '2012-11-19'
    date_time = datetime.datetime.strptime(str_yyyy_mm_dd, '%Y-%m-%d')
    return date_time

def datetime_2_str(date_time):
    #输入时间类型格式为  '2018-03-02 00:00:00'
    date_time_type=date_time.strftime('%Y-%m-%d')
    return date_time_type

def datetime_2_sUnix(date_time):
    #传入格式为类型为  '2018-03-02 00:00:00'
    time_time = date_time.timetuple()
    time_time = time.mktime(time_time)
    time_time = str(time_time)[:-2]
    return  time_time

def datetime_2_msUnix(date_time):
    # 传入格式为类型为  '2018-03-02 00:00:00'
    time_time = datetime_2_sUnix(date_time)+'000'
    return time_time

def judge_unix(unixtime):
    ret_value = -1
    if unixtime.find('.')!=-1:
        str(unixtime).replace('.', '')
    else:
        if len(unixtime)<11:
            ret_value = 1
            #unix时间为秒级别的时候返回值为1
            return unixtime,ret_value
        if len(unixtime)>11 and len(unixtime)<=13:
            ret_value = 2
            #unix时间为毫秒级别时候返回值为2
            return unixtime, ret_value
        else :
            return unixtime, ret_value

def sUnix_and_msUnix(unixtime):
    return_value = judge_unix(unixtime)
    if return_value[2] == 1:
        return_result = str(return_value[1])+'000'
        return return_result
    if return_value[2] == 2:
        return_result = str(return_value[1])[:-3]
        return return_result

def msUnix_2_datetime(msunixtime):
    msunixtime = msunixtime[:-3]
    msunixtime = float(msunixtime)
    time = datetime.datetime.fromtimestamp(msunixtime)
    return time

def sUnix_2_datetime(sunixtime):
    sunixtime = float(sunixtime)
    time = datetime.datetime.fromtimestamp(sunixtime)
    return time

if __name__ == '__main__':
    a = datetime_2_sUnix(str_2_datetime('2018-03-02'))
    print(type(a))