# --------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data =pd.read_csv(path)
loan_status =data['Loan_Status'].value_counts()

plt.figure(figsize=(10,5))
plt.title("Status of loan Applications")
plt.xlabel("Approved and not approved")
plt.ylabel("No of applications")

plt.bar(loan_status.index, loan_status)



# --------------
#Code starts here

property_and_loan =data.groupby(['Property_Area','Loan_Status'])

property_and_loan =property_and_loan.size().unstack()

property_and_loan.plot(kind ="bar", stacked= False, figsize=(15,8))

plt.show()


# --------------
#Code starts here
education_and_loan =data.groupby(['Education','Loan_Status']).size().unstack()

# Plotting the above data
education_and_loan.plot(kind ="bar", stacked =True, figsize =(12,4))
plt.title("Loan based on Education")
plt.xlabel("Education Status")
plt.ylabel('Loan Status')
plt.xticks(rotation =45)
plt.show()


# --------------
#Code starts here

#Data Frame for graduate applicants
graduate =data[data['Education'] =='Graduate']

#Data frame for non graduate applicants
not_graduate =data[data['Education'] =='Not Graduate']

# Plotting a density plot of LoanAmount of Graduate people
graduate['LoanAmount'].plot(kind ='density', title='Graduate', figsize =(10,15))

#Plotting a density plot of LoanAmount of Non graduate people
not_graduate['LoanAmount'].plot(kind ='density', title='Not Graduate', figsize =(10,16))


#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1, ax_2, ax_3) =plt.subplots(3,1, figsize= (18,6))

data['TotalIncome'] =data['ApplicantIncome'] + data['CoapplicantIncome']

ax_1.scatter(x=data['ApplicantIncome'], y=data['LoanAmount'])
ax_2.scatter(x=data['CoapplicantIncome'], y=data['LoanAmount'])
ax_3.scatter(x=data['TotalIncome'], y=data['LoanAmount'])



