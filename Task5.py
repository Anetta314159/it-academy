'''
Задача 5:
Существует массив поисковых запросов, например:
search_queries = [“watch new movies”, “coffee near me”, “how to find the determinant”, “python”, “data science jobs in UK”, “courses for data science”, “taxi”, “google”, “yandex”, “bing”,”foreign exchange rates USD/BYN”, “Netflix movies watch online free”,  “Statistics courses online from top universities”]

Необходимо реализовать функцию, которая принимает на вход данные массива поисковых запросов
и возвращает распределение поисковых запросов по количеству слов в каждом из запросов в процентах.

Результат должен выглядеть следующим образом:
1 слово : 10%
2 слова:  40%
4 слова:  45%
5 слов:    5%
'''

def words_count(lst):
    temp = [i.split(' ') for i in lst]
    temp = [i for j in temp for i in j]
    n = len(temp)
    [print(f'{temp.count(x)} слов {x}: {temp.count(x)/n:2.2%}') for x in set(temp)]