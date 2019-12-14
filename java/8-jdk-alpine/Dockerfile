FROM openjdk:8-jdk-alpine

LABEL version="8-jdk-alpine" \
    description="java 8-jdk-alpine" \
    maintainer="wwek<licoolgo@gmail.com>"

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk update \
    && apk upgrade \
    ##&& apk add s6 \
    ##&& apk add bash \
    #&& apk add nghttp2-dev \
    ##&& apk add ca-certificates \
    ##&& apk add wget \
    && apk add curl \
    #&& apk add tcpdump \
    #&& apk add iputils \
    #&& apk add iproute2 \
    && apk add libc6-compat \
    && apk add -U tzdata \
    && rm -rf /var/cache/apk/*

# 系统设置(设置时区)
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" >/etc/timezone