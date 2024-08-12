import os
import subprocess

# Use 'dir' instead of 'ls' for Windows
os.system("dir")
subprocess.run(["dir"], shell=True)
subprocess.run(["dir", "/B"], shell=True)

# Replace 'ls -l README.md' with an equivalent command in Windows
subprocess.run(["dir", "/B", "README.md"], shell=True)

# Commands like 'uname' and 'ps' are also Unix/Linux specific.
# For system information, use 'systeminfo' in Windows
command = "systeminfo"
print(f'Gathering system information with command: {command}')
subprocess.run(command, shell=True)

# For listing processes, use 'tasklist' in Windows
command = "tasklist"
print(f'Gathering active process information with command: {command}')
subprocess.run(command, shell=True)
