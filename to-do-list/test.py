import requests

"""
GET POST
"""
# response = requests.get('http://127.0.0.1:5000/tasks')

# data = {
#     'title': 'title task 7',
#     'description': 'description task 7',
# }

# response = requests.post('http://127.0.0.1:5000/tasks', json=data)



"""
GET PUT DELETE
"""

# data = {
#     'title': 'new title task 1',
#     'description': 'new description task 1',
#     'done': True
# }

# response = requests.put('http://127.0.0.1:5000/task/1', json=data)
# response = requests.delete('http://127.0.0.1:5000/task/1')


# response = requests.get('http://127.0.0.1:5000/task/1') `ERROR`
# response = requests.get('http://127.0.0.1:5000/task/2')


print(
    f'status code = {response.status_code} | return {response.json()}'
)