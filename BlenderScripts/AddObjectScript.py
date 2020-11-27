bl_info = { 
    "name" : "Object Adder",
    "author" : "Bacon salad",
    "version" : (1,0),
    "blender" : (2, 90,0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Mesh",
    }

import bpy

class TestPanel(bpy.types.Panel):
    # The label that will show up in the N-Panel
    bl_label = "Test Panel"
    # ID that other panels can reference
    bl_idname = "PT_TestPanel"
    # The port that the n-panel will show up on
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    # Tab name or reference to other tab it will be at on the n-panel
    bl_category = 'NewTab'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()  # like a new line character
        # give the row a lable and icon
        row.label(text="Add an Object", icon='OBJECT_ORIGIN')
        row = layout.row()  # like a new line character
        # preform action (create a cube) button, show an icon for it
        row.operator("mesh.primitive_cube_add", icon='CUBE')
        row = layout.row()  # like a new line character
        # preform action (create a uv_sphere) button, show an icon for it
        row.operator("mesh.primitive_uv_sphere_add", icon = 'SPHERE')
        row = layout.row()  # like a new line character
        # preform action (create text) button, show an icon for it
        row.operator("object.text_add", icon='OUTLINER_DATA_FONT')

class PanelA(bpy.types.Panel):
    # The label that will show up in the N-Panel
    bl_label = "PanelA"
    # ID that other panels can reference
    bl_idname = "PT_TestPanelA"
    # The port that the n-panel will show up on
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    # Tab name or reference to other tab it will be at on the n-panel
    bl_category = 'NewTab'
    # This is now a sub panel of "bl_parent_id"
    bl_parent_id = 'PT_TestPanel'
    # close all the menus on startup
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="this is panel a", icon='FONT_DATA')
# NAME OF THE PANEL YOU ARE GOING TO ADD PanelA, PanelB, TestPanel
class PanelB(bpy.types.Panel):
    # The label that will show up in the N-Panel
    bl_label = "PanelB"
    # ID that other panels can reference
    bl_idname = "PT_TestPanelB"
    # The port that the n-panel will show up on
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    # Tab name or reference to other tab it will be at on the n-panel
    bl_category = 'NewTab'
    # This is now a sub panel of "bl_parent_id"
    bl_parent_id = "PT_TestPanel"
    # close all the menus on startup
    bl_options = {''}

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="this is Panel B", icon='COLOR_BLUE')
 
# register the classes so they will show up
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA) 
    bpy.utils.register_class(PanelB)
    
def unregister():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA) 
    bpy.utils.register_class(PanelB)
    
if __name__ == "__main__":
    register()