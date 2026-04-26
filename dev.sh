#!/bin/bash

echo "🔧 开发模式启动..."

# 停止旧容器
docker stop dash-app 2>/dev/null
docker rm dash-app 2>/dev/null

# 运行容器，挂载代码目录
docker run -d \
  --name dash-app \
  -p 8050:8050 \
  -v $(pwd):/app \
  dash-app \
  python app.py

echo "✅ 开发模式启动！修改代码后刷新浏览器即可"