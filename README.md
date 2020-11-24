#Установка

Склонируйте с GitHub проект 

git clone https://github.com/Jostic-git/shop.git

создайте виртуальную среду (virtualenv)

Установите зависимости командой 

pip install -t requirements.txt

Для работы проекта требуется локально установленная MongoDB (https://docs.mongodb.com/manual/installation/)

#Запуск сервера FastAPI 

uvicorn main:app --reload

Сервер будет запущен на 127.0.0.1:8000
# Документация
 будет сгенерирована сервером и доступна здесь
 
http://127.0.0.1:8000/docs
 
http://127.0.0.1:8000/redoc

# Использование

Создание товара

curl -X POST "http://127.0.0.1:8000/item" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"title\":\"Nokia 3310\",\"description\":\"cellphone Nokia\",\"parameters\":[{\"model\":\"3310\"},{\"batery\":\"800\"}]}"

parameters - свободные параметры (ключ/значение). Может быть создано неограниченное количество

Получение товара по ID

curl -X GET "http://127.0.0.1:8000/item/5fbc06cb11bcf5cbbd8b6c3d" -H  "accept: application/json"

Получение товаров по определенным параметрам
 
curl -X GET "http://127.0.0.1:8000/items/?title=Nokia&description=cellphone&model=3310" -H  "accept: application/json"

В запросе может использован один или несколько параметров.

title, description - название, описание товара являются зарезервированными и всегда присусттвуют у товара. Остальные пользовательские.