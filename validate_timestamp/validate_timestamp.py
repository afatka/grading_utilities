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

validate_current_scene(9,9)
