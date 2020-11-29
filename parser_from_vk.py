import requests

token = 'dda4eeaddda4eeaddda4eeadaaddd61e23ddda4dda4eead82a032200963ecfbb7fcf175'

# Парсинг общей информации
def _information_about_user(user_link):
    global token
    fields = 'city,about,bdate,education,interests,career,universities,schools,occupation'
    response = requests.get(f'https://api.vk.com/method/users.get?lang=0&access_token={token}&user_ids={user_link}&v=5.120&fields={fields}')
    return response.json()['response'][0]


# Парсинг друзей
def _ids_of_users_friends(user_id):
    global token
    response = requests.get(f'https://api.vk.com/method/friends.get?lang=0&access_token={token}&user_id={user_id}&v=5.120&return_system=0&order=name')
    return response.json()['response']['items']


# Парсинг групп
def _information_about_users_groups(user_id):
    global token
    response = requests.get(f'https://api.vk.com/method/users.getSubscriptions?lang=0&access_token={token}&user_id={user_id}&v=5.120&extended=1')
    return response.json()['response']['items']


def is_close(user_id):
    information_about_user = _information_about_user(user_id)
    return information_about_user.get('deactivated') is not None or information_about_user['is_closed']


def pars_from_vk(user_id):
    information_about_user = {}

    # Тут мы получаем общую информацию и смотрим закрыт ли профиль
    information_about_user = _information_about_user(user_id)
    _user_id = information_about_user['id']
    # ids_of_users_friends = _ids_of_users_friends(_user_id)
    information_about_users_groups = _information_about_users_groups(_user_id)
    temp = []
    for element in information_about_users_groups:
        if element['type'] == 'profile':
            temp.append(element['first_name'] + ' ' + element['last_name'])
        else:
            temp.append(element['name'])
    information_about_users_groups = temp
    return (information_about_user, information_about_users_groups)

def get_info(user_id):
    global token
    fields = 'photo_max'
    response = requests.get(f'https://api.vk.com/method/users.get?lang=0&access_token={token}&user_ids={user_id}&v=5.120&fields={fields}')
    return response.json()['response'][0]

def main():
    user = 'nomapunkkk'
    if is_close(user):
        print('----')
    else:
        a, c = pars_from_vk(user)
        print(a)
        print(c)


if __name__ == '__main__':
    main()    
