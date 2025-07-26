def employee(first_name, last_name, age):
    user_dict = {
        "first_name" : first_name,
        "last_name" : last_name,
        "age": age
    }
    return user_dict

employee_1 = employee("Zaid", "Mohamed", 21)

print(employee_1)