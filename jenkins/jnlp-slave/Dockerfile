FROM jenkins/jnlp-slave:latest

LABEL version="latest" \
    description="jenkins jnlp slave" \
    maintainer="wwek<licoolgo@gmail.com>"

USER root
# 系统设置(设置时区)
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" >/etc/timezone

#ENV DOCKER_VERSION=19.03.2-ce DOCKER_COMPOSE_VERSION=1.14.0 KUBECTL_VERSION=v1.11.0

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

# Install docker
USER root
ENV DOCKER_VERSION=5:19.03.5~3-0~debian-stretch
RUN curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/debian/gpg | apt-key add - \
    && add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/debian $(lsb_release -cs) stable" \
    && apt-get -y update \
    && apt-cache madison docker-ce \
    && apt-get -y install docker-ce=$DOCKER_VERSION
RUN sudo usermod -aG docker jenkins

USER jenkins
# install docker cn mirrors
RUN mkdir -p ~/.docker/ \
    && touch ~/.docker/config.json \
    && echo '{"registry-mirrors": ["https://dockerhub.azk8s.cn","http://f1361db2.m.daocloud.io","https://hub-mirror.c.163.com","https://docker.mirrors.ustc.edu.cn","https://reg-mirror.qiniu.com"]}' > ~/.docker/config.json

# install docker
# RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz \
#     && tar --strip-components=1 -xvzf docker-${DOCKER_VERSION}.tgz -C /usr/local/bin \
#     && chmod -R +x /usr/local/bin/docker \

USER root
# install docker-compose
# RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-Linux-x86_64 -o /usr/local/bin/docker-compose \
#     && chmod +x /usr/local/bin/docker-compose

# install kubectl
RUN curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add - \
    && echo 'deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main'  >/etc/apt/sources.list.d/kubernetes.list \
    && apt-get update \
    && apt-get install -y kubectl

# RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey  \
#     && add-apt-repository \
#     "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
#     $(lsb_release -cs) \
#     stable" \
#     && apt-get -y update \
#     && apt-get -y install docker-ce \
#     && mkdir -p ~/.docker/ \
#     && touch ~/.docker/config.json \
#     && echo '{"registry-mirrors": ["https://registry.docker-cn.com"]}' > ~/.docker/config.json

# Install Golang
ENV GO_VERSION=1.13.5
RUN wget --no-check-certificate https://dl.google.com/go/go$GO_VERSION.linux-amd64.tar.gz \
    && tar zxf go$GO_VERSION.linux-amd64.tar.gz -C /usr/local/ \
    && rm -rf go$GO_VERSION.linux-amd64.tar.gz
ENV GOROOT /usr/local/go
ENV GOBIN $GOROOT/bin
#ENV GOPATH $WORKSPACE/go
ENV PATH $PATH:$GOBIN


# Install Nodejs
USER root
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs \
    && npm config set registry https://registry.npm.taobao.org \
    && npm config get registry

USER jenkins
# Install Android and Gradle
# Set up environment variables
ENV ANDROID_HOME="/home/jenkins/android-sdk-linux" \
    SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip" \
    GRADLE_URL="https://services.gradle.org/distributions/gradle-5.6.1-all.zip"
# Download Android SDK
RUN mkdir "$ANDROID_HOME" .android \
    && cd "$ANDROID_HOME" \
    && curl -o sdk.zip $SDK_URL \
    && unzip sdk.zip \
    && rm sdk.zip \
    && yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses
# Install Gradle
RUN wget $GRADLE_URL -O gradle.zip \
    && unzip gradle.zip \
    && mv gradle-5.6.1 gradle \
    && rm gradle.zip \
    && mkdir .gradle
ENV PATH="/home/jenkins/gradle/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${PATH}"


#  Install Maven
USER root
ARG MAVEN_VERSION=3.6.2
ARG USER_HOME_DIR="/home/jenkins"
# ARG SHA=b4880fb7a3d81edd190a029440cdf17f308621af68475a4fe976296e71ff4a4b546dd6d8a58aaafba334d309cc11e638c52808a4b0e818fc0fd544226d952544
ARG MAVEN_URL=http://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
    && curl -fsSL -o /tmp/apache-maven.tar.gz ${MAVEN_URL} \
    # && echo "${SHA}  /tmp/apache-maven.tar.gz" | sha512sum -c - \
    && tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 \
    && rm -f /tmp/apache-maven.tar.gz \
    && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn
ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

USER root