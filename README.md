Для запуска на MasOS: 

    DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose up

Эндпоинты:
    
127.0.0.1:8000/api/point/

    GET: Список Point
    POST: Добавление Point, одним элементом либо списком
    Фильтры: name=, search= (Поиск по имени)
Входные данные:
```json
{
   "name": "Точка 1",
   "geometry": {
      "type": "Point",
      "coordinates": [
         92.899501,
         58.34302
      ]
   }
}
```
либо
```json
[
  {
    "name": "Точка 1",
    "geometry": {
      "type": "Point",
      "coordinates": [
        92.899501,
        58.34302
      ]
    }
  },
  {
    "name": "Точка 2",
    "geometry": {
      "type": "Point",
      "coordinates": [
        93.899501,
        59.34302
      ]
    }
  },
  ...
]
```
Выходные данные:
```json
{
"type": "FeatureCollection",
"features": [
    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                92.899501,
                58.34302
            ]
        },
        "properties": {
            "id": 144,
            "name": "Точка 111"
        }
    },
    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                92.899501,
                58.34302
            ]
        },
        "properties": {
            "id": 145,
            "name": "Точка 1111"
        }
    }
]
```

127.0.0.1:8000/api/point/<int:pk>
    
    GET: Вывод Point c id = pk
    PUT: Внесение изменений
    DELETE: Удаление
Выходные данные:
```json
{
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [
            58.297538105220404,
            92.80998236626284
        ]
    },
    "properties": {
        "id": 2,
        "name": "point1234"
    }
}
```

127.0.0.1:8000/api/linestring/

    GET: Список LineString
    POST: Добавление LineString, одним элементом
    Фильтры: name=, search= (Поиск по имени)
Входные данные
```json
{
   "name": "Линия 1",
   "geometry": {
      "type": "LineString",
      "coordinates": [
            [
                58.29677131648106,
                92.80946718275756
            ],
            [
                58.297538105220404,
                92.80998236626284
            ],
            [
                58.297267475797696,
                92.81195723636641
            ]
      ]
   }
}
```


127.0.0.1:8000/api/linestring/<int:pk>

    GET: Вывод LineString с id = pk
    PUT: Внесение изменений
    DELETE: Удаление

Выходные данные:
```json
{
    "type": "Feature",
    "geometry": {
        "type": "LineString",
        "coordinates": [
            ...
        ]
    },
    "properties": {
        "id": 1,
        "name": "Линия №2018"
    }
}
```

127.0.0.1:8000/api/polygon/

    GET: Список Polygon
    POST: Добавление Polygon, одним элементом 
    Фильтры: name=, search= (Поиск по имени),
    dist=100&point=50.32959304166469,92.68833918023194 - фильтрация в пределах заданного радиуса указанной 
    географической точки

Входные данные
```json
{
   "name": "Полигон 1",
   "geometry": {
      "type": "Polygon",
      "coordinates": [
            ...
      ]
   }
}
```

127.0.0.1:8000/api/polygon/<int:pk>

    GET: Вывод Polygon с id = pk
    PUT: Внесение изменений
    DELETE: Удаление
Выходные данные:
```json
{
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            ...
        ]
    },
    "properties": {
        "id": 1,
        "name": "Полигон №2018"
    }
}
```

127.0.0.1:8000/api/upload/ - загрузка данных из файла
    
    POST:
    Поля:
    - name - текстовое поле(необязательное)
    - geom_type - текстовое поле, возможные значения: `Polygon`, `LineString`, `MultiPoint`
    - gpx - файл с расширением `.gpx`


