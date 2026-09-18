import requests, json

base = 'http://127.0.0.1:8000'

def print_res(name, resp):
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

# 1. query with name
resp1 = requests.get(f'{base}/demo/query', params={'name': 'DevMemory'})
print_res('GET /demo/query?name=DevMemory', resp1)

# 2. query without name
resp2 = requests.get(f'{base}/demo/query')
print_res('GET /demo/query (missing name)', resp2)

# 3. Swagger (OpenAPI) verification
openapi_resp = requests.get(f'{base}/openapi.json')
print('\n--- OpenAPI /openapi.json snippet for /demo/query ---')
if openapi_resp.status_code == 200:
    data = openapi_resp.json()
    path_info = data.get('paths', {}).get('/demo/query', {})
    print(json.dumps(path_info, indent=2))
else:
    print('Failed to fetch OpenAPI schema, status', openapi_resp.status_code)
