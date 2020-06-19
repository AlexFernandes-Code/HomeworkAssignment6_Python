import pandas as pd
import csv as csv

d = pd.read_csv(f'C:/Users/Alex/Desktop/INF 354/INF354_HomeworkAssignment6/tips.csv', keep_default_na = False)
d.drop_duplicates(subset = ["total_bill", "tip", "sex", "smoker", "day", "time", "size"], inplace = True, keep = 'first')
d.to_csv('tips_duplicates_removed.csv', index = False)
file = open('C:/Users/Alex/Desktop/INF 354/INF354_HomeworkAssignment6/tips.csv')
reader = csv.reader(file)
total= len(list(reader))
file = open('tips_duplicates_removed.csv')
reader = csv.reader(file)
newtotal= len(list(reader))
duplicates = total - newtotal
print(f'tips.csv total records: {total}')
print(f'Duplicates removed: {duplicates}')
print(f'tips_duplicates_removed.csv created with records: {newtotal}')    

    