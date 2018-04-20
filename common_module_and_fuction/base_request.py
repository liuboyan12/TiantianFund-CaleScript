
import urllib.request
def base_request(str):
    response = urllib.request.urlopen(str)
    return response.read().decode(encoding='utf-8')

if __name__ == '__main__':
    print()