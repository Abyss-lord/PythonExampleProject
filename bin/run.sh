#!/usr/bin/env bash
PROJECT_NAME="exampleproject"
# 获取 BIN 路径
BIN_DIR=$(dirname "$0")
BIN_DIR=$(
    cd "$BIN_DIR" || exit
    pwd
)
# 获取 Root 路径和 Converter 路径
ROOT_DIR=$(dirname "$BIN_DIR")
cd "$ROOT_DIR" || exit

# 设置环境变量,PYTHON专用
if [ -z "$PYTHONPATH" ]; then
    export PYTHONPATH="$ROOT_DIR"
else
    export PYTHONPATH="$PYTHONPATH":"$ROOT_DIR"
fi

# python 调用exampleproject，本质上是调用exampleproject.__main__文件
# 运行 main 方法,这个方法的结果和 pyhthon -m 是一致的。
python "$PROJECT_NAME" "$@"
