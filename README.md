aerich init -t settings.orm.tortoise_orm 
aerich init-db
aerich migrate --name 'init'
aerich upgrade
aerich downgrade

## 部署说明

1. 确保已安装 Docker

2. 构建 Docker 镜像：
   ```
   docker build --build-arg DOCKER_REGISTRY_MIRROR=https://docker.mirrors.ustc.edu.cn -t simple-backend .
   ```
   注意：你可以根据需要更改镜像加速器的 URL。

3. 运行 Docker 容器：
   ```
   docker run -d -p 8000:8000 simple-backend
   ```

4. 访问 http://localhost:8000 验证应用是否正在运行

## 故障排除

如果在构建过程中仍然遇到网络问题，可以尝试以下方法：

1. 重新运行 `docker build` 命令
2. 尝试使用不同的镜像加速器，例如：
   ```
   docker build --build-arg DOCKER_REGISTRY_MIRROR=https://hub-mirror.c.163.com -t simple-backend .
   ```
3. 使用缓存：`docker build --cache-from python:3.11 -t simple-backend .`
4. 尝试使用不同的基础镜像，如 `python:3.11-alpine`
5. 重启 Docker 守护进程