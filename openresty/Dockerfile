FROM openresty/openresty:centos


LABEL version="1.0" \
    description="openresty centos" \
    maintainer="wwek<licoolgo@gmail.com>"

# Install base packages.
RUN yum -y makecache && yum -y update \ 
    && yum -y install epel-release yum-plugin-ovl \
    && yum -y install ssh wget curl iftop dnsutils \
    openssl openssl-devel iproute \
    glibc-static which \
    && yum clean all && rm -rf /var/cache/yum/

# && yum install openssh-server openssh-clients -y \
# && yum install supervisor -y \
# && systemctl enable sshd && systemctl start sshd \

# 系统设置(设置时区).
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime