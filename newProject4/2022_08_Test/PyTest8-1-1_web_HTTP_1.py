'''  8（多任务多线程）-1-1，
    HTTP传输协议：1。使用TCP协议，客户请求--服务解析--组织相应--发送回客户--解析展示
    HTTP请求( request)（请求行，请求头，空行，请求体）
        GET    /   HTTP/1.1    #/:  请求类别，请求内容， 协议版本   \r\n 换行

    http相应( response ) (相应行，相应头，空行，相应体）
        HTTP/1.1   200  OK     #/:  版本信息，相应码， 附加信息
          相应码：  1xx  提示信息，表示请求被接收
                    2xx  相应成功    200 请求成功
                    3xx  相应需要进一步操作，重定向
                    4xx  客户端错误    404 请求失败      5xx  服务器错误

    浏览器输入本机IP + 端口号，即可执行本代码
'''


from socket import *


so = socket()   # 1. 创建tcp套接字
so.bind(('0.0.0.0',8000))  # 2. 绑定本机
so.listen(3)  # 3 设置监听

c, addr = so.accept()  # 4 等待连接
print("Connect from: ",addr)
data = c.recv(4096)  # 接收数据
print(data)

# http相应格式
data = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>hello world  </h1>
"""
# c.send(b"OK")
c.send(data.encode())

c.close()   # 6 关闭客户端
so.close()   # 7 关闭套接字

