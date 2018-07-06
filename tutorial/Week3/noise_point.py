selected_nodes = hou.selectedNodes()
for hou_node in selected_nodes:
    default_positions = ['$TX', '$TY', '$TZ']
    position_tuple = hou_node.parmTuple('t')
    for index, parm in enumerate(position_tuple):
        parm.deleteAllKeyframes()
        new_expression = default_positions[index] + ' + noise($TX, $TY + ' + str(index * 1000) + ', $TZ)'
        parm.setExpression(new_expression)
