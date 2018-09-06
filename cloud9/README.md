Cloud9 v3 Dockerfile
=============

Cloud9 是一个开源的WEB IDE，国内类似的产品为Coding WEB IDE

# 基础镜像
基础镜像采用CnetOS

#  安装

## 安装docker环境

略

## 使用

### 快速使用
```
docker run -it -d -p 80:80 -v /your-path/workspace/:/workspace/ wwek/cloud9
```
默认登陆账号密码为 admin cloud9

## 自定义登陆账号和密码
```
docker run -it -d -p 80:80 -v /your-path/workspace/:/workspace/ -e "CLOUD9_AUTH=myuser:mypassword" wwek/cloud9
```
    
## Build你自定义的docker镜像

clone仓库
    git clone https://github.com/wwek/docker
    cd cloud9

Build

    sudo docker build --force-rm=true -t "$USER/cloud9:latest" .
    
And run

    sudo docker run -d -p 80:80 -v /your-path/workspace/:/workspace/ $USER/cloud9:latest
    
