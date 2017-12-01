import requests


def getRobots(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print("有Robots协议")
            print(r.text)
        else:
            print("无Robots协议")
    except:
        print("Robots检测失败！")


if __name__ == '__main__':
    getRobots("http://www.hnnu.edu.cn/robots.txt")
