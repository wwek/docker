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

# 配置sshd.
#RUN mkdir /var/run/sshd \
# && ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key \
# && ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key \
# && ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key \
# && ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key


# 开放开发常用端口.
#EXPOSE 22

# bash
#CMD ["/bin/bash"]

# 入口设置为ssh.
#ENTRYPOINT ["/usr/sbin/sshd", "-D"]


# Install confd.
ENV CONFD_VERSION 0.15.0
RUN curl -L "https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-linux-amd64" > /usr/bin/confd && \
    chmod +x /usr/bin/confd
ENV CONFD_OPTS '--backend=env --onetime'


# Install s6-overlay 进程守护管理.
ENV S6_VERSION v1.21.4.0
RUN curl -L "https://github.com/just-containers/s6-overlay/releases/download/$S6_VERSION/s6-overlay-amd64.tar.gz" > /tmp/s6-overlay-amd64.tar.gz
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / --exclude="./bin" && \
    tar xzf /tmp/s6-overlay-amd64.tar.gz -C /usr ./bin \
    && rm /tmp/s6-overlay-amd64.tar.gz
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS 1

# Set up a standard volume for logs.
VOLUME ["/var/log/services"]


# 设置入口为 s6-based init.
ENTRYPOINT ["/init"]

