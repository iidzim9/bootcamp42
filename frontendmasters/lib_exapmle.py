# import os
# 
# my_folder = os.getcwd()
# print(f"my folder --> {my_folder}")
# 
# with os.scandir(my_folder) as folder:
    # for entry in folder:
        # print(f"- {entry.name}")

import sys

arg = sys.argv
for av  in arg:
    print(f" -> {av}")

print(f"we are currently running on a {sys.platform} machine")