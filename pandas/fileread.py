import pandas as pd

result=pd.read_csv(r'C:\Users\aish\Desktop\Learning Python\pandas\pizza_sales.csv',
encoding='utf-8')
print(result)
print(result.to_string())