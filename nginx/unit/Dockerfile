FROM nginx/unit
LABEL maintainer="1252409767@qq.com"

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    apt update && \
    apt install busybox net-tools

# 系统设置(设置时区)
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

CMD /usr/sbin/unitd --no-daemon --control 0.0.0.0:8010