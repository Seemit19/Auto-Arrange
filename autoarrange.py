import os
import shutil
import pandas as pd

# mapping different kinds of extension to their respective category.
EXTENSION_MAP = {'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.tif', '.bmp', '.eps'],
                 'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.mpeg', '.amv', '.3gp', '.mpg', '.wmv'],
                 'Documents': ['.pdf', '.docx', '.txt', '.csv', '.doc', '.wps', 'wpd', '.msg', '.rtf'],
                 'Audio': ['.mp3', '.wma', '.wav', '.aac', '.snd', '.ra', '.au'],
                 'Archives': ['.zip', '.rar', '.iso', '.tar', '.arj', '.hqx', '.arc', '.sit', '.gz', '.z'],
                 'Program' : ['.c', '.java' , '.py' , '.js' , '.cpp', '.ts', '.cs', '.swift', '.dta', '.pl', '.sh', '.bat', '.com', '.exe'],
                 'Web Page' : ['.html', '.htm', '.xhtml', '.asp', '.css', '.aspx', '.rss']}

# in "categorize_files" function unorganized folder is taken all real data present in that folder is mapped to their category.
# another map is created by in form dictionary data structure in which all same kind of data is stored as a list and their key is data category.
def categorize_files(folder):
    categorized_files = {}
    files =  os.listdir(folder)

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        category_found = False

        for category , extension in EXTENSION_MAP.items():
            if ext in extension:
                categorized_files.setdefault(category ,[]).append(file)
                category_found = True

        if not category_found:
            categorized_files.setdefault("Others" ,[]).append(file)

    return categorized_files

# now for every key i.e. category , a folder is created to store all respective values of that category.
def create_category_folders(base_folder , categorized_files):

    for category in categorized_files:
        category_path = os.path.join(base_folder,category)
        os.makedirs(category_path, exist_ok=True)

# now all files are actually moved to new category wise folders.
def move_files(source_folder , destination_folder , categorized_files):
    move_log = []

    for category,files in categorized_files.items():

        for file in files:
            source_path = os.path.join(source_folder,file)
            destination_path = os.path.join(destination_folder, category, file)
            move_log.append({"from": source_path , "to": destination_path})
            shutil.move(source_path , destination_path)
    return move_log


def undo_files(move_log):
    print("\nUndoing file organization...")

    for move in move_log:
        try:
            # Swap the paths — from destination → back to original location
            source_path = move["to"]
            destination_path = move["from"]

            # Make sure destination folder exists
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)

            # Move the file back
            shutil.move(source_path, destination_path)

        except Exception as e:
            print(f"❌ Failed to move {source_path} back to {destination_path}. Reason: {e}")

    print("✅ Undo completed. All files moved back to their original location.")

        

# main function to be executed:
if __name__ == "__main__":

    print("Hi fella, Here you can organize your messy folders.")
    print("--------------------\n----- Let's go -----\n--------------------")

    source = input("Enter the path where all unorganized or mixed files are present  :  ").strip()
    destination =  input("Enter the location where all files to be sorted or where a new folder has to be created : ").strip()
    categorized = categorize_files(source)

    # upcoming dry_run function is just to show user that where and how files will be organized in folder.
    dry_run = input("Do you want to see what all files are going to move before doing it real ? <Yes or No> : ")
    if dry_run.strip().lower() == "yes":

        dry_run_data = []
        for category, files in categorized.items():

            for file in files:

                dry_run_data.append({
                    'File Name': file,
                    'Category': category,
                    'Destination Path': os.path.join(destination, category, file)
                    })
                
        df = pd.DataFrame(dry_run_data)
        print(df)

    confirm = input("\nProceed with file organization? <Yes or No> : ").strip().lower()

    if confirm == "yes":
        os.makedirs(destination , exist_ok=True)
        create_category_folders(destination, categorized)
        move_log = move_files(source, destination, categorized)

        print(f"✅ Files organized successfully!, All organized files are saved in folder named : {os.path.basename(destination)}")

        undo_choice = input("Do you want to undo and restore the files to their original location? <Yes/No>: ").strip().lower()

        if undo_choice == "yes":
            undo_files(move_log)
        else:
            print("No undo performed. Your files remain organized.👍")
            
    else :
        print("Program has done execution without organizing files.")
