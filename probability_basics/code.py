# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
# Loading the dataset
df =pd.read_csv(path)

# Calculating probability for event where fico credit score is greater than 700
p_a =len(df[df['fico'] >700])/len(df)

# Calculating probability for event where purpose == 'debt_consolidation'
p_b =len(df[df['purpose'] =='debt_consolidation'])/len(df)

# new datafarem where purpose ='debr_consolidation'
df1 =df[df['purpose'] =='debt_consolidation']

# calculating conditional probability for AnB 
p_a_and_b =len(df1[df1['fico'] >700])/len(df1)

p_a_b =p_a_and_b/p_a
print(p_a)

result =p_a_b == p_a
print(result)
# code ends here


# --------------
# code starts here
# probability of paid back loan
prob_lp =df[df['paid.back.loan'] =='Yes'].shape[0]/df.shape[0]
print(prob_lp)

# probability of credit policy == yes
prob_cs =df[df['credit.policy'] =='Yes'].shape[0]/df.shape[0]

new_df =df[df['paid.back.loan'] =='Yes']

# probability of credit policy given paid back loan is true
prob_pd_cs =new_df[new_df['credit.policy'] =='Yes'].shape[0]/new_df.shape[0]

# Calculating A given B using Bayes
bayes =(prob_pd_cs*prob_lp)/prob_cs
print(bayes)

# code ends here


# --------------
# code starts here

df1 =df[df['paid.back.loan'] =='No']

plt.figure(figsize =(14,12))
plt.bar(df1['purpose'], df1.shape[0])
plt.title("Bar chart for Paid back loan is No")
plt.xlabel("Purpose of Loan")
plt.ylabel("No of defaulters")
plt.show()

# code ends here


# --------------
# code starts here

inst_median =df['installment'].median()
inst_mean =df['installment'].mean()

df['installment'].plot(kind ="hist")
plt.axvline(x =inst_median, color ='red', label ='Median')
plt.axvline(x =inst_mean, color ='green', label ='Mean')
plt.title("Installment ")
plt.legend()
plt.show()


df['log.annual.inc'].plot(kind ="hist")
plt.title("Annual Income")
plt.show()
# code ends here


