# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 

# code starts here
bank =pd.read_csv(path)
print(bank.head())

# Creating a dataframe of categorical values
categorical_var =bank.select_dtypes(include ='object')
print(categorical_var)

# Creating a dataframe of numerical values
numerical_var =bank.select_dtypes(include ='number')
print(numerical_var)

# code ends here


# --------------
# code starts here
# Creating a data frame excluding Loan_ID
banks =bank.drop("Loan_ID",axis =1)
print(banks.isnull().sum())

# Calculating mode
bank_mode =banks.mode().iloc[0]

# Filling missing NaN values
banks.fillna(bank_mode, inplace =True)
print("After filling the NaN values")
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here

avg_loan_amount =pd.pivot_table(banks, index=["Gender", "Married", "Self_Employed"], values= "LoanAmount")
print(avg_loan_amount)


# code ends here



# --------------
# code starts here

# The number of self employed applicants with a loan
loan_approved_se =len(banks[(banks["Self_Employed"] == "Yes") & (banks['Loan_Status'] =='Y')])

# The number of applicants with a job with a loan
loan_approved_nse =len(banks[(banks["Self_Employed"] == "No") & (banks['Loan_Status'] =='Y')])

# Percentage of self employed person with loan
percentage_se =(loan_approved_se/banks['Loan_Status'].count())*100
print(percentage_se)

# Percentage of non self employed person with loan
percentage_nse =(loan_approved_nse/banks['Loan_Status'].count())*100
print(percentage_nse)

# code ends here


# --------------
# code starts here

# Creating a user defined for converting the loan amount tenure
def converting(x):
    return x//12

# Coverting the loan_amount_term into years
loan_term =banks["Loan_Amount_Term"].apply(lambda x:converting(x))

big_loan_term =loan_term[loan_term >= 25].count()
print("The number pf loan applications with tenure greater than 25 years is ",big_loan_term)
# code ends here


# --------------
# code starts here

loan_groupby =banks.groupby('Loan_Status')

# creating a subset of loan groupby by including ApplicantIncome and Credit_History
loan_groupby =loan_groupby[['ApplicantIncome','Credit_History']]

# calculating the mean
mean_values =loan_groupby.mean()
print(mean_values)
# code ends here


