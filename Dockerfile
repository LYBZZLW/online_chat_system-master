# 使用一个基础的 Python 镜像作为基础镜像
FROM python:3.9

# 将当前工作目录设置为 /app
WORKDIR /app

# 将整个项目目录复制到镜像中的 /app 目录下
COPY . /app

# 安装Python依赖库（如果需要的话
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 在容器内运行的命令
CMD ["bash", "-c", "python ./app/models/models.py&&python ./main.py "]
