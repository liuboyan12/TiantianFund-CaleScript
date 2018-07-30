
import urllib.request
def base_request(str):
    response = urllib.request.urlopen(str)
    returnvalue = response.read().decode(encoding='utf-8')
    response.close()
    return returnvalue

if __name__ == '__main__':
    print()