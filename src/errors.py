class UnequalPrefixesAndPaths(Exception):
    def __init__(self):
        self.message = "There must be an equal number of prefixes and paths"
