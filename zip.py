import zipfile
import os
import sys
import argparse


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n))


my_parser = argparse.ArgumentParser(
    prog=zip,
    description="ZIP files into parts divided equally by number of files instead of size",
)
my_parser.add_argument("path", type=str)
my_parser.add_argument("num", type=int)
args = my_parser.parse_args()
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))
# print ('How many files:')
# num_files=int(input())
# num_files = 4  #number of zip files to create

# print ('Path:')
# path = str(input())
# dir_to_zip = os.path.abspath("C:/ebayfeb/en_sg/x/ebayfeb/en_sg/rtarget/align")
num_files = args.num

dir_to_zip = os.path.abspath(args.path)

os.chdir(dir_to_zip)


files = os.listdir(dir_to_zip)

# [os.path.join(dir_to_zip,file) for file in

files_in_parts = list(split(files, num_files))

for i, zip_contents in enumerate(files_in_parts, 1):

    with zipfile.ZipFile("part%s.zip" % i, "w", zipfile.ZIP_DEFLATED) as zipf:
        for j in zip_contents:
            print("kompresuje ", j, "do", zipf.filename)
            zipdir(j, zipf)
        zipf.close()
