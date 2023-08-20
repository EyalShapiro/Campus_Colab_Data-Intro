# -*- coding: utf-8 -*-
"""Chapter2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BwLd-w1pyulJD8bCV3qqt7g9jIBcpaO0

#<div dir="rtl" align=center>2.2 - pandas hands-on צעדים ראשונים</div>
"""

import pandas as pd # video 2.2 t=0:31

"""טעינת קובץ נתונים"""

url = 'https://s3.eu-west-1.amazonaws.com/data.cyber.org.il/virtual_courses/introdata/colab/artists.csv'

artists = pd.read_csv(url) # t=1:19

artists.head() # t=1:43

artists.dtypes # t=4:32

"""#<div dir="rtl" align=center>2.3 - pandas Series</div>"""

series_of_numbers = pd.Series([9, 0, 2, 1, 0]) # t=0:45
series_of_strings = pd.Series(['this', 'is', 'a', 'Pandas', 'Series'])

print(series_of_strings) # t=1:04

sorted_series = series_of_strings.sort_values() # t=2:20

sorted_series # t=2:27

series_of_strings.loc[0] # t=3:52

print(series_of_strings) # t=4:01

sorted_series.loc[0] # t=4:11

sorted_series # t=4:11

series_of_strings.iloc[0] # t=4:32

sorted_series.iloc[0] # t=4:40

words = ['The','quick','brown','fox','jumps','over','the','lazy','dogs'] # t=5:10
words[2:6]

series_of_strings.iloc[0:3] # t=5:25

series_of_strings = pd.Series(['this', 'is', 'a', 'Pandas', 'Series']) # appears on screen, but not typed

series_of_strings.index = ['First','Second','Third','Fourth','Fifth'] # t=6:06

series_of_strings # t=6:13

series_of_strings.loc['Second'] # t=6:22

"""#<div dir="rtl" align=center>2.4 - DataFrame - מיון ושליפה בסיסיים + אינדקסים לוגיים - logical indexing - חלק א</div>"""

artists_by_popularity = artists.sort_values('popularity') # t=0:52

artists_by_popularity.head() # t=0:55

artists_by_popularity.tail() # t=1:21

artists_by_popularity = artists.sort_values('popularity', ascending=False) # t=1:39

artists_by_popularity.head() # t=1:40

artists_by_popularity = artists.sort_values(['popularity', 'followers'], ascending=False) # t=2:14

artists_by_popularity.head() # t=2:26

artists_by_popularity.iloc[10,:] # t=3:51

artists_by_popularity.iloc[10:20,:] # t=4:36

artists_by_popularity[['name','popularity','followers']] # t=4:56

artists_by_popularity.loc[:,['name','popularity','followers']] # t=5:43

artists.columns # t=6:25

artists_by_popularity.iloc[:,[3,4,1]] # t=6:31

artists_by_popularity.iloc[10:20,[3,4,1]] # t=6:52

artists_by_popularity[['name','popularity','followers']].iloc[:10,:] # t=7:13

"""#<div dir="rtl" align=center>2.4 - DataFrame - מיון ושליפה בסיסיים + אינדקסים לוגיים - logical indexing - חלק ב</div>

<div dir="rtl" lang="he" xml:lang="he">

השורה הבאה מייצרת משתנה בשם pop_rock_2000

פקודה ה-iloc בוחרת שורות לפי מיקום, כפי שהוסבר ב2.3

רשימת השורות שמופיעה נבחרה מראש כדי ללקט את האומנים משנות ה-2000 שמשתתפים בדוגמה זו

</div>
"""

pop_rock_2000 = artists_by_popularity[['name','popularity','followers']].iloc[[20,58,120,138,160,446,1265,1517],:] # not typed and not seen onscreen

pop_rock_2000

pop_rock_2000['name']=='Black Eyed Peas' # t=1:06

pop_rock_2000.loc[pop_rock_2000['name']=='Black Eyed Peas',:] # t=1:43

artists_by_popularity.loc[artists_by_popularity['name']=='Mashina',:]   # t=2:20

pop_rock_2000.loc[pop_rock_2000['followers'] > 7000000,:] # t=3:19

artists_new_index = artists_by_popularity.reset_index(drop=True) # t=3:52

artists_new_index.head() # t=4:07

artists_new_index.loc[artists_new_index['name']=='Mashina',:] # t=4:13

len(artists) # t=4:52

artists.shape # t=5:02

artists_new_index.loc[artists_new_index['popularity']==46,:] # t=5:36

artists_new_index.loc[
                      (artists_new_index['popularity']==46) &
                      (artists_new_index['followers']==106065)] # t=6:22

artists_new_index.loc[
                      (artists_new_index['popularity']==46) &
                      (artists_new_index['followers']>=105000) &
                      (artists_new_index['followers']<107000),:
                      ] # t=7:10