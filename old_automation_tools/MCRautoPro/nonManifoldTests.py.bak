##here is some new code... I have it narrowed down to somewhere around line  90
##it is skipping a list item when it iterates... ideas?


#import maya commands
import maya.cmds as mel

#debugging log
def log(message, prefix = 'Debug', hush=False):
    if not hush:
        print("%s : %s " % (prefix,message))
        
#gather assembly nodes
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
    
#gather all nodes
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

#this function takes a range and splits it (i.e. pPlane.vtx[1:5] returns ['pPlane.vtx[1]', 'pPlane.vtx[2]', 'pPlane.vtx[3]', ... ... ])
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


#This function is suppose to take an input and return the edges and vertices that are flagged as nonmanifold
def nonManifoldFinder(nodeListInput):
    log('Start Non-Manifold Finder')
    nodeList = nodeListInput
    log('Node List Collected')
    log('Nodes: %r' % nodeList)
    nonManifoldObjects = []
    newRange = []
    range = []
    log('empty lists declared')
    nonManifoldComponents = mel.polyInfo(nodeList, nonManifoldVertices=1)
    log('removing duplicates from nonManifoldComponents')
    nonManifoldComponents = list(set(nonManifoldComponents))
    log('Non-Manifold Components Collected')
    log('Components: %r' % nonManifoldComponents)
    log('')
    log('')
    log('')
    k=0
    #length = len(nonManifoldComponents)
    #try using <= down in the while loop
    while k < len(nonManifoldComponents): ##k<length
        k+=1
        log('starting iteration of nonManifoldComonent List')
        log('handling: %r' % item)
        tempHolder = item.split('.')
        log('split %r into %r' %(item, tempHolder))
        log('appending %r to nonManifoldObjects' % tempHolder[0])
        nonManifoldObjects.append(tempHolder[0])
        log('%r appended to nonManifoldObjects' % tempHolder[0])
        log('nonManifoldObjects: %r' % nonManifoldObjects)
        log('Testing  %r for :' % item)  
        if ":" in item:
            log(': is in %r' % item)
            log('removing %r from nonManifoldComponents' % item)
            nonManifoldComponents.remove(item)
            log('%r removed from nonManifoldComponents' % item)
            log('nonManifoldComponents : %r' % nonManifoldComponents)
            log('%r appending to range' % item)
            range.append(item)
            log('%r appended to range' % item)
            log('Range: %r' % range)
    log('')
    log('')
    log('')             
    log('splitting ranges')
    newRange = rangeSplit(range)
    log('new ranges / post split::: %r' % newRange)
    log('starting to iterate newRange')
    for t in newRange:
        log('appending %r to nonManifoldComponents' % t)
        nonManifoldComponents.append(t)
        log('%r appended' % t)

    nonManifoldObjects = list(set(nonManifoldObjects))
            
    return nonManifoldObjects, nonManifoldComponents
    
nonMani = nonManifoldFinder(nodeCollect(masterGroup()))
log(nonMani)