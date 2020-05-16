# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data =pd.read_csv(path)

data['Gender'].replace('-', "Agender", inplace=True)
gender_count =data['Gender'].value_counts()
plt.figure(figsize =(3,6))
plt.title("Gender wise distribution of super humans")
plt.bar(gender_count.index, gender_count)
plt.ylabel("No of superhumans")
plt.xlabel("Gender classification")
#Code starts here 




# --------------
#Code starts here

alignment =data['Alignment'].value_counts()

pielabels =['Good','Evil','Neutral']

# Plotting a pie chart
plt.pie(alignment, labels=pielabels)
plt.title("Good vs Evil")
plt.show()


# --------------
#Code starts here
# Subset of dataframe conataining only Strength and Combat columns
sc_df =data[['Strength', 'Combat']]
sc_covariance =sc_df.cov()['Strength'][1]
print("Covariance of Strength and combat",sc_covariance)
sc_strength =sc_df['Strength'].std()
sc_combat =sc_df['Combat'].std()
# Calculating pearson's coefficient
sc_pearson =sc_covariance/(sc_combat*sc_strength)
print(sc_pearson)

ic_df =data[['Intelligence','Combat']].copy()
ic_covariance =ic_df.cov()['Intelligence'][1]
print("Covariance of Intelligence and Combat skills ",ic_covariance)
ic_intelligence =ic_df['Intelligence'].std()
ic_combat =ic_df['Combat'].std()
ic_pearson =ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


# --------------
#Code starts here

total_high =data['Total'].quantile(.99)

# Superbest Heroes
super_best =data[data['Total']>total_high]

super_best_names =list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
# Subplotting the figure into 3 axes
fig ,(ax_1,ax_2,ax_3)= plt.subplots(1,3, figsize=(18,6))

ax_1.boxplot(super_best['Intelligence'])
ax_1.set_title("Intelligence")

ax_2.boxplot(super_best['Speed'])
ax_2.set_title("Speed")

ax_3.boxplot(super_best['Power'])
ax_3.set_title("Power")


