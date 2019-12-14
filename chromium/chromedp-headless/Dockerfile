FROM chromedp/headless-shell:latest

LABEL version="1.0" \
    description="chromedp-headless " \
    maintainer="wwek<licoolgo@gmail.com>"


# 系统设置(设置时区).
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && perl -pi -e 's/us.archive.ubuntu.com/mirrors.aliyun.com\/ubuntu/' /etc/apt/sources.list \
    && apt-get update -y

RUN \
    apt-get install -y \
    language-pack-zh-hans language-pack-zh-hans-base

# 中文支持
#ENV LANG C.UTF-8
# Ensure UTF-8 locale
#COPY locale /etc/default/locale
#RUN locale -a \
#  && sed -i 's/# zh_CN.UTF-8 UTF-8/zh_CN.UTF-8 UTF-8/' /etc/locale.gen \
#  && sed -i 's/ISO.UTF-8 UTF-8/# ISO.UTF-8 UTF-8/' /etc/locale.gen \
#  && cat /etc/locale.gen \
#  && locale-gen zh_CN.UTF-8 \
#  && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales \
#  && locale-gen zh_CN.UTF-8
#
#ENV LANG zh_CN.UTF-8
#ENV LANGUAGE zh_CN:zh
#ENV LC_ALL zh_CN.UTF-8

RUN \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ARG VER

EXPOSE 9222

ENTRYPOINT [ "/headless-shell/headless-shell", "--headless", "--no-sandbox", "--remote-debugging-address=0.0.0.0", "--remote-debugging-port=9222" ]


