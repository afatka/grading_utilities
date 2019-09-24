import maya.cmds as cmds
import os, platform, datetime


def validate_modified_date(path_to_file, max_delta_days):
    output = []

    modified_time = os.path.getmtime(path_to_file) # modified date, expressed as seconds since epoch
    modified_time_datetime = datetime.datetime.fromtimestamp(modified_time) # Convert to datetime

    today = datetime.datetime.now() # This one is pretty obvious... 
    modified_delta = today - modified_time_datetime # how many days between then and now?

    if modified_delta.days > max_delta_days:
        output = [modified_delta, modified_time_datetime]

    return output

def validate_creation_date(path_to_file, max_delta_days):
    output = []

    creation_time = creation_date(path_to_file) #creation date, expressed as seconds since epoch
    creation_time_datetime = datetime.datetime.fromtimestamp(creation_time)# Convert to datetime

    today = datetime.datetime.now() # This one is pretty obvious... 
    creation_delta = today - creation_time_datetime
    if creation_delta.days > max_delta_days:
        output = [creation_delta, creation_time_datetime]

    return output

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

def validate_file(max_modified_delta, max_creation_delta, file_for_validation):
    modified_validation = validate_modified_date(file_for_validation, max_modified_delta)
    creation_validation = validate_creation_date(file_for_validation, max_creation_delta)

    if (not modified_validation) and (not creation_validation):
        return None
    else:
        output_message = ''
        if modified_validation:
            output_message += '\tModified: {}\n'.format(modified_validation[1].strftime('%b %d, %Y'))

        if creation_validation:
            output_message += '\tCreated: {}\n'.format(creation_validation[1].strftime('%b %d, %Y'))

        return (file_for_validation, output_message)

def validate_current_scene(max_modified_delta, max_creation_delta):
    file_path = cmds.file(query = True, sceneName = True)
    modified_validation = validate_modified_date(file_path, max_modified_delta)
    creation_validation = validate_creation_date(file_path, max_creation_delta)

    output_message = ''
    if modified_validation:
        output_message += 'Modified: {}\n\n'.format(modified_validation[1].strftime('%b %d, %Y'))

    if creation_validation:
        output_message += 'Created: {}'.format(creation_validation[1].strftime('%b %d, %Y'))

    if output_message != '':
        cmds.confirmDialog(message = output_message, title = 'Red Alert!')

def validate_directory(max_modified_delta, max_creation_delta):
    file_dir = cmds.fileDialog2(fileMode = 3, caption = 'Select Directory')[0]
    file_types = ('.mb', '.ma')
    found_files = []

    directoryDepth = 0
    maximum_recursion = 8

    for directory_name, subdirectory_name, fileList in os.walk(file_dir):
        if directoryDepth == 0:
            directoryDepth = len(directory_name.split(os.sep))
        if len(directory_name.split(os.sep)) - directoryDepth >= maximum_recursion:
            print('os.walk recursion break triggered')
            break
        
        for item in fileList:
            if item.endswith((file_types)):
                file_to_add = os.path.join(directory_name, item)
                # if directory_name.endswith(os.sep):
                #     fileToAdd = directory_name + item
                # else:
                #     fileToAdd = directory_name + os.sep + item
                found_files.append(file_to_add)
    
    failed_validation = []
    for f in found_files:
        validation = validate_file(max_modified_delta, max_creation_delta, f)
        if validation != None:
            failed_validation.append(validation)

    if failed_validation:
        output_message = ''
        for failed in failed_validation:
            output_message += '{}:\n{}'.format(os.path.basename(failed[0]), failed[1])
        cmds.confirmDialog(message = output_message, title = 'Red Alert!') 



validate_directory(9,9)
