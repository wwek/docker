FROM jenkins/jenkins:lts

MAINTAINER wwek <licoolgo@gmail.com>

USER root

# Install the latest Docker CE binaries
RUN apt-get -y update \
    &&  apt-get -y install apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey  \
    && add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
      $(lsb_release -cs) \
      stable" \
    && apt-get -y update \
    && apt-get -y install docker-ce \
    && mkdir -p ~/.docker/ \
    && touch ~/.docker/config.json \
    && echo "{"registry-mirrors": ["https://registry.docker-cn.com"]}" > ~/.docker/config.json

# 系统设置(设置时区)
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime