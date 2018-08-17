import toolutils
viewer = toolutils.sceneViewer()

selection = viewer.selectGeometry('Select Points to Paint', geometry_types=[hou.geometryType.Points])
selection_node = selection.node()[0]
selection_string = selection.selectionStrings()[0]

blast = toolutils.genericTool(kwargs, 'blast', 'blast_for_painting')
blast.setNextInput(selection_node)
blast.parm('group').set(selection_string)
blast.parm('grouptype').set(3)
blast.parm('negate').set(1)

color_node = blast.createOutputNode('color', 'color_black_for_painting')
color_node.parmTuple('color').set([0, 0, 0])

paint = color_node.createOutputNode('paint', 'paint_on_isolated_geo')
paint.setSelected(True, clear_all_selected=True)
paint.parmTuple('fg').set([1, 0, 0])

scatter = paint.createOutputNode('scatter', 'scatter_points')
scatter.parn('attrib').set('Cd')
scatter.parn('blend').set('mult')
scatter.setDisplayFlag(True)
scatter.setRenderFlag(True)

viewer.enterCurrentNodeState()
