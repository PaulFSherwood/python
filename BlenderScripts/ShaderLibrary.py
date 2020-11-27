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
        row.operator('')
        
        
def register():
    bpy.utils.register_class(ShaderMainPanel)
    
def unregiester():
    bpy.utils.unregister_class(ShaderMainPanel)
    
if __name__ == "__main__":
    register()