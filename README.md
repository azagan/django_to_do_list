Приложение для ведения и отслеживания списка дел
![image](https://user-images.githubusercontent.com/49444203/123849096-dc71c300-d931-11eb-8f6d-031c8c781db9.png)
Проксирование настроено через контейнер nginx, подключена postgresql

Для запуска рекомендуется использоваться .env.dev.example, либо переменные окружения, если DATABASE - не выбрана, будет использоваться sqlite3

Для запуска контейнеров ввести команду:
 - docker-compose up -d
 
Могут возникнуть проблемы с entrypoint.sh.

  Решение:
  - Открыть notepad++
  - Нажать поиск > Замена (или Ctrl + H)
  - Поиск: \r\n.
  - Заменить на: \n.
  - Режим поиска: Расширенный.
  - Заменить все.
