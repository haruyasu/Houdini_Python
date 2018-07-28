for hou_node in hou.selectedNodes():
    #group_parm = hou_node.parm('group')
    #group_parm.setExpression('chs("attributetomatch")')
    #current_value = group_parm.eval()
    #new_value = current_value.replace('tork', 'phon')
    #group_parm.deleteAllKeyframes()
    #group_parm.set(new_value)
    default_positions = ['$TX', '$TY', '$TZ']
    amp_list = ['ampx', 'ampy', 'ampz']
    position_tuple = hou_node.parmTuple('t')

    # add parm templates to node
    frequency_template = hou.FloatParmTemplate('freq', 'Frequency', 3, (1, 1, 1))
    amplitude_template = hou.FloatParmTemplate('amp', 'Amplitude', 3, (1, 1, 1))
    #folder_template = hou.FolderParmTemplate('noise_settings', 'Noise Settings', [frequency_template, amplitude_template])
    parm_group = hou_node.parmTemplateGroup()
    parm_group.insertBefore('t', amplitude_template)
    parm_group.insertBefore(amplitude_template, frequency_template)
    #parm_group.insertBefore('group', folder_template)
    #parm_group.insertBefore('group', amplitude_template)
    #parm_group.insertBefore(amplitude_template, frequency_template)
    hou_node.setParmTemplateGroup(parm_group)

    for index, parm in enumerate(position_tuple):
        parm.deleteAllKeyframes()
        new_expression = default_positions[index] + ' + noise($TX * ch("freqx"), $TY * ch("freqy") + ' + str(index * 10000) + ', $TZ * ch("freqz")) * ch("' + amp_list[index] + '")'
        parm.setExpression(new_expression)