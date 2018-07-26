selected_nodes = hou.selectedNodes()
for node in selected_nodes:
    node_type = node.type()
    parent = node.parent()
    for child_node in parent.children():
        if child_node.type() == node_type:
            child_node.setSelected(True)