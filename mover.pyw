from os import scandir, remove
from zipfile import ZipFile
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "C:\\Users\\folio\\Downloads"
dest_lec = "C:\\Users\\folio\\Desktop\\OOP\\lec"
dest_tut = "C:\\Users\\folio\\Desktop\\OOP\\tut"
dest_ass = "C:\\Users\\folio\\Desktop\\OOP\\ass"


class Mover(FileSystemEventHandler):
    with scandir(source_dir) as it:
        for entry in it:
            name = entry.name
            if name.endswith(".zip"):
                zip_ref = ZipFile(entry)
                if "Lecture" in name:
                    zip_ref.extractall(dest_lec)

                elif "Tutorial" in name:
                    zip_ref.extractall(dest_tut)

                elif "Assignment" in name:
                    zip_ref.extractall(dest_ass)

                zip_ref.close()
                remove(entry)

#trying to add code that deletes __MACOSX folder
        # with scandir(dest_lec) as it:
        #     for entry in it:
        #         if "MAC" in entry.name:
        #             remove(entry)


if __name__ == "__main__":
    path = source_dir
    event_handler = Mover()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
