FROM library/kibana:latest


LABEL version="latest" \
    description="Kibana latest" \
    maintainer="wwek<licoolgo@gmail.com>"


# 系统设置(设置时区)
USER root
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" >/etc/timezone

USER kibana