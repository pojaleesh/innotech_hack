import pandas as pd
import urllib.request
import os
import import_ipynb
import sys
sys.path.append('.')
from Find_profile import find
import torch

df = pd.read_csv('upload_images/Profiles.csv')

print(df)