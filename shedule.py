from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
import re

class FileSchedule(FileSystemEventHandler):
    def __init__(self, file_path :str):
        self.file_path = file_path

    def on_created(self, event):
        sogl = ['u','y','o','i','e','a','а','е','ё','и','о','у','э','ю','я','ы']
        name = event.src_path
        name = name.replace(".\\dir\\",'')
        name = name.replace(".txt", '')
        
        for ch in name:
            isGlasn = False
            for chN in sogl:
                ch = ch.lower()
                if ch == chN:
                    isGlasn = True
            if(isGlasn):
                ch = ch.lower()
            else:
                ch = ch.upper()
            print(ch)
        
            

    def on_modified(self, event):
        sogl = ['u','y','o','i','e','a','а','е','ё','и','о','у','э','ю','я','ы']
        name = event.src_path
        name = name.replace(".\\dir\\",'')
        name = name.replace(".txt", '')
        
        for ch in name:
            isGlasn = False
            for chN in sogl:
                ch = ch.lower()
                if ch == chN:
                    isGlasn = True
            if(isGlasn):
                ch = ch.lower()
            else:
                ch = ch.upper()
            print(ch)
    
path_to_file = ".\\dir"
event_handler = FileSchedule(path_to_file)
observer = Observer()
observer.schedule(event_handler, path = path_to_file, recursive = True)
observer.start()



try:
    while True:
        time.sleep(1)
            
finally:
    observer.stop()
    observer.join()

