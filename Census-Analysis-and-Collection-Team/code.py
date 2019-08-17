# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path, delimiter=",",skip_header=1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
census=np.concatenate([data, new_record ])
print(census)


# --------------
#Code starts here
age=np.array(census[:,0])
max_age=age.max()
print(max_age)
min_age=age.min()
print(min_age)
age_mean=age.mean()
print(age_mean)
age_std=np.std(age)
print(age_std)


# --------------
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
print(len_0)
len_1=len(race_1)
print(len_1)
len_2=len(race_2)
print(len_2)
len_3=len(race_3)
print(len_3)
len_4=len(race_4)
print(len_4)
p=np.array([len_0,len_1,len_2,len_3,len_4])
minrace= min(len_0,len_1,len_2,len_3,len_4)
minority_race=list(p).index(minrace)
print(minority_race)


# --------------
#Code starts here
senior_citizens=np.array(census[census[:,0]>60])
print(senior_citizens)
working_hours_sum=senior_citizens.sum(axis=0)[6]
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
high_sum=high.sum(axis=0)[7]
high_len=len(high)
low_sum=low.sum(axis=0)[7]
low_len=len(low)
avg_pay_high=high_sum/high_len
avg_pay_low=low_sum/low_len
print("AVG pay High",avg_pay_high)
print("AVG pay Low",avg_pay_low)


