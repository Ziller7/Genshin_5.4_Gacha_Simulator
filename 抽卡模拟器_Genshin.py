# coding=gbk
import random
import time


def format_number(num):
    # �жϲ���ʽ��Ϊ���ĵ�λ���
    if num >= 1_000_000_00:  # ��
        return f"{num / 1_000_000_00:.0f}��"
    elif num >= 1_0000:  # ��
        return f"{num / 1_0000:.0f}��"
    else:
        return str(num)


pull = 1000000000  # ���Գ���
formatted_pull = format_number(pull)

print("ԭ��鿨", formatted_pull, "�飬������")

range_c = 0.6  # ������
range_cc = 0.33  # up��ɫ����
range_w = 0.8  # 0.7
range_ww = 0.6  # 0.525
range_www = 0.2625
range_f = 5.1  # ������
range_ff = 0.85  # ĳһup���ǳ���
f = ff = 0
lose = lose_f = 0
z = 0  # �����ۼӴ���
wc = wc_f = 0  # up��ɫ��
ww = 0  # up������
wdg = 0  # ����������
c = 0
cc = 0
wai = 0
max_wai = 0
buwai = 0
max_buwai = 0
all_wai = 0
multiple = multiple_2 = multiple_3 = multiple_4 = multiple_5 = multiple_6 = multiple_7 = multiple_8 = multiple_9 = multiple_10 = 0
light = 1  # �������������
double = 0
up_max = 0
n = 0  # ������������n�ֿ����ԣ�
x = x_f = 0  # ����ԭʯ�������
pull_num = 0
pull_c = 0  # ��ɫ���������ó�����
pull_w = 0  # �������ó���
price = 160  # ÿ������ԭʯ
pull_cost = pull_cost_f = 0  # ������
pull_cost_player = 0  # ���������
pull_cost_min = 1000000  # ��ŷ���ƽ������
pull_cost_max = 0  # ������ƽ������
wc_player = 0  # ��ҳ�����
player_pull = 2000  # ���������ҵĳ���
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


# ���㺯��
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


# ������ʼ������
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
            if n % 1000000 == 0:  # ÿ100������һ�ν���
                # ������Ȱٷֱ�
                elapsed = time.time() - start_time
                progress = (n + 1) / (pull / 100)
                # �����Ѿ���ɵĽ���������
                num_hashes = int(progress)
                num_spaces = 100 - num_hashes
                # �����������ַ���
                progress_bar = f"������ȣ�{progress:.2f}%��Ԥ��ʣ��{(elapsed / progress * (100 - progress)) // 60:.0f}��{(elapsed / progress * (100 - progress)) % 60:.0f}�� [{'��' * num_hashes}{'_' * num_spaces}]"
                # ��ӡ��������ʹ�� \r ����֮ǰ�����
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
    c += 1  # ����һ�����ۼƳ���
    cc += 1  # ����һup����ۼƳ���
    f += 1
    ff += 1
    if c >= 74:  # ����
        z += 1  # �ӽ�����ʱ�ĸ����ۼӴ���
        range_c *= z * 10 + 1
        if range_c > 100:
            range_c = 100

    r = random.random()  # �鿨

    if r * 100 <= range_c:  # ����
        x += 1  # �ۼƳ�����
        multiple += 1
        # if c < 10:
        #     double += 1  # ʮ��˫����
        if c > pull_max:
            pull_max = c
        if c < pull_min:
            pull_min = c
        if lose == 1:  # �󱣵�
            range_cc = range_c
            all_wai += 1
            # light += 1
        else:
            range_cc = range_c * 11 / 20
            # if light > 0:
            #     light -= 1
        if r * 100 <= range_cc or light >= 3:  # ��up
            wc += 1  # �ۼƳ�up��
            wc_player += 1
            pull_cost += cc  # �ۼƳ���
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
            #     print("������������")
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
        else:  # С������
            lose = 1
            wai += 1
            buwai = 0
            if wai > max_wai:
                max_wai = wai
        c = 0
        z = 0
    else:  # û����ʱ�������Ƿ����
        r = random.random()  # ���³鿨
        if f == 9:
            range_f = 56.1
        elif f >= 10:
            range_f = 100
        if lose_f == 1:
            range_ff = range_f
        else:
            range_ff = range_f * 1 / 2
        if r * 100 <= range_f:  # ����
            x_f += 1
            if r * 100 <= range_ff:  # ��up����
                if r * 100 <= range_ff * 1 / 3:  # ��ĳһup����
                    wc_f += 1  # �ۼƳ�up������
                    pull_cost_f += ff  # �ۼƳ���
                    if ff > cost_max_f:
                        cost_max_f = ff
                    ff = 0
                lose_f = 0
            else:  # С������
                lose_f = 1
            f = 0
n -= cc

print("\rʵ�ʳ鿨", n, "�飬��̯��", int(pull / player_pull), "����Ҹ�", player_pull, "�飬��ŷ���ƽ����",
      pull_cost_min,
      "ԭʯ��", round((pull_cost_min / price), 1), "�飩��up��ɫ��������ƽ����", pull_cost_max, "ԭʯ��",
      round((pull_cost_max / price), 1), "�飩��up��ɫ")
print("����", x, "�����ǽ�ɫ��ƽ����", round((pull_cost / x) * price, 1), "ԭʯ�����ۺϳ���", round(x * 100 / n, 3),
      "%������up���ǽ�ɫռ��", round((wc / x) * 100, 1), "%��ƽ����", round((pull_cost / wc) * price, 1),
      "ԭʯ��up���ǣ���໨",
      cost_max * price, "ԭʯ��up���ǣ�������", round((wc - all_wai) * 100 / wc, 2), "%�����", max_buwai, "�����ᣬ���",
      max_wai, "����")
print("������", multiple_2, "��˫�ơ�", multiple_3, "�����ơ�", multiple_4, "���Ļơ�", multiple_5, "����ơ�", multiple_6,
      "�����ơ�", multiple_7, "���߻ơ�", multiple_8, "�ΰ˻ơ�", multiple_9, "�ξŻơ�", multiple_10, "��ʮ��")
print("����", x_f, "�����ǣ�ƽ����", round((pull_cost_f / x_f) * price, 1), "ԭʯ���ϣ��ۺϳ���", round(x_f * 100 / n, 3),
      "%�������ض�up���ǽ�ɫռ��", round((wc_f / x_f) * 100, 1),
      "%��ƽ����", round((pull_cost_f / wc_f) * price, 1), "ԭʯ���ض�up���ǣ���໨", cost_max_f * price,
      "ԭʯ���ض�up����")
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

range_c = 0.6  # ������
range_cc = 0.3  # up��ɫ����
range_w = 0.8  # 0.7
range_ww = 0.6  # 0.525
range_www = 0.2625
lose = 0
lose2 = 0
z = 0
wc = 0  # up��ɫ��
ww = 0  # up������
www = 0  # ����������
c = 0
cc = 0
ccc = 0
pull_num = 0
pull_min = 10000000
pull_max = 0
price = 160  # ÿ������ԭʯ
double = 0

start_time = time.time()
while n <= pull:
    if n % 1000000 == 0:
        # ������Ȱٷֱ�
        elapsed = time.time() - start_time
        progress = (n + 1) / (pull / 100)
        # �����Ѿ���ɵĽ���������
        num_hashes = int(progress)
        num_spaces = 100 - num_hashes
        # �����������ַ���
        progress_bar = f"������ȣ�{progress:.2f}%��Ԥ��ʣ��{elapsed / progress * (100 - progress):.1f}s [{'��' * num_hashes}{'_' * num_spaces}]"
        # ��ӡ��������ʹ�� \r ����֮ǰ�����
        print(f"\r{progress_bar}", end="")
    range_w = 0.7  # 0.8
    n += 1
    c += 1
    cc += 1
    ccc += 1
    if c >= 63:  # 67:  # ����
        z += 1  # �����ۼӴ���
        range_w *= z * 10 + 1
        # if c <= 70:  # 73:
        #     range_w *= z * 14 + 1  # 10 + 1
        # else:
        #     range_w *= z * 7 + 45.6  # 5 + 56
        if range_w > 100:
            range_w = 100
    if lose == 1:  # �󱣵�
        range_ww = range_w
        if lose2 == 1:  # ������
            range_www = range_w
        else:
            range_www = range_ww / 2
    elif lose2 == 1:  # ������
        range_ww = range_w
        range_www = range_w
    else:
        range_ww = range_w * 3 / 4
        range_www = range_ww / 2
    r = random.random()

    if r * 100 <= range_w:  # ����
        x += 1
        # if c < 10:
        #     double += 1
        if r * 100 <= range_ww:  # ��up
            if c > pull_max:
                pull_max = c
            if c < pull_min:
                pull_min = c
            ww += 1
            up[ww - 1] = cc
            if r * 100 <= range_www:  # ������
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
            else:  # ���Ƕ���
                lose = 0
                lose2 += 1
            cc = 0
        else:  # С������
            lose = 1
            lose2 += 1
        c = 0
        z = 0

print("\r����", x, "������������ƽ����", round((pull_cost / x) * price, 1), "ԭʯ�����ۺϳ���", round(x * 100 / n, 3),
      "%������up����ռ��",
      round((ww / x) * 100, 1), "%��ƽ����", round((pull_cost / ww) * price, 1), "ԭʯ��up����������ռ��",
      round((www / x) * 100, 1),
      "%��ƽ����", round((pull_cost / www) * price, 1), "ԭʯ�����죻��໨", cost_max * price, "ԭʯ������")
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

save = int(input("����������ԭʯ����"))  # ԭʯ����

while pull_c < len(c0):
    (n, x, pull_c, pull_cost, cost_min, cost_max) = count(n, x, pull_c, c0[pull_c], pull_cost, cost_min, cost_max)
print("0������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
      "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

while pull_c < len(c1):
    (n, x, pull_c, pull_cost, cost_min, cost_max) = count(n, x, pull_c, c1[pull_c], pull_cost, cost_min, cost_max)
print("1������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
      "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

while pull_c < len(c2):
    (n, x, pull_c, pull_cost, cost_min, cost_max) = count(n, x, pull_c, c2[pull_c], pull_cost, cost_min, cost_max)
print("2������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
      "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

while pull_c < len(c6):
    (n, x, pull_c, pull_cost, cost_min, cost_max) = count(n, x, pull_c, c6[pull_c], pull_cost, cost_min, cost_max)
print("6������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
      "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
(n, x, x_f, pull_c, pull_w, pull_cost, pull_cost_f, cost_min, cost_max, cost_max_f) = clear()

# while pull_w < len(up):
#     (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, up[pull_w], pull_cost, cost_min, cost_max)
# print("up��������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
#       "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_w < len(dg):
#     (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, dg[pull_w], pull_cost, cost_min, cost_max)
# print("������������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
#       "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c0):
#     while pull_w < len(up):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c0[pull_c] + up[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("0��+up��������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
#       "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c0):
#     while pull_w < len(dg):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c0[pull_c] + dg[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("0��+������������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
#       "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c1):
#     while pull_w < len(up):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c1[pull_c] + up[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("1��+up��������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
#       "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c1):
#     while pull_w < len(dg):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c1[pull_c] + dg[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("1��+������������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
#       "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c2):
#     while pull_w < len(up):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c2[pull_c] + up[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("2��+up��������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
#       "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()

# while pull_c < len(c2):
#     while pull_w < len(dg):
#         (n, x, pull_w, pull_cost, cost_min, cost_max) = count(n, x, pull_w, c2[pull_c] + dg[pull_w], pull_cost,
#                                                               cost_min, cost_max)
#     pull_c += 1
#     pull_w = 0
# print("2��+������������", n, "�ֿ����ԣ���������:", round((1 - x / n) * 100, 1),
#       "%��ƽ������", round(pull_cost / n, 1), "�����ٻ���", cost_min, "����໨��", cost_max)
# (n, x, pull_c, pull_w, pull_cost, cost_min, cost_max) = clear()
