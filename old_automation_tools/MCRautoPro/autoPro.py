'''
..::Auto Script::..
written by Adam Fatka :: www.fatkaforce.com

This script generates feedback to assist in completing the professionalism portion of grading.

In order to run this script please select all the objects in the scene and then activate the shelf button.
'''
##imports the mel commands
import maya.cmds as mel
import maya.cmds as cmds

#these functions deal with display layers
##
def find_layers(ignore_layers=['defaultLayer']):
    layers = cmds.ls(long=True,type='displayLayer')
    for current_layer in ignore_layers:
        if current_layer in layers:
            layers.remove(current_layer)       
    return layers
    
def collect_layer_state(layers):
    layerState=[]
    for layer in layers:
        currentState = cmds.getAttr('%s.visibility' % layer)
        layerState.append(currentState)
    return layerState

def set_layers_visibility(layers, values):
    counter = 0
    for layer in layers:        
        cmds.setAttr( '%s.visibility' % layer, values[counter])
        counter+=1
        
def hide_all_layers(layers):
    hide_states = []
    for layer in layers:
        hide_states.append(0)
    set_layers_visibility(layers, hide_states)



#debugging log
def log(message, prefix = 'Debug', hush=False):
    if not hush:
        print("%s : %s " % (prefix,message))

##This function selects the provided nodes
def sel(nodeListInput):
    mel.select(clear=1)
    for item in nodeListInput:
        mel.select(item, add=1)
        
##This is a basic count function it counts the inputed information/array
def count(nodeListInput):
    count = len(nodeListInput)
    return count

##This function takes the selection and bundles it for future use.
def selected():
    selectedGeo= mel.ls(selection=1, long=1)
    mel.select(clear=1)
    return selectedGeo

## This portion of the script compares all of the selected objects to verify their pivots are centered.
def centerPivot(selectedGeo):
    pivots= selectedGeo
    pivotCenter = []
    for item in pivots:
        pivotLocation = mel.xform(item, ws=1, query=1, rotatePivot=1)
        pivotNewLocation = mel.objectCenter(item)
        if(abs(float(pivotLocation[0]) - float(pivotNewLocation[0])) < 0.01):
            if(abs(float(pivotLocation[1]) - float(pivotNewLocation[1])) < 0.01):
                if(abs(float(pivotLocation[2]) - float(pivotNewLocation[2])) < 0.01):
                    pivotCenter.append(item)
    
    pivotNotCenter=[]
    for item in pivots:
        if item in pivotCenter:
            continue
        else: pivotNotCenter.append(item)
        
    return pivotNotCenter

##This function determines if an objects transforms are frozen
def spreadSheet(nodeListInput):
    transforms = nodeListInput
    froze = []
    for item in transforms:
        translation = mel.xform (item, query=1, translation=1)
        rotation = mel.xform (item, query=1, rotation=1)
        scale = mel.xform(item, query=1, relative=1, scale=1)
        if(translation[0]==0 and translation[1]==0 and translation[2]==0 and rotation[0]==0 and rotation[1]==0 and rotation[2]==0 and scale[0]==1 and scale[1]==1 and scale[2]==1):
            froze.append(item)
        
    notFroze = []
        
    for item in transforms:
       if item in froze:
           continue
       else: notFroze.append(item)
    
    return notFroze

##This function checks to see if a scene is named correctly.
## Input for this function must be strings (ex. "1109","03")
def nameCheck(yearMonth, projectNumber):
    fileName = mel.file(query=1, sceneName=1, shortName=1)
    yearMonth = yearMonth
    projectNumber = projectNumber
    if projectNumber == "04":
        if fileName.endswith('_FinalProject_MCR_' + yearMonth + '.mb'):
            return [True, fileName]
    if fileName.endswith('_Project' + projectNumber + '_MCR_' + yearMonth + '.mb'):
        return [True, fileName]
    else:
        return [False, fileName]

##This function selectes the uppermost nodes that are not cameras and returns them
##
def masterGroup():
    assemblies = mel.ls(long=1, assemblies=1)
    upperNodes = []
    for item in assemblies:
        temp = mel.listRelatives(item, path=1)
        if (temp==None):
            upperNodes.append(item)
        else:
            if not (mel.nodeType(temp[0])=='camera'):
                upperNodes.append(item)
    return upperNodes

##This function detects the existence of transform nodes that are children of the masterNode and have their immediate children as transforms (subGroups)
def subGroups(masterNodes):
    if len(masterNodes) != 1:
        return False
    children = mel.listRelatives(masterNodes, path=1)
    subGroups = []
    for child in children:
        if (mel.nodeType(child)=='transform'):
            grandChildren = mel.listRelatives(child, path=1)
            if grandChildren != None:
                if (mel.nodeType(grandChildren[0])=='transform'):
                   subGroups.append(child)
    return subGroups

##This function takes an input and returns all the children of that input.
##
def nodeCollect(masterGroupInput):
    masterGroup = masterGroupInput
    nodeList = []
    iterateList = []
    if(masterGroup == None or len(masterGroup)==0):
        mel.error( "Input in Null")
    elif(len(masterGroup)==1):
        iterateList.append(masterGroup[0])
    else:
        for object in masterGroup:
            iterateList.append(object)
    for item in iterateList:
        descendents = mel.listRelatives(item, allDescendents=1, path=1)
        if (descendents != None):
            if ('master' or 'Master' in item) and (mel.nodeType(descendents[0]) == 'nurbsCurve'):
                continue
            else:
                nodeList.append(item)
                for child in descendents:
                   nodeList.append(child)
    return nodeList



##This function takes an input and a node type and returns all the nodes of that type from that input
##
def listCollect(nodeListInput, nodeType):
    nodeList = nodeListInput
    meshList = []
    for node in nodeList:
        if mel.nodeType(node)==nodeType:
            meshList.append(node)
    return meshList

##This function takes an input and compares it to a default name list. returns a list of inputs that have default matches.
##
def defaultCompare(nodeListInput):
    defaultNames = ["pCube", "pCylinder",  "pSphere", "pCone", "pPlane", "pTorus", "pPrism", "pPyramid", "pPipe", "pHelix", "pSolid", "nurbsSphere", "curve", "nurbsCube", "nurbsCylinder", "nurbsCone", "nurbsPlane", "nurbsTorus", "nurbsCircle", "nurbsSquare", "revolvedSurface", "subdivSphere", "subdivCube", "subdivCylinder", "subdivCone", "subdivPlane", "subdivTorus", "nurbsToPoly", "polySurface", "pasted", "group", "mirroredCutMesh", "extrudedSurface"]
    hasDefaultName = []
    nodeList = nodeListInput
    for object in nodeList:
        try:
            splitCatch = object.split('|')
        except AttributeError:
            continue
        if len(splitCatch) != 1:
            query = splitCatch[-1]
        else:
            query = object
        for name in defaultNames:
            if name in query:
                print "checking for %r in %r" % (name, query)
                if name == 'group':
                    print "Poppout for Group"
                    if ('group' in query) and not (('_group' in query) or ('group_' in query)):
                        print "adding %r to hasDefault" % object
                        hasDefaultName.append(object)
                        continue
                    else:
                        continue
                hasDefaultName.append(object)
    return hasDefaultName

##This function checks for N-gons. It returns Total Number of N-gons, Total Objects Effected by N-gons.
##
def nGonFinder(nodeListInput):
    nodeList = nodeListInput
    nSidedObjects = []
    mel.select(clear=1)
    for node in nodeList:
        mel.select(node, add=1)
    ##This line constrains the selection to faces with more than 4 sides and then selects them.
    ##It also constrains the selection to N-gons so it must be reset before exiting.
    mel.polySelectConstraint(mode=3, type=8, size=3)
    nSidedFaces = mel.ls(selection=1)
    for item in nSidedFaces:
        tempHolder = item.split('.')
        nSidedObjects.append(tempHolder[0])
    newRange = []
    range = []
    for x in nSidedFaces:
        if ":" in x:
            nSidedFaces.remove(x)
            range.append(x)
    newRange = rangeSplit(range)
    for t in newRange:
        nSidedFaces.append(t)
    ##This resets the selection to 'normal'
    mel.polySelectConstraint(mode=0, type=8, size=0)
    nSidedObjects = list(set(nSidedObjects))
    mel.select(clear=1)
            
    return nSidedObjects, nSidedFaces

def historyFinder(nodeListInput):
    nodeList = nodeListInput
    falsePositiveList = [ 'displayLayer', 'groupId', 'shadingEngine', 'mesh', 'animCurveTL']
    historyList = []
    for item in nodeList:
        if mel.listHistory(item, pruneDagObjects=1):
            history = mel.listHistory(item, pruneDagObjects = 1)
            for i in history:
                historyType = mel.nodeType(i)
                if historyType not in falsePositiveList:
                    if item not in historyList:
                        historyList.append(item)
    return historyList

##This function takes an inputed node and tests to see if it is visible. returns true or false.
def visibleTest(nodeInput):
    #gather node to test
    testNode = nodeInput
    #make sure the object exists
    if not mel.objExists(testNode): return False
    #Test to see if the object has a visibility attribute (and by extension, is a DAG node)
    if not mel.attributeQuery('visibility', node = testNode, exists=True): return False
    #Gather objects visibility attribute
    isVisible = mel.getAttr(testNode + '.visibility')
    #test if an objects has an intermediateObject attribute
    if mel.attributeQuery('intermediateObject', node = testNode, exists=True):
        #test if an object is an intermediate object, and as such not visible
        isVisible = isVisible and not mel.getAttr(testNode + '.intermediateObject')
    #test is the object is in a display layer through the existence of an overrideEnabled attribute
    if mel.attributeQuery('overrideEnabled', node = testNode, exists=True) and mel.getAttr(testNode + '.overrideEnabled'):
        #test to see if the display layer is visible
        isVisible = isVisible and mel.getAttr(testNode + '.overrideVisibility')
    #if the object tests visible so far, verify it's parents are visible
    if isVisible:
        nodeParents = mel.listRelatives(testNode, parent=1, path=1)
        if nodeParents != None:
            if len(nodeParents) >0:
                isVisible = isVisible and visibleTest(nodeParents[0])
    #return boolean as to whether the object is visible or not. 
    return isVisible


#creates an outliner window
def outlinerWin(self):
    if mel.window('autoProOutliner', exists = 1):
        mel.deleteUI('autoProOutliner', window =1 )
        
    mel.window('autoProOutliner', title = "autoPro Outliner", iconName = "autoProOut")
    mel.frameLayout( labelVisible=False )
    panel = mel.outlinerPanel()
    outliner = mel.outlinerPanel(panel, query=True,outlinerEditor=True)
    mel.outlinerEditor( outliner, edit=True, mainListConnection='worldList', selectionConnection='modelList', showShapes=False, showAttributes=False, showConnected=False, showAnimCurvesOnly=False, autoExpand=False, showDagOnly=True, ignoreDagHierarchy=False, expandConnections=False, showCompounds=True, showNumericAttrsOnly=False, highlightActive=True, autoSelectNewObjects=False, doNotSelectNewObjects=False, transmitFilters=False, showSetMembers=True, setFilter='defaultSetFilter' )
    mel.showWindow('autoProOutliner')

#creates a spreasheet window
def spreadSheetWin(self):
    if mel.window('autoProSpreadSheetWindow', exists = 1):
        mel.deleteUI('autoProSpreadSheetWindow', window =1 )
        
    window = mel.window('autoProSpreadSheetWindow', title = "autoPro SpreadSheet", iconName = "autoProSprSht", widthHeight=(400, 300) )
    mel.paneLayout()
    activeList = mel.selectionConnection( activeList=True )
    mel.spreadSheetEditor( mainListConnection=activeList )
    mel.showWindow( 'autoProSpreadSheetWindow' )
 
#takes a value and returns a tuple based on that value    
def bgColor(percent):
    if percent == 0:
        return (0.0, 0.8, 0.0)
    elif 0< percent<=5:
        return (0.8, 0.8, 0.0) 
    elif 5<percent<=10:
        return (0.8, 0.5, 0.0)
    elif 10<percent<=15:
        return (0.8, 0.3, 0.0)
    else:
        return (0.8, 0.0, 0.0)
    
def rangeSplit(rangeToSplit):
    range = rangeToSplit
    newRange = []
    k=0
    for r in range:
        item = r
        if len(range[k].split(":")) != 2:
            temp = range[k].split(":")
            range[k] = temp[-2] + ":" + temp[-1]
        colonSplit = range[k].split(":")
        k+=1
        leftSplit = colonSplit[0].split("[")
        rightSplit = colonSplit[1].split("]")
        try:
            i = int(leftSplit[1])
        except IndexError:
            newRange.append(r)
            continue
        while i <= int(rightSplit[0]):
            rangeItem = ("%s[%d]" % (leftSplit[0], i))
            newRange.append(rangeItem)
            i+=1
    return newRange


##This function checks for Tris. It returns Total Number of Tris, Total Objects Effected by Tris.
##
def triFinder(nodeListInput):
    nodeList = nodeListInput
    triObjects = []
    mel.select(clear=1)
    for node in nodeList:
        mel.select(node, add=1)
    ##This line constrains the selection to faces with 3 sides and then selects them.
    ##It also constrains the selection to tris so it must be reset before exiting.
    mel.polySelectConstraint(mode=3, type=8, size=1)
    triFaces = mel.ls(selection=1)
    for item in triFaces:
        tempHolder = item.split('.')
        triObjects.append(tempHolder[0])
    newRange = []
    range = []
    for x in triFaces:
        if ":" in x:
            triFaces.remove(x)
            range.append(x)
    newRange = rangeSplit(range)
    for t in newRange:
        triFaces.append(t)
    ##This resets the selection to 'normal'
    mel.polySelectConstraint(mode=0, type=8, size=0)
    triObjects = list(set(triObjects))
    mel.select(clear=1)
            
    return triObjects, triFaces

##This function checks for lamina faces. It returns Total Number of lamina faces, Total Objects Effected by lamina faces.
##
def laminaFinder(nodeListInput):
    nodeList = nodeListInput
    laminaObjects = []
    laminaFaces = mel.polyInfo(nodeList, laminaFaces = 1)
    if laminaFaces == None:
        return laminaObjects, laminaFaces
    for item in laminaFaces:
        tempHolder = item.split('.')
        laminaObjects.append(tempHolder[0])
    newRange = []
    range = []
    for x in laminaFaces:
        if ":" in x:
            laminaFaces.remove(x)
            range.append(x)
    newRange = rangeSplit(range)
    for t in newRange:
        laminaFaces.append(t)

    laminaObjects = list(set(laminaObjects))
            
    return laminaObjects, laminaFaces



def nonManifoldFinder(nodeListInput):
    nodeList = nodeListInput
    nonManifoldObjects = []
    newRange = []
    range = []
    nonManifoldComponents = mel.polyInfo(nodeList, nonManifoldVertices = 1, nonManifoldEdges=1)
    for item in nonManifoldComponents:
        tempHolder = item.split('.')
        nonManifoldObjects.append(tempHolder[0])
        if ":" in item:
            nonManifoldComponents.remove(item)
            range.append(item)
    newRange = rangeSplit(range)
    for t in newRange:
        nonManifoldComponents.append(t)

    nonManifoldObjects = list(set(nonManifoldObjects))
            
    return nonManifoldObjects, nonManifoldComponents