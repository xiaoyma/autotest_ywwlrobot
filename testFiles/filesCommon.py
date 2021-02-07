import os

class filesCommon():
    def getFilePath(self):
        path = os.path.dirname(__file__)
        return path