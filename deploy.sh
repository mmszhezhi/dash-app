#!/bin/bash

echo "🚀 部署到 Docker..."

# 停止旧容器
docker stop dash-app 2>/dev/null
docker rm dash-app 2>/dev/null

# 构建新镜像
docker build -t dash-app .

# 运行新容器
docker run -d \
  --name dash-app \
  -p 8050:8050 \
  --restart unless-stopped \
  dash-app

echo "✅ 部署完成！访问 http://localhost:8050"