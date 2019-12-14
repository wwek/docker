# whistle
whistle 基于Node实现的跨平台web调试代理工具

https://wproxy.org/whistle/

## docker
```
docker build -t wwek/whistle:latest . 
docker run --rm --name whistle -p 8899:8899 \
-v $(pwd)/data:/root/.WhistleAppData \
 wwek/whistle:latest
```
## 使用
设置系统全局代理 或 chrome插件SwitchyOmega
127.0.0.1:8899

设置代理后可进whistle管理界面
http://local.whistlejs.com/

## whistle 插件
https://github.com/whistle-plugins


