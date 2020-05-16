#!/usr/bin/env python
# coding: utf-8

# In[355]:


import pandas as pd
import collections as cl
import datetime as dt
import itertools as it
import numpy as np


# In[356]:


data=pd.read_csv('data.csv',encoding='koi8_u',parse_dates=['release_date'])
display(data)


# In[357]:


answer=[] #Создаю список ответов


# # Вопрос "1"
# ## У какого фильма из списка самый большой бюджет?
# 1. The Dark Knight Rises (tt1345836) 
# 2. Spider-Man 3 (tt0413300) 
# 3. Avengers: Age of Ultron (tt2395427) 
# 4. The Warrior's Way (tt1032751) 
# 5. Pirates of the Caribbean: On Stranger Tides (tt1298650) 
# 

# In[358]:


answer.append('4')


# In[359]:


data.info()


# In[360]:


data[data.budget==data.budget.max()].original_title


# In[361]:


data.loc[data.original_title=="The Warrior's Way"]


# # Вопрос 2  
# ## Какой из фильмов самый длительный (в минутах)?
# 1. The Lord of the Rings: The Return of the King (tt0167260) 
# 2. Gods and Generals (tt0279111) 
# 3. King Kong (tt0360717) 
# 4. Pearl Harbor (tt0213149) 
# 5. Alexander (tt0346491) 

# In[362]:


answer.append('2')


# In[363]:


data.loc[data.runtime==data.runtime.max()]


# # Вопрос 3
# ## Какой из фильмов самый короткий (в минутах)?
# 1. Home on the Range tt0299172 
# 2. The Jungle Book 2 tt0283426 
# 3. Winnie the Pooh tt1449283 
# 4. Corpse Bride tt0121164 
# 5. Hoodwinked! tt0443536 

# In[364]:


data.loc[data.runtime==data.runtime.min()]


# In[365]:


answer.append('3')


# In[366]:


data.describe()


# In[367]:


data.runtime.mean()


# # Вопрос 4 
# ## Какое число ближе к средней длительности фильма в датасете?
# 1. 115 
# 2. 110 
# 3. 105 
# 4. 120 
# 5. 100 

# In[368]:


answer.append('2')


# # Вопрос 5 
# ## Какое число ближе к медианной длительности фильма в датасете?
# 1. 106 
# 2. 112 
# 3. 101 
# 4. 120 
# 5. 115 

# In[369]:


data.runtime.median()


# In[370]:


answer.append('1')


# # Вопрос 6 
# ## Какой самый прибыльный фильм?
# 
# Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма.
# 1. The Avengers tt0848228 
# 2. Minions tt2293640 
# 3. Star Wars: The Force Awakens tt2488496 
# 4. Furious 7 tt2820852 
# 5. Avatar tt0499549 

# In[371]:


data['Profit']=data.revenue-data.budget
data.loc[data.Profit==data.Profit.max()]


# In[372]:


answer.append('5')


# # Вопрос 7 
# ## Какой фильм самый убыточный?
# 1. Supernova tt0134983 
# 2. The Warrior's Way tt1032751 
# 3. Flushed Away tt0424095 
# 4. The Adventures of Pluto Nash tt0180052 
# 5. The Lone Ranger tt1210819 

# In[373]:


data[data.Profit==data.Profit.min()].original_title


# In[374]:


answer.append('2')


# # Вопрос 8  
# ## У скольких фильмов из датасета объем сборов оказался выше бюджета?
# 1. 1478 
# 2. 1520 
# 3. 1241 
# 4. 1135 
# 5. 1398 

# In[375]:


data[data.revenue>data.budget].original_title.count()


# In[376]:


answer.append('1')


# # Вопрос 9 
# 
# ## Какой фильм оказался самым кассовым в 2008 году?
# 1. Madagascar: Escape 2 Africa tt0479952 
# 2. Iron Man tt0371746 
# 3. Kung Fu Panda tt0441773 
# 4. The Dark Knight tt0468569 
# 5. Mamma Mia! tt0795421 

# In[377]:


data.loc[data.popularity==data[data.release_year==2008].popularity.max()]


# In[378]:


answer.append('4')


# # Вопрос 10 
# ## Самый убыточный фильм за период с 2012 по 2014 гг. (включительно)?
# 1. Winter's Tale tt1837709 
# 2. Stolen tt1656186 
# 3. Broken City tt1235522 
# 4. Upside Down tt1374992 
# 5. The Lone Ranger tt1210819 

# In[379]:


data.loc[data.Profit==data[(data.release_year<=2014)&(data.release_year>=2012)].Profit.min()]


# In[380]:


answer.append('5')


# # Вопрос 11 
# ## Какого жанра фильмов больше всего? 
# 1. Action 
# 2. Adventure 
# 3. Drama 
# 4. Comedy 
# 5. Thriller 

# In[381]:


data.genres.describe() 


# In[382]:


answer.append('3')


# In[383]:


genres=data.genres.map(lambda x:x.split('|',))
import collections
c=collections.Counter()
for gen in genres:
    for word in gen:
        c[word]+=1
print(c)


# # Вопрос 12 
# 
# ## Какого жанра среди прибыльных фильмов больше всего? 
# 1. Action 
# 2. Adventure 
# 3. Drama 
# 4. Comedy 
# 5. Thriller 

# In[384]:


genres=pd.DataFrame(data[data.Profit>0].genres.str.split('|').tolist()).stack()
cl.Counter(genres).most_common()


# In[385]:


answer.append("3")


# # Вопрос 13  
# ## Кто из режиссеров снял больше всего фильмов? 
# 1. Steven Spielberg 
# 2. Ridley Scott 
# 3. Steven Soderbergh 
# 4. Christopher Nolan 
# 5. Clint Eastwood 

# In[386]:


data.director.value_counts()


# In[387]:


answer.append('3')


# # Вопрос 14 
# ## Кто из режиссеров снял больше всего прибыльных фильмов? 
# 1. Steven Spielberg 
# 2. Ridley Scott 
# 3. Steven Soderbergh 
# 4. Christopher Nolan 
# 5. Clint Eastwood 

# In[388]:


data[data.Profit>0].director.value_counts()


# In[389]:


answer.append('2')


# # Вопрос 15 
# ## Кто из режиссеров принес больше всего прибыли?
# 1. Steven Spielberg 
# 2. James Cameron 
# 3. Christopher Nolan 
# 4. David Yates 
# 5. Peter Jackson 
# 

# In[390]:


data[data.Profit==data.Profit.max()].director#Неверный ответ


# In[391]:


data.groupby('director').Profit.sum().sort_values(ascending=False)


# In[392]:


answer.append('5')


# # Вопрос 16
# ## Какой актер принес больше всего прибыли?
# 1. Emma Watson 
# 2. Johnny Depp 
# 3. Michelle Rodriguez 
# 4. Orlando Bloom 
# 5. Rupert Grint 

# In[393]:


list_acter=pd.DataFrame(data.cast.str.split('|').tolist()).stack().unique()
dict_acter = dict.fromkeys(list_acter, 0)
for key, val in dict_acter.items():
    df = data[data['cast'].str.contains(key) ]
    dict_acter[key] += df['Profit'].sum()
acter_tbl=pd.DataFrame.from_dict(dict_acter.items())
acter_tbl.columns=['Actor','Profit']
acter_tbl.loc[acter_tbl.Profit==acter_tbl.Profit.max()]


# In[394]:


answer.append('1')


# # Вопрос 17
# ## Какой актер принес меньше всего прибыли в 2012 году?
# 1. Nicolas Cage 
# 2. Danny Huston 
# 3. Kirsten Dunst 
# 4. Jim Sturgess 
# 5. Sami Gayle 

# In[395]:


df_2012=data[data.release_year==2012]
dict_acter = dict.fromkeys(list_acter, 0)
for key, val in dict_acter.items():
    df=df_2012[df_2012['cast'].str.contains(key)]
    dict_acter[key]+=df['Profit'].sum()
acter_tbl=pd.DataFrame.from_dict(dict_acter.items())
acter_tbl.columns=['Actor','Profit']
acter_tbl.loc[acter_tbl.Profit==acter_tbl.Profit.min()]


# In[396]:


answer.append('3')


# # Вопрос 18 
# ## Какой актер снялся в большем количестве высокобюджетных фильмов? Примечание: в фильмах, где бюджет выше среднего по данной выборке.
# 1. Tom Cruise 
# 2. Mark Wahlberg 
# 3. Matt Damon 
# 4. Angelina Jolie 
# 5. Adam Sandler 

# In[397]:


list_acter=pd.DataFrame(data[data.budget>data.budget.mean()].cast.str.split('|').tolist()).stack()
cl.Counter(list_acter).most_common()


# In[398]:


answer.append('3')


# # Вопрос 19 
# ## В фильмах какого жанра больше всего снимался Nicolas Cage?
# 1. Drama 
# 2. Action 
# 3. Thriller 
# 4. Adventure 
# 5. Crime 
# 

# In[399]:


Cage=pd.DataFrame(data[data.cast.str.contains('Nicolas Cage')].genres.str.split('|').tolist()).stack()
cl.Counter(Cage).most_common()


# In[400]:


answer.append('2')


# # Вопрос 20
# ## Какая студия сняла больше всего фильмов?
# 1. Universal Pictures (Universal) 
# 2. Paramount Pictures 
# 3. Columbia Pictures 
# 4. Warner Bros 
# 5. Twentieth Century Fox Film Corporation 

# In[401]:


studios=pd.DataFrame(data.production_companies.str.split('|').tolist()).stack()
cl.Counter(studios).most_common()


# In[402]:


answer.append('1')


# # Вопрос 21 
# ## Какая студия сняла больше всего фильмов в 2015 году?
# 1. Universal Pictures 
# 2. Paramount Pictures 
# 3. Columbia Pictures 
# 4. Warner Bros 
# 5. Twentieth Century Fox Film Corporation 

# In[403]:


List=pd.DataFrame(data[data.release_year==2015].production_companies.str.split('|').tolist()).stack()
cl.Counter(List).most_common()


# In[404]:


answer.append('4')


# # Вопрос 22  
# ## Какая студия заработала больше всего денег в жанре комедий за все время?
# 1. Warner Bros 
# 2. Universal Pictures (Universal) 
# 3. Columbia Pictures 
# 4. Paramount Pictures 
# 5. Walt Disney 

# In[405]:


std=pd.DataFrame(data.production_companies.str.split('|').tolist()).stack().unique()
dict_studio = dict.fromkeys(std, 0)
df_comedy=data[data.genres=="Comedy"]
for key, val in dict_studio.items():
    df = df_comedy[df_comedy['production_companies'].str.contains(key)]
    dict_studio[key] += df['Profit'].sum()
std_tbl=pd.DataFrame.from_dict(dict_studio.items())
std_tbl.columns=['Studio','Profit']
std_tbl.loc[std_tbl.Profit==std_tbl.Profit.max()]


# In[406]:


answer.append('3')


# # Вопрос 23 
# ## Какая студия заработала больше всего денег в 2012 году?
# 1. Universal Pictures (Universal) 
# 2. Warner Bros 
# 3. Columbia Pictures 
# 4. Paramount Pictures 
# 5. Lucasfilm 

# In[407]:


dict_studio = dict.fromkeys(std, 0)
df=data[data.release_year==2012]
for key, val in dict_studio.items():
    df1 = df[df['production_companies'].str.contains(key)]
    dict_studio[key] += df1['Profit'].sum()
for key,val in dict_studio.items():
    if val==max(dict_studio.values()):
        print(key)


# In[408]:


answer.append('3')


# # Вопрос 24 
# ## Самый убыточный фильм от Paramount Pictures?
# 1. K-19: The Widowmaker tt0267626 
# 2. Next tt0435705 
# 3. Twisted tt0315297 
# 4. The Love Guru tt0811138 
# 5. The Fighter tt0964517 

# In[409]:


data.loc[data.Profit==data[data.production_companies.str.contains('Paramount Pictures')].Profit.min()]


# In[410]:


answer.append('1')


# # Вопрос 25 
# ## Какой самый прибыльный год (в какой год студии заработали больше всего)?
# 1. 2014 
# 2. 2008 
# 3. 2012 
# 4. 2002 
# 5. 2015 

# In[411]:


data.groupby('release_year').Profit.sum().sort_values(ascending=False)


# In[412]:


answer.append('5')


# # Вопрос 26 
# ## Какой самый прибыльный год для студии Warner Bros?
# 1. 2014 
# 2. 2008 
# 3. 2012 
# 4. 2010 
# 5. 2015 

# In[413]:


data_Warner=data[data.production_companies.str.contains('Warner Bros')]
data_Warner.groupby('release_year').Profit.sum().sort_values(ascending=False)


# In[414]:


answer.append('1')


# # Вопрос 27 
# ## В каком месяце за все годы суммарно вышло больше всего фильмов?
# 1. Январь 
# 2. Июнь 
# 3. Декабрь 
# 4. Сентябрь 
# 5. Май 

# In[415]:


data['release_month']=data.release_date.apply(lambda x:x.month)
month=pd.DataFrame(data.release_month.tolist()).stack()
cl.Counter(month).most_common()


# In[416]:


answer.append('4')


# # Вопрос 28 
# ## Сколько суммарно вышло фильмов летом (за июнь, июль, август)?
# 1. 345 
# 2. 450 
# 3. 478 
# 4. 523 
# 5. 381 

# In[417]:


month_sum=pd.DataFrame(data[(data.release_month==6)|(data.release_month==7)|(data.release_month==8)].release_month.tolist()).stack()
len(month_sum)


# In[418]:


answer.append('2')


# # Вопрос 29 
# ## Какой режиссер выпускает (суммарно по годам) больше всего фильмов зимой?
# 1. Steven Soderbergh 
# 2. Christopher Nolan 
# 3. Clint Eastwood 
# 4. Ridley Scott 
# 5. Peter Jackson 

# In[419]:


winter_films=data[(data.release_month==12)|(data.release_month==1)|(data.release_month==2)]
directors=pd.DataFrame(winter_films.director.str.split('|').tolist()).stack()
cl.Counter(directors).most_common()


# In[420]:


answer.append('5')


# # Вопрос 30 
# ## Какой месяц чаще всего самый прибыльный в году?
# Почему нужно считать по годам, а не просто взять самый прибыльный месяц за весь период? Киноиндустрия активно развивается, прибыль компаний растет с каждым годом (например, в 2014 г. индустрия заработала в 2 раза больше, чем в 2004). Поэтому прибыльность более поздних месяцев будет значительно перевешивать предыдущие, что может привести к искажению выводов.
# 1. Январь 
# 2. Июнь 
# 3. Декабрь 
# 4. Сентябрь 
# 5. Май 

# In[421]:


month_profit=data.pivot_table(values=['Profit'],index=['release_year'],columns=['release_month'],aggfunc='sum')
list_month=[]
for year in range(len(month_profit.index)):
    for month in range(len(month_profit.columns)):
        if month_profit.iloc[year][month]==max(month_profit.iloc[year]):
            list_month.append(month+1)
cl.Counter(list_month)


# In[422]:


answer.append('2')


# # Вопрос 31 
# ## Названия фильмов какой студии в среднем самые длинные по количеству символов?
# 1. Universal Pictures (Universal) 
# 2. Warner Bros 
# 3. Jim Henson Company, The 
# 4. Paramount Pictures 
# 5. Four By Two Productions

# In[423]:


data['len_title']=data.original_title.apply(lambda x:len(x))
compain=pd.DataFrame(data.production_companies.str.split('|').tolist()).stack().unique()
sim=dict.fromkeys(compain,0)
for key,val in sim.items():
    dat = data[data['production_companies'].str.contains(key)]
    sim[key]=dat['len_title'].mean()
for key,val in sim.items():
    if val==max(sim.values()):
        print(key)
sim['Four By Two Productions']


# In[424]:


answer.append('5')


# # Вопрос 32 
# ## Названия фильмов какой студии в среднем самые длинные по количеству слов?
# 1. Universal Pictures (Universal) 
# 2. Warner Bros 
# 3. Jim Henson Company, The 
# 4. Paramount Pictures 
# 5. Four By Two Productions 

# In[425]:


data['count_words']=data.original_title.apply(lambda x:len(x.split()))
compain=pd.DataFrame(data.production_companies.str.split('|').tolist()).stack().unique()
diCT=dict.fromkeys(compain,0)
for key,val in diCT.items():
    dt = data[data['production_companies'].str.contains(key)]
    diCT[key]+=dt['count_words'].mean()
for key,val in diCT.items():
    if val==max(diCT.values()):
        print(key)
diCT['Four By Two Productions']


# In[426]:


answer.append('5')


# # Вопрос 33 
# ## Сколько разных слов используется в названиях фильмов (без учета регистра)?
# 1. 6540 
# 2. 1002 
# 3. 2461 
# 4. 28304 
# 5. 3432 

# In[427]:


words=pd.DataFrame(data.original_title.str.split().tolist()).stack().unique()
words=map(lambda x:x.lower(),words)
len(pd.unique(pd.Series(words)))


# In[428]:


answer.append('3')


# # Вопрос 34 
# ## Какие фильмы входят в 1 % лучших по рейтингу?
# 1. Inside Out, Gone Girl, 12 Years a Slave 
# 2. BloodRayne, The Adventures of Rocky and Bullwinkle 
# 3. The Lord of the Rings: The Return of the King, Upside Down 
# 4. 300, Lucky Number Slevin 
# 5. Upside Down, 300, Inside Out, The Lord of the Rings: The Return of the King 
# 

# In[429]:



data[(data.vote_average>=np.percentile(data['vote_average'],99))&(data.vote_average<=np.percentile(data['vote_average'],100))].original_title


# In[430]:


answer.append('1')


# # Вопрос 35 
# ## Какие актеры чаще всего снимаются в одном фильме вместе?
# 1. Johnny Depp and Helena Bonham Carter 
# 2. Hugh Jackman and Ian McKellen 
# 3. Vin Diesel and Paul Walker 
# 4. Adam Sandler and Kevin James 
# 5. Daniel Radcliffe and Rupert Grint 

# In[431]:


cl.Counter(np.sum([list(it.combinations(x, 2)) for x in data.cast.str.split('|')])).most_common(1)


# In[432]:


answer.append('5')


# # Вопрос 36 
# ## У какого из режиссеров самый высокий процент фильмов со сборами выше бюджета?
# 1. Quentin Tarantino 
# 2. Steven Soderbergh 
# 3. Robert Rodriguez 
# 4. Christopher Nolan 
# 5. Clint Eastwood 

# In[433]:


films=data[data.revenue>data.budget]
directors=['Quentin Tarantino','Steven Soderbergh','Robert Rodriguez','Christopher Nolan','Clint Eastwood']
dict_dir=dict.fromkeys(directors,0)
for key,vol in dict_dir.items():
    dict_dir[key]+=films[films.director.str.contains(key)].Profit.sum()
dir_tbl=pd.DataFrame.from_dict(dict_dir.items())
dir_tbl.columns=['Director','profit_films']
display(dir_tbl)
dir_tbl[(dir_tbl.profit_films>=np.percentile(dir_tbl['profit_films'],99))&(dir_tbl.profit_films<=np.percentile(dir_tbl['profit_films'],100))].Director.sort_values(ascending=False)


# In[434]:


answer.append('4')


# In[435]:


len(answer)


# In[436]:


pd.DataFrame({'Id':range(1,len(answer)+1), 'Answer':answer}, columns=['Id', 'Answer'])


# In[ ]:




