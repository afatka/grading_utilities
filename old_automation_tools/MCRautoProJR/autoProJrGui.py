"""
Script to create a GUI in Autodesk Maya to hold supplimental grading tool: AutoProfessionalism



Created By: Adam Fatka
adam.fatka@gmail.com
www.fatkaforce.com

The values in the GUI are objects that are flagged compared to total objects that may be effected.

for example.

Pivots: 1 50%

in this case there is one pivot off center in a scene where two objects with pivots exist (two transform nodes)

"""
#import Maya commands as mel.
import maya.cmds as mel
import maya.cmds as cmds
#imports professionalism functions
from MCRautoProJR import autoProJr as apj


#debugging log
def log(message, prefix = 'Debug', hush=False):
    if not hush:
        print("%s : %s " % (prefix,message))

#This function creates the GUI for the autoProGui Supplemental
def autoProJrGui():
    
    
    if mel.window('autoProJrGuiWindow', exists=1):
        mel.deleteUI('autoProJrGuiWindow', window = 1)
   
    window = mel.window('autoProJrGuiWindow', title = 'autoProJr Supplemental Beta' , iconName = 'autoProJr',)
    mel.scrollLayout(width = 325, height = 670)
    mel.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=300 )
    mel.rowLayout( 'progressRowLayout', numberOfColumns=1, height = 20)
    mel.progressBar("autoProJrProgress", maxValue=14, width=300, visible = 0, enableBackground = True)
    mel.setParent('..')
    mel.rowLayout('autoProJrStatusRowLayout', numberOfColumns=1, height = 20)
    mel.text("autoProJrStatus", label = "Awaiting Command", width=300, visible = 1, enableBackground = True)
    mel.setParent('..')
    mel.rowLayout( numberOfColumns=4, columnWidth4=(75,50,75,50), columnAlign=[(1, 'right'),(3, 'right')], columnAttach4=('left', 'left', 'right', 'right'), height = 20)
    mel.text('yearMonthText', label = "Year/Month", align = 'center')
    mel.textField("yearMonthTextField", text = "####")
    mel.text('projectNumsText', label ="Project", align='center')
    mel.textField("projectNumsTextField", text = "##")
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), height = 25)
    mel.button("runAutoProJrButton", label = "Run AutoProJr", command =runAutoProJr)
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(75, 50), adjustableColumn=1, columnAttach2= ('left', 'right'))
    mel.text(label = "Total Nodes: ")
    mel.textField('totalObjectsTextField', text = "####", font = 'boldLabelFont', editable=False, enableBackground = True)
    mel.setParent('..')
    mel.setParent('..')
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), height = 25)
    #This button resets the GUI but is invisible do to accidental pressing concerns. 
    mel.textField('approvedOrNot', text = "       **PENDING**", font = 'boldLabelFont', editable=False, enableBackground=True)
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(75, 50), adjustableColumn=1, columnAttach2= ('left', 'right'))
    mel.text(label = " Total Objects: ")
    mel.textField('totalShapeObjectsTextField', text = "####", font = 'boldLabelFont', editable=False, enableBackground = True)
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(150, 65), adjustableColumn = 1, columnAttach2= ('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)   
    mel.text(label='File Named Properly:')
    mel.textField('fileNamedTextField', text = '#NULL#', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.textField('studentFileNameTextField', text = '#Student_Joe_MCR_####_Project0#.ma#', font = 'boldLabelFont', editable = False, enableBackground = True)
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Default Names: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (60,25,65), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = defNamSel )
    mel.textField('notNamedTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('notNamedPercentTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Master/Sub Groups: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (60,25,65), adjustableColumn = 1, columnAttach3 = ('left','both','right'), height = 25)
    mel.button(label = 'Outlnr', command = apj.outlinerWin)
    mel.textField(visible = False)
    mel.textField('groupedTextField', text = '#NULL#', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.textField('masterNodeTextField', text = "#[u'masterNode']#", font = 'boldLabelFont', editable = False, enableBackground = True, visible=False)
    mel.textField('subGroupTextField', text = "#[u'subGroups']#", font = 'boldLabelFont', editable = False, enableBackground = True, visible=False)
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Display Layers: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (60,25,65), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = visLayerSel)
    mel.textField('notLayeredTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('notLayeredPercentTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Transforms: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (60,25,65), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(25,25), adjustableColumn =1, columnAttach2 = ('left', 'right'), height = 25)
    mel.button(label = 'Sel', command = notFrozeSel)
    mel.button(label = 'Sprd', command = openSpreadSheet)
    mel.setParent('..')
    mel.textField('notFrozenTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('notFrozenPercentTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Construction History: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (60,25,65), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = withHisSel)
    mel.textField('withHistoryTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('withHistoryPercentTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Pivots: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (60,25,65), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = notCentSel)
    mel.textField('notCenteredTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('notCenteredPercentTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Additional Tools: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (60,25,65), adjustableColumn = 1, columnAttach3 = ('left','both','right'), height = 25)
    mel.button(label = 'Count', command = countTool)
    mel.textField(visible = False)
    mel.textField("countTextField", text = '#NULL#', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'N-gon Objects: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (60,25,65), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = nGonSelect)
    mel.textField('totalNgonObjectsTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('ngonPercentTextField', text = '##', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(150, 65), adjustableColumn = 1, columnAttach2= ('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)   
    mel.text(label='Total N-gons:')
    mel.textField('totalNgonsTextField', text = '#NULL#', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), height = 25)
    mel.button("resetGUI", label = "Clear GUI", command =resetValue)
    mel.setParent('..')
    
    if mel.dockControl('autoProJrDock', query=1, exists=1):
        mel.deleteUI('autoProJrDock', control = True)
        
    mel.dockControl('autoProJrDock',label='autoProJr Beta', content='autoProJrGuiWindow', floating = True, enablePopupOption = True, area = 'left' )   
    #mel.showWindow('autoProJrGuiWindow')
 
 
#This function updates yearMonth and projNum
def updateNameVars():
    global yearMonth
    global projNum
    yearMonth = mel.textField("yearMonthTextField", query = 1, text = 1)
    if len(yearMonth)!= 4:
        mel.progressBar('autoProJrProgress', edit = 1, visible=0)
        statusUpdate('self', 'year/month needs to be 4 digits')
        mel.error("Year/Month needs to be 4 digits. The two digit year and two digit month (i.e. 1109)")
    try:
        int(yearMonth)
    except ValueError:
        mel.progressBar('autoProJrProgress', edit = 1, visible=0)
        statusUpdate('self', 'year/Month must be an integer')
        mel.error("Year/Month needs to be an integer")
    projNum = mel.textField("projectNumsTextField", query = 1, text = 1)
    if len(projNum) !=2:
        mel.progressBar('autoProJrProgress', edit = 1, visible=0)
        statusUpdate('self', 'Project Number needs to be 2 digits')
        mel.error("Project Number needs to be 2 digits. (i.e. 02)")
    try:
        int(projNum)
    except ValueError:
        mel.progressBar('autoProJrProgress', edit = 1, visible=0)
        statusUpdate('self', 'Project Number needs to be an integer')
        mel.error("Project Number needs to be an integer")

  
def runAutoProJr(self):
    global approveCount
    approveCount=0
    print ("approveCount = " + str(approveCount))
    
    statusUpdate(self, 'Starting AutoProJr')
    #reset textField values to default for error detection reasons
    resetValue(self)
    mel.progressBar('autoProJrProgress', edit = 1, visible=1)
    statusUpdate(self, 'Optimizing Scene')
    import maya.mel as mm
    mm.eval('source cleanupScene.mel')
    mm.eval('performCleanUpSceneForEverything')
    statusUpdate(self, 'Finished Optimizing Scene')
    addProgress()
    
    #collect display layers
    display_Layers = apj.find_layers()
    #collect the state of display layers
    display_layers_state = apj.collect_layer_state(display_Layers)
    #hide layers
    apj.hide_all_layers(display_Layers)
    
    #progressWindow()
    #Check to see if a file is loaded
    statusUpdate(self, 'Query Scene Load')
    if not (mel.file(query=1, sceneName=1)):
        mel.progressBar('autoProJrProgress', edit = 1, visible=0)
        statusUpdate(self, 'No file loaded. Please load a file.')
        mel.error("No file loaded. Please load a file")
    #update name variables
    updateNameVars()
    addProgress()
    statusUpdate(self, 'Name Variables Verified')
    
    statusUpdate(self, 'Checking File Name')
    #check the name and edit the GUI accordingly.
    nameCheck = apj.nameCheck(yearMonth, projNum)
    mel.textField("studentFileNameTextField", edit = True, text = nameCheck[1])
    if(nameCheck[0]):
        mel.textField("fileNamedTextField", edit=True, text = "Approved", backgroundColor = apj.bgColor(0))
        approveCount += 1
        print ("approveCount = " + str(approveCount))
    else:
        mel.textField("fileNamedTextField", edit = True, text = "Resubmit", backgroundColor = apj.bgColor(100))
    addProgress()
    statusUpdate(self, 'Name Check Complete')
    
    statusUpdate(self, 'Gathering Nodes')
    #Load the assemblie nodes minus cameras  
    masterNodes = apj.masterGroup()
    #sort to capture all children nodes as well as main assembly nodes
    allNodes = apj.nodeCollect(masterNodes)
    nodes= []
    addProgress()
    statusUpdate(self, 'Nodes Collected')
    
    statusUpdate(self, 'PolySurfaceShape Work Around')
    #this is a bit of a hack to get around the polySurfaceShape node that is created when an object has history
    for tempNode in allNodes:
        if 'polySurfaceShape' not in tempNode:
            nodes.append(tempNode)
    addProgress()
    statusUpdate(self, 'Work Around Complete')
    
    statusUpdate(self, 'Calculating Node Quantities')
    #calculate total nodes and place in GUI
    totalNodes = len(nodes)
    transformNodes = apj.listCollect(nodes, 'transform')    
    visiNodes = apj.listCollect(nodes, 'mesh')
    totalShape = len(visiNodes)
    totalTrans = len(transformNodes)
    mel.textField("totalObjectsTextField", edit=1, text=totalTrans)
    mel.textField("totalShapeObjectsTextField", edit=1, text = totalShape)
    addProgress()
    statusUpdate(self, 'Node Quantities Complete')
    
    statusUpdate(self, 'Comparing Default Names')
    #compare geometry names to defualt name list and calculate and populate GUI fields
    global defaultNames
    defaultNames = apj.defaultCompare(transformNodes)
    mel.textField("notNamedTextField", edit=1, text=len(defaultNames))
    #modify for approved/not approved paradigm.
    if((len(defaultNames) <3)):
        percentDefaultNames = "Approved"
        notNamedColor = apj.bgColor(0)
        approveCount += 1
        print ("approveCount = " + str(approveCount))
    else:
        percentDefaultNames = "Resubmit"
        notNamedColor = apj.bgColor(99)
    ## notNamedPercent = int((float(len(defaultNames))/float(totalTrans))*100.0)
    ## percentDefaultNames = (str(notNamedPercent) + "%")
    ## notNamedColor = apj.bgColor(notNamedPercent)
    mel.textField("notNamedPercentTextField", edit=1, text=percentDefaultNames, backgroundColor = notNamedColor)
    addProgress()
    statusUpdate(self, 'Default Names Compared')
    
    statusUpdate(self, 'Checking Master Group')
    #Check to master Group node and subGroups
    subGroups = apj.subGroups(masterNodes)
    if ((len(masterNodes)) ==1) and subGroups != False:
        mel.textField("groupedTextField", edit=True, text = "Approved", backgroundColor = (0.0, 0.8, 0.0))
        approveCount += 1
        print ("approveCount = " + str(approveCount))
    else:
        mel.textField("groupedTextField", edit = True, text = "Resubmit", backgroundColor = (0.8, 0.0, 0.0))
    mel.textField("masterNodeTextField", edit = True, text = str(masterNodes))
    mel.textField("subGroupTextField", edit=True, text = str(subGroups))
    #checks to see if there are subGroups
    
    addProgress()
    statusUpdate(self, 'Master Group and SubGroups Checked')
    
    statusUpdate(self, 'Checking Display Layers')
    #Checks for geometry to be in display layer and updates GUI
    displayLayers = mel.layout('LayerEditorDisplayLayerLayout', query = 1, childArray =1)
    visibleLayer = []
    if displayLayers != None:
        for dLayer in displayLayers:
            if mel.objExists(dLayer):
                if(mel.getAttr('%s.visibility' % dLayer)):
                    visibleLayer.append(dLayer)
    for layer in visibleLayer:
        mel.setAttr('%s.visibility' % layer, 0)
    global notLayered
    notLayeredLocal = []
    for node in visiNodes:
        if (apj.visibleTest(node)):
            notLayeredLocal.append(node)
    if displayLayers != None:       
        for layer2 in visibleLayer:
            mel.setAttr('%s.visibility' % layer2, 1)
    notLayered = notLayeredLocal
    mel.textField("notLayeredTextField", edit = 1, text = len(notLayered))
    #modify for approved/not approved paradigm.
    if((len(notLayered) <3)):
        percentNotLayer = "Approved"
        notLayeredColor = apj.bgColor(0)
        approveCount += 1
        print ("approveCount = " + str(approveCount))
    else:
        percentNotLayer = "Resubmit"
        notLayeredColor = apj.bgColor(99)
    ## notLayerPercent = int((float(len(notLayered))/float(len(visiNodes)))*100.0)
    ## percentNotLayer = (str(notLayerPercent) + "%")
    ##  notLayeredColor = apj.bgColor(notLayerPercent)
    mel.textField("notLayeredPercentTextField", edit=1, text=percentNotLayer, backgroundColor = notLayeredColor)
    addProgress()
    statusUpdate(self, 'Display Layers Checked')
    
    statusUpdate(self, 'Checking Transforms')
    #Checks for frozen transforms.
    global notFroze
    notFroze = apj.spreadSheet(apj.listCollect(nodes, 'transform'))
    mel.textField("notFrozenTextField", edit= 1, text=len(notFroze))
    #modify for approved/not approved paradigm.
    if((len(notFroze) <3)):
        percentNotFroze = "Approved"
        notFrozeColor = apj.bgColor(0)
        approveCount += 1
        print ("approveCount = " + str(approveCount))
    else:
        percentNotFroze = "Resubmit"
        notFrozeColor = apj.bgColor(99)
    ## notFrozePercent = int((float(len(notFroze))/float(totalTrans))*100.00)
    ## percentNotFroze = (str(notFrozePercent) + "%")
    ## notFrozeColor = apj.bgColor(notFrozePercent)
    mel.textField("notFrozenPercentTextField", edit =1, text = percentNotFroze, backgroundColor = notFrozeColor)
    addProgress()
    statusUpdate(self, 'Transforms Checked')
    
    statusUpdate(self, 'Checking for History')
    #check for History
    global withHistory
    withHistory = apj.historyFinder(apj.listCollect(nodes, 'mesh'))
    mel.textField("withHistoryTextField", edit = 1, text = len(withHistory))
    #modify for approved/not approved paradigm.
    if((len(withHistory) <3)):
        percentWithHistory = "Approved"
        withHistoryColor = apj.bgColor(0)
        approveCount += 1
        print ("approveCount = " + str(approveCount))
    else:
        percentWithHistory = "Resubmit"
        withHistoryColor = apj.bgColor(99)
    ## withHistoryPercent = int((float(len(withHistory))/float(len(visiNodes)))*100.0)
    ## percentWithHistory = (str(withHistoryPercent) + "%")
    ## withHistoryColor = apj.bgColor(withHistoryPercent)
    mel.textField("withHistoryPercentTextField", edit=1, text=percentWithHistory, backgroundColor = withHistoryColor)
    addProgress()
    statusUpdate(self, 'History Checked')
    
    statusUpdate(self, 'Checking Pivots')
    #Check for pivots
    global notCentered
    notCentered = apj.centerPivot(apj.listCollect(nodes, 'transform'))
    mel.textField("notCenteredTextField", edit=1, text = len(notCentered))
    #modify for approved/not approved paradigm.
    if((len(notCentered) <3)):
        percentNotCentered = "Approved"
        notCenteredColor = apj.bgColor(0)
        approveCount += 1
        print ("approveCount = " + str(approveCount))
    else:
        percentNotCentered = "Resubmit"
        notCenteredColor = apj.bgColor(99)
    ## notCenteredPercent = int((float(len(notCentered))/float(totalTrans))*100.0)
    ## percentNotCentered = (str(notCenteredPercent) + "%")
    ## notCenteredColor = apj.bgColor(notCenteredPercent)
    mel.textField("notCenteredPercentTextField", edit = 1, text = percentNotCentered, backgroundColor = notCenteredColor)
    addProgress()
    statusUpdate(self, 'Pivots Checked')
    
    statusUpdate(self, 'Testing N-gons')
    #Test N-gons
    global nGonList
    nGonList = apj.nGonFinder(allNodes)
    nGonPercent = int((float(len(nGonList[0]))/float(len(visiNodes)))*100.0)
    percentNGons = (str(nGonPercent) + "%")
    nGonColor = apj.bgColor(nGonPercent)
    mel.textField("totalNgonObjectsTextField", edit =1, text = len(nGonList[0]))
    mel.textField("ngonPercentTextField", edit = 1, text = percentNGons , backgroundColor = nGonColor)
    mel.textField("totalNgonsTextField", edit =1, text = len(nGonList[1]))
    addProgress()
    statusUpdate(self, 'N-gons Complete')
        
    statusUpdate(self, 'Tool Completed')
    mel.rowLayout( 'progressRowLayout', edit = 1, visible = 0)
    mel.rowLayout('autoProJrStatusRowLayout', edit =1, visible = 0)
    
    if(approveCount >=5):
        mel.textField("approvedOrNot", edit=True, text = "       **Approved**", backgroundColor = apj.bgColor(0))
    else:
        mel.textField("approvedOrNot", edit = True, text = "       **Resubmit**", backgroundColor = apj.bgColor(100))
        
    apj.set_layers_visibility(display_Layers, display_layers_state)




def countTool(self):
    temp = str(apj.count(apj.selected()))
    mel.textField("countTextField", edit=1, text = temp)
    
def nGonSelect(self):
    apj.sel(nGonList[0])
    
def defNamSel(self):
    apj.sel(defaultNames)

def visLayerSel(self):
    apj.sel(notLayered)

def notFrozeSel(self):
    apj.sel(notFroze)
    
def openSpreadSheet(self):
    apj.sel(notFroze)
    apj.spreadSheetWin(self)

def withHisSel(self):
    apj.sel(withHistory)

def notCentSel(self):
    apj.sel(notCentered)
 
def resetGUI(self):
    yrMnth = yearMonth
    prjNm = projNum
    autoProJrGui()
    mel.textField("yearMonthTextField", edit=1, text = yrMnth)
    mel.textField("projectNumsTextField", edit=1, text = prjNm)
    
def resetValue(self):
    defaultNames = []
    notLayered = []
    notFroze = []
    withHistory = []
    notCentered = []
    nGonList = []
    log("reset approveCount")
    approveCount = 0
    print ("approveCount = " + str(approveCount))
    mel.rowLayout( 'progressRowLayout', edit = 1, visible=1)
    mel.progressBar("autoProJrProgress", edit=1,progress = 0)
    mel.rowLayout('autoProJrStatusRowLayout', edit =1, visible = 1)
    mel.textField('approvedOrNot', edit=1, text="       **PENDING**", backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('totalObjectsTextField', edit = 1, text = "##")
    mel.textField('totalShapeObjectsTextField', edit = 1, text = "##")
    mel.textField('fileNamedTextField', edit = 1, text = '#NULL#' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('studentFileNameTextField', edit = 1, text = '#Student_Joe_MCR_####_Project0#.ma#')
    mel.textField('notNamedTextField', edit = 1, text = '##' )
    mel.textField('notNamedPercentTextField', edit = 1, text = '##' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('groupedTextField', edit = 1, text = '#NULL#' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('masterNodeTextField', edit = 1, text = "#[u'masterNode']#")
    mel.textField('notLayeredTextField', edit = 1, text = '##' )
    mel.textField('notLayeredPercentTextField', edit = 1, text = '##' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('notFrozenTextField', edit = 1, text = '##' )
    mel.textField('notFrozenPercentTextField', edit = 1, text = '##' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('withHistoryTextField', edit = 1, text = '##' )
    mel.textField('withHistoryPercentTextField', edit = 1, text = '##' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('notCenteredTextField', edit = 1, text = '##' )
    mel.textField('notCenteredPercentTextField', edit = 1, text = '##' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField("countTextField", edit = 1, text = '#NULL#' )
    mel.textField('totalNgonObjectsTextField', edit = 1, text = '##' )
    mel.textField('ngonPercentTextField', edit = 1, text = '##', backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('totalNgonsTextField', edit = 1, text = '#NULL#' )

        
        
        


 
    
    
def addProgress():
    mel.progressBar("autoProJrProgress", edit=True, step=1)
    if (mel.progressBar("autoProJrProgress", query=1, progress=1)) == mel.progressBar("autoProJrProgress", query =1, maxValue =1):
        mel.progressBar('autoProJrProgress', edit = 1, visible=0)

def statusUpdate(self, message):
    mel.text('autoProJrStatus', edit =1, label = message)
    print message



##launch GUI
autoProJrGui()


    
#if the necessary global variables don't exist. create them
try:
    if(yearMonth):
        mel.textField("yearMonthTextField", edit=1, text = yearMonth)
        mel.textField("projectNumsTextField", edit=1, text = projNum)
except NameError:
    yearMonth = "####"
    projNum = "##"
    
try:
    if(defaultNames):
        pass
except NameError:
    defaultNames = []
    notLayered = []
    notFroze = []
    withHistory = []
    notCentered = []
    nGonList = []
    geoNames = []
    geoLayered = []
    transFroze = []
    histDel = [] 
    pivotCenter = []
    approveCount = 0
