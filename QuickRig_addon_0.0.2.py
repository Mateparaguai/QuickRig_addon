### v1 ###
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
        layout.label("For selected bones")
        layout.operator("def_on.button") 
        layout.operator("def_off.button")
        layout.label("Select deform")
        layout.operator("sel_def_dis.button") 

class Deform_on(bpy.types.Operator): 
    bl_idname = "def_on.button" 
    bl_label = "Enable Deform" 
   
    def execute(self, context): 
        act_bone = bpy.context.selected_pose_bones 
        for deform in act_bone: 
            deform.bone.use_deform = True 
        return{'FINISHED'} 

class Deform_off(bpy.types.Operator): 
    bl_idname = "def_off.button" 
    bl_label = "Disable Deform" 


    def execute(self, context): 
        act_bone = bpy.context.selected_pose_bones 
        for deform in act_bone: 
            deform.bone.use_deform = False 
        return{'FINISHED'} 


class Select_Deform_Disabled(bpy.types.Operator): 
    bl_idname = "sel_def_dis.button" 
    bl_label = "Select all deform On" 

    def execute(self, context): 
        all_bones = bpy.context.active_object.data.bones
        for def_bone in all_bones:
            if def_bone.use_deform == True:
                def_bone.select = True
        return{'FINISHED'} 


bpy.utils.register_module(__name__)

'''
arm = bpy.context.active_object.data
for bone in arm.bones:
    bone.select = False
'''

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
        layout.label("For selected bones")
        layout.operator("def_on.button") 
        layout.operator("def_off.button")
        layout.label("Select deform")
        layout.operator("sel_def_dis.button") 
        layout.label("Create vertex group for selected bones")
        layout.operator("create_bone_groups.button") 

class Deform_on(bpy.types.Operator): 
    bl_idname = "def_on.button" 
    bl_label = "Enable Deform" 
   
    def execute(self, context): 
        act_bone = bpy.context.selected_pose_bones 
        for deform in act_bone: 
            deform.bone.use_deform = True 
        return{'FINISHED'} 

class Deform_off(bpy.types.Operator): 
    bl_idname = "def_off.button" 
    bl_label = "Disable Deform" 


    def execute(self, context): 
        act_bone = bpy.context.selected_pose_bones 
        for deform in act_bone: 
            deform.bone.use_deform = False 
        return{'FINISHED'} 


class Select_Deform_Disabled(bpy.types.Operator): 
    bl_idname = "sel_def_dis.button" 
    bl_label = "Select all deform On" 
 
    def execute(self, context): 
        all_bones = bpy.context.active_object.data.bones
        for def_bone in all_bones:
            if def_bone.use_deform == True:
                def_bone.select = True
        return{'FINISHED'} 

class Select_Deform_Disabled(bpy.types.Operator): 
    bl_idname = "create_bone_groups.button" 
    bl_label = "Create Bone Groups" 

    def execute(self, context): 
        a = bpy.context.selected_objects 
        if a[0].type == 'MESH':
            print(a[0], a[0].type)
            mesh = a[0]
        else:    
            print(a[1], a[1].type)
            mesh = a[1]

        for renamer in bpy.context.selected_pose_bones:
            mesh.vertex_groups.new(name =  renamer.bone.name)
        return{'FINISHED'} 
    
bpy.utils.register_module(__name__)
