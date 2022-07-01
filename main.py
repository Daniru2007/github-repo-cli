import os
import requests
import pyperclip

headers = {
    "Authorization": f"token {open('token.txt').read()}",
    "Content-type": "application/json",
    "Accept": "application/json",
}
name = input("name(default) $ ") or "default"
dir = input("directory('.') $ ") or "."
data = "{\"name\":\""+name+"\"}"

r = requests.post("https://api.github.com/user/repos", data=data, headers=headers).json()

try:
    pyperclip.copy(r["html_url"])
except Exception as e:
    print(f"[ERROR] repository {name} already exits")
    exit()

os.chdir(dir)
os.system(f"git init .")
os.system(f"git remote add origin {r['html_url']}.git")
os.system(f'git add .')
os.system(f'git commit -m "setup"')
os.system(f"git push -u origin main")
