from Katana import NodegraphAPI

TIME = 0

rootNode = NodegraphAPI.GetRootNode()

teapotNode = NodegraphAPI.CreateNode('PrimitiveCreate', rootNode)

teapotNode_x = 4
teapotNode_y = 3
teapotNode_z = 2

teapotNode.getParameter('transform.translate.x').setValue(teapotNode_x, TIME)
teapotNode.getParameter('transform.translate.y').setValue(teapotNode_y, TIME)
teapotNode.getParameter('transform.translate.z').setValue(teapotNode_z, TIME)

teapotNode_x_1 = teapotNode.getParameter('transform.translate.x').getValue(TIME)
teapotNode_y_1 = teapotNode.getParameter('transform.translate.y').getValue(TIME)
teapotNode_z_1 = teapotNode.getParameter('transform.translate.z').getValue(TIME)

print(teapotNode_x_1)
print(teapotNode_y_1)
print(teapotNode_z_1)

teapotNode_3d_pos = teapotNode.getParameter('transform.translate').getValue(TIME)
print(teapotNode_3d_pos)