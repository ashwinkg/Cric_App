import requests

response = requests.post('https://cricapi.com/api/matches/', json={"apikey": "iTmPV7tBHrMJUbjxxcI96eTyY432"})
print("Status Code", response.status_code)
print('Printing the entire code')
# print(response.json())

response_dict = response.json()

# for key in response_dict:
#    print(key ,'->', response_dict[key])
print(response_dict['matches'])
