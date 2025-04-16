import os
folder_path = r'C:\Users\palak\OneDrive\Documents\Desktop\Python-training\FILE HANDLING'
all_files = os.listdir(folder_path)
txt_csv_files = [file for file in all_files if file.endswith('.txt') or file.endswith('.csv')]
print("Text and CSV files in the folder:")
for file in txt_csv_files:
    print(file)
