FROM golang:alpine

LABEL version="1.0" \
    description="golang:alpine" \
    maintainer="wwek<licoolgo@gmail.com>"

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
  && apk add git \
 rm -rf /var/cache/apk/*

# 系统设置(设置时区)
RUN rm -rf /etc/localtime \
 && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 安装包管理工具
RUN go get -v -u github.com/tools/godep \
 && curl https://glide.sh/get | sh

CMD ["/bin/bash"]