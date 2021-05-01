import json
import sys
from os.path import isdir, exists, join
from os import listdir
import argparse


# Format either the whole folder or one file
def FormatJSON(path):
    if (isdir(path)):
        elements=listdir(path)
        for file_name in (elements):
            file_path=join(path, file_name)
            if (isdir(file_path)):
                FormatJSON(file_path)
            else:
                JSONfile = json.load(open(file_path, "r"))
                with open(file_path, 'w') as f:
                    f.write(json.dumps(JSONfile, indent=4 * ' '))
                print("Formatted %s" % (file_path))
    else:
        JSONfile = json.load(open(path, "r"))
        with open(path, 'w') as f:
            f.write(json.dumps(JSONfile, indent=4 * ' '))
        print("Formatted %s" % (path))


# De-Pretty the JSON file
def DeFormatJSON(path):
    if (isdir(path)):
        elements=listdir(path)
        for file_name in (elements):
            file_path=join(path, file_name)
            if (isdir(file_path)):
                DeFormatJSON(file_path)
            else:
                JSONfile = json.load(open(file_path, "r"))
                with open(file_path, 'w') as f:
                    f.write(json.dumps(JSONfile, indent=None))
                print("De-Formatted %s" % (file_path))
    else:
        JSONfile = json.load(open(path, "r"))
        with open(path, 'w') as f:
            f.write(json.dumps(JSONfile, indent=None))
        print("De-Formatted %s" % (path))
    


if __name__ == "__main__":
    try:
        parser=argparse.ArgumentParser(description="Formats or De-formats a JSON file, or a group of JSON files.")
        parser.add_argument('-f','--format', help='Format the file/files in a directory', action="store_true")
        parser.add_argument('-d','--deformat', help="De-Format the file/files in a directory", action="store_true")
        parser.add_argument("Path",metavar="Path", type=str, help="Path or Paths to JSON file(s), or directories where to search for JSON files", nargs='+')
        arguments=parser.parse_args()
        if (arguments.format):
            for path in (arguments.Path):
                FormatJSON(path)
        if (arguments.deformat):
            for path in (arguments.Path):
                DeFormatJSON(path)

    except:
       print ("Invalid usage!")
