FROM jenkins/jenkins:lts

LABEL version="1.0" \
    description="jenkins master lts" \
    maintainer="wwek<licoolgo@gmail.com>"

# Install base pakages.
USER root
RUN apt-get -y update \
    &&  apt-get -y install apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*


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

