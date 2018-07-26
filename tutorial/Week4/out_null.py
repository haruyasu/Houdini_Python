# get all the currently selected nodes
selected_nodes = hou.selectedNodes()
# loop over the selected nodes.  The current node object in the loop will be
# stored in the variable "node".
for node in selected_nodes:
    # get the parent of the currently selected node.  You could also use
    # node.parent() to do this.
    parent = node.node('..')
    # create the null and name it "OUT".  It will be created at position 0, 0
    out_null = parent.createNode('null', 'OUT')
    # set the input to the currently looping node
    out_null.setNextInput(node)
    # set the position to overlap with the currently looping node
    out_null.setPosition(node.position())
    # move the out null downwards one unit, so that they no longer overlap
    out_null.move([0, -1])
    # select the new out null
    out_null.setSelected(True)
    # deselect the currently looping node
    node.setSelected(False)
    
    # create the color object, and set it to RGB 0, 0.2, 0.6.  We got those
    # colors by using node.color() to see what the color of an out null
    # previously created was.
    new_color = hou.Color([0, 0.2, 0.6])
    # set the color of the out null to the color object we just created
    out_null.setColor(new_color)

# the "out_null" variable should still be set to the last null created by
# the loop, so we can use that variable after the loop to affect the last
# null created.  In this case, we are setting the render and display flags.
out_null.setDisplayFlag(True)
out_null.setRenderFlag(True)