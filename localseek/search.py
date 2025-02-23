import os
import fnmatch


class FileSearcher:
    def __init__(self, root_path="."):
        self.root_path = root_path

    def search_by_name(self, pattern):
        matches = []
        for root, dirs, files in os.walk(self.root_path):
            for filename in files:
                if fnmatch.fnmatch(filename.lower(), pattern.lower()):
                    full_path = os.path.join(root, filename)
                    matches.append(full_path)
        return matches