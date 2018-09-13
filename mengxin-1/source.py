# coding: utf-8
# 爬取股票数据源
import tushare as ts
import threading


# 获取历史,如股票海康威视
# data=ts.get_hist_data('002415',start='2017-01-01',end='2018-05-31')
# 保存
# data.to_csv('/Users/loufeng/Work/sidetock.csv')
# 绘图
# draw=np.array(data['high'])[::-1]
# plt.figure()
# plt.plot(draw)
# plt.show()

# 定时输出实时行情
def timer():
    global t
    print(ts.get_realtime_quotes('002415'), '\n\n', ts.get_realtime_quotes('501050'), '\n\n',
          ts.get_realtime_quotes('000963'), '\n\n', ts.get_realtime_quotes('510880'))
    t = threading.Timer(10, timer)
    t.start()


t = threading.Timer(1, timer)
t.start()
