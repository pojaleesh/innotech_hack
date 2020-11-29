import pandas as pd
import urllib.request
import os
import FaceVerification
import torch

professions = ['Accountent', 'Manager', 'Pojarnie']


def build():
    df = pd.DataFrame()
    for name in professions:
        temp = pd.read_csv(name + '.csv')
        df = pd.concat([df, temp], ignore_index=True)

    return df

def get_picture(url, name_of_picture):
    img = urllib.request.urlopen(url).read()
    out = open(os.path.join(os.getcwd(), name_of_picture+'.jpg'), "wb")
    out.write(img)
    out.close()

def find(df, filename):
    for i in range(0, df.shape[0]):
        print(df['id'][i])
        get_picture(df['photo'][i], 'aplliciant')
        if FaceVerification.isSame('aplliciant.jpg', filename):
            return df['id'][i]
    return 'Nothing'