FROM sonarqube:latest


LABEL version="1.0" \
    description="sonarqube " \
    maintainer="wwek<licoolgo@gmail.com>"

USER root
# 系统设置(设置时区).
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime