import os
import uuid


class RandomRename:

    def __init__(self, paths, extensions=None, prefixes=None):
        self.extensions = extensions or []
        self.prefixes = prefixes
        self.paths = paths

        if prefixes and paths:
            if len(prefixes) != 1 and len(prefixes) > len(paths):
                raise Exception("The number of prefixes can either be 1 or the same with the number of paths")

        accepted_file_type = self.get_path_type(paths[0])

        for i, path in enumerate(paths):
            if path == '.':
                self.paths[i] = os.getcwd()

            if self.get_path_type(path) != accepted_file_type:
                raise Exception('You cannot mix files and paths together')

        # extensions cannot exit where the path is a file or are files
        if extensions and accepted_file_type == 1:
            raise Exception('You cannot provide extensions if you only want to rename one file')

    def get_path_type(self, path):
        return 0 if os.path.isdir(path) else 1

    def has_trailing_slash(self, path):
        return path[len(path) -1] == '/'

    def has_trailing_special_character(self, prefix):
        return prefix[len(prefix) - 1] in ['-', '_', '.', '!', '@', '#', '$', '%', '^', '*', '&', '+', ';', ',', '<', '>']

    def get_files(self, path):
        files = []
        try:
            files = os.listdir(path)
        except Exception as e:
            raise e
        return files

    def get_extension(self, _file):
        try:
            return os.path.splitext(_file)[1]
        except Exception as e:
            raise e

    def find_by_extension(self, files,  extensions):
        required = []
        for _file in files:
            file_extension = self.get_extension(_file)
            if file_extension in extensions:
                required.append(_file)
        return required

    def rename_files(self):
        try:
            for i, path in enumerate(self.paths):
                path_type = self.get_path_type(path)

                if path_type == 1:      # if it is a file
                    extension = self.get_extension(os.path.basename(path))
                    new_name = '{}{}'.format(uuid.uuid4(), extension)
                    if self.prefixes:
                        # loop if there are more than one prefixes provided, else, just use the only one existing
                        prefix = self.prefixes[i] if len(self.prefixes) > 1 else self.prefixes[0]
                        if not self.has_trailing_special_character(prefix):
                            prefix = prefix + '_'
                        new_name = prefix + new_name

                    os.rename(path, os.path.dirname(path) + '/' + new_name)

                else:
                    if self.extensions:
                        files = self.find_by_extension(self.get_files(path), self.extensions)
                    else:
                        files = self.get_files(path)

                    for _file in files:
                        extension = self.get_extension(_file)
                        new_name = "{}{}".format(uuid.uuid4(), extension)

                        if self.prefixes:
                            prefix = self.prefixes[i]
                            if not self.has_trailing_special_character(prefix):
                                prefix = prefix + '_'
                            new_name = prefix + new_name

                        path = path
                        if not self.has_trailing_slash(path):
                            path = path + '/'

                        os.rename(path + _file, path + new_name)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    r = RandomRename('werwer')
    print(r.get_path_type('/Users/dejiatoyebi/Documents/Rave-V2/src/components/dashboard/payout'))
    