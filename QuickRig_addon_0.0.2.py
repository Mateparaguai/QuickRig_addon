import bpy

class Bones_Setting(bpy.types.Panel): 
    bl_label = "Bones setting" 
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 

    @classmethod 
    def poll(self, context): 
        if context.object and context.object.type == 'ARMATURE' and bpy.ops.object.mode_set(mode = 'POSE'):
            return len(context.object.data.Bones) 

    def draw(self, context): 
        layout = self.layout
        layout.label("From selected")
        layout.operator("def_on.button") 
        layout.operator("def_off.button") 
        layout.operator("sel_def_dis.button") 

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


class Select_Deform_Disabled(bpy.types.Operator): 
    bl_idname = "sel_def_dis.button" 
    bl_label = "Select all deform disabled" 

    def execute(self, context): 
        all_bones = bpy.context.active_object.data
        for def_bone in all_bones:
            if def_bone.bone.deform == False:
                def_bone.select = True
        return{'FINISHED'} 


bpy.utils.register_module(__name__)

'''
arm = bpy.context.active_object.data
for bone in arm.bones:
    bone.select = False
'''
