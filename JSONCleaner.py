import json
import sys

# Make the JSON file pretty
def FormatJSONFile(PathToJSONFile):
    JSONfile = json.load(open(PathToJSONFile, "r"))
    with open(PathToJSONFile, 'w') as f:
        f.write(json.dumps(JSONfile, indent=4 * ' '))
    print("Formatted %s" % (PathToJSONFile))


# De-Pretty the JSON file
def DeFormatJSONFile(PathToJSONFile):
    JSONfile = json.load(open(PathToJSONFile, "r"))
    with open(PathToJSONFile, 'w') as f:
        f.write(json.dumps(JSONfile, indent=None))
    print("De-Formatted %s" % (PathToJSONFile))


if __name__ == "__main__":
    try:
        if str(sys.argv[1]) == "-d":
            DeFormatJSONFile(str(sys.argv[2]))
        if str(sys.argv[1]) == "-f":
            FormatJSONFile(str(sys.argv[2]))
    except:
        print("Invalid usage!\n\nUsage: 'JSONCleaner.py -f/-d PathToJSONFile'\n'-f' is for formatting the file and '-d' is for de-formatting the file.")
