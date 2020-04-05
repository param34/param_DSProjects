# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:12:27 2020

@author: parvishw
"""

import pandas as pd

person = {
    
    'name':["AJay","Jay",'Mohan'],
    'age':[20,30 ,40],
    'email':["a@abc.com","b@xyz.com","c@pqr.com"]
       }



#df = pd.DataFrame(person,columns=['name','B','C','age'])
#df = pd.DataFrame(person)
df = pd.read_csv("survey_results_public.csv")
#print(df.info())

#print(df.loc[1:4,'MainBranch':'Country'])

########### grouping

country_grp = df.groupby(['Country'])
print(country_grp.get_group('United States'))


filt = df['Country'] == 'India'

df2 = df.loc[filt]['SocialMedia'].value_counts()
#print(df2)

# group by social media
df3 =country_grp['SocialMedia'].value_counts().head()
print(df3)

print(country_grp['ConvertedComp'].median().loc['India'])
##### get multiple fun
print(country_grp['ConvertedComp'].agg(['median','min']).loc['India'])


country_responds= df['Country'].value_counts()
country_use_python=country_grp['LanguageWorkedWith'].apply(lambda x:x.str.contains('Python').sum())

df4 = pd.concat([country_responds,country_use_python]
                ,axis='columns',sort=False)


print(df4)