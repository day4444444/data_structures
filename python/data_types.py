print("hello. welcome to data structures class !!!")
#numerics data types 
number1 = 10 
print(f"Var number1 is: {type(number1)}")
gravity = 9.8 
print(f"Var gravity is : {type(gravity)}")
numberx = 8j
print(f"Var numberx is : {type(numberx)}")
# string data types 
my_name = "david"
fullname= 'Peter McDonald'
description = '''
hello, how's it going?
This is amazing !!!
'''
print(f"Var my_name {type(my_name)}")
print(f"Var fullname is: {type(fullname)}")
print(f"Var description is: {type(description)}")

#listas 

week_days = []
print(week_days)
print(type(week_days)) 
#Clase list( es mutable o modificable)
#multi data type 

fruits = {}
print(fruits)
print(type(fruits))
#class dict (es diccionario)
#multi data type

months =()
print(months)
print(type(months))
#class tuple( no es mutable o no es modificable )
 
personal_info = ['Joan','Ayala', 50, True,'3005910463','Pasto',['Juli', 9]]
print(personal_info)
print(f"father age: {personal_info[2]}")
print("father city:", personal_info[5])
print(f"daugther name:{personal_info[6][0]}")
print(f"daugther age:{personal_info[6][1]}")
#print(type(personal_info))
#update father 
new_age = input("please, type the new father age:")
personal_info[2] =55
print(f" new father age is :{personal_info[2]}")
#add new information
personal_info.append('Malala')

print(personal_info)

#tuple
#user_data =('Benazir', 'Butto', 35, False)
#print(user_data)
#print(user_data[0])
#new_age =40
#user_data[2] = new_age

#diccionario
countries_info = { 'countri_name':'Colombia', 'capital' : 'Bogota', 'Abbrev' : 'Co', 'Code': '123456'}

print(countries_info)