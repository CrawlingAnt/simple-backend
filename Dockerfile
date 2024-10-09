# 使用 Python 3.12 版本
FROM python:3.12

# 设置环境变量以使用镜像加速器
ENV DOCKER_REGISTRY_MIRROR=https://docker.mirrors.ustc.edu.cn

# 设置工作目录为/app
WORKDIR /app

# 安装 poetry
RUN pip install poetry

# 复制 pyproject.toml 和 poetry.lock 文件
COPY pyproject.toml poetry.lock ./

# 安装项目依赖
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# 复制项目文件
COPY . .

# 暴露FastAPI应用程序运行的端口（通常是8000）
EXPOSE 8000

# 定义容器启动时要执行的命令，使用 uvicorn 运行 FastAPI 应用
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
