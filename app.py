# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:09:22 2021

@author: h8273
"""
#[1]
if __name__ == '__main__':
    # You should not modify this part, but additional arguments are allowed.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')

    parser.add_argument('--output',
                        default='submission.csv',
                        help='output file name')
    args = parser.parse_args()


import pmdarima as pm
import numpy as np
import pandas as pd
from pmdarima.arima import ndiffs

# load data
df_training = pd.read_csv(args.training)
data = np.array(df_training)[:, 1]
data *= 10
train = data[-30:]
#%%
# [2]

# choose diffencing
kpss_diffs = ndiffs(train, alpha=0.05, test='kpss', max_d=6)
adf_diffs = ndiffs(train, alpha=0.05, test='adf', max_d=6)
n_diffs = max(adf_diffs, kpss_diffs)

# Fit a simple auto_arima model
auto = pm.auto_arima(train, d=n_diffs, seasonal=False, stepwise=True,
                     suppress_warnings=True, error_action="ignore", max_p=6,
                     max_order=None, trace=True)

# predict with range of 3/22 to 3/29
fc, conf_int = auto.predict(n_periods=8, return_conf_int=True)
#%%
# [3]
# output the result
date = ['20210323', '20210324', '20210325', '20210326', '20210327',
        '20210328', '20210329']
output = pd.DataFrame({"date": date, "operating_reserve(MW)": fc[1:]})
output.to_csv(args.output, index = 0)
