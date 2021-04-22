import os
import sys
import cv2
import numpy as np
import xml.etree.ElementTree as ET

ReSize = 512
InputDir = "./Img/"
OutFile = "./data.pbtxt"

for i in range(0,len(sys.argv)):
	if sys.argv[i] == "-in" or sys.argv[i] == "-I" :
		InputDir = sys.argv[i + 1]

ClassList = []
OutStr = ""

def AutoRead(InputDir) :
	FileList = os.listdir(InputDir)
	for File in FileList:
		if os.path.isdir(InputDir + File + "/") : 
			AutoRead(InputDir + File + "/")
		else :
			if File.find(".xml") != -1 :
				XmlData = ET.parse(InputDir + File)
				XmlData = XmlData.getroot()
				for ClassName in XmlData.findall('object') :
					if ClassName[0].text not in ClassList :
						ClassList.append(ClassName[0].text)
	ClassList.sort()
AutoRead(InputDir)
i = 1;
for ClassName in ClassList :
	OutStr += "item {\n\tid: " + str(i) + "\n\tname: '" + ClassName + "'\n}\n"
	i += 1
print(OutStr)
OutFile = open(OutFile, 'w')
OutFile.write(OutStr)
OutFile.close()
print("Pbtxt OK")