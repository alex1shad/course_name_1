from class_vk import VkPhoto
from class_yad import YaDisk
import logging


logging.basicConfig(format='[%(levelname)s] / %(asctime)s / %(funcName)s / %(lineno)d / %(message)s',
                    filename="info.log",
                    level=logging.NOTSET
                    )
logging.debug('Debug message')
logging.info('Informational message')
logging.error('Error message')

with open('token_vk.txt', 'rt') as file_vk:
    token_vk = file_vk.read().strip()

def quest(prefix, start_var, type=str):
    prefix = prefix + 'Введите "Да" или "Нет":\n'
    while (True):
        quest = str(input(prefix)).lower().strip()
        if quest == 'нет':
            print()
            return start_var
        elif quest == 'да':
            print()
            finish_var = type(input('Введите свой вариант:\n'))
            print()
            return finish_var
        else:
            print('Ответ введен некорректно. Попробуйте еще раз')
            print()

while(True):
    token_yad = str(input('Введите токен для Я.Диска:\n'))
    test_yad = YaDisk(token_yad=token_yad)
    if test_yad.test_token() == 200:
        print()
        break
    else:
        print('Токен введен некорректно. Попробуйте еще раз')
        print()

folder_name = quest('Хотите изменить название для папки хранения файлов на Я.Диске (по умолчанию "VK photocopy"). ',
                    'VK photocopy')
photo_count = quest('Хотите изменить количество фотографий, записываемых на Я.Диск (по умолчанию 5) ', 5, int)
owner_id = int(input('Введите id пользователя, фотографии профиля которого необходимо сохранить:\n'))
print()


if __name__ == '__main__':
    user_vk = VkPhoto(token_vk=token_vk, owner_id=owner_id, photo_count=photo_count)
    user_vk.photo_final()
    user_yad = YaDisk(token_yad=token_yad,  folder_name=folder_name)
    user_yad.yad_write(vk_photo_list=user_vk.photo_final(), vk_photo_data=user_vk.photo_read())
