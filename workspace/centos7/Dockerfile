FROM centos:7

LABEL version="1.1" \
description="Language:PHP7 Golang Nodejs Python3 Java" \
maintainer="wwek<licoolgo@gmail.com>"

ENV WORKSPACE="/workspace"

# 系统设置(设置时区).
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# Install base packages.
RUN yum -y makecache && yum -y update \ 
    && yum -y install epel-release yum-plugin-ovl \
    && yum -y install ssh wget curl htop iftop  tcpdump  dnsutils \
    openssl openssl-devel iproute iproute-doc \
    crontabs less vim-minimal python34 python34-pip python2-pip \
    glibc-static which \
    && yum clean all && rm -rf /var/cache/yum/

# Install base dev soft
RUN yum makecache && yum update -y \
    && yum groupinstall "Development Tools" -y \
    && yum install nodejs -y \
    && yum install java-1.8.0-openjdk java-1.8.0-openjdk-devel -y \
    && yum install python34-pip python2-pip -y \
    && yum clean all && rm -rf /var/cache/yum/

# Install sshd
RUN yum makecache && yum update -y \
    && yum install openssh-server openssh-clients -y \
    && sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config \
    && sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N '' \
    && ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' \
    && ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key -N '' \
    && yum clean all && rm -rf /var/cache/yum/


# Install PHP72
ENV PHP_VERSION=7.2.8
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm \
    && yum install -y php72w php72w-opcache php72w-mysql php72w-pdo php72w-mbstring php72w-gd \
    php72w-imap php72w-ldap php72w-odbc php72w-pear php72w-xml php72w-xmlrpc \
    php72w-devel \
    && pecl install igbinary redis \
    && echo 'extension=igbinary.so' > /etc/php.d/igbinary.ini \
    && echo 'extension=redis.so' > /etc/php.d/redis.ini \
    && mkdir -p $WORKSPACE/php \
    && yum clean all && rm -rf /var/cache/yum/

# Install PHP Composer
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /tmp
ENV COMPOSER_VERSION 1.5.2
RUN curl -s -f -L -o /tmp/installer.php https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer \
 && php -r " \
    \$signature = '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410'; \
    \$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \
    if (!hash_equals(\$signature, \$hash)) { \
        unlink('/tmp/installer.php'); \
        echo 'Integrity check failed, installer is either corrupt or worse.' . PHP_EOL; \
        exit(1); \
    }" \
 && php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer --version=${COMPOSER_VERSION} \
 && composer --ansi --version --no-interaction \
 && rm -rf /tmp/* /tmp/.htaccess

# Install Golang
ENV GO_VERSION=1.11
RUN wget --no-check-certificate https://dl.google.com/go/go$GO_VERSION.linux-amd64.tar.gz \
 && tar zxvf go$GO_VERSION.linux-amd64.tar.gz -C /usr/local/ \
 && mkdir -p /data/go \
 && rm -rf go$GO_VERSION.linux-amd64.tar.gz
ENV GOROOT /usr/local/go
ENV GOBIN $GOROOT/bin
ENV GOPATH $WORKSPACE/go
ENV PATH $PATH:$GOBIN:$GOPATH/bin

# 挂载目录
VOLUME $WORKSPACE
VOLUME /data

# 开放开发常用端口
EXPOSE 22
EXPOSE 80
EXPOSE 81
EXPOSE 88
EXPOSE 443
EXPOSE 3306
EXPOSE 8080
EXPOSE 8081

# bash
#CMD ["/bin/bash"]

# 入口设置为ssh
ENTRYPOINT ["/usr/sbin/sshd", "-D"]