FROM php:7.2-fpm-alpine

LABEL version="1.0" \
description="php-fpm7.2 alpine" \
maintainer="wwek<licoolgo@gmail.com>"

#install base
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk update \
    && apk upgrade \
    # && apk add s6 \
    && apk add supervisor \
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
    && apk add nginx \
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
    # && pecl install -o -f swoole  \
    && echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini \
    # && echo "extension=swoole.so" > /usr/local/etc/php/conf.d/swoole.ini \
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
ADD config/zz-docker.conf /usr/local/etc/php-fpm.d/
ADD config/php.ini /usr/local/etc/php/
COPY config/nginx/ /etc/nginx/
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# COPY s6/ /etc/s6/
# RUN chmod -R +x /etc/s6/* \
#     && chmod +x /etc/s6/.s6-svscan/finish

# install composer
# RUN \
#     &&  EXPECTED_SIGNATURE=$(wget -q -O - https://composer.github.io/installer.sig) \
#     && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
#     && php -r "if (hash_file('SHA384', 'composer-setup.php') === '$EXPECTED_SIGNATURE') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
#     && php composer-setup.php --install-dir=/usr/bin --filename=composer \
#     && php -r "unlink('composer-setup.php');"

## PHP 和 nginx设置
# make php-fpm listen to not tcp port but unix socket
RUN set -xe \
    && sed -i -E "s/127\.0\.0\.1:9000/\/var\/run\/php-fpm\/php-fpm.sock/" /usr/local/etc/php-fpm.d/www.conf \
    # install nginx and create default pid directory
    && mkdir -p /run/nginx \
    # forward nginx logs to docker log collector
    && sed -i -E "s/error_log .+/error_log \/dev\/stderr warn;/" /etc/nginx/nginx.conf \
    && sed -i -E "s/access_log .+/access_log \/dev\/stdout main;/" /etc/nginx/nginx.conf


# 工作目录
WORKDIR /data/wwwroot

EXPOSE 80 443

# supervisord start nginx & php-fpm
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]