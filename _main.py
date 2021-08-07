import requests

data = []
f = open("data.json","a")
for i in range(1, 1000000):
    courseRequest = requests.get(f"https://www.udemy.com/api-2.0/courses/{i}/")
    f.write(courseRequest.text)
    print(courseRequest.text)
f.close()
