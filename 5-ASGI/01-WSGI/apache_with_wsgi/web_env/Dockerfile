FROM httpd:2.4.41

# 备份默认软件源
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
# 替换软件源为清华镜像站
COPY sources.list /etc/apt/
# 更新软件源
RUN apt-get update
# 安装Python运行环境以及C语言编译器用以编译WSGI
RUN apt-get install -y python3 python3-dev gcc g++ make
# 将WSGI源码复制到镜像中
COPY mod_wsgi-4.7.1.tar.gz /opt/
# 切换到工作目录
WORKDIR /opt/
# 解压WSGI源码包
RUN tar -zxvf ./mod_wsgi-4.7.1.tar.gz
# 切换到WSGI源码目录
WORKDIR /opt/mod_wsgi-4.7.1/
# 配置编译环境
RUN ./configure --with-apxs=/usr/local/apache2/bin/apxs --with-python=/usr/bin/python3
# 编译并安装
RUN make&&make install

# 对Apache服务器的配置文件进行修改，添加WSGI相关的配置项
# 包括加载WSGI动态库、配置脚本文件、配置脚本文件所在目录的权限
RUN echo 'LoadModule wsgi_module modules/mod_wsgi.so' >> /usr/local/apache2/conf/httpd.conf
RUN echo 'WSGIScriptAlias /app /opt/server/wsgi_app.py' >> /usr/local/apache2/conf/httpd.conf
RUN echo '<Directory /opt/server/>' >> /usr/local/apache2/conf/httpd.conf
RUN echo 'Require all granted' >> /usr/local/apache2/conf/httpd.conf
RUN echo '</Directory>' >> /usr/local/apache2/conf/httpd.conf
