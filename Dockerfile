# 使用官方的Python基础镜像，版本为3.12（你可以根据自己的需求选择其他版本）
FROM python:3.12

# 设置工作目录为/app
WORKDIR /app

# 将当前目录下的所有文件复制到容器的/app目录下
COPY . /app

# 安装项目所需的依赖
RUN pip3 install -r requirements.txt

# 暴露FastAPI应用程序运行的端口（通常是8000）
EXPOSE 8000

# 定义容器启动时要执行的命令，运行main.py
CMD ["python3", "main.py"]
