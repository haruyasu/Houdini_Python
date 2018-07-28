# get the types so that we can create nodes later
# we are defining these here so that it is easy to change things like versions
# later.
crate_type = 'crate'
sticky_type = 'sticky_input'

# get the first selected node to base the setup on
if hou.selectedNodes():
    # this will be the node we will use to base the setup on
    project_node = hou.selectedNodes()[0]
    parent_node = project_node.parent()

    # create the actual nodes and dump the newly created nodes into variables
    # so that we can modify them later
    # the sticky node is the basis of the setup, so start with that
    sticky_node = parent_node.createNode(sticky_type, 'sticky_input1')
    # wire input
    sticky_node.setInput(1, project_node)
    # position it under the project node
    sticky_node.setPosition(project_node.position())
    sticky_node.move([-1, -1])

    # create the merge node using the createInputNode() function
    merge_node = sticky_node.createInputNode(0, 'merge')
    # position it
    merge_node.setPosition(sticky_node.position())
    merge_node.move([-2, 1])

    # create the first crate node
    crate_node = merge_node.createInputNode(0, crate_type)
    # position it
    crate_node.setPosition(merge_node.position())
    crate_node.move([0, 2])

    # create the merge node at the end
    end_merge_node = sticky_node.createOutputNode('merge', 'merge_ground')
    end_merge_node.setNextInput(project_node)

    # create the out null
    out_null = end_merge_node.createOutputNode('null', 'OUT')
    out_null.setColor(hou.Color([0, 0.2, 0.6]))
    out_null.setDisplayFlag(True)
    out_null.setRenderFlag(True)

else:
    # display error dialog
    hou.ui.displayMessage('You must select some nodes.')