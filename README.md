# PEP Status Parser

Парсер документации на основе Scrapy, который собирает статусы PEP (Python Enhancement Proposal), подсчитывает общее количество документов в каждой категории и сохраняет результаты в файл.

## Особенности
- Сбор всех ссылок на PEP с официального сайта Python.  
- Анализ статусов PEP для подсчёта их количества по категориям (например, "Accepted", "Rejected", "Final").  
- Сохранение результатов в файл формата CSV с автоматическим именем, включающим текущую дату и время.

---

## Установка и запуск

1. Клонирование репозитория:
  
   git clone <https://github.com/Cubaser/scrapy_parser_pep.git>
   
2. Установка зависимостей:
   Убедитесь, что у вас установлен Python версии 3.9 или выше. Затем установите необходимые библиотеки:
  
   pip install -r requirements.txt
   
3. Запуск парсера:
   Для запуска парсера используйте следующую команду:
  
   scrapy crawl pep
   
4. Результаты:
   После выполнения команды, результаты сохранятся в папку result в файл формата pep_<дата_время>.csv и status_summary_<дата_время>.csv, например:
  
   result/pep_2024-11-24T10-17-25.csv
   result/status_summary_2024-11-24T10-17-25.csv
   
---

## Структура проекта
  
- pep_parser/:
  - spiders/pep.py — основной файл паука, содержащий логику парсинга.  
  - pipelines.py — обработка данных перед сохранением.  
  - settings.py — настройки проекта Scrapy.  
- requirements.txt — список зависимостей проекта.  
- result/ — папка, где сохраняются результаты работы парсера.

---

## Пример данных

Собранный файл pep_<дата_время>.csv будет содержать три столбца:  
1. number — номер документа PEP.  
2. name — название документа PEP.
3. status — статус документа PEP (например, "Accepted").

Пример содержимого файла:  
number,name,status  
585,PEP 585 – Type Hinting Generics In Standard Collections,Final  
337,PEP 337 – Logging Usage in the Standard Library,Deferred  
546,PEP 546 – Backport ssl.MemoryBIO and ssl.SSLObject to Python 2.7,Rejected  

Собранный файл status_summary_<дата_время>.csv будет содержать два столбца:  
1. Статус — статус документа PEP (например, "Accepted").  
2. Количество — количество документов с этим статусом.  

В конце файла указана общее кооличество документов(Total)  

Пример содержимого файла:  
Статус,Количество  
Final,325  
Deferred,35  
Rejected,123  
Active,35  
Superseded,24  
Accepted,18  
Withdrawn,65  
Draft,36  
Provisional,3  
April Fool!,1  
Total,665  

---

## Дополнительная информация

- Источник данных: [PEP Index](https://peps.python.org/)  
- Технологии: Python, Scrapy  
