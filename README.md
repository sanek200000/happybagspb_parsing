План:
    1.  Парсим Анькин сайт (https://happybagspb.ru/), собираем данные (id в базе, ссылка на товар, наименование) продуктов без фото.
    2.  Сохраняем данные в json. (shop.py)  
    3.  Ищем в гул-картинках по наименованию первые 10 картинок с белым фоном с сохраняем в папку .img/uid,
        так же добавляем в каждую папку файл readme.txt с данными о товаре. (google.py)


Виртуальная среда:
    1. Для Linux .venv, команда: source .venv/bin/activate 
    2. Для Windows win_venv, команда: win_venv\Scripts\activate 
    В следующий раз нужно будет установить ВС с параметром --without-pip

pip:
    pip freeze > requirements.txt
    pip install -r requirements.txt