#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: octowahle@github
@software: PyCharm Community Edition
@file: gen_online_image.py
@time: 2016/11/28 15:15
"""

import os
import sys
import matplotlib.pyplot as plt
import datetime
# from matplotlib.dates import YearLocator, MonthLocator, DayLocator
# from matplotlib.dates import drange, DateLocator, DateFormatter
# from matplotlib.dates import HourLocator, MinuteLocator, SecondLocator
import matplotlib.dates as mdates


def gen_image_2(l):
    # 格式化刻度单位
    # years=mdates.YearLocator()
    # months=mdates.MonthLocator()
    # days=mdates.DayLocator()
    hours = mdates.HourLocator()
    minutes = mdates.MinuteLocator()
    seconds = mdates.SecondLocator()

    # dateFmt = mdates.DateFormatter('%Y-%m-%d %H:%M')
    # dateFmt = mdates.DateFormatter('%Y-%m-%d')
    dateFmt = mdates.DateFormatter('%H:%M')  # 显示格式化后的结果

    if len(l) != 2:
        return False

    x = l[0]
    y = l[1]

    fig, ax = plt.subplots()
    # format the ticks
    ax.xaxis.set_major_locator(hours)  # 设置主要刻度
    ax.xaxis.set_minor_locator(minutes)  # 设置次要刻度
    ax.xaxis.set_major_formatter(dateFmt)  # 刻度标志格式

    # 添加图片数据
    # plt.plot_date(dates, y, 'm-', marker='.', linewidth=1)
    plt.plot_date(x, y, '-', marker='.')
    # plt.plot(x, y)


    fig.autofmt_xdate()  # 自动格式化显示方式

    plt.show()  # 显示图片


def main():
    pass


if __name__ == '__main__':
    # main()

    # result_list = DbUtils.connet()

    result_list = [[datetime.datetime(2016, 11, 28, 14, 43, 48), datetime.datetime(2016, 11, 28, 14, 45, 48),
                    datetime.datetime(2016, 11, 28, 14, 52, 15), datetime.datetime(2016, 11, 28, 14, 57, 2),
                    datetime.datetime(2016, 11, 28, 15, 4, 14), datetime.datetime(2016, 11, 28, 15, 5, 14),
                    datetime.datetime(2016, 11, 28, 15, 11, 7), datetime.datetime(2016, 11, 28, 15, 18, 21),
                    datetime.datetime(2016, 11, 28, 15, 20, 21), datetime.datetime(2016, 11, 28, 15, 25, 39),
                    datetime.datetime(2016, 11, 28, 15, 30, 54), datetime.datetime(2016, 11, 28, 15, 35, 54),
                    datetime.datetime(2016, 11, 28, 15, 41, 32), datetime.datetime(2016, 11, 28, 15, 46, 24),
                    datetime.datetime(2016, 11, 28, 15, 51, 13), datetime.datetime(2016, 11, 28, 15, 55, 13),
                    datetime.datetime(2016, 11, 28, 16, 0, 13), datetime.datetime(2016, 11, 28, 16, 5, 21),
                    datetime.datetime(2016, 11, 28, 16, 11, 22), datetime.datetime(2016, 11, 28, 16, 15, 3),
                    datetime.datetime(2016, 11, 28, 16, 20, 20), datetime.datetime(2016, 11, 28, 16, 25, 16),
                    datetime.datetime(2016, 11, 28, 16, 30, 48), datetime.datetime(2016, 11, 28, 16, 35, 48),
                    datetime.datetime(2016, 11, 28, 16, 40, 18), datetime.datetime(2016, 11, 28, 16, 47, 38),
                    datetime.datetime(2016, 11, 28, 16, 50, 17), datetime.datetime(2016, 11, 28, 16, 58, 10),
                    datetime.datetime(2016, 11, 28, 17, 0, 40), datetime.datetime(2016, 11, 28, 17, 5, 40),
                    datetime.datetime(2016, 11, 28, 17, 10, 40), datetime.datetime(2016, 11, 28, 17, 15, 40),
                    datetime.datetime(2016, 11, 28, 17, 20, 40), datetime.datetime(2016, 11, 28, 17, 27, 19),
                    datetime.datetime(2016, 11, 28, 17, 30, 43), datetime.datetime(2016, 11, 28, 17, 36, 6),
                    datetime.datetime(2016, 11, 28, 17, 41, 13), datetime.datetime(2016, 11, 28, 17, 45, 39),
                    datetime.datetime(2016, 11, 28, 17, 51, 39), datetime.datetime(2016, 11, 28, 17, 59, 22),
                    datetime.datetime(2016, 11, 28, 18, 0, 42), datetime.datetime(2016, 11, 28, 18, 5, 39),
                    datetime.datetime(2016, 11, 28, 18, 10, 39), datetime.datetime(2016, 11, 28, 18, 15, 39)],
                   [5L, 4L, 1L, 5L, 9L, 16L, 5L, 5L, 3L, 5L, 8L, 18L, 6L, 8L, 22L, 1L, 16L, 11L, 14L, 5L, 7L, 11L, 5L,
                    2L, 7L, 6L, 15L, 6L, 9L, 20L, 23L, 22L, 28L, 4L, 4L, 1L, 4L, 9L, 19L, 4L, 21L, 23L, 24L, 5L]]

    gen_image_2(result_list)
