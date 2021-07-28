from pathlib import Path
import os
import json


class PathHolder:
    path = None

    @classmethod
    def getPath(cls):
        home = str(Path.home())
        dirPath = os.path.join(home, 'Documents', 'ToDoList')
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)
        filePath = os.path.join(dirPath, 'tasks.json')
        cls.path = filePath


class Save:
    @staticmethod
    def saveFile(taskList):
        fileList = [task.get() for task in taskList]
        with open(PathHolder.path, 'w') as fileObject:
            json.dump(fileList, fileObject, indent=1)


class Read:
    @staticmethod
    def readFile():
        try:
            with open(PathHolder.path, 'r') as fileObject:
                fileList = json.load(fileObject)
            return fileList
        except FileNotFoundError:
            with open(PathHolder.path, 'w') as fileObject:
                json.dump([], fileObject)
            return Read.readFile()
