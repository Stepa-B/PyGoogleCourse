#!/usr/bin/env python3
import sys
import subprocess
result=subprocess.run(["host", "1.1.1.1"], capture_output=True)
print(result.returncode)
print (result.stdout)
