import subprocess
import sys

def dump(url):
    try:
        return subprocess.Popen(["pg_dump", url], stdout=subprocess.PIPE)
    except OSError as err:
        print("error: pg_dump not found")
        sys.exit(2)

