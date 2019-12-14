FROM php:7.2-fpm-alpine

LABEL version="1.0" \
description="php-fpm7.2 alpine" \
maintainer="wwek<licoolgo@gmail.com>"

#install base
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk update \
    && apk upgrade \
    && apk add s6 \
    && apk add bash \
    && apk add openssl \
    && apk add openssl-dev \
    && apk add ca-certificates \
    && apk add wget \
    && apk add curl \
    && apk add tcpdump \
    && apk add iputils \
    && apk add iproute2 \
    && apk add libc6-compat \
    && apk add zlib \
    && apk add -U tzdata \
    && apk add libpng \
    && apk add libpng-dev \
    && apk add libstdc++ \
    && rm -rf /var/cache/apk/*

# 系统设置(设置时区)
RUN rm -rf /etc/localtime \
 && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# --- 安装扩展 --- #
# Core核心扩展
RUN docker-php-ext-install opcache mysqli pdo_mysql mbstring zip pcntl gd
# 三方扩展
# redis swoole
RUN set -xe \
    && apk add --no-cache --update --virtual .phpize-deps $PHPIZE_DEPS \
    && pecl install -o -f redis  \
    && pecl install -o -f swoole  \
    && echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini \
    && echo "extension=swoole.so" > /usr/local/etc/php/conf.d/swoole.ini \
    && rm -rf /usr/share/php \
    && rm -rf /tmp/* \
    && apk del  .phpize-deps

# --- 设置 --- #
# 设置php运行权限为母鸡中 www的用户和组 1000:1000
RUN addgroup -g 1000 -S www && \
    adduser -u 1000 -S www -G www www

# 设置php-fpm运行账户和组为 www www
# RUN set -ex \
#     && cd /usr/local/etc \
#     && { \
#         echo 'listen.owner = www'; \
#         echo 'listen.group = www'; \
#         echo 'listen.mode = 0660'; \
#     } | tee php-fpm.d/www.conf

# 增加配置文件
ADD www.conf /usr/local/etc/php-fpm.d

# 工作目录
WORKDIR /data/wwwroot
