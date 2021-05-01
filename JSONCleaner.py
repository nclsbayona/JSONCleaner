import json
import sys
from os.path import isdir, exists, join
from os import listdir


# Format either the whole folder or one file
def FormatJSON(path):
    if (isdir(path)):
        elements=listdir(path)
        for file_name in (elements):
            file_path=join(path, file_name)
            if (isdir(file_path)):
                formatJson(file_path)
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
                formatJson(file_path)
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
        operation=str(sys.argv[1])
        path=str(sys.argv[2])
        if (not path or not exists(path)):
            raise EOFError
        if (operation == "-d" or operation == "-f"):
            for (path) in (sys.argv[2:]):
                if operation == "-d":
                    DeFormatJSON(path)
                elif operation == "-f":
                    FormatJSON(path)
        else:
            raise IndexError
    except:
        print("Invalid usage!\n\nUsage: 'JSONCleaner.py -f/-d Path(s)'\n\t'-f' is for formatting the file/files in a directory\n\t'-d' is for de-formatting the file/files in a directory")
