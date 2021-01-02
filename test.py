import os
from random import randint

MAX_COMMITS = 5
THRESHOLD = 3

def commit():
  os.system("echo $(date) >> note.txt")
  os.system("git add note.txt")
  os.system("git commit -m Update note.txt")
  os.system("git push")

if (randint(0, 10) > THRESHOLD):
  for i in range(randint(0, MAX_COMMITS)):
    commit()