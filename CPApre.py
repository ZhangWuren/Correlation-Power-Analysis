import sys
import csv
import numpy as np
import xlwt
import pandas as pd
import xlsxwriter as xs


def num_turn_str(num):
    if num < 10:
        return '00' + str(num)
    if num < 100:
        return '0' + str(num)
    else:
        return str(num)


if __name__ == "__main__":
    plaintext_csv = csv.reader(open('CPA测试数据/相关能量分析_原始波_无滤波_100条_8500点/Plaintext.csv', 'r'))
    plaintext = list()

    # 读取明文
    for i in plaintext_csv:
        if plaintext_csv.line_num % 4 == 3:
            plaintext.append(i)

    workbook = xs.Workbook('plaintext.xlsx')
    worksheet = workbook.add_worksheet('sheet1')
    for i in range(300):
        for j in range(0):
            worksheet.write(i, j, plaintext[j][i])
    workbook.close()

    trace = list()
    # 读取波形
    for order in range(100):
        trace_temp = list()
        print(order)
        filename = 'CPA测试数据/相关能量分析_原始波_无滤波_100条_8500点/Trace000' + num_turn_str(order + 1) + '.csv'
        trace_temp.clear()
        trace_csv = csv.reader(open(filename, 'r'))
        for i in trace_csv:
            trace_temp.append(i[1])
        # trace.append(np.array(trace_temp))
        trace.append(trace_temp)

    workbook = xs.Workbook('trace.xlsx')
    worksheet = workbook.add_worksheet('sheet1')
    for i in range(8500):
        for j in range(100):
            worksheet.write(i, j, trace[j][i])
    workbook.close()
