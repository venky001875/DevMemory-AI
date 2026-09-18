import requests
import json

base_url = 'http://127.0.0.1:8000'

def print_result(name, resp):
    try:
        status = resp.status_code
        try:
            body = resp.json()
        except Exception:
            body = resp.text
    except Exception as e:
        status = None
        body = str(e)
    print(f'--- {name} ---')
    print('Status:', status)
    print('Body:', json.dumps(body, indent=2) if isinstance(body, (dict, list)) else body)

# 1. GET /demo/header with header
resp1 = requests.get(f'{base_url}/demo/header', headers={'X-Project-Name': 'MyProject'})
print_result('GET /demo/header with X-Project-Name', resp1)

# 2. GET /demo/header without header
resp2 = requests.get(f'{base_url}/demo/header')
print_result('GET /demo/header without header', resp2)

# 3. GET /demo/dependency
resp3 = requests.get(f'{base_url}/demo/dependency')
print_result('GET /demo/dependency', resp3)

# 4. POST /projects
project_payload = {"name": "TestProject", "path": "/tmp/test"}
resp4 = requests.post(f'{base_url}/projects', json=project_payload)
print_result('POST /projects', resp4)

# 5. GET /projects
resp5 = requests.get(f'{base_url}/projects')
print_result('GET /projects', resp5)
