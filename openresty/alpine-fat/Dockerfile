FROM openresty/openresty:alpine-fat


LABEL version="1.0" \
description="openresty alpine-fat" \
maintainer="wwek<licoolgo@gmail.com>"

#install base
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk update \
 && apk upgrade \
 && apk add bash \
 && apk add openssl \
 && apk add openssl-dev \
 && apk add nghttp2-dev \
 && apk add ca-certificates \
 && apk add wget \
 && apk add curl \
 && apk add tcpdump \
 && apk add iputils \
 && apk add iproute2 \
 && apk add libc6-compat \
 && apk add -U tzdata \
 rm -rf /var/cache/apk/*

# 系统设置(设置时区)
RUN rm -rf /etc/localtime \
 && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime