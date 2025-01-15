from rclone_python import rclone  # Import the rclone module
import subprocess

#print(rclone.is_installed())  # Check if rclone is installed




def is_installed():
    try:
        subprocess.check_output(["rclone", "--version"])
        return True
    except FileNotFoundError:
        return False

print(is_installed())

if is_installed():
    print("rclone is installed")

if not is_installed():
    print("rclone is not installed")
    
#print(rclone.version())  # Get the version of rclone

print(rclone.get_remotes())  # Get a list of available remotes
