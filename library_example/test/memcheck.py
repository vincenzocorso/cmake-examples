import subprocess

file_name = 'library_test'
subprocess.run(['valgrind', '--leak-check=full', '-v', './' + file_name])
