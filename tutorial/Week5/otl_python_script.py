# OTL
# parameter tab
# callback Script -> hou.pwd().hdaModule().callbackTest()
# or
# kwargs['node'].hdaModule().callbackTest(kwargs['node'])

# script tab
# add Event Handler -> PythonModule
def callbackTest(hou_node):
    hou_node.setColor(hou.Color([0.2, 0, 0.6]))
    hou.ui.displayMessage("Test")
