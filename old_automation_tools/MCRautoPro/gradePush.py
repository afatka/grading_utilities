##This module handles pushing data into the gradeTool

#import maya commands
import maya.cmds as mel
#import stuff to make the intercommunication work
import __main__ as mn
import maya.cmds as cmds

#Push the file named correctly field
def pushNamed(self, boolean):
    if boolean ==True:
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
def pushSelfAss(self, boolean):
    if boolean ==True:
        mel.radioButtonGrp('saButGrp1', edit=1, select=1 )
        mn.proSAButton1()
    else:
        mel.radioButtonGrp('saButGrp1', edit=1, select=2 )
        mn.proSAButton1()
        
#Push the Geometry Named Field
def pushGeoNamed(self, boolean):
    if boolean ==True:
        mel.radioButtonGrp('onButGrp1', edit=1, select=1 )
        mn.proONButton1()
    else:
        mel.radioButtonGrp('onButGrp1', edit=1, select=2 )
        mn.proONButton1()
        
#push the geo grouped field
def pushGeoGrouped(self, boolean):
    if boolean ==True:
        mel.radioButtonGrp('ogButGrp1', edit=1, select=1 )
        mn.proOGButton1()
    else:
        mel.radioButtonGrp('ogButGrp1', edit=1, select=2 )
        mn.proOGButton1()
    
#push the geo layered field
def pushGeoLayered(self, boolean):
    if boolean ==True:
        mel.radioButtonGrp('olButGrp1', edit=1, select=1 )
        mn.proOLButton1()
    else:
        mel.radioButtonGrp('olButGrp1', edit=1, select=2 )
        mn.proOLButton1()
        
#push the transforms froze field
def pushTransFroze(self, boolean):
    if boolean== True:
        mel.radioButtonGrp('ftButGrp1', edit=1, select=1 )
        mn.proFTButton1()
    else:
        mel.radioButtonGrp('ftButGrp1', edit=1, select=2 )
        mn.proFTButton1()
        
#push the history deleted field
def pushHistoryDel(self, boolean):
    if boolean ==True:
        mel.radioButtonGrp('dhButGrp1', edit=1, select=1 )
        mn.proDHButton1()
    else:
        mel.radioButtonGrp('dhButGrp1', edit=1, select=2 )
        mn.proDHButton1()
        
#push the pivots centered field
def pushPivotsCenter(self, boolean):
    if boolean ==True:
        mel.radioButtonGrp('pcButGrp1', edit=1, select=1 )
        mn.proPCButton1()
    else:
        mel.radioButtonGrp('pcButGrp1', edit=1, select=2 )
        mn.proPCButton1()
        
        