#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:21:27 2018

@author: kazuki.onodera
"""


# =============================================================================
# 
# =============================================================================

f001 = ['f001_NAME_CONTRACT_TYPE',
         'f001_CODE_GENDER',
         'f001_FLAG_OWN_CAR',
         'f001_FLAG_OWN_REALTY',
         'f001_NAME_TYPE_SUITE',
         'f001_NAME_INCOME_TYPE',
         'f001_NAME_EDUCATION_TYPE',
         'f001_NAME_FAMILY_STATUS',
         'f001_NAME_HOUSING_TYPE',
         'f001_OCCUPATION_TYPE',
         'f001_WEEKDAY_APPR_PROCESS_START',
         'f001_ORGANIZATION_TYPE',
         'f001_FONDKAPREMONT_MODE',
         'f001_HOUSETYPE_MODE',
         'f001_WALLSMATERIAL_MODE',
         'f001_EMERGENCYSTATE_MODE']

# =============================================================================
# 
# =============================================================================


f002 = ['f002_NAME_CONTRACT_TYPE-CODE_GENDER', 'f002_NAME_CONTRACT_TYPE-FLAG_OWN_CAR', 'f002_NAME_CONTRACT_TYPE-FLAG_OWN_REALTY', 'f002_NAME_CONTRACT_TYPE-NAME_TYPE_SUITE', 'f002_NAME_CONTRACT_TYPE-NAME_INCOME_TYPE', 'f002_NAME_CONTRACT_TYPE-NAME_EDUCATION_TYPE', 'f002_NAME_CONTRACT_TYPE-NAME_FAMILY_STATUS', 'f002_NAME_CONTRACT_TYPE-NAME_HOUSING_TYPE', 'f002_NAME_CONTRACT_TYPE-OCCUPATION_TYPE', 'f002_NAME_CONTRACT_TYPE-WEEKDAY_APPR_PROCESS_START', 'f002_NAME_CONTRACT_TYPE-ORGANIZATION_TYPE', 'f002_NAME_CONTRACT_TYPE-FONDKAPREMONT_MODE', 'f002_NAME_CONTRACT_TYPE-HOUSETYPE_MODE', 'f002_NAME_CONTRACT_TYPE-WALLSMATERIAL_MODE', 'f002_NAME_CONTRACT_TYPE-EMERGENCYSTATE_MODE', 'f002_CODE_GENDER-FLAG_OWN_CAR', 'f002_CODE_GENDER-FLAG_OWN_REALTY', 'f002_CODE_GENDER-NAME_TYPE_SUITE', 'f002_CODE_GENDER-NAME_INCOME_TYPE', 'f002_CODE_GENDER-NAME_EDUCATION_TYPE', 'f002_CODE_GENDER-NAME_FAMILY_STATUS', 'f002_CODE_GENDER-NAME_HOUSING_TYPE', 'f002_CODE_GENDER-OCCUPATION_TYPE', 'f002_CODE_GENDER-WEEKDAY_APPR_PROCESS_START', 'f002_CODE_GENDER-ORGANIZATION_TYPE', 'f002_CODE_GENDER-FONDKAPREMONT_MODE', 'f002_CODE_GENDER-HOUSETYPE_MODE', 'f002_CODE_GENDER-WALLSMATERIAL_MODE', 'f002_CODE_GENDER-EMERGENCYSTATE_MODE', 'f002_FLAG_OWN_CAR-FLAG_OWN_REALTY', 'f002_FLAG_OWN_CAR-NAME_TYPE_SUITE', 'f002_FLAG_OWN_CAR-NAME_INCOME_TYPE', 'f002_FLAG_OWN_CAR-NAME_EDUCATION_TYPE', 'f002_FLAG_OWN_CAR-NAME_FAMILY_STATUS', 'f002_FLAG_OWN_CAR-NAME_HOUSING_TYPE', 'f002_FLAG_OWN_CAR-OCCUPATION_TYPE', 'f002_FLAG_OWN_CAR-WEEKDAY_APPR_PROCESS_START', 'f002_FLAG_OWN_CAR-ORGANIZATION_TYPE', 'f002_FLAG_OWN_CAR-FONDKAPREMONT_MODE', 'f002_FLAG_OWN_CAR-HOUSETYPE_MODE', 'f002_FLAG_OWN_CAR-WALLSMATERIAL_MODE', 'f002_FLAG_OWN_CAR-EMERGENCYSTATE_MODE', 'f002_FLAG_OWN_REALTY-NAME_TYPE_SUITE', 'f002_FLAG_OWN_REALTY-NAME_INCOME_TYPE', 'f002_FLAG_OWN_REALTY-NAME_EDUCATION_TYPE', 'f002_FLAG_OWN_REALTY-NAME_FAMILY_STATUS', 'f002_FLAG_OWN_REALTY-NAME_HOUSING_TYPE', 'f002_FLAG_OWN_REALTY-OCCUPATION_TYPE', 'f002_FLAG_OWN_REALTY-WEEKDAY_APPR_PROCESS_START', 'f002_FLAG_OWN_REALTY-ORGANIZATION_TYPE', 'f002_FLAG_OWN_REALTY-FONDKAPREMONT_MODE', 'f002_FLAG_OWN_REALTY-HOUSETYPE_MODE', 'f002_FLAG_OWN_REALTY-WALLSMATERIAL_MODE', 'f002_FLAG_OWN_REALTY-EMERGENCYSTATE_MODE', 'f002_NAME_TYPE_SUITE-NAME_INCOME_TYPE', 'f002_NAME_TYPE_SUITE-NAME_EDUCATION_TYPE', 'f002_NAME_TYPE_SUITE-NAME_FAMILY_STATUS', 'f002_NAME_TYPE_SUITE-NAME_HOUSING_TYPE', 'f002_NAME_TYPE_SUITE-OCCUPATION_TYPE', 'f002_NAME_TYPE_SUITE-WEEKDAY_APPR_PROCESS_START', 'f002_NAME_TYPE_SUITE-ORGANIZATION_TYPE', 'f002_NAME_TYPE_SUITE-FONDKAPREMONT_MODE', 'f002_NAME_TYPE_SUITE-HOUSETYPE_MODE', 'f002_NAME_TYPE_SUITE-WALLSMATERIAL_MODE', 'f002_NAME_TYPE_SUITE-EMERGENCYSTATE_MODE', 'f002_NAME_INCOME_TYPE-NAME_EDUCATION_TYPE', 'f002_NAME_INCOME_TYPE-NAME_FAMILY_STATUS', 'f002_NAME_INCOME_TYPE-NAME_HOUSING_TYPE', 'f002_NAME_INCOME_TYPE-OCCUPATION_TYPE', 'f002_NAME_INCOME_TYPE-WEEKDAY_APPR_PROCESS_START', 'f002_NAME_INCOME_TYPE-ORGANIZATION_TYPE', 'f002_NAME_INCOME_TYPE-FONDKAPREMONT_MODE', 'f002_NAME_INCOME_TYPE-HOUSETYPE_MODE', 'f002_NAME_INCOME_TYPE-WALLSMATERIAL_MODE', 'f002_NAME_INCOME_TYPE-EMERGENCYSTATE_MODE', 'f002_NAME_EDUCATION_TYPE-NAME_FAMILY_STATUS', 'f002_NAME_EDUCATION_TYPE-NAME_HOUSING_TYPE', 'f002_NAME_EDUCATION_TYPE-OCCUPATION_TYPE', 'f002_NAME_EDUCATION_TYPE-WEEKDAY_APPR_PROCESS_START', 'f002_NAME_EDUCATION_TYPE-ORGANIZATION_TYPE', 'f002_NAME_EDUCATION_TYPE-FONDKAPREMONT_MODE', 'f002_NAME_EDUCATION_TYPE-HOUSETYPE_MODE', 'f002_NAME_EDUCATION_TYPE-WALLSMATERIAL_MODE', 'f002_NAME_EDUCATION_TYPE-EMERGENCYSTATE_MODE', 'f002_NAME_FAMILY_STATUS-NAME_HOUSING_TYPE', 'f002_NAME_FAMILY_STATUS-OCCUPATION_TYPE', 'f002_NAME_FAMILY_STATUS-WEEKDAY_APPR_PROCESS_START', 'f002_NAME_FAMILY_STATUS-ORGANIZATION_TYPE', 'f002_NAME_FAMILY_STATUS-FONDKAPREMONT_MODE', 'f002_NAME_FAMILY_STATUS-HOUSETYPE_MODE', 'f002_NAME_FAMILY_STATUS-WALLSMATERIAL_MODE', 'f002_NAME_FAMILY_STATUS-EMERGENCYSTATE_MODE', 'f002_NAME_HOUSING_TYPE-OCCUPATION_TYPE', 'f002_NAME_HOUSING_TYPE-WEEKDAY_APPR_PROCESS_START', 'f002_NAME_HOUSING_TYPE-ORGANIZATION_TYPE', 'f002_NAME_HOUSING_TYPE-FONDKAPREMONT_MODE', 'f002_NAME_HOUSING_TYPE-HOUSETYPE_MODE', 'f002_NAME_HOUSING_TYPE-WALLSMATERIAL_MODE', 'f002_NAME_HOUSING_TYPE-EMERGENCYSTATE_MODE', 'f002_OCCUPATION_TYPE-WEEKDAY_APPR_PROCESS_START', 'f002_OCCUPATION_TYPE-ORGANIZATION_TYPE', 'f002_OCCUPATION_TYPE-FONDKAPREMONT_MODE', 'f002_OCCUPATION_TYPE-HOUSETYPE_MODE', 'f002_OCCUPATION_TYPE-WALLSMATERIAL_MODE', 'f002_OCCUPATION_TYPE-EMERGENCYSTATE_MODE', 'f002_WEEKDAY_APPR_PROCESS_START-ORGANIZATION_TYPE', 'f002_WEEKDAY_APPR_PROCESS_START-FONDKAPREMONT_MODE', 'f002_WEEKDAY_APPR_PROCESS_START-HOUSETYPE_MODE', 'f002_WEEKDAY_APPR_PROCESS_START-WALLSMATERIAL_MODE', 'f002_WEEKDAY_APPR_PROCESS_START-EMERGENCYSTATE_MODE', 'f002_ORGANIZATION_TYPE-FONDKAPREMONT_MODE', 'f002_ORGANIZATION_TYPE-HOUSETYPE_MODE', 'f002_ORGANIZATION_TYPE-WALLSMATERIAL_MODE', 'f002_ORGANIZATION_TYPE-EMERGENCYSTATE_MODE', 'f002_FONDKAPREMONT_MODE-HOUSETYPE_MODE', 'f002_FONDKAPREMONT_MODE-WALLSMATERIAL_MODE', 'f002_FONDKAPREMONT_MODE-EMERGENCYSTATE_MODE', 'f002_HOUSETYPE_MODE-WALLSMATERIAL_MODE', 'f002_HOUSETYPE_MODE-EMERGENCYSTATE_MODE', 'f002_WALLSMATERIAL_MODE-EMERGENCYSTATE_MODE']



# =============================================================================
# 
# =============================================================================

f108 = ['f108_NAME_CONTRACT_TYPE',
                     'f108_WEEKDAY_APPR_PROCESS_START',
                     'f108_NAME_CASH_LOAN_PURPOSE',
                     'f108_NAME_CONTRACT_STATUS',
                     'f108_NAME_PAYMENT_TYPE',
                     'f108_CODE_REJECT_REASON',
                     'f108_NAME_TYPE_SUITE',
                     'f108_NAME_CLIENT_TYPE',
                     'f108_NAME_GOODS_CATEGORY',
                     'f108_NAME_PORTFOLIO',
                     'f108_NAME_PRODUCT_TYPE',
                     'f108_CHANNEL_TYPE',
                     'f108_NAME_SELLER_INDUSTRY',
                     'f108_NAME_YIELD_GROUP',
                     'f108_PRODUCT_COMBINATION']

# =============================================================================
# 
# =============================================================================
f109 = ['f109_NAME_CONTRACT_TYPE',
         'f109_WEEKDAY_APPR_PROCESS_START',
         'f109_NAME_CASH_LOAN_PURPOSE',
         'f109_NAME_CONTRACT_STATUS',
         'f109_NAME_PAYMENT_TYPE',
         'f109_CODE_REJECT_REASON',
         'f109_NAME_TYPE_SUITE',
         'f109_NAME_CLIENT_TYPE',
         'f109_NAME_GOODS_CATEGORY',
         'f109_NAME_PORTFOLIO',
         'f109_NAME_PRODUCT_TYPE',
         'f109_CHANNEL_TYPE',
         'f109_NAME_SELLER_INDUSTRY',
         'f109_NAME_YIELD_GROUP',
         'f109_PRODUCT_COMBINATION']

# =============================================================================
# 
# =============================================================================
maxwell = ['FLAG_PHONE_PATTERN', 'FLAG_DOC_PATTERN']



# =============================================================================
# all
# =============================================================================

ALL = f001 + f002 + f108 + f109 + maxwell


































