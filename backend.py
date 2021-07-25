from pathlib import Path
import os


class PathHolder:
    path = None

    @classmethod
    def getPath(cls):
        home = str(Path.home())
        dirPath = os.path.join(home, 'Documents', 'ToDoList')
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)
        filePath = os.path.join(dirPath, 'zadania.txt')
        cls.path = filePath


class Save:
    @staticmethod
    def saveFile(taskList):
        fileList = [task.get() for task in taskList]
        with open(PathHolder.path, 'w') as fileObject:
            fileObject.write('\n'.join(fileList))


class Read:
    @staticmethod
    def readFile():
        try:
            with open(PathHolder.path, 'r') as fileObject:
                fileList = fileObject.readlines()
            fileList = [task for task in fileList if not task.__eq__('\n')]
            fileList = [task.removesuffix('\n') for task in fileList]
            return fileList
        except FileNotFoundError:
            with open(PathHolder.path, 'w') as fileObject:
                fileObject.close()
            return Read.readFile()

