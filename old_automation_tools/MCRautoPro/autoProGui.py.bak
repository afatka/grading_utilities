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
#imports professionalism functions
from MCRautoPro import autoPro as ap
#imports grade pushing functions
from MCRautoPro import gradePushBoolean as gp
#import grade pushing for non-boolean buckets
from MCRautoPro import gradePushGradiant as gpg

#debugging log
def log(message, prefix = 'Debug', hush=False):
    if not hush:
        print("%s : %s " % (prefix,message))

#This function creates the GUI for the autoProGui Supplemental
def autoProGui():
    
    
    if mel.window('autoProGuiWindow', exists=1):
        mel.deleteUI('autoProGuiWindow', window = 1)
   
    window = mel.window('autoProGuiWindow', title = 'autoPro Supplemental v0.96' , iconName = 'autoPro',)
    mel.scrollLayout(width = 325, height = 800)
    mel.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=300 )
    mel.rowLayout( 'progressRowLayout', numberOfColumns=1, height = 20)
    mel.progressBar("autoProProgress", maxValue=14, width=300, visible = 0, enableBackground = True)
    mel.setParent('..')
    mel.rowLayout('autoProStatusRowLayout', numberOfColumns=1, height = 20)
    mel.text("autoProStatus", label = "Awaiting Command", width=300, visible = 1, enableBackground = True)
    mel.setParent('..')
    mel.rowLayout( numberOfColumns=4, columnWidth4=(75,50,75,50), columnAlign=[(1, 'right'),(3, 'right')], columnAttach4=('left', 'left', 'right', 'right'), height = 20)
    mel.text('yearMonthText', label = "Year/Month", align = 'center')
    mel.textField("yearMonthTextField", text = "0000")
    mel.text('projectNumsText', label ="Project", align='center')
    mel.textField("projectNumsTextField", text = "00")
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), height = 25)
    mel.button("runAutoProButton", label = "Run AutoPro", command =runAutoPro)
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(75, 50), adjustableColumn=1, columnAttach2= ('left', 'right'))
    mel.text(label = "Total Nodes: ")
    mel.textField('totalObjectsTextField', text = "####", font = 'boldLabelFont', editable=False, enableBackground = True)
    mel.setParent('..')
    mel.setParent('..')
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), height = 25)
    #This button resets the GUI but is invisible do to accidental pressing concerns. 
    mel.button("autoProGui", label = "Push Grades", command = pushGrades, visible = 0)
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(75, 50), adjustableColumn=1, columnAttach2= ('left', 'right'))
    mel.text(label = " Total Objects: ")
    mel.textField('totalShapeObjectsTextField', text = "####", font = 'boldLabelFont', editable=False, enableBackground = True)
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(150, 50), adjustableColumn = 1, columnAttach2= ('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)   
    mel.text(label='File nd Properly:')
    mel.textField('fileNamedTextField', text = '#NULL#', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.textField('studentFileNameTextField', text = '#Studnet_Joe_ProjectComponent0#_MCR_####.mb#', font = 'boldLabelFont', editable = False, enableBackground = True)
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Default Names: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (70,40,40), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = defNamSel )
    mel.textField('notNamedTextField', text = '####', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('notNamedPercentTextField', text = '##%', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Master/Sub Groups: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (70,30,50), adjustableColumn = 1, columnAttach3 = ('left','both','right'), height = 25)
    mel.button(label = 'Outlnr', command = ap.outlinerWin)
    mel.textField(visible = False)
    mel.textField('groupedTextField', text = '#NULL#', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.textField('masterNodeTextField', text = "#[u'masterNode']#", font = 'boldLabelFont', editable = False, enableBackground = True)
    mel.textField('subGroupTextField', text = "#[u'subGroups']#", font = 'boldLabelFont', editable = False, enableBackground = True)
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Display Layers: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (70,40,40), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = visLayerSel)
    mel.textField('notLayeredTextField', text = '####', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('notLayeredPercentTextField', text = '##%', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Transforms: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (70,40,40), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(25,25), adjustableColumn =1, columnAttach2 = ('left', 'right'), height = 25)
    mel.button(label = 'Sel', command = notFrozeSel)
    mel.button(label = 'Sprd', command = openSpreadSheet)
    mel.setParent('..')
    mel.textField('notFrozenTextField', text = '####', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('notFrozenPercentTextField', text = '##%', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Construction History: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (70,40,40), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = withHisSel)
    mel.textField('withHistoryTextField', text = '####', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('withHistoryPercentTextField', text = '##%', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Pivots: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (70,40,40), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = notCentSel)
    mel.textField('notCenteredTextField', text = '####', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('notCenteredPercentTextField', text = '##%', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.separator( height=5, style='in' )
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Additional Tools: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (70,30,50), adjustableColumn = 1, columnAttach3 = ('left','both','right'), height = 25)
    mel.button(label = 'Count', command = countTool)
    mel.textField(visible = False)
    mel.textField("countTextField", text = '#NULL#', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'N-gon Objects: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (70,40,40), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = nGonSelect)
    mel.textField('totalNgonObjectsTextField', text = '####', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('ngonPercentTextField', text = '##%', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(150, 50), adjustableColumn = 1, columnAttach2= ('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)   
    mel.text(label='Total N-gons:')
    mel.textField('totalNgonsTextField', text = '#NULL#', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Lamina Objects: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (70,40,40), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = laminaSelect)
    mel.textField('totalLaminaObjectsTextField', text = '####', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('laminaPercentTextField', text = '##%', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(150, 50), adjustableColumn = 1, columnAttach2= ('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)   
    mel.text(label='Total Lamina Faces:')
    mel.textField('totalLaminaTextField', text = '#NULL#', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.rowLayout(numberOfColumns = 2, columnWidth2 = (150, 150),adjustableColumn = 1,  columnAttach2=('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)
    mel.text(label = 'Tri Objects: ')
    mel.rowLayout(numberOfColumns = 3, columnWidth3 = (70,40,40), adjustableColumn = 1, columnAttach3 = ('left', 'both', 'right'), height = 25)
    mel.button(label = 'Select', command = triSelect)
    mel.textField('totalTriObjectsTextField', text = '####', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.textField('triPercentTextField', text = '##%', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    mel.rowLayout(numberOfColumns = 2, columnWidth2=(150, 50), adjustableColumn = 1, columnAttach2= ('left', 'right'), columnAlign2 = ('left', 'right'), height = 25)   
    mel.text(label='Total Tri Faces:')
    mel.textField('totalTriTextField', text = '#NULL#', font = 'boldLabelFont', editable = False, enableBackground = True )
    mel.setParent('..')
    mel.setParent('..')
    
    if mel.dockControl('autoProDock', query=1, exists=1):
        mel.deleteUI('autoProDock', control = True)
        
    mel.dockControl('autoProDock',label='autoPro v0.96', content='autoProGuiWindow', floating = True, enablePopupOption = True, area = 'left' )   
    #mel.showWindow('autoProGuiWindow')
 
 
#This function updates yearMonth and projNum
def updateNameVars():
    global yearMonth
    global projNum
    yearMonth = mel.textField("yearMonthTextField", query = 1, text = 1)
    if len(yearMonth)!= 4:
        mel.progressBar('autoProProgress', edit = 1, visible=0)
        statusUpdate('self', 'year/month needs to be 4 digits')
        mel.error("Year/Month needs to be 4 digits. The two digit year and two digit month (i.e. 1109)")
    try:
        int(yearMonth)
    except ValueError:
        mel.progressBar('autoProProgress', edit = 1, visible=0)
        statusUpdate('self', 'year/Month must be an integer')
        mel.error("Year/Month needs to be an integer")
    projNum = mel.textField("projectNumsTextField", query = 1, text = 1)
    if len(projNum) !=2:
        mel.progressBar('autoProProgress', edit = 1, visible=0)
        statusUpdate('self', 'Project Number needs to be 2 digits')
        mel.error("Project Number needs to be 2 digits. (i.e. 02)")
    try:
        int(projNum)
    except ValueError:
        mel.progressBar('autoProProgress', edit = 1, visible=0)
        statusUpdate('self', 'Project Number needs to be an integer')
        mel.error("Project Number needs to be an integer")

  
def runAutoPro(self):
    
    
    statusUpdate(self, 'Starting AutoPro')
    #reset textField values to default for error detection reasons
    resetValue(self)
    mel.progressBar('autoProProgress', edit = 1, visible=1)
    statusUpdate(self, 'Optimizing Scene')
    import maya.mel as mm
    mm.eval('source cleanupScene.mel')
    mm.eval('performCleanUpSceneForEverything')
    statusUpdate(self, 'Finished Optimizing Scene')
    addProgress()
    
    #collect display layers
    display_Layers = ap.find_layers()
    #collect the state of display layers
    display_layers_state = ap.collect_layer_state(display_Layers)
    #hide layers
    ap.hide_all_layers(display_Layers)
    
    #progressWindow()
    #Check to see if a file is loaded
    statusUpdate(self, 'Query Scene Load')
    if not (mel.file(query=1, sceneName=1)):
        mel.progressBar('autoProProgress', edit = 1, visible=0)
        statusUpdate(self, 'No file loaded. Please load a file.')
        mel.error("No file loaded. Please load a file")
    #update name variables
    updateNameVars()
    addProgress()
    statusUpdate(self, 'Name Variables Verified')
    
    statusUpdate(self, 'Checking File Name')
    #check the name and edit the GUI accordingly.
    nameCheck = ap.nameCheck(yearMonth, projNum)
    mel.textField("studentFileNameTextField", edit = True, text = nameCheck[1])
    if(nameCheck[0]):
        mel.textField("fileNamedTextField", edit=True, text = "Yes", backgroundColor = ap.bgColor(0))
    else:
        mel.textField("fileNamedTextField", edit = True, text = "No", backgroundColor = ap.bgColor(100))
    addProgress()
    statusUpdate(self, 'Name Check Complete')
    
    statusUpdate(self, 'Gathering Nodes')
    #Load the assemblie nodes minus cameras  
    masterNodes = ap.masterGroup()
    #sort to capture all children nodes as well as main assembly nodes
    allNodes = ap.nodeCollect(masterNodes)
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
    transformNodes = ap.listCollect(nodes, 'transform')    
    visiNodes = ap.listCollect(nodes, 'mesh')
    totalShape = len(visiNodes)
    totalTrans = len(transformNodes)
    mel.textField("totalObjectsTextField", edit=1, text=totalTrans)
    mel.textField("totalShapeObjectsTextField", edit=1, text = totalShape)
    addProgress()
    statusUpdate(self, 'Node Quantities Complete')
    
    statusUpdate(self, 'Comparing Default Names')
    #compare geometry names to defualt name list and calculate and populate GUI fields
    global defaultNames
    defaultNames = ap.defaultCompare(transformNodes)
    mel.textField("notNamedTextField", edit=1, text=len(defaultNames))
    notNamedPercent = int((float(len(defaultNames))/float(totalTrans))*100.0)
    percentDefaultNames = (str(notNamedPercent) + "%")
    notNamedColor = ap.bgColor(notNamedPercent)
    mel.textField("notNamedPercentTextField", edit=1, text=percentDefaultNames, backgroundColor = notNamedColor)
    addProgress()
    statusUpdate(self, 'Default Names Compared')
    
    statusUpdate(self, 'Checking Master Group')
    #Check to master Group node and subGroups
    subGroups = ap.subGroups(masterNodes)
    if ((len(masterNodes)) ==1) and subGroups != False:
        mel.textField("groupedTextField", edit=True, text = "Yes", backgroundColor = (0.0, 0.8, 0.0))
    else:
        mel.textField("groupedTextField", edit = True, text = "No", backgroundColor = (0.8, 0.0, 0.0))
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
        if (ap.visibleTest(node)):
            notLayeredLocal.append(node)
    if displayLayers != None:       
        for layer2 in visibleLayer:
            mel.setAttr('%s.visibility' % layer2, 1)
    notLayered = notLayeredLocal
    mel.textField("notLayeredTextField", edit = 1, text = len(notLayered))
    notLayerPercent = int((float(len(notLayered))/float(len(visiNodes)))*100.0)
    percentNotLayer = (str(notLayerPercent) + "%")
    notLayeredColor = ap.bgColor(notLayerPercent)
    mel.textField("notLayeredPercentTextField", edit=1, text=percentNotLayer, backgroundColor = notLayeredColor)
    addProgress()
    statusUpdate(self, 'Display Layers Checked')
    
    statusUpdate(self, 'Checking Transforms')
    #Checks for frozen transforms.
    global notFroze
    notFroze = ap.spreadSheet(ap.listCollect(nodes, 'transform'))
    mel.textField("notFrozenTextField", edit= 1, text=len(notFroze))
    notFrozePercent = int((float(len(notFroze))/float(totalTrans))*100.00)
    percentNotFroze = (str(notFrozePercent) + "%")
    notFrozeColor = ap.bgColor(notFrozePercent)
    mel.textField("notFrozenPercentTextField", edit =1, text = percentNotFroze, backgroundColor = notFrozeColor)
    addProgress()
    statusUpdate(self, 'Transforms Checked')
    
    statusUpdate(self, 'Checking for History')
    #check for History
    global withHistory
    withHistory = ap.historyFinder(ap.listCollect(nodes, 'mesh'))
    mel.textField("withHistoryTextField", edit = 1, text = len(withHistory))
    withHistoryPercent = int((float(len(withHistory))/float(len(visiNodes)))*100.0)
    percentWithHistory = (str(withHistoryPercent) + "%")
    withHistoryColor = ap.bgColor(withHistoryPercent)
    mel.textField("withHistoryPercentTextField", edit=1, text=percentWithHistory, backgroundColor = withHistoryColor)
    addProgress()
    statusUpdate(self, 'History Checked')
    
    statusUpdate(self, 'Checking Pivots')
    #Check for pivots
    global notCentered
    notCentered = ap.centerPivot(ap.listCollect(nodes, 'transform'))
    mel.textField("notCenteredTextField", edit=1, text = len(notCentered))
    notCenteredPercent = int((float(len(notCentered))/float(totalTrans))*100.0)
    percentNotCentered = (str(notCenteredPercent) + "%")
    notCenteredColor = ap.bgColor(notCenteredPercent)
    mel.textField("notCenteredPercentTextField", edit = 1, text = percentNotCentered, backgroundColor = notCenteredColor)
    addProgress()
    statusUpdate(self, 'Pivots Checked')
    
    statusUpdate(self, 'Testing N-gons')
    #Test N-gons
    global nGonList
    nGonList = ap.nGonFinder(allNodes)
    nGonPercent = int((float(len(nGonList[0]))/float(len(visiNodes)))*100.0)
    percentNGons = (str(nGonPercent) + "%")
    nGonColor = ap.bgColor(nGonPercent)
    mel.textField("totalNgonObjectsTextField", edit =1, text = len(nGonList[0]))
    mel.textField("ngonPercentTextField", edit = 1, text = percentNGons , backgroundColor = nGonColor)
    mel.textField("totalNgonsTextField", edit =1, text = len(nGonList[1]))
    addProgress()
    statusUpdate(self, 'N-gons Complete')
    
    statusUpdate(self, 'Testing Lamina Faces')
    #test Lamina faces
    global laminaList
    laminaList = ap.laminaFinder(allNodes)
    laminaPercent = int((float(len(laminaList[0]))/float(len(visiNodes)))*100.0)
    percentLamina = (str(laminaPercent) + "%")
    laminaColor = ap.bgColor(laminaPercent)
    mel.textField("totalLaminaObjectsTextField", edit =1, text = len(laminaList[0]))
    mel.textField("laminaPercentTextField", edit = 1, text = percentLamina , backgroundColor = laminaColor)
    if laminaList[1]==None:
        laminaListLen =0
    else:
        laminaListLen = len(laminaList[1])
    mel.textField("totalLaminaTextField", edit =1, text = laminaListLen)
    addProgress()
    statusUpdate(self, 'Laminas Complete')
    
    statusUpdate(self, 'Tool Completed')
    mel.rowLayout( 'progressRowLayout', edit = 1, visible = 0)
    mel.rowLayout('autoProStatusRowLayout', edit =1, visible = 0)

    statusUpdate(self, 'Testing Tri Faces')
    #test Lamina faces
    global triList
    triList = ap.triFinder(allNodes)
    triPercent = int((float(len(triList[0]))/float(len(visiNodes)))*100.0)
    percentTri = (str(triPercent) + "%")
    triColor = ap.bgColor(triPercent)
    mel.textField("totalTriObjectsTextField", edit =1, text = len(triList[0]))
    mel.textField("triPercentTextField", edit = 1, text = percentTri , backgroundColor = triColor)
    if triList[1]==None:
        triListLen =0
    else:
        triListLen = len(triList[1])
    mel.textField("totalTriTextField", edit =1, text = triListLen)
    addProgress()
    statusUpdate(self, 'Tris Complete')
    
    statusUpdate(self, 'Tool Completed')
    mel.rowLayout( 'progressRowLayout', edit = 1, visible = 0)
    mel.rowLayout('autoProStatusRowLayout', edit =1, visible = 0)
    
    ap.set_layers_visibility(display_Layers, display_layers_state)
    
    #push grades auto
    pushGrades('self')



def countTool(self):
    temp = str(ap.count(ap.selected()))
    mel.textField("countTextField", edit=1, text = temp)
    
def nGonSelect(self):
    ap.sel(nGonList[0])
    
def laminaSelect(self):
    ap.sel(laminaList[0])
    
def triSelect(self):
    ap.sel(triList[0])
    
def defNamSel(self):
    ap.sel(defaultNames)

def visLayerSel(self):
    ap.sel(notLayered)

def notFrozeSel(self):
    ap.sel(notFroze)
    
def openSpreadSheet(self):
    ap.sel(notFroze)
    ap.spreadSheetWin(self)

def withHisSel(self):
    ap.sel(withHistory)

def notCentSel(self):
    ap.sel(notCentered)
 
def resetGUI(self):
    yrMnth = yearMonth
    prjNm = projNum
    autoProGui()
    mel.textField("yearMonthTextField", edit=1, text = yrMnth)
    mel.textField("projectNumsTextField", edit=1, text = prjNm)
    
def resetValue(self):
    defaultNames = []
    notLayered = []
    notFroze = []
    withHistory = []
    notCentered = []
    nGonList = []
    mel.rowLayout( 'progressRowLayout', edit = 1, visible=1)
    mel.progressBar("autoProProgress", edit=1,progress = 0)
    mel.rowLayout('autoProStatusRowLayout', edit =1, visible = 1)
    mel.textField('totalObjectsTextField', edit = 1, text = "####")
    mel.textField('totalShapeObjectsTextField', edit = 1, text = "####")
    mel.textField('fileNamedTextField', edit = 1, text = '#NULL#' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('studentFileNameTextField', edit = 1, text = '#Student_Joe_MCR_####_Project0#.ma#')
    mel.textField('notNamedTextField', edit = 1, text = '####' )
    mel.textField('notNamedPercentTextField', edit = 1, text = '##%' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('groupedTextField', edit = 1, text = '#NULL#' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('masterNodeTextField', edit = 1, text = "#[u'masterNode']#")
    mel.textField('notLayeredTextField', edit = 1, text = '####' )
    mel.textField('notLayeredPercentTextField', edit = 1, text = '##%' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('notFrozenTextField', edit = 1, text = '####' )
    mel.textField('notFrozenPercentTextField', edit = 1, text = '##%' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('withHistoryTextField', edit = 1, text = '####' )
    mel.textField('withHistoryPercentTextField', edit = 1, text = '##%' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('notCenteredTextField', edit = 1, text = '####' )
    mel.textField('notCenteredPercentTextField', edit = 1, text = '##%' , backgroundColor = (0.25, 0.25, 0.25))
    mel.textField("countTextField", edit = 1, text = '#NULL#' )
    mel.textField('totalNgonObjectsTextField', edit = 1, text = '####' )
    mel.textField('ngonPercentTextField', edit = 1, text = '##%', backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('totalNgonsTextField', edit = 1, text = '#NULL#' )
    mel.textField('totalLaminaObjectsTextField', edit = 1, text = '####' )
    mel.textField('laminaPercentTextField', edit = 1, text = '##%', backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('totalLaminaTextField', edit = 1, text = '#NULL#' )
    mel.textField('totalTriObjectsTextField', edit = 1, text = '####' )
    mel.textField('triPercentTextField', edit = 1, text = '##%', backgroundColor = (0.25, 0.25, 0.25))
    mel.textField('totalTriTextField', edit = 1, text = '#NULL#' )

def pushGrades(self):
    gpg.loadPush()
    name = mel.textField('fileNamedTextField', query=1, text=1)
    masterGroup = mel.textField('groupedTextField', query=1, text=1)
    
    
    if (projNum =='04'):
        
        defaultNames = mel.textField('notNamedTextField', query = 1, text=1)
        dispLayers = mel.textField('notLayeredTextField', query=1, text=1)
        transforms = mel.textField('notFrozenTextField', query=1, text=1)
        conHist = mel.textField('withHistoryTextField', query=1, text=1)
        pivot = mel.textField('notCenteredTextField', query=1, text=1)
        
        #push name field info
        if (name == 'Yes'):
            gp.pushNamed('self', True)
        else:
            gp.pushNamed('self', False)
        
        #push geo named field info
        if (int(defaultNames) >=3):
            gp.pushGeoNamed('self', False)
        else:
            gp.pushGeoNamed('self', True)
            
        #push master group field info
        if (masterGroup =='Yes'):
            gp.pushGeoGrouped('self', True)
        else:
            gp.pushGeoGrouped('self', False)
            
        #push geo layered field info
        if (int(dispLayers)>=3):
            gp.pushGeoLayered('self', False)
        else:
            gp.pushGeoLayered('self', True)
        
        #push transforms frozen field info
        if ((int(transforms))>=3):
            print "transforms is false"
            gp.pushTransFroze('self', False)
        else:
            print "transforms are true"
            gp.pushTransFroze('self', True)
        
        #push history deleted field info
        if (int(conHist)>=3):
            gp.pushHistoryDel('self', False)
        else:
            gp.pushHistoryDel('self', True)
        
        #push pivots centered field info
        if (int(pivot)>=3):
            gp.pushPivotsCenter('self', False)
        else:
            gp.pushPivotsCenter('self', True)
            
    if (projNum == '01' or projNum=='03'):
        
        defaultNames = mel.textField('notNamedPercentTextField', query=1, text=1)
        defaultNamesValue = defaultNames.split('%')
        
        #push name field info
        if (name == 'Yes'):
            gp.pushNamed('self', True)
        else:
            gp.pushNamed('self', False)
            
        gpg.pushGeoNamed('self', int(defaultNamesValue[0]))
    
        #push master group field info
        if (masterGroup =='Yes'):
            gp.pushGeoGrouped('self', True)
        else:
            gp.pushGeoGrouped('self', False)
            
        dispLayers = mel.textField('notLayeredPercentTextField', query=1, text=1)
        dispLayersValue = dispLayers.split('%')
        gpg.pushGeoLayered('self', int(dispLayersValue[0]))
        
        transforms = mel.textField('notFrozenPercentTextField', query=1, text=1)
        transformsValue = transforms.split('%')
        gpg.pushTransFroze('self', int(transformsValue[0]))
        
        conHist = mel.textField('withHistoryPercentTextField', query=1, text=1)
        conHistValue = conHist.split('%')
        gpg.pushHistoryDel('self', int(conHistValue[0]))
        
        pivot = mel.textField('notCenteredPercentTextField', query=1, text =1)
        print "pivot: %r" % pivot
        pivotValue = pivot.split('%')
        print "pivotValue: %r" % pivotValue[0]
        gpg.pushPivotsCenter('self', int(pivotValue[0]))
        
        
        


 
    
    
def addProgress():
    mel.progressBar("autoProProgress", edit=True, step=1)
    if (mel.progressBar("autoProProgress", query=1, progress=1)) == mel.progressBar("autoProProgress", query =1, maxValue =1):
        mel.progressBar('autoProProgress', edit = 1, visible=0)

def statusUpdate(self, message):
    mel.text('autoProStatus', edit =1, label = message)
    print message



##launch GUI
autoProGui()


    
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
    laminaList = []
    triList = []
    #Declare variables for the grade push functionality
    geoNames = []
    geoLayered = []
    transFroze = []
    histDel = [] 
    pivotCenter = []
