##This module handles pushing data into the gradeTool

#import maya commands
import maya.cmds as mel
#import stuff to make the intercommunication work
import __main__ as mn
import maya.cmds as cmds

#this function takes a value and returns a row and radio button
def valueConvert(self, value):
    if (value==0):
        return "1", "1", "0"
    elif (1<=value<=2):
        return "1", "3", "0"
    elif (2<= value<=3):
        return "2", "1", "1"
    elif (4<= value <=10):
        return "2", "2", "1"
    elif (11<= value <=60):
        return "3", "2", "2"
    else:
        return "3", "3", "2"

def loadPush():
    try:
        print "LoadPush"
        print "1"
        global geoNames
        global geoLayered
        global transFroze
        global histDel
        global pivotCenter
        print "2"
        geoNames = [mn.proONButton1, mn.proONButton2, mn.proONButton3]
        print "3"
        geoLayered = [mn.proOLButton1, mn.proOLButton2, mn.proOLButton3]
        print "4"
        transFroze = [mn.proFTButton1, mn.proFTButton2, mn.proFTButton3]
        print "5"
        histDel = [mn.proDHButton1, mn.proDHButton2, mn.proDHButton3]
        print "6"
        pivotCenter = [mn.proPCButton1, mn.proPCButton2, mn.proPCButton3]
        print "7"
    except AttributeError:
        print "Push Functionality not loaded"

#Push the file named correctly field
def pushNamed(self, value):
    if value ==True:
        try:
            mel.radioButtonGrp('fnpButGrp1', edit=1, select= 1 )
            mn.proFNPButton1()
        except RuntimeError:
            mel.radioButtonGrp('snButGrp1', edit=1, select = 1 )
            mn.proSNButton1()
    else:
        try:
            mel.radioButtonGrp('fnpButGrp1', edit=1, select=2)
            mn.proFNPButton1()
        except RuntimeError:
            mel.radioButtonGrp('snButGrp1', edit=1, select = 2)
            mn.proSNButton1()
        
        
#Push the self assessment field
def pushSelfAss(self, value):
    if value ==True:
        mel.radioButtonGrp('saButGrp1', edit=1, select=1 )
        mn.proSAButton1()
    else:
        mel.radioButtonGrp('saButGrp1', edit=1, select=2 )
        mn.proSAButton1()
        
#Push the Geometry Named Field
def pushGeoNamed(self, value):
    grade = valueConvert('', value)
    mel.radioButtonGrp('onButGrp%s' % grade[0], edit=1, select=int(grade[1]))
    geoNames[int(grade[2])]()
    
          
#push the geo grouped field
def pushGeoGrouped(self, value):
    if value ==True:
        mel.radioButtonGrp('ogButGrp1', edit=1, select=1 )
        mn.proOGButton1()
    else:
        mel.radioButtonGrp('ogButGrp1', edit=1, select=2 )
        mn.proOGButton1()
    

#push the geo layered field
def pushGeoLayered(self, value):
    grade = valueConvert('', value)
    mel.radioButtonGrp('olButGrp%s' % grade[0], edit=1, select=int(grade[1]))
    geoLayered[int(grade[2])]()
        

#push the transforms froze field
def pushTransFroze(self, value):
    grade = valueConvert('', value)
    mel.radioButtonGrp('ftButGrp%s' % grade[0], edit=1, select=int(grade[1]))
    transFroze[int(grade[2])]()
   
    
#push the history deleted field
def pushHistoryDel(self, value):
    grade = valueConvert('', value)
    mel.radioButtonGrp('dhButGrp%s' % grade[0], edit=1, select=int(grade[1]))
    histDel[int(grade[2])]()
        
        
#push the pivots centered field
def pushPivotsCenter(self, value):
    grade = valueConvert('', value)
    mel.radioButtonGrp('pcButGrp%s' % grade[0], edit=1, select=int(grade[1]))
    pivotCenter[int(grade[2])]()
        
        