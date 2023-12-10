import pandas as pd
import numpy as np
from 单变量分析 import badrate,sigle_analysis_badrate
def t1():
    data = pd.DataFrame(np.random.randint(0,5,(100,50)),columns=range(50))
    index = sigle_analysis_badrate(badrate,data)
    print()
def t2():
    data = pd.DataFrame(np.random.randint(0, 5, (100, 50)), columns=range(50))
    index = sigle_analysis_badrate(badrate, data,name=[1,])
    print()
if __name__ == '__main__':
    t2()