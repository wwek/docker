# openresty
openresty 

## 
latest 使用 centos系统


## quick install
```
docker run -d --name openresty -p 80:80 -p 443:443 -v /my/custom/conf.d:/etc/nginx/conf.d openresty/openresty:latest
```
```
docker run -d --restart=unless-stopped --name openresty -p 880:80 -p 4443:443 -v /data/conf/home/nginx/conf.d/:/etc/nginx/conf.d/ registry.cn-shanghai.aliyuncs.com/wwek/openresty:latest
```
## dockerfile
https://github.com/openresty/docker-openresty

## docker hub
https://hub.docker.com/r/openresty/openresty/