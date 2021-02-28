import os
import sys

if __name__ == '__main__':
    print(os.path.join(os.path.dirname(__file__), '../'))

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))