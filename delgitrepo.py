import os
import sys
from github import Github

foldername = str(sys.argv[1])
if "_" in foldername:
    foldername = foldername.replace("_"," ")
    gitname = foldername.replace(" ","-")
else:
    gitname = foldername
_dir =f"C:/My Projects/"


token = os.environ.get('gt')
g = Github(token)
user = g.get_user()
login = user.login
repo = g.get_repo(f"namanshah24/{gitname}")
repo.delete()
print("Github repo deleted")
os.chdir(_dir)
os.system(f"rmdir /q/s {foldername}")
print("Local Folder deleted")