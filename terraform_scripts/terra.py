import subprocess

def terraform_run(command):
    try:
        process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print (process.stdout.decode())
    except subprocess.CalledProcessError as e:
        # Handle errors and print the outputs
        print(f"An error occurred: {e}")
        print(f"Standard Output:\n{e.stdout.decode()}")
        print(f"Standard Error:\n{e.stderr.decode()}")

directory = r"path/to/directory"
command = f"terraform -chdir={directory} init"

terraform_run(command)
