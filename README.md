# docker
Docker基础镜像库，托管在Docker官方镜像库中
这里查看[Docker基础镜像库](https://hub.docker.com/r/wwek/)

# docker build && run
workspace为例

## 直接运行
```
#运行后删除
docker  run --rm -p 2221:22 -v d:/projects:/data --hostname="workspace-centos7" wwek/workspace:centos7
#后台运行且不删除
docker  run -d -p 2221:22 -v d:/projects:/data --hostname="workspace-centos7" --name="workspace-centos7" wwek/workspace:centos7
```
## build workspace
```
docker build -t wwek/workspace .
```