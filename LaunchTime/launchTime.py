# coding=utf-8
import os
import time
import csv

# App类
class App():
    def __init__(self):
        self.content = ''
        self.starttime = 0

    # 启动APP

    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.ss.android.article.video/.activity.SplashActivity'
        self.content = os.popen(cmd)

    # 关闭APP

    def StopApp(self):
        cmd = 'adb shell am force-stop com.ss.android.article.video'
        # cmd = 'adb shell iput keyevent 3'
        os.popen(cmd)
    # 获取启动时间
    def GetLaunchTime(self):
        for line in self.content.readlines():
            if 'ThisTime' in line:
                self.starttime = line.split(":")[1]
                break
        return self.starttime

# 控制类
class Controller():
    def __init__(self, count):
        self.app = App()
        self.counter = count
        self.alldata = [("tampstamp", "elapesedtime")]

    # 单次运行 
    def testprocess(self):
        self.app.LaunchApp()
        time.sleep(5)
        elapesedtime = self.app.GetLaunchTime()
        self.app.StopApp()
        time.sleep(3)
        currenttime = self.getCurrenttime()
        return self.alldata.append((currenttime, elapesedtime))

    # 运行多次
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter -1

    # 获取当前的时间戳
    def getCurrenttime(self):
        currenttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currenttime

    # 数据存储
    def SaveDataToCsv(self):
        with open('starttime2.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.alldata)

if __name__ == "__main__":
    controller = Controller(10)
    controller.run()
    controller.SaveDataToCsv()

