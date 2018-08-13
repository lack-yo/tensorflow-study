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

# 优质个股选择(配仓)
# A股：海康威视（28以下加仓，拿到37~40以上减仓清仓）、华东医药（40附近可建仓，拿到50以上）、格力电器（40下可建仓）
# H股：小米（发行价破后16左右建仓，可长期持有，看到30以上）、吉利（17左右可建仓，可长期持有，看到30）
# 美股：好未来（30以下建仓，拿到40以上）、BILI（10元左右以下加仓，拿到18~20以上）、ADOBE（230以下）

# 优质定投基金推荐
# 50AH（501050），上证红利（510880）
