# -*- coding: utf-8 -*-
"""
Created on Thu Jul 09 16:38:17 2015

@author: t72j7j2
"""

import pandas as pd
import sys

def check_stats(df):
    print df.shape
    print df.head(10)   
    
def check_sum_sqn(df):
    print ""
    new_df = df.groupby('toy_sqn').count()
    print "There are %i unique toy sqns." % len(new_df.index.tolist())
    print ""
    print "The following toy sqns have no associated toy name:"
    print new_df[new_df['toy_nm']==0].index.tolist()
    print ""
    print "The following toy sqns have no associated toy address:"
    print new_df[new_df['toy_add']==0].index.tolist()
    print ""
    print "The following distribution of coolness is associated with toy sqns having no toy name:"
    new_df_list = df.groupby('toy_sqn').last()
    print new_df_list[new_df['toy_nm']==0]['toy_status'].value_counts()
    print ""
    print "The following distribution of coolness is associated with toy sqns having no toy address:"
    new_df_list = df.groupby('toy_sqn').last()
    print new_df_list[new_df['toy_add']==0]['toy_status'].value_counts()

data_frame = pd.DataFrame(pd.read_csv(sys.argv[1], low_memory=False))

#check_stats(data_frame)
check_sum_sqn(data_frame)
