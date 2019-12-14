FROM library/nginx:latest


LABEL version="1.0" \
    description="nginx latest" \
    maintainer="wwek<licoolgo@gmail.com>"


# 系统设置(设置时区)
RUN rm -rf /etc/localtime \
 && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime