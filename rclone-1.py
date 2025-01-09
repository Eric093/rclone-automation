from rclone_python import rclone  # Import the rclone module

print(rclone.is_installed())  # Check if rclone is installed
print(rclone.version())  # Get the version of rclone

print(rclone.get_remotes())  # Get a list of available remotes
