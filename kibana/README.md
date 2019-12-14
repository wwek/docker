# kibana
kibana

```
docker run -d -p 5601:5601 --link elasticsearch --name kibana kibana:6.5.4
```



```
version: '2'
services:
  kibana:
    image: docker.elastic.co/kibana/kibana:6.5.4
    volumes:
      - ./kibana.yml:/usr/share/kibana/config/kibana.yml
```


## 参考
https://www.elastic.co/guide/en/kibana/6.5/docker.html
https://hub.docker.com/_/kibana