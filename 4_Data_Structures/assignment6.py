""" print values from a nested dictionary """

# nested dictionary

personal_details = {
    'name' : "Manisha Mali",
    'age' : 22,
    'dob' : '15 Nov 2001',
    'address' : {
        'street' : 'Main road 120',
        'city' : 'Murud',
        'state' : 'Maharashtra',
        'pincode' : 413510
    }
}


# accessing values using keys

print(personal_details['name'])
print(personal_details['address']['street'])
print(personal_details['address']['city'])
