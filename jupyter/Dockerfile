FROM jupyterhub/jupyterhub

LABEL version="1.0" \
    description="jupyter jupyterhub latest" \
    maintainer="wwek<licoolgo@gmail.com>"

# 系统设置(设置时区)
USER root
RUN rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" >/etc/timezone

USER jovyan
# change pip' mirror url
RUN mkdir -p ~/.pip \
    && echo "[global]" >  ~/.pip/pip.conf \
    && echo "timeout = 6000" >> ~/.pip/pip.conf \
    && echo "index-url = http://mirrors.aliyun.com/pypi/simple/\ntrusted-host = mirrors.aliyun.com" >> ~/.pip/pip.conf \
    && echo "[install]" >> ~/.pip/pip.conf \
    && echo "use-mirrors = true" >> ~/.pip/pip.conf \
    && echo "mirrors = http://mirrors.aliyun.com/pypi/simple/" >> ~/.pip/pip.conf \
    && echo "trusted-host = mirrors.aliyun.com" >>  ~/.pip/pip.conf