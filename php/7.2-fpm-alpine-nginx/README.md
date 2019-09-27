# php-7.2-fpm-alpine-nginx
 php7.2 fpm alpine nginx


## 容器化

```
docker build -t wwek/php:7.2-fpm-alpine-nginx .
docker run --rm -it wwek/php:7.2-fpm-alpine-nginx
```

使用工具自定义构建容器
```
python ./dfsbuild.py  -a dfs -r wwek php/7.2-fpm-alpine-nginx
```

 ## Dockerfile
https://github.com/wwek/docker