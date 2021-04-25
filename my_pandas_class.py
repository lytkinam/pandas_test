import pandas as pd

class my_pandas():
 
    def my_info():
        # Как называется приложение, расположенное первым в наборе данных?
        print(df.head())
        
        # К какой категории (Category) относится приложение, расположенное последним в наборе данных?
        print(df.tail())
        
        # Сколько столбцов содержится в наборе данных?
        # Данные какого типа хранятся в каждом из столбцов?
        print(df.info())
        
        # Укажи среднее арифметическое и медиану размера приложений (Size)
        # Сколько стоит самое дорогое приложение?
        # *Укажи среднее арифметическое и медиану количества установок приложений (Installs)
        print(df.describe())

    def my_filter():
        # Сколько стоит (Price) самое дешёвое платное приложение (Type == 'Paid)?
        print(df[df['Type'] == 'Paid']['Price'].min())
        
        # Чему равно медианное (median) количество установок (Installs)
        # приложений из категории (Category) "ART_AND_DESIGN"?
        print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())
        
        # На сколько максимальное количество отзывов (Reviews) для бесплатных приложений (Type == 'Free')
        # больше максимального количества отзывов для платных приложений (Type == 'Paid')?
        free = df[df['Type'] == 'Free']['Reviews'].max()
        paid = df[df['Type'] == 'Paid']['Reviews'].max()
        print(free - paid)
        
        # Каков минимальный размер (Size) приложения для тинейджеров (Content Rating == 'Teen')?
        print(df[df['Content Rating'] == 'Teen']['Size'].min())
        
        # *К какой категории (Category) относится приложение с самым большим количеством отзывов (Reviews)?
        print(df[df['Reviews'] == df['Reviews'].max()]['Category'])
        
        # *Каков средний (mean) рейтинг (Rating) приложений стоимостью (Price) более 20 долларов и 
        # с количеством установок (Installs) более 10000?
        print(df[(df['Price'] > 20) & (df['Installs'] > 10000)]['Rating'].mean())

    def my_value_counts():
        # 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
        print(df['Category'].value_counts())
    
    def my_value_counts_2():
        # 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
        # Ответ запиши с точностью до сотых.
        temp = df['Content Rating'].value_counts()
        print('Соотношение:', round(temp['Teen'] / temp['Everyone 10+'], 2))
 
    def my_groupby():
        # 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений?
        # Ответ запиши с точностью до сотых.
        temp = df.groupby(by = 'Type')['Rating'].mean()
        print(temp['Paid'])
        # 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
        # Ответ запиши с точностью до сотых.
        print(round(temp['Paid'] - temp['Free'], 2))
 
    def my_groupby_agg():
        # 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
        # Запиши ответы с точностью до сотых.
        print(df.groupby(by = 'Category')['Size'].agg(['min', 'max']))

    def my_groupby_agg_2():
        # 1 Выведи на экран минимальный, средний и максимальный рейтинг ('Rating') платных и бесплатных приложений ('Type') с точностью до десятых.
        print(round(df.groupby(by = 'Type')['Rating'].agg(['min', 'mean', 'max']), 1))
 
    def my_groupby_agg_3():
        # 2 Выведи на экран минимальную, медианную (median) и максимальную цену ('Price') платных приложений (Type == 'Paid') для
        # разных целевых аудиторий ('Content Rating')
        print(df[df['Type'] == 'Paid'].groupby(by = 'Content Rating')['Price'].agg(['min', 'median', 'max']))
 
    def my_pivot_table():
        # 3 Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом
        # посчитай максимальное количество отзывов ('Reviews') в каждой группе.
        # Сравни результаты для категорий 'EDUCATION', 'FAMILY' и 'GAME':
        # В какой возрастной группе больше всего отзывов получило приложение из категории 'EDUCATION'? 'FAMILY'? 'GAME'?
        
        # Подсказка: ты можешь выбрать из DataFrame несколько столбцов одновременно с помощью такого синтаксиса:
        # df[[<столбец 1>, <столбец 2>, <столбец 3>]]
        temp = df.pivot_table(index = 'Content Rating', columns = 'Category', values = 'Reviews', aggfunc = 'max')
        print(temp[['EDUCATION', 'FAMILY', 'GAME']])
 
    def my_pivot_table_2():
        # 4 Сгруппируй платные (Type == 'Paid') приложения по категории ('Category') и целевой аудитории ('Content Rating')
        # Посчитай среднее количество отзывов ('Reviews') в каждой группе
        # Обрати внимание, что в некоторых ячейках полученной таблицы отражается не число, а значение "NaN" - Not a Number
        # Эта запись означает, что в данной группе нет ни одного приложения.
        # Выбери названия категорий, в которых есть платные приложения для всех возрастных групп и расположи их в алфавитном порядке.
        print(df[df['Type'] == 'Paid'].pivot_table(columns = 'Content Rating', index = 'Category', values = 'Reviews', aggfunc = 'mean'))
 
    def my_pivot_table_3():
        # Бонусная задача. Найди категории бесплатных (Type == 'Free') приложений,
        # в которых приложения разработаны не для всех возрастных групп ('Content Rating')
        print(df[df['Type'] == 'Free'].pivot_table(index = 'Category', columns = 'Content Rating', values = 'Reviews', aggfunc = 'mean'))


df = pd.read_csv('GoogleApps.csv')
my_pandas.my_info()


