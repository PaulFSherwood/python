###################################################################################################
##### REFERENCES                                                                              #####
# https://docs.blender.org/api/current/bpy.types.html                                             #
# https://www.youtube.com/watch?v=8mSSCQ7LGVo&list=PLFtLHTf5bnym_wk4DcYIMq1DkjqB7kDb-&index=4     #
#                                                                                                 #
###################################################################################################

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

def hex_to_rgb1( hex_value ):
    b = (hex_value & 0xFF) / 255.0
    g = ((hex_value >> 8) & 0xFF) / 255.0
    r = ((hex_value >> 16) & 0xFF) / 255.0
    return r, g, b

def hex_to_rgb(value):
    gamma = 2.2
    value = value.lstrip('#')
    lv = len(value)
    fin = list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    r = pow(fin[0] / 255, gamma)
    g = pow(fin[1] / 255, gamma)
    b = pow(fin[2] / 255, gamma)
    fin.clear()
    fin.append(r)
    fin.append(g)
    fin.append(b)
    fin.append(1.0)
    return tuple(fin)

# Main Panel
class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Shader Library"                 # The label that will show up in the N-Panel
    bl_idname = "SHADER_PT_MAINPANEL"           # ID that other panels can reference
    bl_space_type = 'VIEW_3D'                   # The port that the n-panel will show up on
    bl_region_type = 'UI'                       #
    bl_category = 'Shader Libary'               # Tab name or reference to other tab it will be at on the n-panel
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()                      # like a new line character
        row.label(text= "Select a Basic Metallic Shader.")
        row = layout.row()
        row.operator('shader.diamond_operator', icon= 'HANDLETYPE_ALIGNED_VEC')
        
        
# Sub panel for Metalics
class ShaderMetalicsPanel(bpy.types.Panel):
    bl_label = "Metallics"
    bl_idname = "SHADER_PT_METALS"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Shader Libary'
    
    #bl_parent_id = 'SHADER_PT_MAINPANEL'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('shader.gold_operator', icon= 'KEYTYPE_MOVING_HOLD_VEC')
        row.operator('shader.silver_operator', icon= 'HANDLETYPE_FREE_VEC')
        row.operator('shader.copper_operator', icon= 'KEYTYPE_EXTREME_VEC')
        row = layout.row()

        
# Sub panel for Stylized
class ShaderStylizedPanel(bpy.types.Panel):
    bl_label = "Stylized"
    bl_idname = "SHADER_PT_STYLIZED"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Shader Libary'
    
    #bl_parent_id = 'SHADER_PT_MAINPANEL'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        #row.label(text="For Stylized Materials.")
        row.operator('shader.hologram_operator', icon= 'KEYTYPE_MOVING_HOLD_VEC')
        row.operator('shader.ghost_operator', icon= 'GHOST_ENABLED')
        row = layout.row()
        
        
#################################################################################################
#################################################################################################
######## DIAMOND          ####################################################################### 
     
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
        
        ############################################################################ GLASS ######
                                                                                                #
        # adding glass1 node                                                                    #
        glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')               #
        # set location of node                                                                  #
        glass1_node.location = (-600, 0)                                                        #
        # set the default color                                                                 #
        glass1_node.inputs[0].default_value = (1, 1, 1, 1)                                      #
        # Setting the default IOR value                                                         #
        glass1_node.inputs[2].default_value = 1.446                                             #
                                                                                                #
        # adding glass2 node                                                                    #
        glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')               #
        # set location of node                                                                  #
        glass2_node.location = (-600, -150)                                                     #
        # set the default color                                                                 #
        glass2_node.inputs[0].default_value = (0, 1, 0, 1)                                      #
        # Setting the default IOR value                                                         #
        glass2_node.inputs[2].default_value = 1.450                                             #
                                                                                                #
        # adding glass3 node                                                                    #
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')               #
        # set location of node                                                                  #
        glass3_node.location = (-600, -300)                                                     #
        # set the default color                                                                 #
        glass3_node.inputs[0].default_value = (0, 0, 1, 1)                                      #
        # Setting the default IOR value                                                         #
        glass3_node.inputs[2].default_value = 1.450                                             #
                                                                                                #
        # Cretate the Glass Node and Reference it as 'glass4'                                   #
        glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')               #
        # set location of node                                                                  #
        glass4_node.location = (-150, -150)                                                     #
        # set the default color                                                                 #
        glass4_node.inputs[0].default_value = (1, 1, 1, 1)                                      #
        # Setting the default IOR value                                                         #
        glass4_node.inputs[2].default_value = 1.450                                             #
        # Deselect the Node                                                                     #
        glass4_node.select = False                                                              #
                                                                                                #
        ############################################################################ GLASS ######
        
        ####################################################################### ADD SHADER ######
                                                                                                #
        # Create the Add Shader Node and REference it as 'Add1'                                 #
        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')                 #
        # set location of node                                                                  #
        add1_node.location = (-400, -50)                                                        #
        # set the Label                                                                         #
        add1_node.label = "Add 1"                                                               #
        # minimizes the Node                                                                    #
        add1_node.hide = True                                                                   #
        #deslect the Node                                                                       #
        add1_node.select = False                                                                #
                                                                                                #
        # Create the Add Shader Node and REference it as 'Add2'                                 #
        add2_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')                 #
        # set location of node                                                                  #
        add2_node.location = (-100, 0)                                                          #
        # set the Label                                                                         #
        add2_node.label = "Add 2"                                                               #
        # minimizes the Node                                                                    #
        add2_node.hide = True                                                                   #
        #deslect the Node                                                                       #
        add2_node.select = False                                                                #
                                                                                                #
        ####################################################################### ADD SHADER ######
        
        ####################################################################### MIX SHADER ######
                                                                                                #
        # Create the mix shader node and referen it as 'Mix1'                                   #
        mix1_node = material_diamond.node_tree.nodes.new('ShaderNodeMixShader')                 #
        # Setting the Location                                                                  #
        mix1_node.location = (200, 0)                                                           #
        #deslect the Node                                                                       #
        mix1_node.select = False                                                                #
                                                                                                #
        ####################################################################### MIX SHADER ######
        
        ####################################################################### LINK NODES ######
                                                                                                #
        # create the link glass1 to add1                                                        #
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])       #
        # create the link glass2 to add1                                                        #
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])       #
        # create the link add1 to add2                                                          #
        material_diamond.node_tree.links.new(add1_node.outputs[0], add2_node.inputs[0])         #
        # create the link glass3 to add2                                                        #
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[1])       #
        # create the link add2 to mix1                                                          #
        material_diamond.node_tree.links.new(add2_node.outputs[0], mix1_node.inputs[1])         #
        # create the link glass4 to mix1                                                        #
        material_diamond.node_tree.links.new(glass4_node.outputs[0], mix1_node.inputs[2])       #
        # create the link mix1 to outputs                                                       #
        material_diamond.node_tree.links.new(mix1_node.outputs[0], material_output.inputs[0])   #
                                                                                                #
        ################################################################### LINK NODES ##########
        
        bpy.context.object.active_material = material_diamond
        
        return{'FINISHED'}

#################################################################################################
#################################################################################################
######## GOLD             #######################################################################        
        
# Create a custerom operator for the GOLD shader    
class SHADER_OT_GOLD(bpy.types.Operator):
    bl_label = "Gold"
    bl_idname = 'shader.gold_operator'
    
    def execute(self, context):
        # create a new shader and calling it Gold
        material_gold = bpy.data.materials.new(name = "Gold")
        material_gold.use_nodes = True
        
        material_gold.node_tree.nodes.remove(material_gold.node_tree.nodes.get('Principled BSDF'))

        # Create a refernce  to the Material Output
        material_output = material_gold.node_tree.nodes.get('Material Output')
        # set location of node
        material_output.location = (300, 0)
        
        ################################################################ NOISE TEXTURE ######
                                                                                            #
        # Adding Noise Texture node                                                         #
        noise1_node = material_gold.node_tree.nodes.new('ShaderNodeTexNoise')               #
        # set location of node                                                              #
        noise1_node.location = (-200, 0)                                                    #
        # set the default scale                                                             #
        noise1_node.inputs[2].default_value = 89.00                                         #
        # Setting the default detail                                                        #
        noise1_node.inputs[3].default_value = 8.90                                          #
        # Setting the default Roughness                                                     #
        noise1_node.inputs[4].default_value = 0.192                                         #
        # Setting the default Distortion                                                    #
        noise1_node.inputs[5].default_value = 2.20                                          #
                                                                                            #
        ################################################################ NOISE TEXTURE ######
        
        ############################################################## PRINCIPLED BSDF ######
                                                                                            #
        # adding Principled BSDF node                                                       #
        Pbsdf_node = material_gold.node_tree.nodes.new('ShaderNodeBsdfPrincipled')          #
        # set location of node                                                              #
        Pbsdf_node.location = (0, 0)                                                        #
        # set the default color                                                             #
        ## hex = E79B40         #F4CD89                                                     #
        Pbsdf_node.inputs[0].default_value = (0.658375, 0.42869, 0.038204, 1)               #
        # Setting the default Metallic value                                                #
        Pbsdf_node.inputs[4].default_value =  0.932                                         #
        # Setting the default Specular value                                                #
        Pbsdf_node.inputs[5].default_value =  0.495                                         #
                                                                                            #
        ############################################################## PRINCIPLED BSDF ######
        
        ########################################################## LINK NODES TOGETHER ######
                                                                                            #
        # create the link Noise1 to Pbsdf                                                   #
        material_gold.node_tree.links.new(noise1_node.outputs[1], Pbsdf_node.inputs[7])     #
        # create the link Pbsdf to outputs                                                  #
        material_gold.node_tree.links.new(Pbsdf_node.outputs[0], material_output.inputs[0]) #
                                                                                            #
        ################################################################### LINK NODES ######
        
        bpy.context.object.active_material = material_gold
        
        return{'FINISHED'}

#################################################################################################
#################################################################################################
######## SILVER           #######################################################################        
        
# Create a custerom operator for the SILVER shader    
class SHADER_OT_SILVER(bpy.types.Operator):
    bl_label = "Silver"
    bl_idname = 'shader.silver_operator'
    
    def execute(self, context):
        # create a new shader and calling it Silver
        material_silver = bpy.data.materials.new(name = "Silver")
        material_silver.use_nodes = True
        
        material_silver.node_tree.nodes.remove(material_silver.node_tree.nodes.get('Principled BSDF'))

        # Create a refernce  to the Material Output
        material_output = material_silver.node_tree.nodes.get('Material Output')
        # set location of node
        material_output.location = (300, 0)
        
        ################################################################ NOISE TEXTURE ######
                                                                                            #
        # Adding Noise Texture node                                                         #
        noise1_node = material_silver.node_tree.nodes.new('ShaderNodeTexNoise')             #
        # set location of node                                                              #
        noise1_node.location = (-200, 0)                                                    #
        # set the default scale                                                             #
        noise1_node.inputs[2].default_value = 89.00                                         #
        # Setting the default detail                                                        #
        noise1_node.inputs[3].default_value = 8.90                                          #
        # Setting the default Roughness                                                     #
        noise1_node.inputs[4].default_value = 0.192                                         #
        # Setting the default Distortion                                                    #
        noise1_node.inputs[5].default_value = 2.20                                          #
                                                                                            #
        ################################################################ NOISE TEXTURE ######
        
        ############################################################## PRINCIPLED BSDF ######
                                                                                            #
        # adding Principled BSDF node                                                       #
        Pbsdf_node = material_silver.node_tree.nodes.new('ShaderNodeBsdfPrincipled')        #
        # set location of node                                                              #
        Pbsdf_node.location = (0, 0)                                                        #
        # set the default color                                                             #
        ## hex = E79B40         #F4CD89                                                     #
        Pbsdf_node.inputs[0].default_value = (0.527115, 0.527115, 0.527115, 1)              #
        # Setting the default Metallic value                                                #
        Pbsdf_node.inputs[4].default_value =  0.932                                         #
        # Setting the default Specular value                                                #
        Pbsdf_node.inputs[5].default_value =  0.495                                         #
                                                                                            #
        ############################################################## PRINCIPLED BSDF ######
        
        ########################################################## LINK NODES TOGETHER ######
                                                                                            #
        # create the link Noise1 to Pbsdf                                                   #
        material_silver.node_tree.links.new(noise1_node.outputs[1], Pbsdf_node.inputs[7])   #
        # create the link Pbsdf to outputs                                                  #
        material_silver.node_tree.links.new(Pbsdf_node.outputs[0], material_output.inputs[0]) #
                                                                                            #
        ################################################################### LINK NODES ######
        
        bpy.context.object.active_material = material_silver
        
        return{'FINISHED'}

#################################################################################################
#################################################################################################
########  COPPER          #######################################################################        
        
# Create a custerom operator for the COPPER shader    
class SHADER_OT_COPPER(bpy.types.Operator):
    bl_label = "Copper"
    bl_idname = 'shader.copper_operator'
    
    def execute(self, context):
        # create a new shader and calling it Copper
        material_copper = bpy.data.materials.new(name = "Copper")
        material_copper.use_nodes = True
        
        material_copper.node_tree.nodes.remove(material_copper.node_tree.nodes.get('Principled BSDF'))

        # Create a refernce  to the Material Output
        material_output = material_copper.node_tree.nodes.get('Material Output')
        # set location of node
        material_output.location = (300, 0)
        
        ################################################################ NOISE TEXTURE ######
                                                                                            #
        # Adding Noise Texture node                                                         #
        noise1_node = material_copper.node_tree.nodes.new('ShaderNodeTexNoise')             #
        # set location of node                                                              #
        noise1_node.location = (-200, 0)                                                    #
        # set the default scale                                                             #
        noise1_node.inputs[2].default_value = 89.00                                         #
        # Setting the default detail                                                        #
        noise1_node.inputs[3].default_value = 8.90                                          #
        # Setting the default Roughness                                                     #
        noise1_node.inputs[4].default_value = 0.192                                         #
        # Setting the default Distortion                                                    #
        noise1_node.inputs[5].default_value = 2.20                                          #
                                                                                            #
        ################################################################ NOISE TEXTURE ######
        
        ############################################################## PRINCIPLED BSDF ######
                                                                                            #
        # adding Principled BSDF node                                                       #
        Pbsdf_node = material_copper.node_tree.nodes.new('ShaderNodeBsdfPrincipled')        #
        # set location of node                                                              #
        Pbsdf_node.location = (0, 0)                                                        #
        # set the default color                                                             #
        ## hex = E79B40         #F4CD89                                                     #
        Pbsdf_node.inputs[0].default_value = (0.47932, 0.171441, 0.033105, 1)               #
        # Setting the default Metallic value                                                #
        Pbsdf_node.inputs[4].default_value =  0.932                                         #
        # Setting the default Specular value                                                #
        Pbsdf_node.inputs[5].default_value =  0.495                                         #
                                                                                            #
        ############################################################## PRINCIPLED BSDF ######
        
        ########################################################## LINK NODES TOGETHER ######
                                                                                            #
        # create the link Noise1 to Pbsdf                                                   #
        material_copper.node_tree.links.new(noise1_node.outputs[1], Pbsdf_node.inputs[7])   #
        # create the link Pbsdf to outputs                                                  #
        material_copper.node_tree.links.new(Pbsdf_node.outputs[0], material_output.inputs[0]) #
                                                                                            #
        ################################################################### LINK NODES ######
        
        bpy.context.object.active_material = material_copper
        
        return{'FINISHED'}


#################################################################################################
#################################################################################################
######## HOLOGRAM          ###################################################################### 
     
# Create a custerom operator for the hologram shader    
class SHADER_OT_HOLOGRAM(bpy.types.Operator):
    bl_label = "Hologram"
    bl_idname = 'shader.hologram_operator'
    
    def execute(self, context):
        # create a new shader and calling it hologram
        material_hologram = bpy.data.materials.new(name = "Hologram")
        material_hologram.use_nodes = True
        
        material_hologram.node_tree.nodes.remove(material_hologram.node_tree.nodes.get('Principled BSDF'))

        # Create a refernce  to the Material Output
        material_output = material_hologram.node_tree.nodes.get('Material Output')
        # set location of node
        material_output.location = (400, 0)
        
        ############################################################################ COLUMN 1 ######
        # adding layerWeight1 node                                                                 #
        layerWeight1_node = material_hologram.node_tree.nodes.new('ShaderNodeLayerWeight')         #
        # set location of node                                                                     #
        layerWeight1_node.location = (-300, 0)                                                     #
        # set the default color                                                                    #
        layerWeight1_node.inputs[0].default_value = 0.080                                          #
                                                                                                   #
        # Cretate the Glass Node and Reference it as 'Transparent'                                 #
        transparent1_node = material_hologram.node_tree.nodes.new('ShaderNodeBsdfTransparent')     #
        # set location of node                                                                     #
        transparent1_node.location = (-300, -120)                                                  #
        # set the default color                                                                    #
        transparent1_node.inputs[0].default_value = (1, 1, 1, 1)                                   #
        # Deselect the Node                                                                        #
        transparent1_node.select = False                                                           #
                                                                                                   #
        # adding emission node                                                                     #
        emission1_node = material_hologram.node_tree.nodes.new('ShaderNodeEmission')               #
        # set location of node                                                                     #
        emission1_node.location = (-300, -200)                                                     #
        # set the default color                                                                    #
        emission1_node.inputs[0].default_value = (0, 0, 1, 1)                                      #
        # Setting the default Strength value                                                       #
        emission1_node.inputs[1].default_value = 1000                                              #
                                                                                                   #
        # adding wire1 node                                                                        #
        wire1_node = material_hologram.node_tree.nodes.new('ShaderNodeWireframe')                  #
        # set location of node                                                                     #
        wire1_node.location = (-300, -300)                                                         #
        # set the default color                                                                    #
        wire1_node.use_pixel_size = True                                                           #
        # Setting the default IOR value                                                            #
        wire1_node.inputs[0].default_value = 0.201                                                 #
                                                                                                   #
        ############################################################################ COLUMN 1 ######
        
        ############################################################################ COLUMN 2 ######
        # Create the Add Shader Node and REference it as 'Add1'                                    #
        mix1_node = material_hologram.node_tree.nodes.new('ShaderNodeMixShader')                   #
        # set location of node                                                                     #
        mix1_node.location = (-60, 0)                                                              #
        #deslect the Node                                                                          #
        mix1_node.select = False                                                                   #
                                                                                                   #
        # Create the Add Shader Node and REference it as 'Add1'                                    #
        mix2_node = material_hologram.node_tree.nodes.new('ShaderNodeMixShader')                   #
        # set location of node                                                                     #
        mix2_node.location = (-60, -120)                                                           #
        #deslect the Node                                                                          #
        mix2_node.select = False                                                                   #
                                                                                                   #
        ############################################################################ COLUMN 2 ######
        
        #################################################################### FINAL MIX SHADER ######
        # Create the mix shader node and referen it as 'Mix1'                                      #
        mix3_node = material_hologram.node_tree.nodes.new('ShaderNodeMixShader')                   #
        # Setting the Location                                                                     #
        mix3_node.location = (200, 0)                                                              #
        # set the default factor to .5                                                             #
        mix3_node.inputs[0].default_value = 0.50                                                   #
        #deslect the Node                                                                          #
        mix3_node.select = False                                                                   #
                                                                                                   #
        ################################################################### FINAL  MIX SHADER ######
        
        ########################################################################## LINK NODES ######
        # create the link layer weight to mix1                                                     #
        material_hologram.node_tree.links.new(layerWeight1_node.outputs[1], mix1_node.inputs[0])   #
        # create the link transparent1 to mix1                                                     #
        material_hologram.node_tree.links.new(transparent1_node.outputs[0], mix1_node.inputs[1])   #
        # create the link transparent1 to mix2                                                     #
        material_hologram.node_tree.links.new(transparent1_node.outputs[0], mix2_node.inputs[1])   #
        # create the link emmision1 to mix1                                                        #
        material_hologram.node_tree.links.new(emission1_node.outputs[0], mix1_node.inputs[2])      #
        # create the link emmision1 to mix2                                                        #
        material_hologram.node_tree.links.new(emission1_node.outputs[0], mix2_node.inputs[2])      #
        # create the link wire1 to mix2                                                            #
        material_hologram.node_tree.links.new(wire1_node.outputs[0], mix2_node.inputs[0])          #
        # create the link MIX1 to MIX3                                                             #
        material_hologram.node_tree.links.new(mix1_node.outputs[0], mix3_node.inputs[1])           #
        # create the link MIX2 to MIX3                                                             #
        material_hologram.node_tree.links.new(mix2_node.outputs[0], mix3_node.inputs[2])           #
        # create the link MIX3 to outputs                                                          #
        material_hologram.node_tree.links.new(mix3_node.outputs[0], material_output.inputs[0])     #
        ###################################################################### LINK NODES ##########
        
        bpy.context.object.active_material = material_hologram
        
        return{'FINISHED'}


#################################################################################################
#################################################################################################
######## GHOST          ######################################################################### 
     
# Create a custerom operator for the hologram shader    
class SHADER_OT_GHOST(bpy.types.Operator):
    bl_label = "Ghost"
    bl_idname = 'shader.ghost_operator'
    
    def execute(self, context):
        # create a new shader and calling it hologram
        material_ghost = bpy.data.materials.new(name = "Ghost")
        material_ghost.use_nodes = True
        
        material_ghost.node_tree.nodes.remove(material_ghost.node_tree.nodes.get('Principled BSDF'))

        # Create a refernce  to the Material Output
        material_output = material_ghost.node_tree.nodes.get('Material Output')
        # set location of node
        material_output.location = (400, 0)
                
        
        ############################################################################ COLUMN 1 ######
                                                                                                   #
        # Cretate the Glass Node and Reference it as 'Transparent'                                 #
        fresnel1_node = material_ghost.node_tree.nodes.new('ShaderNodeFresnel')                    #
        # set location of node                                                                     #
        fresnel1_node.location = (-300, 100)                                                       #
        # set the default color                                                                    #
        fresnel1_node.inputs[0].default_value = 1.200                                              #
                                                                                                   #
        # adding emission node                                                                     #
        diffuse1_node = material_ghost.node_tree.nodes.new('ShaderNodeBsdfDiffuse')                #
        # set location of node                                                                     #
        diffuse1_node.location = (-300, 0)                                                         #
        # set the default color                                                                    #
        diffuse1_node.inputs[0].default_value = (0.8, 0.8, 0.8, 1)                                 #
                                                                                                   #
        # adding wire1 node                                                                        #
        diffuse2_node = material_ghost.node_tree.nodes.new('ShaderNodeBsdfDiffuse')                #
        # set location of node                                                                     #
        diffuse2_node.location = (-300, -120)                                                      #
        # set the default color                                                                    #
        diffuse2_node.inputs[0].default_value = (0.8, 0.0, 0.0, 1)                                 #
                                                                                                   #
        ############################################################################ COLUMN 1 ######
        
        ############################################################################ COLUMN 2 ######
                                                                                                   #
        # Create the Add Shader Node and REference it as 'Mix1'                                    #
        mix1_node = material_ghost.node_tree.nodes.new('ShaderNodeMixShader')                      #
        # set location of node                                                                     #
        mix1_node.location = (-60, 0)                                                              #
        #deslect the Node                                                                          #
        mix1_node.select = False                                                                   #
                                                                                                   #
        # Cretate the Glass Node and Reference it as 'Transparent'                                 #
        transparent1_node = material_ghost.node_tree.nodes.new('ShaderNodeBsdfTransparent')        #
        # set location of node                                                                     #
        transparent1_node.location = (-60, -120)                                                   #
        # set the default color                                                                    #
        transparent1_node.inputs[0].default_value = (1, 1, 1, 1)                                   #
        # Deselect the Node                                                                        #
        transparent1_node.select = False                                                           #
                                                                                                   #
        ############################################################################ COLUMN 2 ######
        
        #################################################################### FINAL MIX SHADER ######
                                                                                                   #
        # Create the mix shader node and referen it as 'Mix2'                                      #
        mix2_node = material_ghost.node_tree.nodes.new('ShaderNodeMixShader')                      #
        # Setting the Location                                                                     #
        mix2_node.location = (200, 0)                                                              #
        # set the default factor to .5                                                             #
        mix2_node.inputs[0].default_value = 0.50                                                   #
        #deslect the Node                                                                          #
        mix2_node.select = False                                                                   #
                                                                                                   #
        ################################################################### FINAL  MIX SHADER ######
        
        ########################################################################## LINK NODES ######
                                                                                                   #
        # create the link fresnel1 to mix1                                                         #
        material_ghost.node_tree.links.new(fresnel1_node.outputs[0], mix1_node.inputs[0])          #
        # create the link diffuse1 to mix1                                                         #
        material_ghost.node_tree.links.new(diffuse1_node.outputs[0], mix1_node.inputs[1])          #
        # create the link diffuse2 to mix1                                                         #
        material_ghost.node_tree.links.new(diffuse2_node.outputs[0], mix1_node.inputs[2])          #
                                                                                                   #
        # create the link MIX1 to MIX1                                                             #
        material_ghost.node_tree.links.new(mix1_node.outputs[0], mix2_node.inputs[1])              #
        # create the link transparent1 to mix2                                                     #
        material_ghost.node_tree.links.new(transparent1_node.outputs[0], mix2_node.inputs[2])      #
                                                                                                   #
        # create the link MIX2 to OUT                                                              #
        material_ghost.node_tree.links.new(mix2_node.outputs[0], material_output.inputs[0])        #
                                                                                                   #
        ###################################################################### LINK NODES ##########
        
        bpy.context.object.active_material = material_ghost
        
        return{'FINISHED'}
        
        
def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(ShaderMetalicsPanel)
    bpy.utils.register_class(ShaderStylizedPanel)
    
    bpy.utils.register_class(SHADER_OT_DIAMOND)
    bpy.utils.register_class(SHADER_OT_GOLD)
    bpy.utils.register_class(SHADER_OT_SILVER)
    bpy.utils.register_class(SHADER_OT_COPPER)
    bpy.utils.register_class(SHADER_OT_HOLOGRAM)
    bpy.utils.register_class(SHADER_OT_GHOST)
    
def unregiester():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(ShaderMetalicsPanel)
    bpy.utils.unregister_class(ShaderStylizedPanel)
    
    bpy.utils.unregister_class(SHADER_OT_DIAMOND)
    bpy.utils.unregister_class(SHADER_OT_GOLD)
    bpy.utils.unregister_class(SHADER_OT_SILVER)
    bpy.utils.unregister_class(SHADER_OT_COPPER)
    bpy.utils.unregister_class(SHADER_OT_HOLOGRAM)
    bpy.utils.unregister_class(SHADER_OT_GHOST)
    
if __name__ == "__main__":
    register()
    
