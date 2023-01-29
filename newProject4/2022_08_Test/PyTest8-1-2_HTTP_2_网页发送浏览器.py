''' Python学习 8-1-2
    http 2 :
    将网页发送给浏览器显示
'''

from socket import *

# 搭建tcp网络
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(3)
    print("Listen the port 8000...")
    while True:   # 循环接收
        connfd,addr = sockfd.accept()
        handle(connfd)  # 处理浏览器请求
        connfd.close()  # 关闭本次连接


# 处理浏览器的http请求
def handle(connfd):
    print("Request from",connfd.getpeername())   # 获取套接字地址
    request = connfd.recv(4096)  # 接收http请求
    # 防止客户端断开
    if not request:
        return

    # 将request 按行分割    33：33
    request_line = request.splitlines()[0].decode()  # 选择第一行 转为字符串格式
    info = request_line.split(' ')[1]   # 以空格分割字符串，选择第二个

    if info == '/':
        f = open('index.html')   # 拼接HTTP相应码 和 相应内容网页
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += "\r\n"
        response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"  # 未找到网页发送错误提示
        response += "Content-Type: text/html\r\n"
        response += "\r\n"
        response += "<h1> Sorry: Not found you input the page  </h1>"
    # 向浏览器发送内容
    connfd.send(response.encode())



if __name__ == "__main__":
    main()
