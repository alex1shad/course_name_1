import requests
from datetime import datetime


class VkPhoto:
    def __init__(self, token_vk, owner_id, photo_count):
        self.token = token_vk
        self.owner_id = owner_id
        self.photo_count = photo_count

    def photo_read(self):
        photo_read_url = 'https://api.vk.com/method/photos.get'
        photo_read_params = {
            'access_token': self.token,
            'v': '5.131',
            'owner_id': self.owner_id,
            'album_id': 'profile',
            'extended': '1',
            'photo_sizes': '1',
            'count': '1000'
        }
        req = requests.get(url=photo_read_url, params=photo_read_params).json()
        vk_photo_data = []
        for photo in req['response']['items']:
            photo_height = 0
            photo_type = ''
            photo_url = ''
            for size in photo['sizes']:
                if size['height'] > photo_height:
                    photo_height = size['height']
                    photo_type = size['type']
                    photo_url = size['url']
            if photo_height == 0:
                vk_photo_data.append({'date': photo['date'],
                                      'likes': photo['likes']['count'],
                                      'url': photo['sizes'][-1]['url'],
                                      'size': photo['sizes'][-1]['type']
                                      })
            else:
                vk_photo_data.append({'date': photo['date'],
                                      'likes': photo['likes']['count'],
                                      'url': photo_url,
                                      'size': photo_type
                                      })
        return vk_photo_data[:self.photo_count]

    def photo_final(self):
        photo_list = self.photo_read()
        vk_photo_list = []
        likes_list = []
        for el in photo_list:
            likes_list.append(el['likes'])
        for el in photo_list:
            if likes_list.count(el['likes']) > 1:
                date = datetime.utcfromtimestamp(int(el['date'])).strftime('%Y%m%d_%H%M')
                vk_photo_list.append({'file_name': f'{el["likes"]}_{date}.jpg',
                                      'size': el['size']})
            else:
                vk_photo_list.append({'file_name': f'{el["likes"]}.jpg',
                                      'size': el['size']})
        with open('vk_photo.json', 'w') as file:
            file.write(str(vk_photo_list))
        return vk_photo_list
