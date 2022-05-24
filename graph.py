import ui
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#git test

class Main_graph():
    def initDATALIST(x1, y1):
        cnt = [1, 2, 3, 4, 5, 6, 7]
        for i in cnt[0:6]:
            x1[i] = str(x1[i])
            for i in cnt:
                y1[i] = int(y1[i])

            return x1, y1

    def initDATA1(self):
        data1 = pd.read_csv(self, encoding='cp949')
        df1 = pd.DataFrame(data1)

        x1 = df1.loc[0].to_list()
        y1 = df1.loc[1].to_list()

        x1, y1 = Main_graph.initDATALIST(x1, y1)
        Main_graph.initPLOT(x1, y1)


    def initDATA2(self):
        data2 = pd.read_csv(self)
        df2 = pd.DataFrame(data2)

        x1 = df2.loc[0].to_list()
        y1 = df2.loc[1].to_list()

        x1, y1 = Main_graph.initDATALIST(x1, y1)
        Main_graph.initPLOT(x1, y1)

    def initPLOT(x1, y1, x2, y2):
        plt.figure()

        plt.rc('font', family='Malgun Gothic')  # 그래프 한국어 설정

        fig, axs = plt.subplots(2, figsize=(7, 7))  # 그래프 2개 설정

        axs[0].plot(x1[1:7], y1[1:7], 'co-')  # 데이터 1 그래프 설정
        axs[0].ticklabel_format(axis='y', useOffset=False, style='plain')  # 데이터 1 y축 숫자 그대로 표기하기(없으면 과학적 표기로 변경됨)
        axs[0].set_xlabel('연도')
        axs[0].set_ylabel('1인 가구수(명)')
        axs[0].set_title('연도별 1인 가구수')
        axs[0].grid()

        # 데이터 1 그래프 상단, 우측 선 삭제
        axs[0].spines['right'].set_visible(False)
        axs[0].spines['top'].set_visible(False)

        axs[1].plot(x2[1:7], y2[1:7], 'mo-')  # 데이터 2 그래프 설정
        axs[1].set_xlabel('연도')  # 데이터 2 y축 숫자 그대로 표기하기(없으면 과학적 표기로 변경됨)
        axs[1].set_ylabel('무연고 사망자수(명)')
        axs[1].set_title('연도별 무연고 사망자수')
        axs[1].grid()

        # 데이터 2 그래프 상단, 우측 선 삭제
        axs[1].spines['right'].set_visible(False)
        axs[1].spines['top'].set_visible(False)

        plt.subplots_adjust(wspace=0.3, hspace=0.5)  # 그래프 2개 사이 거리 조절

        # for문: 마커 값 데이터 표시
        # for i in cnt[0:6]:
        #     height1 = y1[i]
        #     axs[0].text(x1[i], height1 + 80000, '%d' % height1, horizontalalignment='center', size=10)
        #
        # for i in cnt[0:6]:
        #     height2 = y2[i]
        #     axs[1].text(x2[i], height2 + 100, '%d' % height2, horizontalalignment='center', size=10)

        plt.show()



