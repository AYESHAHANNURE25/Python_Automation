from google.colab import drive
drive.mount('/content/drive')

import os

# Define the root folder path
root_folder = '/content/drive/My Drive/DT'

# Create the root folder if it doesn't exist
if not os.path.exists(root_folder):
    os.makedirs(root_folder)

# Create subfolders for 164B and VN6
subfolders = ['164B', 'VN6']
for subfolder in subfolders:
    subfolder_path = os.path.join(root_folder, subfolder)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

# Create subfolders for 164B (6B, 7B, 8B)
subfolders_164B = ['6B', '7B', '8B']
for subfolder in subfolders_164B:
    subfolder_path = os.path.join(root_folder, '164B', subfolder)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    # Create DT folders inside 164B subfolders
    dt_folders = ['DT1(PS)','DT2(Sol1)','DT2(Sol2)','DT4(Plan)','DT5(Plan)','DT6(Prototype)','DT7']
    for dt_folder in dt_folders:
        dt_folder_path = os.path.join(subfolder_path, dt_folder)
        if not os.path.exists(dt_folder_path):
            os.makedirs(dt_folder_path)

# Create subfolders for VN6 (6A, 6B, 7A, 7B, 8A, 8B, 8C)
subfolders_VN6 = ['6A', '6B', '7A', '7B', '8A', '8B', '8C']
for subfolder in subfolders_VN6:
    subfolder_path = os.path.join(root_folder, 'VN6', subfolder)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    # Create DT folders inside VN6 subfolders
    dt_folders = ['DT1(PS)','DT2(Sol1)','DT2(Sol2)','DT4(Plan)','DT5(Plan)','DT6(Prototype)','DT7']
    for dt_folder in dt_folders:
        dt_folder_path = os.path.join(subfolder_path, dt_folder)
        if not os.path.exists(dt_folder_path):
            os.makedirs(dt_folder_path)

print("Folders created successfully!")
