import os, shutil, sys

## README ##
## Instalar Python 3
## sudo python3 -m pip install mysql-connector
## sudo python3 -m pip install Pillow
##

def main():
    if len(sys.argv) == 1:
        sys.exit("Please pass absolute path of img folder")

    srcpath = sys.argv[1]
    for root, dirs, files in os.walk(srcpath):
        hasImage = False
        path = root.split(os.sep)
        print (root)
        
        for file in files:
            if (file.endswith(".jpg") or file.endswith(".png" or file.endswith(".webp"))):
                hasImage = True
        if (hasImage):
            print ("has image")
        else:
            print ("no image")
                
        if not hasImage and not dirs:
            shutil.rmtree(root)
            print ("delete folder:" + root)

if __name__ == "__main__":
    main()
