
import os
import shutil
import os.path



def bytype():
    path = input(" Enter the path of directory you want to organize: ")

    lis = os.listdir(path)
    lis.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)

    os.chdir(path)

    arr = os.listdir()

    slash = "\\"

    file_types = {

        "Text": [".doc", ".rtf", ".txt", ".wps", ".docx"],
        "Data": [".csv", ".pps", ".ppt", ".pptx", ".xml"],
        "Music": [".mp3", ".m4a", ".m4a",  ".m4p", ".mp3", "ogg"],
        "Video": [".3gp", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".wmv"],
        "notes": [".pdf"],
        "Spreadsheet": [".xlr", ".xls", ".xlsx"],
        "apps": [".apk", ".app", ".exe", ".jar"],
        "Web": [".css", ".htm", ".html", ".js", ".php", ".xhtml"],
        "Compressed": [".rar", ".zip"],
        "Programmes": [".c", ".class", ".cpp", ".cs", ".java", ".py"],
        "Misc": [".ics", ".msi", ".torrent"],
        "images": [".jpeg", ".png", ".jpg"]
    }

    for x in arr:
        fflag = 0
        if os.path.isfile(x):
            if "." in x:
                extension_name = x[x.index("."):]
                for file_type, extensions in file_types.items():
                    if extension_name in extensions:
                        fflag = 1
                        folder_name = file_type
                        newpath = path + slash + folder_name
                        print(newpath)
                        break
                if fflag == 0:
                    folder_name = "Other"
                    newpath = path + slash + folder_name
                    print(newpath)
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            shutil.move(path + slash + x, newpath + slash + x)

bytype()