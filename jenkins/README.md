# jenkins:latest
jenkins master

```
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v /your/home:/var/jenkins_home jenkins
```
```
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v /your/home:/var/jenkins_home registry.cn-shanghai.aliyuncs.com/wwek/jenkins:latest
```