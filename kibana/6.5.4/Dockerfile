FROM library/kibana:6.5.4


LABEL version="6.5.4" \
    description="Kibana 6.5.4" \
    maintainer="wwek<licoolgo@gmail.com>"


# 系统设置(设置时区)
USER root
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" >/etc/timezone

USER kibana