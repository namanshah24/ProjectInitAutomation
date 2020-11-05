import os
import sys


foldername = str(sys.argv[1])
path = os.environ.get("mp")

_dir =f"{path}/{foldername}"


commands = [f"echo # {foldername} >> README.md",
                "echo .vscode >> .gitignore",
                "echo *.log >> .gitignore"
                "git init",
                'git add .',
                'git commit -m "Initial commit"',
]
                
os.mkdir(_dir)
os.chdir(_dir)

for cmd in commands:
    os.system(cmd)

os.system("code .")
print("Local Project Created")