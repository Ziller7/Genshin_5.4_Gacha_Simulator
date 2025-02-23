# coding=gbk
import random
import time


def format_number(num):
    # 判断并格式化为中文单位输出
    if num >= 1_000_000_00:  # 亿
        return f"{num / 1_000_000_00:.0f}亿"
    elif num >= 1_0000:  # 万
        return f"{num / 1_0000:.0f}万"
    else:
        return str(num)


pull = 1000000000  # 测试抽数
formatted_pull = format_number(pull)

print("原神抽卡", formatted_pull, "抽，启动！")

range_c = 0.6  # 出金率
range_cc = 0.33  # up角色出率
range_w = 0.8  # 0.7
range_ww = 0.6  # 0.525
range_www = 0.2625
range_f = 5.1  # 出紫率
range_ff = 0.85  # 某一up四星出率
f = ff = 0
lose = lose_f = 0
z = 0  # 概率累加次数
wc = wc_f = 0  # up角色数
ww = 0  # up武器数
wdg = 0  # 定轨武器数
c = 0
cc = 0
wai = 0
max_wai = 0
buwai = 0
max_buwai = 0
all_wai = 0
multiple = multiple_2 = multiple_3 = multiple_4 = multiple_5 = multiple_6 = multiple_7 = multiple_8 = multiple_9 = multiple_10 = 0
light = 1  # 捕获明光计数器
double = 0
up_max = 0
n = 0  # 遍历次数（第n种可能性）
x = x_f = 0  # 消耗原石超额次数
pull_num = 0
pull_c = 0  # 角色（命座所用抽数）
pull_w = 0  # 武器所用抽数
price = 160  # 每抽消耗原石
pull_cost = pull_cost_f = 0  # 总消耗
pull_cost_player = 0  # 玩家总消耗
pull_cost_min = 1000000  # 最欧玩家平均消耗
pull_cost_max = 0  # 最非玩家平均消耗
wc_player = 0  # 玩家出金数
player_pull = 2000  # 分配给各玩家的抽数
pull_min = 1000000
pull_max = 0
cost_min = 1000000
cost_max = cost_max_f = 0

c0 = {}
c1 = {}
c2 = {}
c6 = {}
up = {}
dg = {}


# 计算函数
def count(n, x, pull, pull_num, pull_cost, cost_min, cost_max):
    n += 1
    cost = pull_num * price
    pull_cost += cost
    if cost < cost_min:
        cost_min = cost
    if cost > cost_max:
        cost_max = cost
    if cost > save:
        x += 1
    pull += 1
    pull *= 1
    return n, x, pull, pull_cost, cost_min, cost_max


# 变量初始化函数
def clear():
    return 0, 0, 0, 0, 0, 0, 0, 100000000, 0, 0


start_time = time.time()
while n <= pull:
    if n % 10 == 0:
        if n % player_pull == 0 and wc_player > 0:
            player_cost = round((pull_cost_player / wc_player) * price, 1)
            if player_cost > pull_cost_max:
                pull_cost_max = player_cost
            elif player_cost < pull_cost_min:
                pull_cost_min = player_cost
            pull_cost_player = wc_player = 0
            if n % 1000000 == 0:  # 每100万抽更新一次进度
                # 计算进度百分比
                elapsed = time.time() - start_time
                progress = (n + 1) / (pull / 100)
                # 计算已经完成的进度条长度
                num_hashes = int(progress)
                num_spaces = 100 - num_hashes
                # 构建进度条字符串
                progress_bar = f"计算进度：{progress:.2f}%，预计剩余{(elapsed / progress * (100 - progress)) // 60:.0f}分{(elapsed / progress * (100 - progress)) % 60:.0f}秒 [{'█' * num_hashes}{'_' * num_spaces}]"
                # 打印进度条，使用 \r 覆盖之前的输出
                print(f"\r{progress_bar}", end="")
        if multiple > 1:
            if multiple == 2:
                multiple_2 += 1
            elif multiple == 3:
                multiple_3 += 1
            elif multiple == 4:
                multiple_4 += 1
            elif multiple == 5:
                multiple_5 += 1
            elif multiple == 6:
                multiple_6 += 1
            elif multiple == 7:
                multiple_7 += 1
            elif multiple == 8:
                multiple_8 += 1
            elif multiple == 9:
                multiple_9 += 1
            elif multiple == 10:
                multiple_10 += 1
        multiple = 0
    range_c = 0.6
    range_f = 5.1
    n += 1
    c += 1  # 自上一金后的累计抽数
    cc += 1  # 自上一up后的累计抽数
    f += 1
    ff += 1
    if c >= 74:  # 保底
        z += 1  # 接近保底时的概率累加次数
        range_c *= z * 10 + 1
        if range_c > 100:
            range_c = 100

    r = random.random()  # 抽卡

    if r * 100 <= range_c:  # 出金
        x += 1  # 累计出金数
        multiple += 1
        # if c < 10:
        #     double += 1  # 十连双黄数
        if c > pull_max:
            pull_max = c
        if c < pull_min:
            pull_min = c
        if lose == 1:  # 大保底
            range_cc = range_c
            all_wai += 1
            # light += 1
        else:
            range_cc = range_c * 11 / 20
            # if light > 0:
            #     light -= 1
        if r * 100 <= range_cc or light >= 3:  # 出up
            wc += 1  # 累计出up数
            wc_player += 1
            pull_cost += cc  # 累计抽数
            pull_cost_player += cc
            if lose == 0:
                buwai += 1
                wai = 0
            #     light -= 1
            # else:
            #     light += 1
            if buwai > max_buwai:
                max_buwai = buwai
            # if light >= 3:
            #     light = 1
            #     print("触发捕获明光")
            c0[wc - 1] = cc
            if wc % 2 == 0:
                c1[wc / 2 - 1] = c0[wc - 1] + c0[wc - 2]
            if wc % 3 == 0:
                c2[wc / 3 - 1] = c0[wc - 1] + c0[wc - 2] + c0[wc - 3]
            if wc % 7 == 0:
                c6[wc / 7 - 1] = c0[wc - 1] + c0[wc - 2] + c0[wc - 3] + c0[wc - 4] + c0[wc - 5] + c0[wc - 6] + c0[
                    wc - 7]
            if cc > cost_max:
                cost_max = cc
            if cc < cost_min:
                cost_min = cc
            cc = 0
            lose = 0
        else:  # 小保底歪
            lose = 1
            wai += 1
            buwai = 0
            if wai > max_wai:
                max_wai = wai
        c = 0
        z = 0
    else:  # 没出金时再讨论是否出紫
        r = random.random()  # 重新抽卡
        if f == 9:
            range_f = 56.1
        elif f >= 10:
            range_f = 100
        if lose_f == 1:
            range_ff = range_f
        else:
            range_ff = range_f * 1 / 2
        if r * 100 <= range_f:  # 出紫
            x_f += 1
            if r * 100 <= range_ff:  # 出up四星
                if r * 100 <= range_ff * 1 / 3:  # 出某一up四星
                    wc_f += 1  # 累计出up四星数
                    pull_cost_f += ff  # 累计抽数
                    if ff > cost_max_f:
                        cost_max_f = ff
                    ff = 0
                lose_f = 0
            else:  # 小保底歪
                lose_f = 1
            f = 0
n -= cc

print("\r实际抽卡", n, "抽，分摊给", int(pull / player_pull), "名玩家各", player_pull, "抽，最欧玩家平均花",
      pull_cost_min,
      "原石（", round((pull_cost_min / price), 1), "抽）出up角色，最非玩家平均花", pull_cost_max, "原石（",
      round((pull_cost_max / price), 1), "抽）出up角色")
print("共出", x, "个五星角色，平均花", round((pull_cost / x) * price, 1), "原石出金，综合出率", round(x * 100 / n, 3),
      "%，其中up五星角色占比", round((wc / x) * 100, 1), "%，平均花", round((pull_cost / wc) * price, 1),
      "原石出up五星，最多花",
      cost_max * price, "原石出up五星，不歪率", round((wc - all_wai) * 100 / wc, 2), "%，最多", max_buwai, "连不歪，最多",
      max_wai, "连歪")
print("共出现", multiple_2, "次双黄、", multiple_3, "次三黄、", multiple_4, "次四黄、", multiple_5, "次五黄、", multiple_6,
      "次六黄、", multiple_7, "次七黄、", multiple_8, "次八黄、", multiple_9, "次九黄、", multiple_10, "次十黄")
print("共出", x_f, "个四星，平均花", round((pull_cost_f / x_f) * price, 1), "原石出紫，综合出率", round(x_f * 100 / n, 3),
      "%，其中特定up四星角色占比", round((wc_f / x_f) * 100, 1),
      "%，平均花", round((pull_cost_f / wc_f) * price, 1), "原石出特定up四星，最多花", cost_max_f * price,
      "原石出特定up四星")
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

range_c = 0.6  # 出金率
range_cc = 0.3  # up角色出率
range_w = 0.8  # 0.7
range_ww = 0.6  # 0.525
range_www = 0.2625
lose = 0
lose2 = 0
z = 0
wc = 0  # up角色数
ww = 0  # up武器数
www = 0  # 定轨武器数
c = 0
cc = 0
ccc = 0
pull_num = 0
pull_min = 10000000
pull_max = 0
price = 160  # 每抽消耗原石
double = 0

start_time = time.time()
while n <= pull:
    if n % 1000000 == 0:
        # 计算进度百分比
        elapsed = time.time() - start_time
        progress = (n + 1) / (pull / 100)
        # 计算已经完成的进度条长度
        num_hashes = int(progress)
        num_spaces = 100 - num_hashes
        # 构建进度条字符串
        progress_bar = f"计算进度：{progress:.2f}%，预计剩余{elapsed / progress * (100 - progress):.1f}s [{'█' * num_hashes}{'_' * num_spaces}]"
        # 打印进度条，使用 \r 覆盖之前的输出
        print(f"\r{progress_bar}", end="")
    range_w = 0.7  # 0.8
    n += 1
    c += 1
    cc += 1
    ccc += 1
    if c >= 63:  # 67:  # 保底
        z += 1  # 概率累加次数
        range_w *= z * 10 + 1
        # if c <= 70:  # 73:
        #     range_w *= z * 14 + 1  # 10 + 1
        # else:
        #     range_w *= z * 7 + 45.6  # 5 + 56
        if range_w > 100:
            range_w = 100
    if lose == 1:  # 大保底
        range_ww = range_w
        if lose2 == 1:  # 满定轨
            range_www = range_w
        else:
            range_www = range_ww / 2
    elif lose2 == 1:  # 满定轨
        range_ww = range_w
        range_www = range_w
    else:
        range_ww = range_w * 3 / 4
        range_www = range_ww / 2
    r = random.random()

    if r * 100 <= range_w:  # 出金
        x += 1
        # if c < 10:
        #     double += 1
        if r * 100 <= range_ww:  # 出up
            if c > pull_max:
                pull_max = c
            if c < pull_min:
                pull_min = c
            ww += 1
            up[ww - 1] = cc
            if r * 100 <= range_www:  # 出定轨
                www += 1
                dg[www - 1] = ccc
                pull_cost += ccc
                if ccc > cost_max:
                    cost_max = ccc
                if ccc < cost_min:
                    cost_min = ccc
                ccc = 0
                if lose2 == 0:
                    lose = 0
                lose2 = 0
            else:  # 出非定轨
                lose = 0
                lose2 += 1
            cc = 0
        else:  # 小保底歪
            lose = 1
            lose2 += 1
        c = 0
        z = 0

print("\r共出", x, "把五星武器，平均花", round((pull_cost / x) * price, 1), "原石出金，综合出率", round(x * 100 / n, 3),
      "%，其中up武器占比",
      round((ww / x) * 100, 1), "%，平均花", round((pull_cost / ww) * price, 1), "原石出up武器；定轨占比",
      round((www / x) * 100, 1),
      "%，平均花", round((pull_cost / www) * price, 1), "原石出定轨；最多花", cost_max * price, "原石出定轨")
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

save = int(input("请输入所持原石数："))  # 原石积蓄

while pull_c < len(c0):
    (n, x, pull_c, pull_cost, cost_min, cost_max) = count(n, x, pull_c, c0[pull_c], pull_cost, cost_min, cost_max)
print("0命共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
      "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

while pull_c < len(c1):
    (n, x, pull_c, pull_cost, cost_min, cost_max) = count(n, x, pull_c, c1[pull_c], pull_cost, cost_min, cost_max)
print("1命共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
      "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

while pull_c < len(c2):
    (n, x, pull_c, pull_cost, cost_min, cost_max) = count(n, x, pull_c, c2[pull_c], pull_cost, cost_min, cost_max)
print("2命共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
      "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

while pull_c < len(c6):
    (n, x, pull_c, pull_cost, cost_min, cost_max) = count(n, x, pull_c, c6[pull_c], pull_cost, cost_min, cost_max)
print("6命共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
      "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

# while pull_w < len(up):
#     (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, up[pull_w], pull_cost, cost_min, cost_max)
# print("up武器共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
#       "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_w < len(dg):
#     (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, dg[pull_w], pull_cost, cost_min, cost_max)
# print("定轨武器共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
#       "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c0):
#     while pull_w < len(up):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c0[pull_c] + up[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("0命+up武器共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
#       "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c0):
#     while pull_w < len(dg):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c0[pull_c] + dg[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("0命+定轨武器共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
#       "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c1):
#     while pull_w < len(up):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c1[pull_c] + up[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("1命+up武器共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
#       "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c1):
#     while pull_w < len(dg):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c1[pull_c] + dg[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("1命+定轨武器共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
#       "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c2):
#     while pull_w < len(up):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c2[pull_c] + up[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("2命+up武器共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
#       "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c2):
#     while pull_w < len(dg):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c2[pull_c] + dg[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("2命+定轨武器共有", n, "种可能性，保出概率:", round((1 - x / n) * 100, 1),
#       "%，平均花费", round(pull_cost / n, 1), "，最少花费", cost_min, "，最多花费", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()
