# import .py
import ui

# import package
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

### 시도별 각 자료 데이터 프레임 추가하기

def setData2Frame(self):
    data = pd.read_csv(self, encoding='cp949')
    df = pd.DataFrame(data)
    return df

def setDataCsv(data_path_1, data_path_2, data_path_3, data_path_4):
    data1 = setData2Frame(data_path_1)
    data2 = setData2Frame(data_path_2)
    data3 = setData2Frame(data_path_3)
    data4 = setData2Frame(data_path_4)
    return data1, data2, data3, data4

def setFrame2Inf(data1, data2, data3, data4):
    opt = [data1, data2, data3, data4]  # 각 옵션별 데이터 프레임
    opt_corr = [data1, data2, data3, data4]  # 각 옵션별 상관계수 설정을 위한 데이터 프레임

    name = ['무연고', '기초생활수급자', '1인가구', '실업자']  # 특정 지역과 옵션을 묶기 위해 리스트 작성 1
    local = ['전국', '서울', '강원', '경기', '경남', '경북', '광주', '대구', '대전',
             '부산', '세종', '울산', '인천', '전북', '전남', '제주', '충북', '충남']  # 특정 지역과 옵션을 묶기 위해 리스트 작성 2

    df_local = []
    df_local_corr = []
    for i in range(18):
        df_local.append(0) #지역을 필터로 4개 옵션 비교를 위해 리스트 작성
        df_local_corr.append(0) #지역을 필터로 4개 옵션 비교 상관계수를 설정하기 위해 리스트 작성

    # 옵션별 데이터 행열 변환
    for i in range(len(opt)):
        df = opt[i].set_index('시도별')  # 인덱스 시도별 열로 변경
        opt[i] = df.transpose()  # 행열 전환

    # 지역별 데이터 인덱스 설정 후 행열 변환
    for i in range(len(local)):
        df_local[i] = pd.DataFrame()
        df_local[i] = data4.set_index('시도별')
        df_local[i] = df_local[i].transpose()  # 행열 전환

    # 지역별 상관관계 생성
    for i in range(len(name)):
        for j in range(len(local)):
            df_local[j][name[i] + '_' + local[j]] = opt[i][local[j]]

    # 지역별 상관관계를 위해 전국 열 삭제
    for i in range(len(local)):
        df_local[i].drop(local, axis=1, inplace=True)

    for i in range(len(local)):
        df_local_corr[i] = df_local[i].corr(method='pearson')  # 전국 무연고 사망자 기준 상관계수 분석(기초생활수급자/1인가구/실업자)

    opt_corr[0] = opt[0].corr(method='pearson')  # 지역별 무연고 사망자 상관계수 분석(전국~충남)

    return df_local, df_local_corr, opt


def setInf2Heat(df_local_corr, i, ax):
    sns.heatmap(df_local_corr[i], annot = True, fmt = '.6f', linewidths = .5, cbar_kws={"shrink": .5},
                cmap = 'RdYlBu_r', vmin = -1, vmax =1, ax = ax)
    ax.set_title("<1인가구와 고독사 현황>")


class initReg():
    def setInf2Reg(df_local, i, j, opt, ax):
        sns.regplot(x=df_local[i].iloc[:, [0]], y=df_local[0].iloc[:, [j]], data=opt[0], line_kws={'color': 'red'},
                    ax = ax)
        if j == 1:
            ax.set_title("<Scatter of 무연고 사망자와 기초생활수급자>")
        elif j == 2:
            ax.set_title("<Scatter of 무연고 사망자와 1인가구>")
        elif j == 3:
            ax.set_title("<Scatter of 무연고 사망자와 실업자>")
    def setInf2RegisnotCheck(df_local, i, j, opt, ax):
        sns.regplot(x=df_local[i].iloc[:, [0]], y=df_local[0].iloc[:, [j]], data=opt[0], line_kws={'color': 'red'},
                    fit_reg = False, ax = ax)
        if j == 1:
            ax.set_title("<Scatter of 무연고 사망자와 기초생활수급자>")
        elif j == 2:
            ax.set_title("<Scatter of 무연고 사망자와 1인가구>")
        elif j == 3:
            ax.set_title("<Scatter of 무연고 사망자와 실업자>")








#상관계수 HeatMap############################################
# plt.figure(figsize = (13,10))
# plt.rc('font', family='Malgun Gothic') #그래프 한국어 설정
#
# # 지역별 무연고 사망자와 그 외 옵션 상관계수 HEATMAP
# # df_local_corr[0번부터 17번]까지
# # ['전국(0)', '서울(1)', '강원(2)', '경기(3)', '경남(4)', '경북(5)', '광주(6)', '대구(7)', '대전(8)',
# #  '부산(9)', '세종(10)', '울산(11)', '인천(12)', '전북(13)', '전남(14)', '제주(15)', '충북(16)', '충남(17)']
# sns.heatmap(df_local_corr[0], annot = True, fmt = '.6f', linewidths = .5, cbar_kws={"shrink": .5}, cmap = 'RdYlBu_r', vmin = -1, vmax =1)
#
# plt.title("<1인가구와 고독사 현황>", fontsize = 23)
# plt.show()
#
#
# #산점도 그래프##############################################
# plt.figure(figsize = (13,10))
# plt.rc('font', family='Malgun Gothic') #그래프 한국어 설정
#
# # df_local[0번부터 17번]까지
# # ['전국(0)', '서울(1)', '강원(2)', '경기(3)', '경남(4)', '경북(5)', '광주(6)', '대구(7)', '대전(8)',
# #  '부산(9)', '세종(10)', '울산(11)', '인천(12)', '전북(13)', '전남(14)', '제주(15)', '충북(16)', '충남(17)']
# # df_local[].iloc[:,[0번부터 3번까지]]
# # ['무연고(0)', '기초생활수급자(1)', '1인가구(2)', '실업자(3)']
#
# # 지역별 무연고 사망자 [0]번의 무연고 사망자와 기초생활수급자 산점도
# a = sns.regplot(x = df_local[0].iloc[:,[0]], y = df_local[0].iloc[:,[1]], data=opt[0], line_kws={'color': 'red'})
# a.set_title('Scatter of 무연고 사망자와 1인가구')
#
# plt.show()