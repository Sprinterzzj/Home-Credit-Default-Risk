#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:23:35 2018

@author: kazuki.onodera
"""

import numpy as np
import pandas as pd
import os
import utils
utils.start(__file__)
#==============================================================================

PREF = 'prev_101_'

KEY = 'SK_ID_CURR'

os.system(f'rm ../feature/t*_{PREF}*')
# =============================================================================
# 
# =============================================================================
prev = utils.read_pickles('../data/previous_application')
base = prev[[KEY]].drop_duplicates().set_index(KEY)

gr = prev.groupby(KEY)
gr_app = prev[prev['NAME_CONTRACT_STATUS']=='Approved'].groupby(KEY)
gr_ref = prev[prev['NAME_CONTRACT_STATUS']=='Refused'].groupby(KEY)
gr_act = prev[prev['active']==1].groupby(KEY)
gr_cmp = prev[prev['completed']==1].groupby(KEY)

col = ['AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY', 
       'AMT_CREDIT-dby-AMT_ANNUITY', 'DAYS_BIRTH']
train = utils.load_train([KEY]+col)
test = utils.load_test([KEY]+col)

train.columns = [KEY] + ['app_'+c for c in train.columns[1:]]
test.columns  = [KEY] + ['app_'+c for c in test.columns[1:]]

col_init = train.columns.tolist()

# =============================================================================
# feature
# =============================================================================

c = 'total_debt'
base[f'{c}_min']  = gr[c].min()
base[f'{c}_mean'] = gr[c].mean()
base[f'{c}_max']  = gr[c].max()
base[f'{c}_sum'] = gr[c].sum()

c = 'amt_paid'
base[f'{c}_min']  = gr[c].min()
base[f'{c}_mean'] = gr[c].mean()
base[f'{c}_max']  = gr[c].max()
base[f'{c}_sum'] = gr[c].sum()

c = 'amt_unpaid'
base[f'{c}_min']  = gr[c].min()
base[f'{c}_mean'] = gr[c].mean()
base[f'{c}_max']  = gr[c].max()
base[f'{c}_sum'] = gr[c].sum()

c = 'cnt_paid'
base[f'{c}_min']  = gr[c].min()
base[f'{c}_mean'] = gr[c].mean()
base[f'{c}_max']  = gr[c].max()
base[f'{c}_sum'] = gr[c].sum()

c = 'cnt_unpaid'
base[f'{c}_min']  = gr[c].min()
base[f'{c}_mean'] = gr[c].mean()
base[f'{c}_max']  = gr[c].max()
base[f'{c}_sum'] = gr[c].sum()

c = 'AMT_ANNUITY'
base[f'{c}_act_min']  = gr_act[c].min()
base[f'{c}_act_mean'] = gr_act[c].mean()
base[f'{c}_act_max']  = gr_act[c].max()
base[f'{c}_act_sum'] = gr_act[c].sum()

c = 'DAYS_LAST_DUE_1ST_VERSION'
base[f'{c}_act_min']  = gr_act[c].min()
base[f'{c}_act_mean'] = gr_act[c].mean()
base[f'{c}_act_max']  = gr_act[c].max()
base[f'{c}_act_sum'] = gr_act[c].sum()


base['active_cnt'] = gr['active'].sum()
base['active_ratio'] = gr['active'].mean()
base['completed_cnt'] = gr['completed'].sum()

base['DAYS_DECISION_min'] = gr['DAYS_DECISION'].min()
base['DAYS_DECISION_max'] = gr['DAYS_DECISION'].max()

base['amt_paid_sum-dby-total_debt_sum'] = base['amt_paid_sum'] / base['total_debt_sum']
base['amt_paid_sum-dby-amt_unpaid_sum'] = base['amt_paid_sum'] / base['amt_unpaid_sum']


# app, ref
base['cnt_approved'] = gr_app.size()
base['cnt_refused'] = gr_ref.size()
base['approved_ratio'] = base['cnt_approved'] / base['cnt_approved'] + base['cnt_refused'] 

base['DAYS_DECISION_app_min'] = gr_app['DAYS_DECISION'].min()
base['DAYS_DECISION_app_max'] = gr_app['DAYS_DECISION'].max()

base['DAYS_DECISION_ref_min'] = gr_ref['DAYS_DECISION'].min()
base['DAYS_DECISION_ref_max'] = gr_ref['DAYS_DECISION'].max()



# future payment
col = prev.head().filter(regex='^amt_future_payment_').columns
col_future = []
for c in col:
    base[f'{c}_sum'] = gr_app[c].sum()
    col_future.append(f'{c}_sum')

# past payment
col = prev.head().filter(regex='^amt_past_payment_').columns
col_past = []
for c in col:
    base[f'{c}_sum'] = gr_app[c].sum()
    col_past.append(f'{c}_sum')


base.reset_index(inplace=True)

# =============================================================================
# merge
# =============================================================================

def mk_feature(df):
    
    df[col_future+col_past] = df[col_future+col_past].fillna(0)
    df['total_debt_sum-p-app']            = df['total_debt_sum'] + df['app_AMT_CREDIT']
    df['total_debt_sum-p-app-dby-income'] = df['total_debt_sum-p-app'] / df['app_AMT_INCOME_TOTAL']
    df['amt_unpaid_sum-p-app']            = df['amt_unpaid_sum'] + df['app_AMT_CREDIT']
    df['amt_unpaid_sum-p-app-dby-income'] = df['amt_unpaid_sum-p-app'] / df['app_AMT_INCOME_TOTAL']

    # future payment
    col_1 = []
    col_2 = []
    df['tmp'] = df['app_AMT_CREDIT-dby-AMT_ANNUITY'].map(np.ceil)
    for i,c in enumerate( col_future ):
        c1 = f'amt_future_payment-p-app_{i+1}m'
        c2 = f'amt_future_payment-p-app_{i+1}m-dby-AMT_INCOME_TOTAL'
        df[c1] = df[c] + df['tmp'].map(lambda x: min(x, 1)) * df['app_AMT_ANNUITY']
        df[c2] = df[c1] / df['app_AMT_INCOME_TOTAL']
        df['tmp'] -= 1
        df['tmp'] = df['tmp'].map(lambda x: max(x, 0))
        col_1.append(c1); col_2.append(c2)
        
    del df['tmp']
    
    df['amt_future_payment-p-app_max'] = df[col_1].max(1)
    df['amt_future_payment-p-app-dby-AMT_INCOME_TOTAL_max'] = df[col_2].max(1)
    df['amt_past_payment_sum_max'] = df[col_past].max(1)
    
    df['amt_future_payment-p-app_max-dby-amt_past_payment_sum_max'] = df['amt_future_payment-p-app_max'] / df['amt_past_payment_sum_max']
    
    df['DAYS_DECISION_min-m-DAYS_BIRTH'] = df['DAYS_DECISION_min'] - df['app_DAYS_BIRTH']
    df['DAYS_DECISION_max-m-DAYS_BIRTH'] = df['DAYS_DECISION_max'] - df['app_DAYS_BIRTH']



train2 = pd.merge(train, base, on=KEY, how='left')
mk_feature(train2)


test2 = pd.merge(test, base, on=KEY, how='left')
mk_feature(test2)

# =============================================================================
# output
# =============================================================================
train2.drop(col_init, axis=1, inplace=True)
test2.drop(col_init, axis=1, inplace=True)
utils.to_feature(train2.add_prefix(PREF), '../feature/train')
utils.to_feature(test2.add_prefix(PREF),  '../feature/test')

#==============================================================================
utils.end(__file__)


