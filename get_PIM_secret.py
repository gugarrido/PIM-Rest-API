import getpass
import requests
import json

def get_token():
    url = "https://yourSecretServerURL/oauth2/token"
    username = ''
    #I use getpass lib to input the password, avoiding leave it as clear text
    password = getpass.getpass('Security Center Security Manager password: ')
    payload = {'username': username,
    'password': password,
    'grant_type': 'password'}
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload).text
    response_data = json.loads(response)
    getResponseStr = response_data["access_token"]
    token = json.dumps(getResponseStr).replace('"', '')
    return token
 
def get_secret(token):
    #Specify the Secret ID you want to get information,
    secret_id = 1234
    #Specify the API endpoint with the Secret ID specified above 
    url = "https://yourSecretServerURL/api/v1/secrets/"+str(secret_id)
    headers = {'Authorization':'Bearer ' + token, 'content-type':'application/json'}
    response = requests.get(url, headers=headers)
    getResponseStr = json.dumps(response.json())

def main():
    token = get_token()
    get_secret(token)

if __name__ == '__main__':
    main()
