#*  Dictonary are used to store data in  a key:value pair
#* like an object in js
# * Dict are mutable

info ={
    'name': 'Arnab',
    'cgpa': 6.97,
    'course': 'BCA',
    'skills': ['java', 'javascript', 'python', 'react', 'nodejs', 'mysql'],
    'age': 24
}

#! print(info.keys()) #to show all the keys (return all keys)
#! print(info.items()) #to show all the items (return all items key:value pairs)

#? print(info.get('name')) #No error(return according to the values)

#? To update the dictionary
# info.update({'city':'Delhi'})
# print(info)
# print(info.values()) (return all the values)