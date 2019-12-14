FROM node:10-alpine

LABEL version="2.4.2" \
    description="whistle 基于Node实现的跨平台web调试代理工具" \
    maintainer="wwek<licoolgo@gmail.com>"

# whistle
RUN npm config set registry https://registry.npm.taobao.org -g \
    && npm install whistle@2.4.2 -g \
    && w2 help

# Install plugins
RUN npm i -g whistle.inspect \
    && npm i -g whistle.vase \
    && npm i -g whistle.script \
    && npm i -g whistle.autopac \
    && npm i -g whistle.autosave \
    && npm i -g whistle.pinned-ip \
    && npm i -g whistle whistle.show-frames \
    && npm i -g whistle.proxyauth \
    && npm i -g whistle.combo \
    && npm i -g whistle.help \
    && npm i -g whistle.swmock \
    && npm i -g whistle.rules \
    && npm i -g whistle.test

EXPOSE 8899/tcp

CMD ["w2","run"]
