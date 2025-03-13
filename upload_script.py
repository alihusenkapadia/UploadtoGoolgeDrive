from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def upload_to_drive(file_path):
    client_secrets="C:/Assignment3/client_secrets.json"
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile(client_secrets)
    gauth.LocalWebserverAuth()  # This handles authentication
    drive = GoogleDrive(gauth)

    file_drive = drive.CreateFile({'title': file_path.split("/")[-1]})  
    file_drive.SetContentFile(file_path)
    file_drive.Upload()

    return f"Uploaded {file_path} to Google Drive."
