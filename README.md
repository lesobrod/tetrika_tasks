# tetrika_tasks
## Задача №1.
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то количество подряд идущих нулей:  
`111111111111111111111111100000000`  
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)  
```
def task(array):
    pass

print(task("111111111110000000000000000"))
>> OUT: 10
```
### *Комментарии к решению*
В условии есть противоречие. В начале речь идет о массиве, но в примере кода использована строка.
Поэтому в решении сделана обработка трех возможных типов данных: массив, строка и кортеж.
Другой тип вызовет ошибку.
Сделана валидация на вид данных. `10` подойдет, а `01` нет.
Сам алгоритм поиска реализован 4 возможными способами, проведено сравнение на их эффективность по времени выполнения.

## Задача №2.
В функцию передаются координаты двух противоположных вершин одного прямоугольника и двух противоположных вершин второго прямоугольника. 
Найти, пересекаются ли эти прямоугольники?
Немного посложнее – найти площадь пересечения
```
def task(x1,y1,x2,y2,x3,y3,x4,y4):
    `pass`  

print(task(1,1,2,2,3,3,4,4))
>> OUT: False
```
### *Комментарии к решению*

## Задача №3.

В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), мы генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного, имени животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:
- А: 642
- Б: 412
- В:....

### *Комментарии к решению*

## Задача №4.
Мы сохраняем время присутствия каждого пользователя на уроке в виде интервалов. В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах):

lesson – начало и конец урока
pupil – интервалы присутствия ученика
tutor – интервалы присутствия учителя
Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия ученика и учителя на уроке (в секундах).
```
def appearance(intervals):
    pass
```
### *Комментарии к решению*
Данные хранятся в файле tests.json
  
