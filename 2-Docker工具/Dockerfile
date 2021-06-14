# 指定该镜像基于python:3.8-alpine
FROM python:3.8-alpine
# 将py文件复制到镜像中的/opt目录下
COPY aio_http_server.py /opt/
# 指定该镜像启动后的默认运行命令，通过该命令启动HTTP服务器
CMD python /opt/aio_http_server.py
