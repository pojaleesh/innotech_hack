from parser_from_vk import is_close, get_info
import pandas as pd

with open('links', 'r') as f:
    tmp = f.readlines()
    links = []
    for e in tmp:
        links += e.split()
    for i in range(len(links)):
        links[i] = links[i].split('/')[-1]
    df = pd.DataFrame(columns=['id', 'photo'])
    for new_id in links:
        new_photo = get_info(new_id)['photo_max']
        df = df.append({'id' : ' '.join(new_id.split()), 'photo' : ' '.join(new_photo.split())}, ignore_index=True)
    df.to_csv('Profiles.csv')