import requests

# URL for your Flask API
url = "http://127.0.0.1:5000/fix_code"

# Buggy code input
buggy_code = """
def add(a, b)
    print(a + b)
"""

# Send the POST request
response = requests.post(url, json={"code": buggy_code})

# Show result
if response.status_code == 200:
    print("✅ Fixed Code:\n")
    print(response.json()["fixed_code"])
else:
    print("❌ Error:", response.status_code)
    print(response.text)
