# smartping
smartping 一款ping监控工具
https://github.com/smartping/smartping
https://docs.smartping.org

# 参数信息

## 数据卷

/data/smartping/db


# 官方docker iamges

```
docker run --name smartping --restart always -d -p 8899:8899 -v /data/smartping/db:/data/smartping/db wwek/smartping:latest
```

# 资料
