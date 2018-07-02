import objecttoolutils

crate_type = 'crate'
sticky_type = 'sticky_input'

if hou.selectedNodes():
    project_node = hou.selectedNodes()[0]
    parent_node = project_node.parent()

    objecttoolutils.genericTool(kwargs, 'null')

    curNode = parent_node.currentNode()

    curNode.setInput(1, project_node)

    curNode.setName("test")
    curNode.setColor(hou.Color((0.6, 0.4, 1.0)))
    curNode.setDisplayFlag(True)
    curNode.setRenderFlag(True)


kwargs['bbox'] = hou.BoundingBox(-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
objecttoolutils.genericTool(kwargs, 'null')

curNode = kwargs['pane'].currentNode()

name = hou.ui.readInput("Give out name", title="Out null")[1]
name = name.upper()
name = name.replace(" ", "_")

curNode.setName(name)
curNode.setColor(hou.Color((0.6, 0.4, 1.0)))
curNode.setDisplayFlag(True)
curNode.setRenderFlag(True)
