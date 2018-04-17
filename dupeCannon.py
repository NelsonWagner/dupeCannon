import dupeID, fileID
from shutil import copy2, move

output = 'X:\\Cad Data\\'
drive1 = {'path': '', 'fileFilters': [], 'dirFilters': ''}
drives = [drive1]

listOfDrives = dupeID.GetDrives(drives)
print('Gotten Drives')

listOfUniqueDupes = dupeID.GetUniqueDuplicates(listOfDrives)
print('Gotten Unique Dupe Files')

listOfAllFiles = []
for d in dupeID.ListOfAllFiles:
    listOfAllFiles.extend(d.listOfFiles)
print('Gotten Lists')

listOfAllUniqueFiles = fileID.GetAllUniqueFiles(listOfUniqueDupes, listOfAllFiles)
print('Gotten List of Unique Files')
print(len(listOfAllUniqueFiles))

for f in listOfAllUniqueFiles:
    f.outPath = (output + f.filename)
    copy2(f.filePath, f.outPath)
    
print('All Done')