# Pattern 1: Import the whole module
import math
# Now use: math.sqrt(16)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
# Now use: sqrt(16)
#################################################
# Common built-in modules
# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)

####################################

# Sharing your project: requirements.txt
'''When you share your Python project, others need to know which packages to install. The standard way is using a requirements.txt file:
​
Creating requirements.txt
List all your project’s packages:
pip freeze > requirements.txt
'''