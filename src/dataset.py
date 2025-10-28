class Dataset():
    def __init__(self, *filePaths: str):
        self.filePaths = []
        for filePath in filePaths:
            self.filePaths.append(filePath)

    def divideData(filePath: str) -> (list[str], list[str]):
        pass

    def preprocessData(filePaths: list[str]) -> (list[str], list[str]):
        pass