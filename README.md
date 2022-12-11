# 2OP3_files_organizer
Organize lecture, assignment, and tutorial files for 2OP3. After downloading a lecture, tutorial, or assignment from a2l. Run this program to move them into the
folder u keep them in. If anyone know how to make it automatic, as it not having to run the file everytime please let me know.

## Usage
To use the script, you need to specify the paths for the source and destination directories in the script:

```
# add source and destination directories ex. C:\\Users\\...
source_dir = ""
dest_lec = ""
dest_tut = ""
dest_ass = ""
```
Then, run the script using the following command:

```
python mover.pyw
```

The script will begin monitoring the source directory for new zip files. When a new zip file is detected, it will extract the contents of the file into one of the destination directories depending on the name of the zip file.
