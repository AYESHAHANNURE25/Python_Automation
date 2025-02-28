# Install necessary libraries
!pip install PyDrive pandas openpyxl

# Import libraries
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
from google.colab import auth
from oauth2client.client import GoogleCredentials
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# Specify the folder IDs as a list
folder_ids = ['1GOGeYA_kvZSbV2hUm8LS6e6MUxXJ21Bz']  # Replace with your folder IDs

# Create an empty list to store all files data
all_files_data = []

# Iterate through each folder ID
for folder_id in folder_ids:
    # List files in the current folder and get their names and links
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

    # Get the folder name using the folder ID
    folder = drive.CreateFile({'id': folder_id})
    folder.FetchMetadata(fields='title')  # Fetch the 'title' metadata
    folder_name = folder['title']

    # Extract file names and links for the current folder
    # "Result" as display text, "Folder Name" instead of "Hyperlink"
    files_data = [{'File Name': file['title'],
                   'Folder Name': folder_name,  # Replaced "Hyperlink" with "Folder Name"
                   'Bill': f'=HYPERLINK("{file["alternateLink"]}", "Bill")'
                   } for file in file_list]

    # Add the files data for the current folder to the all_files_data list
    all_files_data.extend(files_data)

    # Add a blank row
    all_files_data.append({'File Name': '', 'Folder Name': '', 'Result': ''})  # Blank row

# Save the data to an Excel sheet
df = pd.DataFrame(all_files_data)
df.to_excel('/content/drive/My Drive/Travling.xlsx', index=False)

print("File names, folder names, and result hyperlinks have been saved to 'Travling.xlsx' in your Google Drive.")
