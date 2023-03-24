import os
def deleteOldManifests():
    manifestFiles = []
    files = os.listdir("/home/ubuntu/XurTracker/src")
    print(files)
    for f in range(len(files)):
        if files[f].find(".content") != -1:
            manifestFiles.append(files[f])
    newestFile = manifestFiles[0]
    print(newestFile)
    newestFileTime = os.path.getctime(os.path.join("/home/ubuntu/XurTracker/src",manifestFiles[0]))

    #find the newest .content file in the dir
    for f in range(len(manifestFiles)): 
        fileCreatedTime = os.path.getctime(os.path.join("/home/ubuntu/XurTracker/src",manifestFiles[f]))
        if(fileCreatedTime > newestFileTime):
            newestFile = manifestFiles[f]
    
    #remove the newest file from the list of files to be deleted
    manifestFiles.remove(newestFile)

    #delete all old manifest files from the directory
    for f in range(len(manifestFiles)): 
        os.remove(os.path.join("/home/ubuntu/XurTracker/src",manifestFiles[f]))

deleteOldManifests()