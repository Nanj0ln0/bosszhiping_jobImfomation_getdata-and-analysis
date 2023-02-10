# JobSpider

### 依赖版本

| 程序         | 版本      |
| ---------- | ------- |
| python     | 3.5+    |
| 依赖库      | requirements.txt |

### 软件使用说明

~~~
一，安装环境
创建虚拟环境(可选)
python -m venv venv

激活虚拟环境(可选)
venv\Scripts\activate

python常用国内源（可以加速pip安装第三方库的速度）
https://pypi.tuna.tsinghua.edu.cn/simple

更新pip版本(可选)
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

根据requirements.txt 安装第三方库
python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

二，启动软件

第一步：命令行启动一个指定端口的谷歌浏览器
chrome --remote-debugging-port=9555

第二步：运行程序
python main.py

~~~
