FROM python:3.8-slim

# 备份默认软件源
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
# 替换软件源为清华镜像站
COPY sources.list /etc/apt/
# 安装Daphne的过程中可能需要编译原生代码，所以需要安装GCC编译器
RUN apt update&&apt install -y gcc make
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple daphne
