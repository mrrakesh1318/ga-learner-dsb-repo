# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Loading data into array from text file
data = np.genfromtxt(path, delimiter=",",skip_header =1)
print("\nData: \n\n",data)
print("Type of data ",type(data))

census = np.concatenate((data,np.asarray(new_record)))
print(census)
#Code starts here



# --------------
#Code starts here
#Storing the ages from the census into a new arrray
#Slicing the first coloumn
age = np.array(census[:,0],dtype ='int16')
print(age)

max_age = age.max()
print("Maximum age is ",max_age)

min_age = age.min()
print("Minimum age is ",min_age)

#Calculating the mean age
age_mean = age.mean()
print("Mean age of country is ",age_mean)

#Calculating the standard deviation
age_std = np.std(age)
print("Standard deviation of age ",age_std)
print("Country is young")


# --------------
#Code starts here
#Slicing the race coloumn from census data on the basis of race value
race_0 = np.array(census[census[:,2] ==0], dtype= int)
race_1 = np.array(census[census[:,2] ==1], dtype= int)
race_2 = np.array(census[census[:,2] ==2], dtype= int)
race_3 = np.array(census[census[:,2] ==3], dtype= int)
race_4 = np.array(census[census[:,2] ==4], dtype= int)

print(race_0)
#Calculating the lengths of the arrays
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

#Storing the lengths in a list
race_len = [len_0,len_1,len_2,len_3,len_4]

#Getting the index of the race with least population
print(race_len)

minority_race = race_len.index(min(race_len))
print("Minority race is :",minority_race)






# --------------
#Code starts here
#slicing array on the basis of age
senior_citizens = np.array(census[census[:,0] >60], dtype =int)
#senior_citizen.dtype = 'int16'
#print(senior_citizen)
#Calculating the total working hours of senior citizens
working_hours_sum = sum(np.array(senior_citizens[:,6]))
print("Total working hours is: ",working_hours_sum)
#The number of senior citizens is 
senior_citizens_len = len(senior_citizens)
print("The total number of senior citizen is :",senior_citizens_len)
#Calculating the average working hours
avg_working_hours = working_hours_sum/senior_citizens_len
print("Average working hours is ",avg_working_hours)
print("since the average working hours is greater than 25hrs government norm is not satisfied")


# --------------
#Code starts here
#Getting the citizens with education above high school
high = np.array(census[census[:,1] >10] ,dtype = int)
#print(len(high))

#Getting the citizen with education below high school
low = np.array(census[census[:,1] <=10] ,dtype = int)
#print(len(low))

#Getting the salary with high education
#salary_high_sum = sum(np.array(high[:,7]))

#Getting the salary with low education
#salary_low_sum = sum(np.array(low[:,7]))

''' #Alternate method calculating average high and low salary
avg_pay_high = salary_high_sum/len(high)
avg_pay_low = salary_low_sum/len(low) '''

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print("Mean of salary of high education ",avg_pay_high)
print("mean of salary of low education",avg_pay_low)

if avg_pay_high > avg_pay_low:
    print("Good Education results in better job")
else:
    print("Education is necessary for good job")


