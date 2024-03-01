import requests

res = requests.get("https://dummyjson.com/products/1")
res_j=res.json()
print(res_j['id'], res_j['title'])  # Output: 1 Product A

# Get all products from the API and print their names
all_prod = requests.get('https://dummyjson.com/products').json()
for x in all_prod['products']:
    print(x['title'])