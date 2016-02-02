import bpy

class Bones_Setting(bpy.types.Panel): 
    bl_label = "Bones setting" 
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 

    @classmethod 
    def poll(self, context): 
        if context.object and context.object.type == 'ARMATURE': 
            return len(context.object.data.Bones) 

    def draw(self, context): 
        layout = self.layout 
        scn = context.scene 
        layout.operator("def_on.button") 
        layout.operator("def_off.button") 

class Deform_on(bpy.types.Operator): 
    bl_idname = "def_on.button" 
    bl_label = "Deform On" 
   
    def execute(self, context): 
        act_bone = bpy.context.selected_pose_bones 
        for deform in act_bone: 
            deform.bone.use_deform = True 
        return{'FINISHED'} 

class Deform_off(bpy.types.Operator): 
    bl_idname = "def_off.button" 
    bl_label = "Deform Off" 


    def execute(self, context): 
        act_bone = bpy.context.selected_pose_bones 
        for deform in act_bone: 
            deform.bone.use_deform = False 
        return{'FINISHED'} 

bpy.utils.register_module(__name__)
