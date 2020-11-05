import os
import sys
from github import Github

foldername = str(sys.argv[1])

_dir =f"C:/My Projects/{foldername}"
viz_status = str(sys.argv[2])
viz = True if viz_status == "Private" or viz_status == "private" or viz_status == "" else False

token = os.environ.get('gt')
g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(foldername, private= viz)
print("Github repo created")

commands = [f"echo # {foldername} >> README.md",
                "echo .vscode >> .gitignore",
                "echo *.log >> .gitignore"
                "git init",
                f"git remote add origin git@github.com:{login}/{foldername}.git",
                'git add .',
                'git commit -m "Initial commit"',
                'git push -u origin master']    
os.mkdir(_dir)
os.chdir(_dir)

for cmd in commands:
    os.system(cmd)

os.system("code .")
print("Project created")


