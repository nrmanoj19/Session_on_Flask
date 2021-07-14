import requests
import json

my_url = 'http://localhost:5000/add_get'
name = input("name of the user")
age = int(input("enter age"))
mailid = input("enter the mailid")
my_query = "?name="+name+"&age="+str(age)+"&mailid="+mailid
print(my_query)

my_final_url = my_url + my_query
print(my_final_url)

res2 = requests.get(my_final_url)
# json_data = res2.json()
# print(json_data)
print("Status code is: ", res2.status_code)

if res2.ok:
    print("Status code is: ", res2.status_code)
    print("Result is: ", res2.json())
    # print("result is", res2.json().decode('utf-8'))
    # print("Result is", res2.get_data(as_text=True))

    # print(res2.requests.Response.json())
    # print(json_data)
