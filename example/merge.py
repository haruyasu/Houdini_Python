selNodes = hou.selectedNodes()

mrgNode = selNodes[0].parent().createNode('merge')
mrgNode.moveToGoodPosition()

mrgNode.setDisplayFlag(True)
mrgNode.setRenderFlag(True)


for i, node in enumerate(selNodes):
    mrgNode.setInput(i, node)
    # node.moveToGoodPosition()

mrgNode.setSelected(True, clear_all_selected=True)
