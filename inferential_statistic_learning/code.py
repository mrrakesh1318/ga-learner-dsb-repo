# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]

#Code starts here
data =pd.read_csv(path)

# Sample of data
data_sample =data.sample(n =sample_size, random_state=0)

# Sample mean
sample_mean =data_sample['installment'].mean()

# Sample Standard deviation
sample_std =data_sample['installment'].std()

# Margin of error
margin_of_error =z_critical*(sample_std/math.sqrt(sample_size))

# Confidence Interval
confidence_interval =(sample_mean-margin_of_error,sample_mean+margin_of_error)

# Actual mean of population
true_mean =data['installment'].mean()

print(true_mean)
print(confidence_interval)


# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
# subplotting the figure
fig ,axes =plt.subplots(3,1, figsize=(5,15))

# Sampling using given sample size
for i in range(len(sample_size)):
    m =[]
    for j in range(1000):
        sample =data['installment'].sample(n =sample_size[i], random_state =0)
        mean =sample.mean()
        m.append(mean)
    mean_series =pd.Series(m)
    axes[i].hist(mean_series, bins =10)



# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here

# Remove % from int.rate column
data['int.rate'] =data['int.rate'].apply(lambda x: x.replace('%',""))

# Converting the int.rate column to float
data['int.rate'] =data['int.rate'].astype(float) / 100

# performing z-test
z_statistic, p_value =ztest(x1 =data[data['purpose'] =='small_business']['int.rate'],
value =data['int.rate'].mean(),
alternative ='larger')

# Hypothesis testing
if p_value <0.05:
    print("We reject null hypothesis")
else:
    print("We accept null hypothesis")


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here

# Applying ztest on loan installment paid =yes and loan installment paid=no
z_statistic, p_value =ztest(x1 =data[data['paid.back.loan']== 'No']['installment'],
x2 =data[data['paid.back.loan']== 'Yes']['installment'])

print("Z-statistic :",z_statistic)
print("p-value ",p_value)

if p_value< 0.05:
    print("Reject null hypothesis")
else:
    print("Accept null hypothesis")


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here

# Counting the observed categorical variables
yes =data[data['paid.back.loan'] =='Yes']['purpose'].value_counts()
no =data[data['paid.back.loan'] =='No']['purpose'].value_counts()

# Concatenating the yes, no into a table
observed =pd.concat((yes.transpose(), no.transpose()), axis =1, keys =['Yes','No'])

# Applying chi2_contigency() on observed
chi2, p, dof, ex = stats.chi2_contingency(observed)

print("Chi-Statistic is ",chi2)
print("p-value is ",p)
print("Degree of freedom for given data is ",dof)
print("Expected values are ")
print(ex)
print("Observed values are ")
print(observed)

if chi2 > critical_value:
    print("Reject the null hypothesis")
else:
    print("Accept the null hypothesis")


