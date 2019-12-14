# jupyter
jypyter 
https://hub.docker.com/r/jupyterhub/jupyterhub
https://hub.docker.com/r/jupyter/datascience-notebook
https://hub.docker.com/r/jupyter/scipy-notebook/
https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html

```
docker run -p 8000:8000 -d --name jupyterhub -v "$PWD":/home/jovyan/work jupyterhub/jupyterhub jupyterhub
```
```
docker run -d --restart=always --name=jupyter-scipy \
--user root \
-e GRANT_SUDO=yes \
-e NB_UID=1000 \
-e NB_GID=100 \
-p 10000:8888 \
-e JUPYTER_LAB_ENABLE=yes \
-v /data/workspace:/home/jovyan/work \
jupyter/scipy-notebook
```