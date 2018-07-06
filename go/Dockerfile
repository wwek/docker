FROM golang:latest

LABEL version="1.0" \
    description="golang" \
    maintainer="wwek<licoolgo@gmail.com>"


# 系统设置(设置时区)
RUN rm -rf /etc/localtime \
 && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 安装包管理工具
RUN go get -v -u github.com/tools/godep \
 && curl https://glide.sh/get | sh

CMD ["/bin/bash"]