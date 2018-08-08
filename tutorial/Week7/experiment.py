node = hou.pwd()
geo = node.geometry()

if node.evalParm('live_geo'):
    color = node.parmTuple('color').eval()
    group = node.evalParm('group')

    cd_attrib = geo.findPointAttrib('Cd')
    if cd_attrib.dataType() == hou.attribData.Int:
        raise hou.NodeError, 'Cd is an Integer. It must be a Float.'

    geo.addAttrib(hou.attribType.Point, 'blorg', (0.0, 0.0, 1.0), transform_as_normal=True)

    if group:
        point_list = geo.globPoints(group)
    else:
        point_list = geo.points()

    for curr_point in ccpoint_list:
        curr_color = curr_point.attribValue('Cd')
        output_color = []
        for curr_value, new_value in zip(curr_color, color):
            output_color.append(curr_value + new_value)
        curr_point.setAttribValue('Cd', output_color)

    rotates = node.parmTuple('rotate').eval()
    xform_matrix = hou.hmath.buildRotate(rotates)
    geo.transform(xform_matrix)

    geo.deletePoints(point_list)
    create_point_list = ((0, 0, 0), (0, 0, 2), (0, 0, 2))
    curr_poly = geo.createPolygon()
    for position in create_point_list:
        curr_point = geo.createPoint()
        curr_point.setPosition(position)
        curr_poly.addVertex(curr_point)
else:
    path = node.evalParm('output_file')
    geo.loadFromFile(path)
