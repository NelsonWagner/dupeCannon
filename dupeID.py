import os
from _operator import attrgetter
from collections import Counter

class Drive():
    def __init__(self, drivePath, fileFilters, dirFilters):
        self.listOfFiles = []
        fileFilters = ''.join(fileFilters)
        dirFilters = ''.join(dirFilters)
        for dir, subdir, files, in os.walk(drivePath):
            for file in files:
                if not dirFilters in file.lower():
                    if 'sld' in file.lower():
                        if not fileFilters in file.lower():
                            temp = {'file': file, 'dir': dir, 'path': ''.join(dir + '\\' + file)}
                            self.listOfFiles.append(temp)

class File():
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path
        self.filePath = self.path + "\\" + self.filename
        
class DupeFile():
    def __init__(self, dupeName):
        self.filename = dupeName
                
    def GetLocations(self, listOfFilepaths):
        self.dupeList = [file for file in listOfFilepaths if file.filename == self.filename]
                
    def GetUniqueFiles(self):
        self.uniqueFile = 'nil'
        for d in self.dupeList:
            d.modifiedTime = round(os.path.getmtime(d.filePath), 0)
            self.dupeList = sorted(self.dupeList, key=attrgetter('modifiedTime'), reverse=True)
            self.uniqueFile = self.dupeList[0]
        return self.uniqueFile

def GetDrives(listOfDrives):
    driveObjList = []
    for d in listOfDrives:
        driveObjList.append(Drive(d['path'], d['fileFilters'], d['dirFilters']))
    return driveObjList

def ListOfAllFiles(listOfFiles):
    listOfAllFiles = []
    for f in listOfFiles:
        listOfAllFiles.append(File(f['file'], f['dir']))
    return listOfAllFiles

def GetUniqueDuplicates(driveObjects):
    listOfAllFilenames = []
    filePaths = []
    for d in driveObjects:
        for f in d.listOfFiles:
            listOfAllFilenames.append(f['file'])
            filePaths.append(File(f['file'], f['dir']))
    
    duplicateFilenames = [k for k,v in Counter(listOfAllFilenames).items() if v>1] # Produces a list of all duplicated filenames
    dupes = []
    for d in duplicateFilenames:
        dupes.append(DupeFile(d))
    
    listOfUniqueFiles = []   
    for dupe in dupes:
        dupe.GetLocations(filePaths)
        listOfUniqueFiles.append(dupe.GetUniqueFiles())
    return listOfUniqueFiles