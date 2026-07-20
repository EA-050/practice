import requests
import json
class TaskManager:
    def __init__(self,url):
        self.url = url
    def get_all(self):
        try:
            r = requests.get(f"{self.url}")
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Error : ", e)
    def get_one(self,endpoint):
        try:
            r = requests.get(f"{self.url}/{endpoint}")
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Error :", e)
    def create(self,data):
        try:
            r = requests.post(f"{self.url}", json = data)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Error:", e)
    def update(self,data,endpoint):
        try:
            r = requests.put(f"{self.url}/{endpoint}" , json = data)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Error:" , e)
    def remove(self,endpoint):
        try:
            r = requests.delete(f"{self.url}/{endpoint}")
            r.raise_for_status()
            return r.status_code()
        except requests.exceptions.RequestException as e:
            print("Error: ",e)
    @staticmethod
    def completed(todos):
        return len([todo for todo in todos if todo["completed"] == True])
    @staticmethod
    def save_to_file(filename,data):
        with open(filename, "w") as f:
            json.dump(data,f)
    @classmethod
    def from_config(cls,config_dict):
        return cls(config_dict["url"])
tool = TaskManager.from_config({"url":"https://jsonplaceholder.typicode.com/todos"})
print(tool.url)

new_tool = TaskManager("https://jsonplaceholder.typicode.com/todos")
#print(new_tool.get_all())
print(new_tool.get_one(4))