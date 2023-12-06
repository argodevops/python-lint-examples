import requests

newHeaders = {"Content-type": "application/json", "Accept": "text/plain"}

# fmt: off
heatmap_gp = bytes([
    0, 255, 255, 255, # White
    64, 255, 255, 0,  # Yellow
    128, 255, 0, 0,   # Red
    255, 0, 0, 0])    # Black
# fmt: on

response = requests.post(
    "https://httpbin.org/post", data={"id": 1, "name": "Jessa"}, headers=newHeaders
)

print("Status code: ", response.status_code)

response_Json = response.json()
print("Printing Post JSON data")
print(response_Json["data"])

print("Content-Type is ", response_Json["headers"]["Content-Type"])
