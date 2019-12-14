#!/usr/bin/env python3
#coding=utf-8

"""
dfsbuild.py
单Git仓库多Dockerfile构建工具，提高了构建效率

快速使用：
chmod +x ./dfsbuild.py
只构建Git最近一次修改的Dockerfile
./dfsbuild.py  -a auto -r registry.cn-shanghai.aliyuncs.com/userename

构建所有的Dockerfile
./dfsbuild.py  -a all -r registry.cn-shanghai.aliyuncs.com/userename

构建特定的Dockerfile
./dfsbuild.py  -a dfs -r registry.cn-shanghai.aliyuncs.com/userename nginx

解决的问题：
通常我们用大量的基础Dockerfile需要维护
很多时候这些大量的Dockerfile会放在同一个Git仓库当中
当Git push时Git server的webhook功能去触发CI（Jenkins等）系统
CI系统会去自动docker build镜像
产生的问题是每次都会docker build全部的Dockerfile文件
构建的过程中虽然会使用缓存，但实际的构建时间还是不能接受的
本工具可以自动处理只构建Git最近一次修改的Dockerfile
从而大大提高了单Git仓库多Dockerfile的docker build构建速度

关键点：
git最近一次修改的Dockerfile
git --no-pager whatchanged --name-only --oneline -1
参看gitLastDockerFiles函数实现
"""


import os
import argparse
import datetime

def walkDockerfiles(path,splitFirt=True):
    """ 遍历目录中的所有dockerfile
    
    Arguments:
        path {string} -- 目录路径
    
    Keyword Arguments:
        splitFirt {bool} -- 去除文件开头的path (default: {True})
    
    Returns:
        array -- dockerfile文件列表
    """


    files_list = []
    if not os.path.exists(path):
        return -1
    for root, sub_dirs, files in os.walk(path):
        for filename in files:
            if isDockerfile(filename):
                fullFileName = os.path.join(root, filename)
                if splitFirt:
                    fullFileName = fullFileName.replace(path,"")
                files_list.append(fullFileName)  # 路径和文件名连接构成完整路径
    return files_list

def isDockerfile(filename):
    dockerfileStr = "Dockerfile"
    if dockerfileStr in filename:
        return True
    return False

def gitLastDockerFiles():
    """ git最近一次修改的Dockerfile文件
    
    Returns:
        array -- 最近一次修改的Dockerfile
    """

    gitlastcmd = "git --no-pager whatchanged --name-only --oneline -1"
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    process = os.popen(gitlastcmd)  # return file
    gitlastOut = process.read()
    process.close()
    lines = gitlastOut.split('\n')
    last_files = []
    for line in lines:
        line = line.strip('\n')
        if isDockerfile(line):
            last_files.append(line)
    return last_files
    

def dockerDo(df="", action="build", registry=""):
    if df == "" or registry == "":
        printMsg("E","输入的参数不完整")
    
    """tag生成策略
        nginx/Dockerfile >> registry/nginx:latest
        nginx/alpine/Dockerfile >> registry/nginx:alpine
        php/7.2-fpm-alpine/Dockerfile >> registry/php:7.2-fpm-alpine
        目前只支持两级目录
    """
    dfpath = df.replace('/Dockerfile','')
    tagArr = dfpath.split('/')
    tagArrLen = len(tagArr)
    if 1 == tagArrLen:
        tag = registry + "/" + tagArr[0] + ":latest"
    elif 2 <= tagArrLen:
        tag = registry + "/" + tagArr[0] + ":" + tagArr[1]
    cmd = "docker info"
    if action == "build":
       cmd = 'docker build -t ' + tag + ' ./' + dfpath
    elif action == "push":
       cmd = 'docker push ' + tag
    os.system(cmd)

def scan_files(directory,prefix=None,postfix=None):
    files_list=[]
    
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root,special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root,special_file))
            else:
                files_list.append(os.path.join(root,special_file))
                          
    return files_list


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'dfs',
        nargs='*',
        help='Dockerfile文件相对路径支持多个，用空格分割',
        metavar='dfs'
    )
    parser.add_argument(
        '-a', '--action',
        default='auto',
        help="设置build Dockerfile的范围 \
              auto(默认)为自动模式取git最后一次修改的Dockerfile \
              all全部的Dockerfile \
              dfs指定的Dockerfile",
        metavar='action',
    )
    parser.add_argument(
        '-r', '--registry',
        default='index.docker.io',
        help="定义docker仓库地址",
        metavar='registry',
    )
    parser.add_argument(
        '-p', '--push',
        default=True,
        help="build完成是否运行docker push",
        metavar='push',
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 1.0.0',
    )
    return parser.parse_args()

def printMsg(level="I",msg=""):
    print(datetime.datetime.now().isoformat() + " ["+level+"] "+msg)

def main():

    parser = _parse_args()
    dfs = parser.dfs
    registry = parser.registry
    push = parser.push
    action = parser.action
    if action == "auto":
        dfs = gitLastDockerFiles()
        if len(dfs) < 1:
            printMsg("I", "最近1次无Dockerfile修改")
        
    elif action == "all":
        dfs = walkDockerfiles("./")
    elif action == "dfs":
        pass
    else:
        printMsg("E","-a 错误，输入的参数，未定义")

    if len(dfs) > 0:
       for df in dfs:
            dockerDo(df, 'build', registry)
            if True == push:
                dockerDo(df, 'push', registry)
    else:
        printMsg("E", "Dockerfile未找到")

if __name__ == '__main__':
  main()
