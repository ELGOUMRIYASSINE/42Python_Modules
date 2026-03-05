# import pandas as pd
import requests

response = requests.get("https://api.github.com/users/octocat")
print(response.status_code)
print(response.json()['login'])
# data = {
#     "Name":   ["Alice", "Bob", "Charlie"],
#     "Age":    [25, 30, 35],
#     "Salary": [50000, 60000, 70000]
# }

# df = pd.DataFrame(data)
# df['Tax'] = df['Salary'] * 0.1
# df['Goals'] = [0, 0, 0]
# # print(df)
# print(df.describe())