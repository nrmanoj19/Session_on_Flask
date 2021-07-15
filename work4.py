import requests

my_url = 'http://localhost:5000/add_post'
#my_body = {​​​​​"num1": 10, "num2": 10}​​​​​
name=input("enter the name")
age=int(input("enter age"))
mailid=input("enter the mailid")
my_body = {"name": name, "age": age, "mailid": mailid}
print(my_body)
res1 = requests.post(my_url, json=my_body)
print("Status code is: ", res1.status_code)
if res1.ok:
    print("Status code is: ", res1.status_code)
    print("Result is: ", res1.json())