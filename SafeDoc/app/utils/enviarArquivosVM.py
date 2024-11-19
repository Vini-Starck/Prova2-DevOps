import paramiko
import os

def send_to_vm_linux(local_path, vm_linux_ip, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(vm_linux_ip, username=username, password=password)

        sftp = ssh.open_sftp()
        remote_path = '/home/azureuser/documents/' + os.path.basename(local_path)
        sftp.put(local_path, remote_path)
        sftp.close()
        ssh.close()
        print(f"Documento enviado para VM Linux: {remote_path}")
    except Exception as e:
        print(f"Erro ao enviar documento para VM Linux: {str(e)}")


def send_to_vm_windows(local_path, vm_windows_ip, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(vm_windows_ip, username=username, password=password)

        sftp = ssh.open_sftp()
        remote_path = f'C:\\Users\\azureuser\\photos\\{os.path.basename(local_path)}'
        sftp.put(local_path, remote_path)
        sftp.close()
        ssh.close()
        print(f"Foto enviada para VM Windows: {remote_path}")
    except Exception as e:
        print(f"Erro ao enviar foto para VM Windows: {str(e)}")
