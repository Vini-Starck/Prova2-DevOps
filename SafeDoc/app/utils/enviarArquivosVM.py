import paramiko

def send_to_vm_linux(local_path, vm_linux_ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(vm_linux_ip, username=username, password=password)

    sftp = ssh.open_sftp()
    sftp.put(local_path, '/home/azureuser/documents/' + os.path.basename(local_path))
    sftp.close()
    ssh.close()

def send_to_vm_windows(local_path, vm_windows_ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(vm_windows_ip, username=username, password=password)

    sftp = ssh.open_sftp()
    sftp.put(local_path, 'C:\\Users\\azureuser\\photos\\' + os.path.basename(local_path))
    sftp.close()
    ssh.close()
