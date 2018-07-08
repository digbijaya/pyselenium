import os
print("hello world")
os.system('python --version')
os.system('pip --version')
print(os.getcwd())

import datetime as dt
import shutil


#git-clone## No no no ## gitclone would be handled from shellscript

os.system('pip install -r requirement.txt')
os.system('which python')
os.system('which pip')
os.system('pip freeze')
os.system('python setup.py test -a "-v tests/IAMdemotest -s --html=report/report.html"')


# creating a Directory Name with current date
report_folder = dt.datetime.today().strftime("%m-%d-%Y")
report_folder = r"report/"+report_folder

# Creating Directory with above folder name if not exit
if not os.path.exists(report_folder):
    os.makedirs(report_folder)

# Cut-Paste report to timestamp folder
# shutil.move(r"report/assets", report_folder)
# shutil.move(r"report/report.html", report_folder)

os.system(r"cp report/report.html "+report_folder)
os.system(r"cp report/assets -r "+report_folder)
