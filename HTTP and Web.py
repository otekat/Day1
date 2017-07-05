import requests
user = input('Enter your github username')
if user > 0:
    result = requests.get('https://api.github.com/users/'+ user + '/events')
    if result.status_code == 200:
        print(result.json())
    else:
        print('HTTP ERROR %d.' %result.status_code)
else:
    print ('BAD USER NAME')