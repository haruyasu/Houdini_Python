hou_node = hou.pwd()
path_name = hou_node.evalParm('path_name')
base_path = 'C:/Users/haruyasu/Desktop/'
full_path = base_path + path_name + '/'
file_name = path_name + '.$F4.bgeo'
full_path = full_path + file_name
return hou.expandString(full_path)


# pre-render Script
import os
hou_node = hou.pwd()
full_path = hou_node.evalParm('sopoutput')
dir_path = os.path.dirname(full_path)
if not os.path.exists(dir_path):
    os.mkdir()
