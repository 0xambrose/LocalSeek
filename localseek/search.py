import os
import fnmatch
import re


class FileSearcher:
    def __init__(self, root_path="."):
        self.root_path = root_path

    def _should_skip_file(self, filename, file_ext_filter=None):
        if file_ext_filter:
            _, ext = os.path.splitext(filename)
            return ext.lower() not in [f".{f.lower()}" for f in file_ext_filter]
        return False

    def search_by_name(self, pattern, file_ext_filter=None):
        matches = []
        for root, dirs, files in os.walk(self.root_path):
            for filename in files:
                if self._should_skip_file(filename, file_ext_filter):
                    continue
                if fnmatch.fnmatch(filename.lower(), pattern.lower()):
                    full_path = os.path.join(root, filename)
                    matches.append(full_path)
        return matches

    def search_content(self, pattern, use_regex=False, file_ext_filter=None):
        matches = []
        compiled_pattern = None

        if use_regex:
            try:
                compiled_pattern = re.compile(pattern, re.IGNORECASE)
            except re.error:
                return []

        for root, dirs, files in os.walk(self.root_path):
            for filename in files:
                if self._should_skip_file(filename, file_ext_filter):
                    continue
                full_path = os.path.join(root, filename)
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        if use_regex and compiled_pattern:
                            for line_num, line in enumerate(f, 1):
                                if compiled_pattern.search(line):
                                    matches.append((full_path, line_num, line.strip()))
                        else:
                            for line_num, line in enumerate(f, 1):
                                if pattern.lower() in line.lower():
                                    matches.append((full_path, line_num, line.strip()))
                except (IOError, UnicodeDecodeError):
                    continue
        return matches