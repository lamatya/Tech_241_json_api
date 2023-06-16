import json
import os
import sys
import yaml

# checking there is a file name passed

if len(sys.argv) > 1:
    # opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    #failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
else:
    print("usage: json2yaml.py <source_file.json> [target_file.yaml]")

# processing the conversation

output = yaml.dump(source_content)

# if no target file send to stdout

if len(sys.argv) < 3:
    print(output)
# if the target file already exists exit

elif os.path.exists(sys.argv[2]):
    print("ERROR: " + sys.argv[2] + "already exists")
    exit(1)
# otherwise write to the specified file

else:
    target_file = open(sys.argv[2], "w")
    target_file.write(output)
    target_file.close()




