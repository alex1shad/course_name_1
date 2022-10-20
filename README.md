## Приложение для резервного копирования фотографий профиля в VK (далее - приложение)
___
### **1. Подготовка к работе с приложением** 
* Перед началом работы с приложением необходимо получить токен для [**Я.Диска**](https://yandex.ru/dev/disk/poligon/), на который будут загружены фотографии  
* Кроме того, для корректной работы приложения следует установить необходимые библиотеки из файла [**"requiremеnts.txt"**](/requirements.txt)  

### **2. Работа с приложением**
* Для работы с приложением необходимо запустить файл [**"main.py"**](main.py). После запуска в консоли следует указать запрашиваемые параметры для приложения:
  - токен для Я.Диска  
  - название папки для хранения фотографий на Я.Диске (по умолчанию - "*VK photocopy*"  
  - количество фотографий, которые будут загружены на Я.Диск (по умолчанию - 5, максимальное количество - 1000)  
* Процесс работы приложения будет отображен в консоли в виде прогресс-бара. Также основные шаги выполнения приложения будут записаны в виде лога в файл "***info.log***"  

### **3. Выходные данные**
* Json-файл с информацией о фотографиях  
* Измененный Я.диск  