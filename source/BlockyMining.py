from AppInventorFileReader import AppInventorFileReader
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--source', type=str, default = 'appinventor') #options: appinventor
parser.add_argument('--database', type=str, default = 'none') #options: none or mysql
parser.add_argument('--path', type=str, default = '.') #options: current directory or valid path
args = parser.parse_args()

print(args.source)
print(args.database)
print(args.path)

if args.source == "appinventor":
  AppInventorFileReader.readFiles(args.path, args.database)
