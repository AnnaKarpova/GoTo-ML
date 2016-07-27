
# coding: utf-8

# In[15]:

import pandas as pd
import numpy as np
import json
from collections import Counter

train_likes_df = pd.DataFrame(pd.read_csv(r'data/train_likes.csv'))
with open(r'data/items.json') as f:
    items_dicts = json.load(f)
    
films_counter=Counter(train_likes_df.item_id)

num_films= len([number for number in films_counter.itervalues() if number>=5])
print num_films

channel_counter=Counter(train_likes_df.channel)
channel_mean_likes=round(np.mean(channel_counter.values()),2)
print channel_mean_likes


# In[ ]:



