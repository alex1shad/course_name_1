import requests
import time


class YaDisk:
    def __init__(self, token_yad, folder_name='test'):
        self.token_yad = token_yad
        self.url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': f'OAuth {token_yad}'
                        }
        self.folder_name = folder_name

    def test_token(self):
        url_test = 'https://cloud-api.yandex.net/v1/disk'
        resp = requests.get(url=url_test, headers=self.headers).status_code
        return resp

    def _yad_new_folder(self):
        url_new_folder = f'{self.url_ya}?path={self.folder_name}'
        requests.put(url=url_new_folder, headers=self.headers)

    def _bar(self, prefix, data):
        symbol_bar = '█'
        step_bar = 100 / len(data)
        for i, el in enumerate(data):
            print(end='\r')
            print(f'{prefix}: {symbol_bar * (i + 1)} {round(step_bar * (i + 1), 2)} ', end='')
            time.sleep(0.5)

    def yad_write(self, vk_photo_list, vk_photo_data):
        self._yad_new_folder()
        yad_path = self.folder_name
        url_write = self.url_ya + '/upload'
        for i, el in enumerate(vk_photo_list):
            params = {'path': f'{yad_path}/{el["file_name"]}',
                      'overwrite': 'True'
                      }
            print(f'Загружается {i + 1}/{len(vk_photo_list)}:')
            print('Обработка файла VK...', end='')
            resp_read = requests.get(url=url_write, headers=self.headers, params=params).json()
            print(end='\r')
            self._bar('Чтение файла из VK', resp_read)
            print(end='\r')
            print('Чтение файла из VK завершено')
            href = resp_read['href']
            image_file = requests.get(vk_photo_data[i]['url']).content
            print('Загрузка файла на Яндекс.Диск...', end='')
            resp_write = requests.put(url=href, data=image_file)
            print(end='\r')
            if resp_write.status_code == 409:
                print(f'Файл {el["file_name"]}.jpg не загружен, файл не найден\n')
            elif resp_write.status_code == 201:
                print(f'Файл {el["file_name"]}.jpg загружен на Яндекс.Диск\n')
        print('Файлы загружены на Яндекс.Диск')
