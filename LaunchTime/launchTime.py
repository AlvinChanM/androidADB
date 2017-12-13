# coding=utf-8
import os
import time

# App类
class App():
    def __init__(self):
        self.content = ''
        self.starttime = 0

    # 启动APP

    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.ss.android.article.news/.activity.MainActivity'
        content = os.popen(cmd)

    # 关闭APP

    def StopApp(self):
        cmd = 'adb shell am force-stop com.ss.android.article.news'
        os.popen(cmd)
    # 获取启动时间
    def GetLaunchTime(self):
        for line in self.content.readlines():
            if 'ThisTime' in line:
                self.starttime = line.split(":")[1]
                break
        return  starttime

# 控制类
class controller():
    def __init__(self, count):
        self.app = App()
        self.counter = count
        self.alldata = [("tampstamp", "elapesedtime")

    # 单次运行 
    def testprocess(self):
        self.app.LaunchApp()
        time = self.app.GetLaunchTime()
        self.app.StopApp()

    def run(self):
        while counter > 0:
            self.testprocess()
            self.counter = self.counter -1

    # 获取当前的时间戳
    def getCurrenttime(self):
        currenttime = time.strptime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currenttime

    def collectalldata(self):
    def SaveDataToCsv(self):