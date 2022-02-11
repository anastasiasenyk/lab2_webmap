# lab2_webmap

###used libraries:
- argparse, math, folium, pandas (as pd)

###example of map
######$python main.py 2015 49.83826 -0.02324 'locations_coordinate.csv'
![](https://user-images.githubusercontent.com/91616572/153593820-6c95ed7f-70ff-42de-8d8e-9f5a3acde0b9.jpg)


##argparse
![](https://user-images.githubusercontent.com/91616572/153593858-69e6fec1-b6d7-4fc2-b796-b7704d06fe43.jpg)


##functions
1) distance
    ![](https://user-images.githubusercontent.com/91616572/153593620-6343471d-9f7c-447a-91b1-347a7d98fd1f.jpg)
    

    функція рахує відстань між двома парами координат, використовуючи формулу гаверсинусів

2) row_lenght
    ![](https://user-images.githubusercontent.com/91616572/153593900-d6be3f0e-2140-4a52-ab0e-e5dec06b9357.jpg)
    
    функція рахує модуль різниці між координатами довготи
    the function calculates the module of the difference of the longitude coordinates

3) find_10_films
   ![](https://user-images.githubusercontent.com/91616572/153593934-e3fa041d-f89c-4e13-9371-4e754abfdcfc.jpg)

    функція сортує базу даних із фільм, вбираючи фільм із заданим роком випуску та сортує,
використовуючи функцію 1, відносно найменшої відстані щодо заданих координат до місця зйомки

4) top_5_films
    ![](https://user-images.githubusercontent.com/91616572/153594064-38b9dcfb-8f62-4fa3-9ce2-77de97499225.jpg)
    функція, використовуючи базу даних із фільмів сортує їх за найменшою відстанню до місця зйомки,
відносно заданих координат. виводить перших 5 фільмів

5) in_row
    ![](https://user-images.githubusercontent.com/91616572/153594097-00140baa-8ac4-4e7f-bcea-9364f3d90efe.jpg)
    функція, сортує базу даних фільмів, вибираючи з неї тільки ті, які зняті пізніше,
ніж у заданий рік. Окрім цього, використовуючи функцію 2) сортує список, та виводить перші 10 фільмів

6) map_create
    функція створює веб-карту із шарами із різних міток
    основний шар: карта та круг, що позначає задані координати
    другий шар: координати, що відображають функцію in_row
    третій шар: функція top_5_films
    четвертий шар: функція find_10_films
