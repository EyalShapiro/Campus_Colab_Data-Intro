import pandas as pd
info = pd.read_csv(
    'https://s3.eu-west-1.amazonaws.com/data.cyber.org.il/virtual_courses/introdata/colab/artists.csv')
info.head()
print(info)