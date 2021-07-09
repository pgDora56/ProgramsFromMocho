import subprocess
result = subprocess.check_output(["sh", "programs/gitpush.sh"])
print(result)
