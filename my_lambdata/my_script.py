# my_lambdata/my_script.py
import pandas
from my_mod import enlarge

print('Hello World')

df = pandas.DataFrame({'State': ['CT', 'ca', 'cb']})
print(df.head())

print('--------------')

x = 5
print("Number:", x)
print('Number enlarged', enlarge(x)) # invoke the function