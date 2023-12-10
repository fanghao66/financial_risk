import pandas  as pd
import numpy as np

def badrate(x):
    return (x==0).mean(axis=0)



def sigle_analysis_badrate(index,data:pd.DataFrame,name:list=False):
    if not name:
        all_indexes = {}
        for var in data.columns:
            var_class = list(set(data[var]))
            labels = data.iloc[:,-1]
            data_var = data[var]
            indexes = {}
            for _class in var_class:
                _c=data_var[data_var.values==_class]
                _label= labels.loc[_c.index]
                index_ = index(_label)
                indexes[_class]=index_
            all_indexes[var]=indexes
    else:
        all_indexes = {}
        for var in name:
            var_class = list(set(data[var]))
            labels = data.iloc[:, -1]
            data_var = data[var]
            indexes = {}
            for _class in var_class:
                _c = data_var[data_var.values == _class]
                _label = labels.loc[ _c.index]
                index_ = index(_label)
                indexes[_class] = index_
            all_indexes[var] = indexes
    return all_indexes
