# --------------
# Code starts here
# Initialization of Variables
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatinating the two lists
new_class = class_1+class_2
print(new_class)
# Adding an element to the existing list
new_class.append('Peter Warden')
print(new_class)
# Removing an element from the list
del new_class[5]
print(new_class)
print(type(new_class))
# Code ends here


# --------------
# Code starts here
# Variable Initialization
courses = {'Math':65,'English':70,'History':80,'French':70,'Science':60}
"""totalsubjetcs = len(courses)
print(totalsubjetcs)
print(courses.keys()," | ",courses.values())"""
print(courses)
# Total marks
total = sum(courses.values())
print("Total marks scored by Geoffrey Hinton :",total)
# Percentage of marks out of 500
percentage = (total/500)*100
print("Percentage obtained by Geoffrey Hinton :",percentage)
# Code ends here


# --------------
# Code starts here
# Creating a dictionary for students
mathematics = {'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,
'Peter Warden':75}
# Calculating the max in dictionary
topper = max(mathematics,key = mathematics.get)
print('The topper in mathematics is '+topper)



# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here
# Splitting the name using split() mtehod
first_name = topper.split()[0]
last_name = topper.split()[1]
full_name = last_name+" "+first_name
#Converting to upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


