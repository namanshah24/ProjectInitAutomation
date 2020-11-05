import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

foldername = str(sys.argv[1])
path = "C:\My Projects"
_dir = path + f"\{foldername}"
driver = webdriver.Chrome()
driver.get("https://github.com/login")
login_box = driver.find_element_by_xpath('//*[@id="login_field"]')
login_box.send_keys("namanshah24")
pwd_box = driver.find_element_by_xpath('//*[@id="password"]')
pwd_box.send_keys("Muktinaman@1524")
pwd_box.send_keys(Keys.RETURN)
driver.get("https://github.com/new")
repo_name = driver.find_element_by_xpath('//*[@id="repository_name"]')
repo_name.send_keys(foldername)
privatebutton = driver.find_element_by_xpath('//*[@id="repository_visibility_private"]')
privatebutton.click()
create_button = driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
create_button.submit()
commands = [f"echo # {foldername} >> README.md",
                "echo .vscode >> .gitignore",
                "git init",
                f"git remote add origin git@github.com:namanshah24/{foldername}.git",
                'git add .',
                'git commit -m "Initial commit"',
                'git push -u origin master']    
os.mkdir(_dir)
os.chdir(_dir)

for cmd in commands:
    os.system(cmd)

os.system("code .")



#  commands = [f'echo # {foldername} >> README.md',
#                 'git init',
#                 f'git remote add origin https://github.com/namnshah24/{foldername}.git',
#                 'git add .',
#                 'git commit -m "Initial commit"',
#                 'git push -u origin master']    
#     os.mkdir(_dir)
#     os.chdir(_dir)
