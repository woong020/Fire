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

    def initDATA1(self):
        data1 = pd.read_csv(self, encoding='cp949')
        df1 = pd.DataFrame(data1)

        x1 = df1.loc[0].to_list()
        y1 = df1.loc[1].to_list()

        Main_graph.initDATALIST(self, x1, y1)



    def initDATA2(self):
        data2 = pd.read_csv(self)
        df2 = pd.DataFrame(data2)

        x1 = df2.loc[0].to_list()
        y1 = df2.loc[1].to_list()

        x1, y1 = Main_graph.initDATALIST(x1, y1)

    def initPLOT(self):



