# pythonbase
python base knowledge collection
python3 虚拟环境

安装虚拟环境
```
virtualenv -p python3 .venv
```
进入虚拟环境
```
source .venv/bin/activate
```
退出虚拟环境
```
deactivate
```

然后在虚拟环境里安装需要的包,需要的包放在requirements.txt里面
```
pip3 install -r requirements.txt
```