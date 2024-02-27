# Установка и запуск проекта

1. Склонируйте репозиторий: git clone "https://github.com/dezween/graphql_api.git"

2. 2. Установите Docker, если у вас его нет. Вы можете загрузить его [отсюда](https://www.docker.com/get-started).

3. Перейдите в директорию с проектом: cd <название_директории>

4. Соберите и запустите контейнеры Docker: docker-compose up --build

5. Откройте ваш браузер и перейдите по адресу http://localhost:8000/graphql для доступа к приложению.




Документация по использованию API
Добро пожаловать в документацию по использованию API для получения информации о персонажах из мира Гарри Поттера.

1. Описание API
Это API предоставляет доступ к информации о персонажах книги Гарри Поттера, включая их имя, факультет, описание, палочку, боггарт и патронус.

2. Эндпоинт
API доступен по следующему эндпоинту:


POST /graphql
3. Формат запросов
Запросы к API отправляются методом POST и имеют тело запроса в формате GraphQL. Ниже приведен пример базового запроса:

query {
  character(faculty: "Slytherin") {
    name
    faculty
    description
    wand
    boggart
    patronus
  }
}


4. Параметры запросов:
    name
    faculty
    description
    wand
    boggart
    patronus

   
6. Формат ответа
Ответы возвращаются в формате JSON и содержат запрошенные данные. Пример ответа:


{
    "character": [
        {
            "boggart": "Neville Longbottom telling him he is his greatest fear",
            "description": "The Potions Master at Hogwarts and a complex character.",
            "faculty": "Slytherin",
            "name": "Severus Snape",
            "patronus": "Doe",
            "wand": "Aspen, 10¼', with a unicorn hair core"
        },
        {
            "boggart": "Voldemort",
            "description": "A rival of Harry and member of the wealthy Malfoy family.",
            "faculty": "Slytherin",
            "name": "Draco Malfoy",
            "patronus": "None",
            "wand": "Hawthorn, 10', with a unicorn hair core"
        },
        {
            "boggart": "His own corpse",
            "description": "The main antagonist of the series, later known as Lord Voldemort.",
            "faculty": "Slytherin",
            "name": "Tom Riddle",
            "patronus": "None",
            "wand": "Yew, 13½', with a phoenix feather core"
        }
    ]
}
