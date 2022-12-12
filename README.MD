Для запуска приложения необходимо выполнить следующие действия:
1. Запускаем "docker-compose up -d --build"
2. Подключаемся к сервису django командой "docker exec -it <номер контейнера> 
   /bin/sh"
3. Вводим команды:
    1. "python manage.py makemigrations"
    2. "python manage.py migrate"
    3. "python manage.py createsuperuser"
4. Переходим по адресу "http://localhost/admin/" и создаем фильмы.
5. Переходим по адресу "http://localhost/api/v1/movies/" и наблюдаем весь 
   список фильмов.
6. Переходим по адресу "http://localhost/api/v1/movies/<uuid:pk>" и получаем 
   детальную информацию о конкретном фильме.

Для просмотра информации через swagger переходим
по адресу "http://localhost:8080/"