import bpy



class ExplodedBake(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Bake out Texture"
    bl_idname = "OBJECT_PT_exploded_bake" # follow Blender convention for id names
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    #bl_context = "object"
    bl_category = "Create Texture"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        #row.prop(obj, "name")
        row.label(text="Combine to one texture", icon='CUBE')
        
        row = layout.row()
        row.operator("button.explode")


class buttonExplode(bpy.types.Operator):
    bl_idname = "button.explode" # translates to C-name BUTTON_OT_explode
    bl_label = "Create Texture"
    
    obj = bpy.context.object.name
            

    def execute(self, context):
        #self.report({'INFO'}, "Hello world!")
        # Save the name of the FIRST OBJECT
        object1 = bpy.context.object.name  #example BACON
        object2 = object1 + '.H'
        
        #### SECOND OBJECT #### START ####
        # Duplicate the selected objec
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

        bpy.context.object.name = object2    # RENAME

        bpy.ops.object.select_all(action='TOGGLE') # DESELECT SELECT EVERYTHING
        bpy.data.objects[object2].select_set(True) # SELECT HIGH POLY

        print("##########################")
        print("SUBSURF STARTED")
        # Add a Simple | Subsurf modifier | 2 divisions
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].subdivision_type = 'SIMPLE'
        bpy.context.object.modifiers["Subdivision"].levels = 2
        print("SUBSURF COMPLETED")
        print("##########################")

        #### SECOND OBJECT #### END ###
        bpy.ops.object.select_all(action='TOGGLE') # DESELECT SELECT EVERYTHING
        #### FIRST OBJECT #### START ###
        # Reselect the first object
        bpy.data.objects[object1].select_set(True) # SELECT THE ORIGINAL FOR UNWRAPPING
        bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[object1] 

        # Change to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Select everything
        bpy.ops.mesh.select_all(action='SELECT')

        # UV unwrap
        print("##########################")
        print("UV UNWRAP START")
        #bpy.data.window_managers["WinMan"].(null) = 0.15
        bpy.ops.uv.smart_project(island_margin=0.05)
        print("UV UNWRAP COMPLETED")
        print("##########################")
        # Get back into Object mode
        bpy.ops.object.editmode_toggle()
        #### FIRST OBJECT #### END ###

        #### UV baking START ####
        print("##########################")
        print("BAKING START")
        # Select all the things
        bpy.data.objects[object1].select_set(True)
        bpy.data.objects[object2].select_set(True)
        bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[object1] 
        bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[object2] 


        # Change the render engine
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.device = 'GPU'

        # set texTools UV size
        bpy.context.area.ui_type = 'UV'
        bpy.context.scene.texToolsSettings.size_dropdown = '8192'

        # Select the right bake map type
        bpy.context.scene.TT_bake_mode = 'diffuse.png'

        ###### THIS IS BROKEN
        print("READY FOR BAKING SWITCH TO UV Editing")
        bpy.context.scene['TT_bake_mode']
        bpy.ops.uv.textools_bake()  # __init__.py  line 848
        #bpy.ops.uv.textools_bake
        print("BAKING COMPLETED")
        print("##########################")

        # # remove the high res
        print("##########################")
        bpy.data.objects.remove(bpy.data.objects[object2], do_unlink=True)
        print("High RES Object removed")
        print("##########################")
        # #### UV baking END ####

        ### TEXTURE NEEDS TO BE SAVED FIRST

        ### CREATE NEW TEXTURE APPLY 

        # NewMaterial = bpy.data.materials.new("Default")  # make new material

        # bpy.context.object.active_material = NewMaterial # assign it to the object

        # bpy.data.materials["Default"].node_tree.nodes["Principled BSDF"].input[0].



        # bpy.ops.cycles.use_shadding_node()
        
        
        
        
        
        
        return {'FINISHED'}
    
    
# (un-)register entire module, so you don't need to add every class here...
def register():
    bpy.utils.register_class(ExplodedBake)
    bpy.utils.register_class(buttonExplode)

def unregister():
    bpy.utils.unregister_class(ExplodedBake)
    bpy.utils.unregister_class(buttonExplode)
    
if __name__ == "__main__":
    register()
