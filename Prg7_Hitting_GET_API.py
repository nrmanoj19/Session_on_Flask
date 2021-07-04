import requests

my_url = 'http://localhost:5000/add_get'
my_query = '?num1=10&num2=10'
my_final_url = my_url + my_query
res2 = requests.get(my_final_url)

if res2.ok:
    print("Status code is: ", res2.status_code)
    print("Result is: ", res2.json())
