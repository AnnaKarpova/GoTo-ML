
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import json
from tqdm import tqdm
from collections import Counter, defaultdict
import pickle


# In[ ]:

train_likes_df = pd.DataFrame(pd.read_csv(r'data/train_likes.csv'))
with open(r'data/items.json') as f:
    items_dicts = json.load(f)


# In[ ]:

#список фильмов с определенным жанром
films_with_description=[]
for i in tqdm(xrange(len(items_dicts))):
    films_with_description.append(items_dicts[i]['id'])


# In[ ]:

#список всех фильмов, если жанр не определен - в поле значение = 10
list_of_item_genres=defaultdict(int)
for item in tqdm(train_likes_df.item_id.unique()):
    if item not in films_with_description:
        list_of_item_genres[item]=10
    else:
        for item_dict in items_dicts:
            if item_dict['id'] == item:
                list_of_item_genres[item]=item_dict['genre']


# In[ ]:

#популярность жанров на основе количетсва лайков фильмов
films_counter=Counter(train_likes_df.item_id)
genre_counter = defaultdict(int)
for value, count in tqdm(films_counter.iteritems()):
    genre_counter[list_of_item_genres[value]]+=count


# In[ ]:

#ноль, если фильмы этого жанра не получили лайков
for i in range(11):
    if not genre_counter[i]:
        genre_counter[i]=0


# In[ ]:

#вывод результата по первой части задания
for genre, counter in genre_counter.iteritems():
    if genre==10: print '{} - {}'.format('not identified', counter)
    else: print '{} - {}'.format(genre, counter)


# In[ ]:

#вторая часть - самые популярные каналы
most_common_channels=[]
for channel in channel_counter.most_common(10):
    most_common_channels.append(channel[0])


# In[ ]:

#создаем болванку словаря для подсчетов 
channel_genre_counter=defaultdict()
for channel in most_common_channels:
    channel_genre_counter[channel]=defaultdict(int)


# In[ ]:

#считаем лайки по каналам и жанрам
for i in tqdm(xrange(len(train_likes_df))):                                                          
    if train_likes_df.channel[i] in most_common_channels:
        channel_genre_counter[train_likes_df.channel[i]][list_of_item_genres[train_likes_df.item_id[i]]]+=1


# In[ ]:

#если поле не присутствует, ставим ноль
for channel in most_common_channels:
    for i in range(11):
        if not channel_genre_counter[channel][i]:
            channel_genre_counter[channel][i]=0


# In[ ]:

#печатаем результат
for channel in most_common_channels:
    print 'Channel # {}:'.format(channel)
    for genre, counter in channel_genre_counter[channel].iteritems():
        if genre==10: print '{} - {}'.format('not identified', counter)
        else: print '{} - {}'.format(genre, counter)

