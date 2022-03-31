import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path1")
parser.add_argument("path2")
args = parser.parse_args()
path1 = args.path1
path2 = args.path2

def compare_dir_layout(dir1, dir2):
    def _compare_dir_layout(dir1, dir2):
        for (dirpath, dirnames, filenames) in os.walk(dir1):
            for dirname in dirnames:
                relative_path = dirpath.replace(dir1, "")
                if os.path.exists( dir2 + relative_path + '\\' +  dirname) == False:
                    print (relative_path, dirname)
        return

    print ('directiries in "' + dir1 + '" but not in "' + dir2 +'"')
    _compare_dir_layout(dir1, dir2)
    print ('directories in "' + dir2 + '" but not in "' + dir1 +'"')
    _compare_dir_layout(dir2, dir1)

compare_dir_layout(path1, path2)