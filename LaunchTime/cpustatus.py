# coding=utf-8
import csv
import os
import time

# 控制类
class Contoller(object):
    def __init__(self, count):
        self.counter = count
        self.alldata = [("timestamp", "cpustatus")]


    # 单次测试过程
    def testprocess(self):

        result = os.popen("adb shell \"dumpsys cpuinfo | grep com.ss.android.article.video\"")
        # result = os.popen("adb shell \"dumpsys cpuinfo | grep com.cubic.autohome\"")
        for line in result.readlines():
            # 将每一行用%分隔，组成list，取第1个元素
            # cpuvalue = line.split("%")[0]
            cpuvalue = line
            currenttime = self.getCurrenttime()
            self.alldata.append((currenttime, cpuvalue))
            break

    # 获取当前的时间戳
    def getCurrenttime(self):
        currenttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currenttime

    # 数据存储
    def SaveDataToCsv(self):
        with open('cpustatus.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.alldata)

    # 运行多次
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1
            time.sleep(3)
if __name__ == "__main__":
    controller = Contoller(5)
    controller.run()
    controller.SaveDataToCsv()