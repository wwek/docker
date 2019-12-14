FROM jenkins/jenkins

LABEL version="latest" \
    description="jenkins master" \
    maintainer="wwek<licoolgo@gmail.com>"

USER root
# install aliyun repo
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak \
    && echo 'deb http://mirrors.aliyun.com/debian/ stretch main non-free contrib'  >/etc/apt/sources.list \
    && echo 'deb-src http://mirrors.aliyun.com/debian/ stretch main non-free contrib'  >>/etc/apt/sources.list \
    && echo 'deb http://mirrors.aliyun.com/debian-security stretch/updates main'  >>/etc/apt/sources.list \
    && echo 'deb-src http://mirrors.aliyun.com/debian-security stretch/updates main'  >>/etc/apt/sources.list \
    && echo 'deb http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib'  >>/etc/apt/sources.list \
    && echo 'deb-src http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib'  >>/etc/apt/sources.list \
    && echo 'deb http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib'  >>/etc/apt/sources.list \
    && echo 'deb-src http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib'  >>/etc/apt/sources.list \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && apt-get update

# Install base pakages.
RUN apt-get update -qq && apt-get install -y -qq --no-install-recommends \
    git \
    gcc \
    gcc+ \
    make \
    automake \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# 系统设置(设置时区)
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" >/etc/timezone

# Switch user to jenkins
USER jenkins

# Install Jenkins Plugins
#RUN /usr/local/bin/install-plugins.sh ansicolor \
#&& /usr/local/bin/install-plugins.sh greenballs \
#&& /usr/local/bin/install-plugins.sh kubernetes

# COPY plugins.txt /usr/share/jenkins/plugins.txt
# RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt