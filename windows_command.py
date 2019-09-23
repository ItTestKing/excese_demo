# -*- coding:utf-8 -*-
import random
import time

class Command(object):
    # 1.打开文件,读取文件
    def command_list(self):
        with open("windows常用命令.txt", "r") as f:
            command = f.readlines()
            return command

    # 随机读取列表。
    def randomprt_command(self):
        command = self.command_list()
        # print(len(command))
        list_sort = random.randint(1, 37)
        print(list_sort)
        return command[list_sort]

    # 打印数据
    def prt(self):
        i = 0
        while i < 100:
            i += 1
            print(self.randomprt_command())
            time.sleep(5)


if __name__ == "__main__":
    try:
        Command().prt()
    except IndexError as e:
        print(e)
