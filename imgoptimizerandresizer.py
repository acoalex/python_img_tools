import os, shutil, sys
from PIL import Image

## README ##
## Instalar Python 3
## sudo python3 -m pip install mysql-connector
## sudo python3 -m pip install Pillow
##

QUALITY = 80
WIDTH = 800

def copyFile(file, path, qual):
    imgPath = os.getcwd() + os.sep +  "/".join(path)
    sourceFilePath = imgPath + os.sep + file
    if os.path.getsize(sourceFilePath) > 0:
        # Optimize img
        try:
            image = Image.open(sourceFilePath)
            if image.mode in ("RGBA", "P"): 
                return
                #try:
                #    image= image.convert("RGB")
                #except Error as e:     
                #    print(str(e))
                    
            print(sourceFilePath)
            wpercent = (WIDTH/float(image.size[0]))
            hsize = int((float(image.size[1])*float(wpercent)))
            image.resize((WIDTH, hsize), PIL.Image.ANTIALIAS)
            image.save(sourceFilePath,optimize=True,quality=qual)
        except ValueError as e:
            print("Error optimizing file: " + sourceFilePath)
            print (str(e))

def main():
    if len(sys.argv) == 1:
        sys.exit("Please pass absolute path of img folder")

    srcpath = sys.argv[1]
    quality = int(sys.argv[2]) if len(sys.argv) == 3 else QUALITY
    for root, dirs, files in os.walk(srcpath):
        path = root.split(os.sep)
        for file in files:
            if (file.endswith(".jpg") or file.endswith(".png")):
                copyFile(file, path, quality)

if __name__ == "__main__":
    main()
