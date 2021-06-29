import pandas as pd
import plotly.figure_factory as ff
import statistics as stat
import plotly.graph_objects as go

def_read = pd.read_csv('StudentsPerformance.csv')

score = def_read['math score']

mean = stat.mean(score.tolist())
median =  stat.median(score.tolist())
Stan_dev = stat.stdev(score.tolist())
mode = stat.mode(score.tolist())

print("mean : " , mean)
print("median : " , median)
print("mode : " , mode)
print("Standard Deviation : ", Stan_dev)

# #68% of all data lie within one standard deviation of the mean
sd1_start, sd1_end= mean-Stan_dev , mean+Stan_dev

# 95% of all the data lie within two standard deviation of the mean
sd2_start, sd2_end= mean-(2*Stan_dev) , mean+(2*Stan_dev)

# 99% of all the data lie within three standard deviation of the mean
sd3_start, sd3_end= mean-(3*Stan_dev) , mean+(3*Stan_dev)

list_dataWithin_sd1 = []

for i in score.tolist():
    if(i> sd1_start and i< sd1_end):
        list_dataWithin_sd1.append(i)

percent1 = len(list_dataWithin_sd1)*100/len(score.tolist())
print(percent1)

list_dataWithin_sd2 = []

for i in score.tolist():
    if(i> sd2_start and i< sd2_end):
        list_dataWithin_sd2.append(i)

percent2 = len(list_dataWithin_sd2)*100/len(score.tolist())
print(percent2)


list_dataWithin_sd3 = []

for i in score.tolist():
    if(i> sd3_start and i< sd3_end):
        list_dataWithin_sd3.append(i)

percent3 = len(list_dataWithin_sd3)*100/len(score.tolist())
print(percent3)


          

