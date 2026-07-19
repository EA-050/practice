import requests
import json
class APIToolkit:
    def __init__(self,base_url):
        self.base_url = base_url
    def get(self,endpoint):
        try:
            r = requests.get(f"{self.base_url}/posts/{endpoint}")
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Error:", e)
    def post(self,data):
        try:
            r = requests.post(f"{self.base_url}/posts" , json = data)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Error:", e)
    @staticmethod
    def save_to_file(data,filename):
        with open(filename,"w") as f:
            json.dump(data,f)
    @classmethod
    def from_config(cls,config_dict):
        return cls(config_dict["base_url"])
    @classmethod
    def default_toolkit(cls):
        return cls("https://jsonplaceholder.typicode.com")

Tool = APIToolkit.from_config({"base_url":"https://jsonplaceholder.typicode.com"})


print(Tool.base_url)