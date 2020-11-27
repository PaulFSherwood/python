bl_info = {
    "name": "Shader Library",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "View3D > Toolshelf",
    "description": "Adds a new Shader to your Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Shadder",
}

import bpy

class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Shader Libary'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Select a Shader to be added.")
        row.operator('shader.diamond_operator')
        
# Create a custerom operator for the diamon shader    
class SHADER_OT_DIAMOND(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = 'shader.diamond_operator'
    
    def execute(self, context):
        # create a new shader and calling it diamond
        material_diamond = bpy.data.materials.new(name = "Diamond")
        material_diamond.use_nodes = True
        
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))

        # Create a refernce  to the Material Output
        material_output = material_diamond.node_tree.nodes.get('Material Output')
        # set location of node
        material_output.location = (400, 0)
        
        ######################################################################## GLASS ######
        # adding glass1 node                                                                #
        glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')           #
        # set location of node                                                              #
        glass1_node.location = (-600, 0)                                                    #
        # set the default color                                                             #
        glass1_node.inputs[0].default_value = (1, 1, 1, 1)                                  #
        # Setting the default IOR value                                                     #
        glass1_node.inputs[2].default_value = 1.446                                         #
                                                                                            #
        # adding glass2 node                                                                #
        glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')           #
        # set location of node                                                              #
        glass2_node.location = (-600, -150)                                                 #
        # set the default color                                                             #
        glass2_node.inputs[0].default_value = (0, 1, 0, 1)                                  #
        # Setting the default IOR value                                                     #
        glass2_node.inputs[2].default_value = 1.450                                         #
                                                                                            #
        # adding glass3 node                                                                #
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')           #
        # set location of node                                                              #
        glass3_node.location = (-600, -300)                                                 #
        # set the default color                                                             #
        glass3_node.inputs[0].default_value = (0, 0, 1, 1)                                  #
        # Setting the default IOR value                                                     #
        glass3_node.inputs[2].default_value = 1.450                                         #
                                                                                            #
        # Cretate the Glass Node and Reference it as 'glass4'                               #
        glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')           #
        # set location of node                                                              #
        glass4_node.location = (-150, -150)                                                 #
        # set the default color                                                             #
        glass4_node.inputs[0].default_value = (1, 1, 1, 1)                                  #
        # Setting the default IOR value                                                     #
        glass4_node.inputs[2].default_value = 1.450                                         #
        # Deselect the Node                                                                 #
        glass4_node.select = False                                                          #
        ######################################################################## GLASS ######
        
        ################################################################### ADD SHADER ######
        # Create the Add Shader Node and REference it as 'Add1'                             #
        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')             #
        # set location of node                                                              #
        add1_node.location = (-400, -50)                                                    #
        # set the Label                                                                     #
        add1_node.label = "Add 1"                                                           #
        # minimizes the Node                                                                #
        add1_node.hide = True                                                               #
        #deslect the Node                                                                   #
        add1_node.select = False                                                            #
                                                                                            #
        # Create the Add Shader Node and REference it as 'Add2'                             #
        add2_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')             #
        # set location of node                                                              #
        add2_node.location = (-100, 0)                                                      #
        # set the Label                                                                     #
        add2_node.label = "Add 2"                                                           #
        # minimizes the Node                                                                #
        add2_node.hide = True                                                               #
        #deslect the Node                                                                   #
        add2_node.select = False                                                            #
        ################################################################### ADD SHADER ######
        
        ################################################################### MIX SHADER ######
        # Create the mix shader node and referen it as 'Mix1'                               #
        mix1_node = material_diamond.node_tree.nodes.new('ShaderNodeMixShader')             #
        # Setting the Location                                                              #
        mix1_node.location = (200, 0)                                                       #
        #deslect the Node                                                                   #
        mix1_node.select = False                                                            #
        ################################################################### MIX SHADER ######
        
        ################################################################### LINK NODES ######
        # create the link glass1 to add1                                                    #
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])    #
        # create the link glass2 to add1                                                    #
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])    #
        # create the link add1 to add2                                                      #
        material_diamond.node_tree.links.new(add1_node.outputs[0], add2_node.inputs[0])      #
        # create the link glass3 to add2                                                    #
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[1])    #
        # create the link add2 to mix1                                                      #
        material_diamond.node_tree.links.new(add2_node.outputs[0], mix1_node.inputs[1])      #
        # create the link glass4 to mix1                                                    #
        material_diamond.node_tree.links.new(glass4_node.outputs[0], mix1_node.inputs[2])    #
        # create the link mix1 to outputs                                                   #
        material_diamond.node_tree.links.new(mix1_node.outputs[0], material_output.inputs[0])#
        ################################################################### LINK NODES ######
        
        bpy.context.object.active_material = material_diamond
        
        return{'FINISHED'}
        
        
        
        
        
def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(SHADER_OT_DIAMOND)
    
def unregiester():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(SHADER_OT_DIAMOND)
    
if __name__ == "__main__":
    register()