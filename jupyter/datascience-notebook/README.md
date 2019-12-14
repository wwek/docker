# jupyter
jypyter datascience-notebook
https://hub.docker.com/r/jupyter/datascience-notebook/

```
docker run -d --restart=always --name=jupyter \
--user root \
-e GRANT_SUDO=yes \
-e NB_UID=1000 \
-e NB_GID=100 \
-p 10000:8888 \
-e JUPYTER_LAB_ENABLE=yes \
-v /data/workspace:/home/jovyan/work \
jupyter/datascience-notebook
```