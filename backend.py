class PathHolder:
    filePath = "C:\\Users\\Paweł\\Documents\\ToDoList\\xd.txt"


class Save:
    @staticmethod
    def saveFile(taskList):
        fileList = [task.get() for task in taskList]
        with open(PathHolder.filePath, 'w') as fileObject:
            fileObject.write('\n'.join(fileList))


class Read:
    @staticmethod
    def readFile():
        with open(PathHolder.filePath, 'r') as fileObject:
            fileList = fileObject.readlines()
        fileList = [task for task in fileList if not task.__eq__('\n')]
        # fileList = [task.removesuffix('\n') for task in fileList]
        return fileList

