def GetAllUniqueFiles(listOfDupes, listOfFiles):
    listOfDupeNames = []
    for d in listOfDupes:
        listOfDupeNames.append(d.filename)
    listOfAllUniqueFiles = [x for x in listOfFiles if x.filename not in listOfDupeNames]
    listOfAllUniqueFiles = listOfAllUniqueFiles + listOfDupes
    return listOfAllUniqueFiles