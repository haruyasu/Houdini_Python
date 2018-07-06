selected_nodes = hou.selectedNodes()
for node in selected_nodes:
    parent = node.node('..')
    out_null = parent.createNode('null', 'OUT')
    out_null.setNextInput(node)
    out_null.setPosition(node.position())
    out_null.move([0, -1])
    out_null.setSelected(True)
    node.setSelected(False)

    new_color = hou.Color([0, 0, 1])
    out_null.setColor(new_color)

out_null.setDisplayFlag(True)
out_null.setRenderFlag(True)
