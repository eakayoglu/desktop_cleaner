from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'emre':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)

extensions_folders = {
#No name
    'noname' : "/Users/emreakayoglu/Downloads/TEST/Other/Uncategorized",
#Audio
    '.aif' : "/Users/emreakayoglu/Downloads/TEST/Media/Audio",
    '.cda' : "/Users/emreakayoglu/Downloads/TEST/Media/Audio",
    '.mid' : "/Users/emreakayoglu/Downloads/TEST/Media/Audio",
    '.midi' : "/Users/emreakayoglu/Downloads/TEST/Media/Audio",
    '.mp3' : "/Users/emreakayoglu/Downloads/TEST/Media/Audio",
    '.mpa' : "/Users/emreakayoglu/Downloads/TEST/Media/Audio",
    '.ogg' : "/Users/emreakayoglu/Downloads/TEST/Media/Audio",
    '.wav' : "/Users/emreakayoglu/Downloads/TEST/Media/Audio",
    '.wma' : "/Users/emreakayoglu/Downloads/TEST/Media/Audio",
    '.wpl' : "/Users/emreakayoglu/Downloads/TEST/Media/Audio",
    '.m3u' : "/Users/emreakayoglu/Downloads/TEST/Media/Audio",
#Text
    '.txt' : "/Users/emreakayoglu/Downloads/TEST/Text/TextFiles",
    '.doc' : "/Users/emreakayoglu/Downloads/TEST/Text/Microsoft/Word",
    '.docx' : "/Users/emreakayoglu/Downloads/TEST/Text/Microsoft/Word",
    '.odt ' : "/Users/emreakayoglu/Downloads/TEST/Text/TextFiles",
    '.pdf': "/Users/emreakayoglu/Downloads/TEST/Text/PDF",
    '.rtf': "/Users/emreakayoglu/Downloads/TEST/Text/TextFiles",
    '.tex': "/Users/emreakayoglu/Downloads/TEST/Text/TextFiles",
    '.wks ': "/Users/emreakayoglu/Downloads/TEST/Text/TextFiles",
    '.wps': "/Users/emreakayoglu/Downloads/TEST/Text/TextFiles",
    '.wpd': "/Users/emreakayoglu/Downloads/TEST/Text/TextFiles",
#Video
    '.3g2': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.3gp': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.avi': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.flv': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.h264': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.m4v': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.mkv': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.mov': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.mp4': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.mpg': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.mpeg': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.rm': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.swf': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.vob': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
    '.wmv': "/Users/emreakayoglu/Downloads/TEST/Media/Video",
#Images
    '.ai': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.bmp': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.gif': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.ico': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.jpg': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.jpeg': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.png': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.ps': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.psd': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.svg': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.tif': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.tiff': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
    '.CR2': "/Users/emreakayoglu/Downloads/TEST/Media/Images",
#Internet
    '.asp': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.aspx': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.cer': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.cfm': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.cgi': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.pl': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.css': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.htm': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.js': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.jsp': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.part': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.php': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.rss': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
    '.xhtml': "/Users/emreakayoglu/Downloads/TEST/Other/Internet",
#Compressed
    '.7z': "/Users/emreakayoglu/Downloads/TEST/Other/Compressed",
    '.arj': "/Users/emreakayoglu/Downloads/TEST/Other/Compressed",
    '.deb': "/Users/emreakayoglu/Downloads/TEST/Other/Compressed",
    '.pkg': "/Users/emreakayoglu/Downloads/TEST/Other/Compressed",
    '.rar': "/Users/emreakayoglu/Downloads/TEST/Other/Compressed",
    '.rpm': "/Users/emreakayoglu/Downloads/TEST/Other/Compressed",
    '.tar.gz': "/Users/emreakayoglu/Downloads/TEST/Other/Compressed",
    '.z': "/Users/emreakayoglu/Downloads/TEST/Other/Compressed",
    '.zip': "/Users/emreakayoglu/Downloads/TEST/Other/Compressed",
#Disc
    '.bin': "/Users/emreakayoglu/Downloads/TEST/Other/Disc",
    '.dmg': "/Users/emreakayoglu/Downloads/TEST/Other/Disc",
    '.iso': "/Users/emreakayoglu/Downloads/TEST/Other/Disc",
    '.toast': "/Users/emreakayoglu/Downloads/TEST/Other/Disc",
    '.vcd': "/Users/emreakayoglu/Downloads/TEST/Other/Disc",
#Data
    '.csv': "/Users/emreakayoglu/Downloads/TEST/Programming/Database",
    '.dat': "/Users/emreakayoglu/Downloads/TEST/Programming/Database",
    '.db': "/Users/emreakayoglu/Downloads/TEST/Programming/Database",
    '.dbf': "/Users/emreakayoglu/Downloads/TEST/Programming/Database",
    '.log': "/Users/emreakayoglu/Downloads/TEST/Programming/Database",
    '.mdb': "/Users/emreakayoglu/Downloads/TEST/Programming/Database",
    '.sav': "/Users/emreakayoglu/Downloads/TEST/Programming/Database",
    '.sql': "/Users/emreakayoglu/Downloads/TEST/Programming/Database",
    '.tar': "/Users/emreakayoglu/Downloads/TEST/Programming/Database",
    '.xml': "/Users/emreakayoglu/Downloads/TEST/Programming/Database",
    '.json': "/Users/emreakayoglu/Downloads/TEST/Programming/Database",
#Executables
    '.apk': "/Users/emreakayoglu/Downloads/TEST/Other/Executables",
    '.bat': "/Users/emreakayoglu/Downloads/TEST/Other/Executables",
    '.com': "/Users/emreakayoglu/Downloads/TEST/Other/Executables",
    '.exe': "/Users/emreakayoglu/Downloads/TEST/Other/Executables",
    '.gadget': "/Users/emreakayoglu/Downloads/TEST/Other/Executables",
    '.jar': "/Users/emreakayoglu/Downloads/TEST/Other/Executables",
    '.wsf': "/Users/emreakayoglu/Downloads/TEST/Other/Executables",
#Fonts
    '.fnt': "/Users/emreakayoglu/Downloads/TEST/Other/Fonts",
    '.fon': "/Users/emreakayoglu/Downloads/TEST/Other/Fonts",
    '.otf': "/Users/emreakayoglu/Downloads/TEST/Other/Fonts",
    '.ttf': "/Users/emreakayoglu/Downloads/TEST/Other/Fonts",
#Presentations
    '.key': "/Users/emreakayoglu/Downloads/TEST/Text/Presentations",
    '.odp': "/Users/emreakayoglu/Downloads/TEST/Text/Presentations",
    '.pps': "/Users/emreakayoglu/Downloads/TEST/Text/Presentations",
    '.ppt': "/Users/emreakayoglu/Downloads/TEST/Text/Presentations",
    '.pptx': "/Users/emreakayoglu/Downloads/TEST/Text/Presentations",
#Programming
    '.c': "/Users/emreakayoglu/Downloads/TEST/Programming/C&C++",
    '.class': "/Users/emreakayoglu/Downloads/TEST/Programming/Java",
    '.dart': "/Users/emreakayoglu/Downloads/TEST/Programming/Dart",
    '.py': "/Users/emreakayoglu/Downloads/TEST/Programming/Python",
    '.sh': "/Users/emreakayoglu/Downloads/TEST/Programming/Shell",
    '.swift': "/Users/emreakayoglu/Downloads/TEST/Programming/Swift",
    '.html': "/Users/emreakayoglu/Downloads/TEST/Programming/C&C++",
    '.h': "/Users/emreakayoglu/Downloads/TEST/Programming/C&C++",
#Spreadsheets
    '.ods' : "/Users/emreakayoglu/Downloads/TEST/Text/Microsoft/Excel",
    '.xlr' : "/Users/emreakayoglu/Downloads/TEST/Text/Microsoft/Excel",
    '.xls' : "/Users/emreakayoglu/Downloads/TEST/Text/Microsoft/Excel",
    '.xlsx' : "/Users/emreakayoglu/Downloads/TEST/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.cab' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.cfg' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.cpl' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.cur' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.dll' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.dmp' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.drv' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.icns' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.ico' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.ini' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.lnk' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.msi' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.sys' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
    '.tmp' : "/Users/emreakayoglu/Downloads/TEST/Text/Other/System",
}

folder_to_track = '/Users/emreakayoglu/Desktop/TEST'
folder_destination = '/Users/emreakayoglu/Downloads/TEST'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()