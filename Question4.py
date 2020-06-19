import pandas as pd
import scipy
import csv as csv
import seaborn as sns
from matplotlib import pyplot as plt
from pandas import DataFrame as myDataFrame


myDataFrame = pd.read_csv('C:/Users/Alex/Desktop/INF 354/INF354_HomeworkAssignment6/tips.csv')

print ("Original shape:")
print (myDataFrame.shape)

myDataFrame['total_due'] = myDataFrame["total_bill"] + myDataFrame["tip"]

print ("After addition of calculated column:")
print (myDataFrame.shape)

print ("Only dinner meals:")
print (myDataFrame[myDataFrame.time == "Dinner"].shape)

a = round(myDataFrame['size'].corr(myDataFrame['tip']), 3)

if a < 0.8 and a > -0.8:
    print ("Insignificant correlation between meal size and tips: "+str(a))
else:
    print ("Significant correlation between meal size and tips: "+str(a))

sns.lineplot(x="day", y="total_bill",color = 'b', data=myDataFrame)
plt.show()