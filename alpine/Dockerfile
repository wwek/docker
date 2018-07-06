FROM alpine:latest

LABEL version="1.0" \
    description="alpine:latest" \
    maintainer="wwek<licoolgo@gmail.com>"

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk update \
    && apk upgrade \
    && apk add s6 \
    && apk add bash \
    #&& apk add nghttp2-dev \
    && apk add ca-certificates \
    && apk add wget \
    #&& apk add curl \
    #&& apk add tcpdump \
    && apk add iputils \
    && apk add iproute2 \
    #&& apk add libc6-compat \
    && apk add -U tzdata \
    && rm -rf /var/cache/apk/*

# 系统设置(设置时区)
RUN rm -rf /etc/localtime \
 && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime


# instlal glibc
ENV LANG=C.UTF-8

# Here we install GNU libc (aka glibc) and set C.UTF-8 locale as default.

RUN apk del libc6-compat \
&&  ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-glibc/releases/download" \
&&  ALPINE_GLIBC_PACKAGE_VERSION="2.27-r0"  \
&&  ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk" \
&&  ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk"  \
&&  ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"\
&&  apk add --no-cache --virtual=.build-dependencies wget ca-certificates \
&&  wget \
        "https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub" \
        -O "/etc/apk/keys/sgerrand.rsa.pub" \
&&  wget \
        "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" \
&&  apk add --no-cache \
        "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  \
&&   rm "/etc/apk/keys/sgerrand.rsa.pub" \
&&   /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 "$LANG" || true \
&&  echo "export LANG=$LANG" > /etc/profile.d/locale.sh  \
    \
&&  apk del glibc-i18n \
    \
&&   rm "/root/.wget-hsts"  \
&&  apk del .build-dependencies \
&&  rm \
        "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" \
&& rm -rf /var/cache/apk/*     

# install Golang
#RUN wget --no-check-certificate https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz /tmp
#RUN tar -C /usr/local -xzf /tmp/go1.9.2.linux-amd64.tar.gz
#ENV GOPATH /data/go
#ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH
#RUN mkdir -p "$GOPATH" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
#WORKDIR $GOPATH

CMD ["/bin/bash"]