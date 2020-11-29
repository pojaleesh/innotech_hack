import pandas as pd
import urllib.request
import os
import import_ipynb
import sys
import os
from Find_profile import find
import torch


df = pd.read_csv('Profiles.csv')
filename = 'upload_images/images_uploaded/img_temp'

print(df)