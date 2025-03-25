# ftp client to interact with MALT FTP server
from ftplib import FTP, error_perm
import os

class MALTFTPClient:
    def __init__(self, host, username='Anonymous', password=''):
        self.ftp = FTP(host)
        self.ftp.login(user=username, passwd=password)

    def list_dir(self):
        files = []
        self.ftp.dir(files.append)
        return files

    def list_names(self):
        return self.ftp.nlst()

    def get_current_dir(self):
        return self.ftp.pwd()

    def change_dir(self, path):
        try:
            self.ftp.cwd(path)
            return f"Changed to: {self.ftp.pwd()}"
        except error_perm as e:
            return f"Error: {e}"

    def download_file(self, filename, local_path="."):
        local_file = os.path.join(local_path, filename)
        with open(local_file, 'wb') as f:
            self.ftp.retrbinary(f'RETR {filename}', f.write)
        return f"Downloaded {filename} to {local_path}"

    def download_selected(self, filenames, local_path="."):
        results = []
        for filename in filenames:
            results.append(self.download_file(filename, local_path))
        return results

    def delete_file(self, filename):
        try:
            self.ftp.delete(filename)
            return f"Deleted file: {filename}"
        except error_perm as e:
            return f"Error deleting file: {e}"

    def delete_selected(self, filenames):
        results = []
        for filename in filenames:
            results.append(self.delete_file(filename))
        return results

    def close(self):
        self.ftp.quit()
