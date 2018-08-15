import toolutils

geo_node = toolutils.genericTool(kwargs, 'geo', 'merge')
geo_node.setSelected(False)
geo_node.displayNode().destroy()

merge_node = geo_node.createNode('object_merge', 'merge_from_obj')
merge_node.parm('xformtype').set(1)

viewer = toolutils.sceneViewer()
selection = viewer.selectObjects()
nodes_to_merge = []
for node in selection:
    nodes_to_merge.append(node.path())
print node_to_merge

merge_node.parm('objpath1').set(' '.join(nodes_to_merge))
