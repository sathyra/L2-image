# Import the required module for text 
# to speech conversion

from PIL import Image
from pytesseract import pytesseract
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\ADMIN\Downloads\rohitmantri_intern_project1-1628106430-rohit0207\rohitmantri_intern_project1\imagetext.jpg"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract


# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)


  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=text, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
os.system("welcome.mp3")

  
# Playing the converted file
#os.system("mpg321 welcome.mp3")