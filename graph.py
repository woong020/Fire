# import package
import seaborn as sns
import pandas as pd



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
    df_local_corr2 = []
    df_local_corr3 = []
    df_local_corr4 = []

    for i in range(18):
        df_local.append(0) # 지역을 필터로 4개 옵션 비교를 위해 리스트 작성
        df_local_corr.append(0) # 지역을 필터로 4개 옵션 비교 상관계수를 설정하기 위해 리스트 작성
        df_local_corr2.append(0) # local2 기초생활수급자수와의 상관관계를 위한 리스트 설정
        df_local_corr3.append(0) # local3 1인가구수와의 상관관계를 위한 리스트 설정
        df_local_corr4.append(0) # local4 실업자수와의 상관관계를 위한 리스트 설정

    # 옵션별 데이터 행열 변환
    for i in range(len(opt)):
        df = opt[i].set_index('시도별')  # 인덱스 시도별 열로 변경
        opt[i] = df.transpose()  # 행열 전환

    # 세종시 결측치 보완
    opt[2]['세종'] = opt[2]['세종'].fillna(method='backfill')
    opt[3]['세종'] = opt[3]['세종'].fillna(method='backfill')

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

    for i in range(len(df_local)):
        df_local_corr[i] = df_local[i].corr(method='pearson')  # 전국 무연고 사망자 기준 상관계수 분석(기초생활수급자/1인가구/실업자)

    # 무연고 사망자수와 다른 옵션들(기초생활수급자/1인가구/실업자와의 상관관계 값 표시)
    for i in range(len(local)):
        df_local_corr2[i] = df_local[i]['무연고_' + local[i]].corr(df_local[i]['기초생활수급자_' + local[i]], method='pearson')
        df_local_corr3[i] = df_local[i]['무연고_' + local[i]].corr(df_local[i]['1인가구_' + local[i]], method='pearson')
        df_local_corr4[i] = df_local[i]['무연고_' + local[i]].corr(df_local[i]['실업자_' + local[i]], method='pearson')

    return df_local, df_local_corr, opt, df_local_corr2, df_local_corr3, df_local_corr4

def setInf2Heat(df_local_corr, i, ax):
    sns.heatmap(df_local_corr[i], annot=True, fmt='.6f', linewidths=.5, cbar=True,
                cbar_kws={"shrink": .5}, cmap='RdYlBu_r', vmin=0.4, vmax=1, ax=ax)  # 'RdYlBu_r' 'YIGnBu'
    ax.set_title("<1인가구와 고독사 현황>")
    ax.set_yticklabels(ax.get_yticklabels(), size=7)
    ax.set_xticklabels(ax.get_xticklabels(), size=7)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

def initCorrHeatmap(df_local_corr, i):
    p = i  # 지역코드 i 를 p에 할당
    local = ['전국', '서울', '강원', '경기', '경남', '경북', '광주', '대구', '대전',
             '부산', '세종', '울산', '인천', '전북', '전남', '제주', '충북', '충남']  # 지역 코드

    if df_local_corr[p]['기초생활수급자_' + local[p]][0] > df_local_corr[p]['1인가구_' + local[p]][0] > \
            df_local_corr[p]['실업자_' + local[p]][0]:
        x = '기초생활수급자 > 1인가구 > 실업자'
    elif df_local_corr[p]['기초생활수급자_' + local[p]][0] > df_local_corr[p]['실업자_' + local[p]][0] > \
            df_local_corr[p]['1인가구_' + local[p]][0]:
        x = '기초생활수급자 > 실업자 > 1인가구'
    elif df_local_corr[p]['1인가구_' + local[p]][0] > df_local_corr[p]['기초생활수급자_' + local[p]][0] > \
            df_local_corr[p]['실업자_' + local[p]][0]:
        x = '1인가구 > 기초생활수급자 > 실업자'
    elif df_local_corr[p]['1인가구_' + local[p]][0] > df_local_corr[p]['실업자_' + local[p]][0] > \
            df_local_corr[p]['기초생활수급자_' + local[p]][0]:
        x = '1인가구 > 실업자 > 기초생활수급자'
    elif df_local_corr[p]['실업자_' + local[p]][0] > df_local_corr[p]['기초생활수급자_' + local[p]][0] > \
            df_local_corr[p]['1인가구_' + local[p]][0]:
        x = '실업자 > 기초생활수급자 > 1인가구'
    elif df_local_corr[p]['실업자_' + local[p]][0] > df_local_corr[p]['1인가구_' + local[p]][0] > \
            df_local_corr[p]['기초생활수급자_' + local[p]][0]:
        x = '실업자 > 1인가구 > 기초생활수급자'

    res = local[p] + ' : ' + x
    return res


class initReg():
    def setInf2Reg(df_local, i, j, opt, ax, corr1, corr2, corr3):
        graph = sns.regplot(x=df_local[i].iloc[:, [0]], y=df_local[0].iloc[:, [j]], data=opt[0], line_kws={'color': 'red'},
                    ax = ax)
        graph.ticklabel_format(axis='y', useOffset=False, style='plain')  # y축 숫자 그대로 표기하기(없으면 과학적 표기로 변경됨)
        if j == 1:
            ax.set_title("<Scatter of 무연고 사망자와 기초생활수급자>")
            res = str(corr1[i])
            return res
        elif j == 2:
            ax.set_title("<Scatter of 무연고 사망자와 1인가구>")
            res = str(corr2[i])
            return res
        elif j == 3:
            ax.set_title("<Scatter of 무연고 사망자와 실업자>")
            res = str(corr3[i])
            return res
    def setInf2RegisnotCheck(df_local, i, j, opt, ax, corr1, corr2, corr3):
        graph = sns.regplot(x=df_local[i].iloc[:, [0]], y=df_local[0].iloc[:, [j]], data=opt[0], line_kws={'color': 'red'},
                    fit_reg = False, ax = ax)
        graph.ticklabel_format(axis='y', useOffset=False, style='plain')  # y축 숫자 그대로 표기하기(없으면 과학적 표기로 변경됨)
        if j == 1:
            ax.set_title("<Scatter of 무연고 사망자와 기초생활수급자>")
            res = str(corr1[i])
            return res
        elif j == 2:
            ax.set_title("<Scatter of 무연고 사망자와 1인가구>")
            res = str(corr2[i])
            return res
        elif j == 3:
            ax.set_title("<Scatter of 무연고 사망자와 실업자>")
            res = str(corr3[i])
            return res

