import pandas as pd
import urllib.request
import os
import import_ipynb
import sys
import os
from Find_profile import find
import torch
from ParserEgrul.run import get_data


df = pd.read_csv('Profiles.csv')
filename = 'images_uploaded/img_temp.jpg'

ans = find(df, filename)

if ans:
    print(ans)
    import sys
    sys.path.append('../vk_alg')
    from script import get_profession
    profession, city, salary, first_name, second_name = get_profession(ans)
    print(profession, city, salary, first_name, second_name)
    MAPA = get_data(first_name + ' ' + second_name)
else:
    print('nothing')
