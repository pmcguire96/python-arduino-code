import pyautogui
from time import sleep

PICPATH = 'C:\\Users\\SciAps\\Documents\\pythonFiles\\automationScreenshots\\'
ANALYZE = 'Capture1.PNG'
DATAENTRY = 'Capture3.PNG'
KEYBOARD = 'Capture4.PNG'
KEYBOARD_ALT = 'Capture4a.PNG'
START = 'Capture7.PNG'
CLEAR = 'Capture8.PNG'
ENTER = 'Capture9.PNG'
DONESIGN = 'Capture10.PNG'
MAX_WAIT = 120

def findAltOnScreen(buttonFile, altFile):
  pic1 = PICPATH + buttonFile
  pic2 = PICPATH + altFile
  standards = 1.0 # accuracy
  ret = False
  while not ret:
    try:
      x, y = pyautogui.locateCenterOnScreen(pic1, confidence = standards)
      ret = True
    except Exception as e:
      try:
        x, y = pyautogui.locateCenterOnScreen(pic2, confidence = standards)
        print("found alt image!")
        ret = True
      except Exception as e:
        sleep(.2)
        standards = standards * .9
        if standards < .5:
          print("Trouble finding %s or its alt"%buttonFile)
          return -1, -1
  return x, y

def findOnScreen(buttonFile):
  pic = PICPATH + buttonFile
  ret = False
  standards = 1.0
  while not ret:
    try:
      x, y = pyautogui.locateCenterOnScreen(pic, confidence = standards)
      ret = True
    except Exception as e:
      sleep(.2)
      standards = standards * .9
      if standards < .5:
        print("Trouble finding %s"%buttonFile)
        return -1, -1
  return x, y

def waitFor(buttonFile):
  x, y = findOnScreen(buttonFile)
  i = 0
  while -1 == x and i < MAX_WAIT:
    sleep(1)
    x, y = findOnScreen(buttonFile)
    i = i+1
  if i == MAX_WAIT:
    return False
  else:
    return True

def clickButton(buttonFile):
  success = False
  try:
    sleep(.2)
    x, y = findOnScreen(buttonFile)
    pyautogui.click(x, y)
    success = True
  except Exception as e:
    print(e)
  return success

def fancyPrint(char):
  pyautogui.keyUp('shift')
  #print(char)
  if char.isnumeric() or char.islower():
    pyautogui.hotkey(char)
    #print("Not upper")
  elif char.isupper():
    #print("Upper")
    pyautogui.keyDown('shift')
    pyautogui.hotkey(char.lower())
    pyautogui.keyUp('shift')
    pyautogui.press('shift')
  #else:
    #print("Other")
    

def clickAnalyze():
  return clickButton(ANALYZE)

def clickDataEntry():
  return clickButton(DATAENTRY)

def enterData(sampleName):
  x, y = findAltOnScreen(KEYBOARD, KEYBOARD_ALT)
  pyautogui.click(x + 115, y)
  success = clickButton(CLEAR)
  if success:
    for c in sampleName:
      fancyPrint(c)
    return True
  else:
    return False

def clickStart():
  return clickButton(START)

def XRFStart(sampleList):
  working = clickAnalyze()
  if working:
    working = clickDataEntry()
  if working:
    for sample in sampleList:
      working = XRFCycle(sample)
      if not working:
        print("An error occured")
        break

def XRFCycle(sampleName):
  working = enterData(sampleName)
  if working:
    working = clickStart()
    sleep(.5)
    pyautogui.hotkey('enter')
  if not working:
    print("There was an error")
    return False
  else:
    sleep(3)
    if waitFor(DONESIGN):
      pyautogui.hotkey('enter')
      print("Everything fine w/ %s"%sampleName)
    else:
      print("Timed out on %s"%sampleName)
      return False
    return True

if __name__ == '__main__':
  testList = ["TestA1","TestB1","TestC1"]
  XRFStart(testList)
  #XRFCycle("Test1")