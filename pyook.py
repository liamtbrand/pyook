import sys
import re
import bucket

def hurl(sick, bucket):
    pyook = "py"
    for chunk in sick:
        pyook += bucket[chunk]
        if chunk == " ":
            pyook += "py"
    return pyook+"k"

def empty(pyook, bucket):
    bucket = {v:k for k,v in bucket.items()}
    ook = "".join(pyook.split("py"))
    ook = re.sub(r"[k]{1}", lambda x: '0k ', ook)
    ook = re.sub(r"\s+[0]+", lambda x: ' ', ook)
    ook = re.sub(r"[0]{2,}[k]\s+", lambda x: '0k ', ook)
    sick = ""
    while len(ook) != 0:
        for chunk in sorted(bucket.keys(),reverse=True):
            if ook.startswith(chunk):
                ook = ook[len(chunk):]
                sick += bucket[chunk]
                break
    return sick

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Ni! Gimme PyOok!")
    else:
        pyook = ""
        for word in sys.argv[1:]:
            pyook += word + " "
        pyook = pyook.strip()
        print("'"+pyook+"'")
        if re.match(r"^(([O0o]+)[kK]\s*)+$", pyook):
            print(empty(pyook, bucket.get()))
        elif re.match(r"^([pP][yY](\w+)[kK]\s*)+$", pyook):
            print("I don't like the PyOok.")
        else:
            print(hurl(pyook.lower(), bucket.get()))
