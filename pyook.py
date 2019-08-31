import sys
import re
import bucket

def hurl(sick, bucket):
    pyook = "py"
    for chunk in sick:
        pyook += bucket[chunk]
        if chunk == " ":
            pyook += "py"
        else:
            pyook += "0"
    return pyook[:-1]+"k"

def pour(pyook, bucket):
    pyook = re.sub(r"([pP][yY])|([0]*[kK])", lambda x: '', pyook)
    return "".join([bucket[chunk] for chunk in re.compile(r"[0]+").split(pyook)])

def empty(pyook, bucket):
    bucket = {v:k for k,v in bucket.items()}
    return re.sub(r"([pP][yY])?[O0o]+[kK]", lambda x: pour(x.group(0), bucket), pyook)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Ni! Gimme PyOok!")
    else:
        pyook = " ".join(sys.argv[1:]).strip()
        if re.match(r"^(([pP][yY])?[O0o]+[kK]\s*)+$", pyook):
            print(empty(pyook, bucket.get()))
        elif re.match(r"^(([pP][yY])?\w+[kK]\s*)+$", pyook):
            print("I don't like the PyOok.")
        else:
            print(hurl(pyook.lower(), bucket.get()))
