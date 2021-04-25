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

    def my_isnull():
        # Выведи информацию о всем DataFrame, чтобы узнать, какие столбцы нуждаются в очистке
        print(df.info())
        
        # Сколько в датасете приложений, у которых не указан ('NaN') рейтинг ('Rating')?
        print(len(df[pd.isnull(df['Rating'])]))
        # Замени пустое значение ('NaN') рейтинга ('Rating') для таких приложений на -1.
        df['Rating'].fillna(-1, inplace = True)
        
    def set_size(size):
        if size[-1] == 'M':
            return float(size[:-1])
        elif size[-1] == 'k':
            return float(size[:-1]) / 1024
        return -1

    def my_apply(size):
        # Определи, какое ещё значение размера ('Size') хранится в датасете помимо Килобайтов и Мегабайтов, замени его на -1.
        # Преобразуй размеры приложений ('Size') в числовой формат (float). Размер всех приложений должен измеряться в Мегабайтах.
        print(df['Size'].value_counts())

        df['Size'] = df['Size'].apply(set_size)

        # Чему равен максимальный размер ('Size') приложений из категории ('Category') 'TOOLS'?
        print(df[df['Category'] == 'TOOLS']['Size'].max())
 
    def set_installs(installs):
        if installs == '0':
            return 0
        return int(installs[:-1].replace(',', ''))

    def my_apply_2():
        # Бонусные задания
        # Замени тип данных на целочисленный (int) для количества установок ('Installs').
        # В записи количества установок ('Installs') знак "+" необходимо игнорировать.
        # Т.е. если в датасете количество установок равно 1,000,000+, то необходимо изменить значение на 1000000
        df['Installs'] = df['Installs'].apply(set_installs)
 
        # Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом,
        # посчитай среднее количество установок ('Installs') в каждой группе. Результат округли до десятых.
        # В полученной таблице найди ячейку с самым большим значением.
        # К какой возрастной группе и типу приложений относятся данные из этой ячейки?
        print(round(df.pivot_table(index = 'Content Rating', columns = 'Type', values = 'Installs', aggfunc = 'mean')), 1)
 
    def my_fillna():
        # У какого приложения не указан тип ('Type')? Какой тип там необходимо записать в зависимости от цены?
        print(df[pd.isnull(df['Type'])])
        # Чтобы увидеть все столбцы вместо многоточия, можно применить iloc[0].
        # print(df[pd.isnull(df['Type'])].iloc[0])
        df['Type'].fillna('Free', inplace = True)
 
    def my_iloc():      
        # Выведи на экран приложение с индексом 10472. Посмотри, какие ошибки допущены в значениях.
        print(df.iloc[10472])
        
        # Исправь ошибки, допущенные в значениях
        columns = list(df.columns)
        index = 10472
        for i in range(len(columns) -1, 1, -1):
            df[columns[i]][index] = df[columns[i - 1]][index]
        
        # Среди значений приложения стоит несколько пустых ('NaN'). Замени эти пустые значения на 'Lifestyle'.
        df['Category'][index] = 'LIFESTYLE'
        df['Genres'][index] = 'Lifestyle'
        
        # Выведи на экран приложение, чтобы убедиться, что очистка прошла успешно
        print(df.iloc[10472])


df = pd.read_csv('GoogleApps.csv')
my_pandas.my_info()


