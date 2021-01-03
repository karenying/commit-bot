import os
from random import randint

MAX_COMMITS = 5
THRESHOLD = 3

def commit():
  os.system("echo $(date) >> output.txt")
  os.system("git add output.txt")
  os.system("git commit -m Update output.txt")
  os.system("git push")

if (randint(0, 10) > THRESHOLD):
  for i in range(randint(0, MAX_COMMITS)):
    commit()