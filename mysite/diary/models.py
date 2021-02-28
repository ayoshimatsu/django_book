import sys
import pathlib

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + "/../")
print(sys.path)


from django.db import models
