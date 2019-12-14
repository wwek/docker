FROM centos:7

LABEL version="2.0" \
    description="Centos7 Base" \
    maintainer="wwek<licoolgo@gmail.com>"

# Install base packages.
RUN yum -y makecache && yum -y update \
 && yum -y install epel-release yum-plugin-ovl \
 && yum -y install ssh wget curl htop iftop  tcpdump  dnsutils \
 openssl openssl-devel iproute iproute-doc \
 crontabs less vim-minimal python34 python34-pip python2-pip \
 glibc-static which \
 && yum clean all && rm -rf /var/cache/yum/

 # && yum install openssh-server openssh-clients -y \
# && yum install supervisor -y \
# && systemctl enable sshd && systemctl start sshd \

# 系统设置(设置时区).
RUN rm -rf /etc/localtime \
 && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime


# Install pip2 pip3.
#RUN yum install -y  python34-pip python2-pip \
# && yum clean all && rm -rf /var/cache/yum/


# 处理目录
RUN mkdir -p /data
WORKDIR /data
      
ENV PACKAGES="\
  git \
#  mariadb \
#  mariadb-server \
  gcc \
  gc++ \
  cloc \
  flex \
  bison \
  bzip2 \
"


RUN yum install -y $PACKAGES  \
&& yum clean all && rm -rf /var/cache/yum/

# config logs path
RUN cd / && \
    git clone https://github.com/wufeifei/cobra && \
    cd cobra && \
    mkdir logs && \
    touch logs/cobra.log && \
    cp config.template config && \
    sed -i "s#host: 127.0.0.1#host: 0.0.0.0#" config && \
    sed -i "s#port: 5000#port: 5000#" config && \
    sed -i "s#secret_key: your_secret_key#secret_key: 07b7b67e61834f90fa8ca9f25eb58b4f#" config && \
    sed -i "s#max_size: 200#max_size: 1000#" config && \
    pip install -r requirements.txt
    
# Install official PhantomJS release
ENV PHANTOM_JS_VERSION ${phantomjs:-2.1.1-linux-x86_64}
RUN set -x \
 && mkdir -p /tmp/phantomjs \
 && curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOM_JS_VERSION}.tar.bz2 \
        | tar -xj --strip-components=1 -C /tmp/phantomjs \
 && mv /tmp/phantomjs/bin/phantomjs /usr/local/bin \
 && rm -rf /tmp/phantomjs

#RUN groupadd -r mysql \
#&& useradd -g mysql -r -s /sbin/nologin mysql \
#&& mkdir -p /run/mysqld && ls /var/lib \
#&& chown -R mysql:mysql /run/mysqld /var/lib/mysql \
#&& mysql_install_db --user=mysql --verbose=1 --basedir=/usr --datadir=/var/lib/mysql --rpm > /dev/null

RUN echo "#!/bin/sh" > /start.sh && \
    #echo "nohup mysqld --skip-grant-tables --bind-address 0.0.0.0 --user mysql > /dev/null 2>&1 &" >> /start.sh && \
    echo "sleep 3" >> /start.sh && \
    #echo "python /cobra/cobra.py --help &" >> /start.sh && \
    echo "python /cobra/cobra.py -H 0.0.0.0 -P 5000 &" >> /start.sh && \
    echo "tail -f /cobra/logs/cobra.log" >> /start.sh && \
    chmod u+x /start.sh
    
WORKDIR /cobra

EXPOSE 5000
#EXPOSE 3306

ENTRYPOINT ["/start.sh"]