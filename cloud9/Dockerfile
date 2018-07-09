# Pull base image.
FROM wwek/centos

LABEL version="1.0" \
    description="Cloud9 WEB IDE" \
    maintainer="wwek<licoolgo@gmail.com>"

#-------------------------------------------------------------------------------
# Install Aliyun Repo Mirror
RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup \
    && curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo \
    && yum makecache

# ------------------------------------------------------------------------------
# Install base packages.
RUN yum install -y gcc-c++ make git glibc-static which unzip wget vim tmux screen \
 && yum clean all && rm -rf /var/cache/yum/


# ------------------------------------------------------------------------------
# Add volumes
ENV WORKSPACE=/workspace
RUN mkdir $WORKSPACE
VOLUME $WORKSPACE

# ------------------------------------------------------------------------------
# Install Node.js
# RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash - \
#     && yum install -y nodejs \
#     && npm config set registry http://registry.npm.taobao.org

RUN  yum install -y nodejs npm --enablerepo=epel \
    && npm config set registry http://registry.npm.taobao.org

# ------------------------------------------------------------------------------
# Install Cloud9
ENV CLOUD9_ROOT /usr/local/cloud9
RUN git clone https://github.com/c9/core.git $CLOUD9_ROOT
WORKDIR $CLOUD9_ROOT
RUN scripts/install-sdk.sh

# Tweak standlone.js conf
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' $CLOUD9_ROOT/configs/standalone.js 


# ------------------------------------------------------------------------------
# Install PHP
ENV PHP_VERSION=7.2.7
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm \
&& yum install -y php72w php72w-opcache php72w-mysql php72w-pdo php72w-mbstring php72w-gd \
   php72w-imap php72w-ldap php72w-odbc php72w-pear php72w-xml php72w-xmlrpc \
   php72w-devel \
&& pecl install igbinary redis \
&& echo 'extension=igbinary.so' > /etc/php.d/igbinary.ini \
&& echo 'extension=redis.so' > /etc/php.d/redis.ini \
&& mkdir -p $WORKSPACE/php \
&& yum clean all && rm -rf /var/cache/yum/

# ------------------------------------------------------------------------------
# Install PHP Composer
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /tmp
ENV COMPOSER_VERSION 1.6.5
RUN curl -s -f -L -o /tmp/installer.php https://raw.githubusercontent.com/composer/getcomposer.org/fe44bd5b10b89fbe7e7fc70e99e5d1a344a683dd/web/installer \
 && php -r " \
    \$signature = '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061'; \
    \$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \
    if (!hash_equals(\$signature, \$hash)) { \
        unlink('/tmp/installer.php'); \
        echo 'Integrity check failed, installer is either corrupt or worse.' . PHP_EOL; \
        exit(1); \
    }" \
 && php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer --version=${COMPOSER_VERSION} \
 && composer --ansi --version --no-interaction \
 && rm -rf /tmp/* /tmp/.htaccess

# ------------------------------------------------------------------------------
# Install Golang
ENV GO_VERSION=1.10.3
RUN wget --no-check-certificate https://dl.google.com/go/go$GO_VERSION.linux-amd64.tar.gz \
&& tar zxvf go$GO_VERSION.linux-amd64.tar.gz -C /usr/local/ \
&& mkdir -p $WORKSPACE/go \
&& rm -rf go$GO_VERSION.linux-amd64.tar.gz

RUN echo " " >> /root/.bashrc  \
&& echo 'WORKSPACE=/workspace' >> /root/.bashrc  \
&& echo 'GOROOT=/usr/local/go' >> /root/.bashrc  \
&& echo 'GOBIN=$GOROOT/bin' >> /root/.bashrc  \
&& echo 'GOPATH=$WORKSPACE/go' >> /root/.bashrc  \
&& echo 'export WORKSPACE' >> /root/.bashrc  \
&& echo 'export GOROOT' >> /root/.bashrc  \
&& echo 'export GOBIN' >> /root/.bashrc  \
&& echo 'export GOPATH' >> /root/.bashrc  \
&& echo 'export PATH=$PATH:$GOBIN:$GOPATH/bin' >> /root/.bashrc

ENV GOROOT /usr/local/go
ENV GOBIN $GOROOT/bin
ENV GOPATH $WORKSPACE/go
ENV PATH $PATH:$GOBIN:$GOPATH/bin


# ------------------------------------------------------------------------------
# Add Dev Tools
RUN yum groupinstall -y "Development Tools" \
 && yum install -y telnet bind-utils mtr tcpdump wireshark httpry psmisc \
 && yum clean all && rm -rf /var/cache/yum/

# ------------------------------------------------------------------------------
# Add S6 conf
RUN mkdir -p /etc/services.d/cloud9/ && ln -s /bin/true /etc/services.d/cloud9/finish
ADD conf/cloud9.run /etc/services.d/cloud9/run
ADD conf/cloud9.conf /etc/supervisor/conf.d/

# ------------------------------------------------------------------------------
# Add Monit conf

# ------------------------------------------------------------------------------
# Clean up  when done AND other
USER root
ENV CLOUD9_AUTH="admin:cloud9"

# ------------------------------------------------------------------------------
# Expose ports.
# SSH
EXPOSE 22
# WEB
EXPOSE 80 81 82 83 84 85 86 87 88 89 90 8080 8888
# 
EXPOSE 3000

# mysql
EXPOSE 3306
# redis
EXPOSE 6379
#mongodb
EXPOSE 27017
#memcache
EXPOSE 11211 
#postgresql
EXPOSE 5432


# ------------------------------------------------------------------------------
# Start S6, define default command.
ENTRYPOINT ["/init"]
