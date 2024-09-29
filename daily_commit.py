import os
import datetime
import subprocess

# Set the path to your local Git repository
REPO_DIR = 'C:/Users/Kush/OneDrive/Desktop/DevOps2024/Python/Automation'
FILE_NAME = 'daily_commit.txt'

# Change directory to the repository
os.chdir(REPO_DIR)

# Modify the file or create it if it doesn't exist
with open(FILE_NAME, 'a') as file:
    file.write(f"Daily commit: {datetime.datetime.now()}\n")

# Git commands to add, commit, and push
subprocess.run(['git', 'add', FILE_NAME])
subprocess.run(['git', 'commit', '-m', f"Automated commit: {datetime.datetime.now().date()}"])
subprocess.run(['git', 'push'])
