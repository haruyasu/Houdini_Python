for hou_node in hou.selectedNodes():
    #group_parm = hou_node.parm('group')
    #group_parm.setExpression('chs("attributetomatch")')
    #current_value = group_parm.eval()
    #new_value = current_value.replace('tork', 'phon')
    #group_parm.deleteAllKeyframes()
    #group_parm.set(new_value)
    default_positions = ['$TX', '$TY', '$TZ']
    position_tuple = hou_node.parmTuple('t')
    for index, parm in enumerate(position_tuple):
        parm.deleteAllKeyframes()
        new_expression = default_positions[index] + ' + noise($TX, $TY + ' + str(index * 10000) + ', $TZ)'
        parm.setExpression(new_expression)