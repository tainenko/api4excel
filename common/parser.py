import os
import configparser

# 获取当前py文件地址
proDir = os.path.split(os.path.realpath(__file__))[0]
# 组合config文件地址
configPath = os.path.join(proDir,"config.ini")

class ReadConfig:
    def __init__(self):
        #获取当前路径下的配置文件
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_config(self,field,key):
        #获取配置文件中的key值
        result = self.cf.get(field,key)
        return result

    def set_config(self,field,key,value):
        #向配置文件中写入配置信息
        fb = open(configPath,'w')
        self.cf.set(field,key,value)
        self.cf.write(fb)

作者：牛哄哄的QA
链接：https://juejin.im/post/5b91e070f265da0abf7cc53b
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。