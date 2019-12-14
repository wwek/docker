# jenkins:jnlp-slave-latest
jnlp 模式的 jenkins slave

https://hub.docker.com/r/jenkins/jnlp-slave/

JENKINS_URL: url for the Jenkins server, can be used as a replacement to -url option, or to set alternate jenkins URL
JENKINS_TUNNEL: (HOST:PORT) connect to this agent host and port instead of Jenkins server, assuming this one do route TCP traffic to Jenkins master. Useful when when Jenkins runs behind a load balancer, reverse proxy, etc.
JENKINS_SECRET: agent secret, if not set as an argument
JENKINS_AGENT_NAME: agent name, if not set as an argument
JENKINS_AGENT_WORKDIR: agent work directory, if not set by optional parameter -workDir

## build
```
./dfsbuild.py -a dfs -r registry.cn-shanghai.aliyuncs.com/wwek jenkins/jnlp-slave
```