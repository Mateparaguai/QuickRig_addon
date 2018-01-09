import bpy

class Bones_Setting(bpy.types.Panel): 
    bl_label = "RIG_HELPER" 
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 

    @classmethod 
    def poll(self, context): 
        if context.object and context.object.type == 'ARMATURE' and bpy.ops.object.mode_set(mode = 'POSE'):
            return len(context.object.data.Bones) 

    def draw(self, context): 
        layout = self.layout
        layout.label("For selected bones")
        layout.operator("def_on.button", icon = "CHECKBOX_HLT") 
        layout.operator("def_off.button",  icon = "CHECKBOX_DEHLT")
        layout.label("Select deform")
        layout.operator("sel_def_dis.button", icon = "OUTLINER_OB_ARMATURE") 
        layout.label("Create vertex group for selected bones")
        layout.operator("create_bone_groups.button", icon = "GROUP_VERTEX") 

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

import bpyimport bpy

# POSE MODE PANEL
class Bones_Setting(bpy.types.Panel): 
    bl_label = "RIG_HELPER" 
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 

    def draw(self, context): 
        layout = self.layout
        layout.label("Create bones in origins of selected objects")
        layout.operator("create_arms.button", icon = "GROUP_BONE") 
        layout.label("Delete all consraints for selectes bones")
        layout.operator("Mute_constraints.button", icon = "RESTRICT_VIEW_ON")         
        layout.label("For selected bones")
        layout.operator("def_on.button", icon = "CHECKBOX_HLT") 
        layout.operator("def_off.button",  icon = "CHECKBOX_DEHLT")
        layout.label("Select deform")import bpy

# POSE MODE PANEL
class Bones_Setting(bpy.types.Panel): 
    bl_label = "RIG_HELPER" 
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 

    def draw(self, context): 
        layout = self.layout
        layout.label("Create bones in origins of selected objects")
        layout.operator("create_arms.button", icon = "GROUP_BONE") 
        layout.label("Delete all consraints for selectes bones")
        layout.operator("del_constraints.button", icon = "CONSTRAINT")         
        layout.label("For selected bones")
        layout.operator("def_on.button", icon = "CHECKBOX_HLT") 
        layout.operator("def_off.button",  icon = "CHECKBOX_DEHLT")
        layout.label("Select deform")
        layout.operator("sel_def_dis.button", icon = "OUTLINER_OB_ARMATURE") 
        layout.label("Create vertex group for selected bones")
        layout.operator("create_bone_groups.button", icon = "GROUP_VERTEX") 


class Del_all_constraints(bpy.types.Operator): 
    bl_idname = "del_constraints.button" 
    bl_label = "Delete all constraints" 
   
    def execute(self, context):
        sel_bones = bpy.context.selected_pose_bones

        for i in sel_bones:
            consList = i.constraints
            for n in consList:
                i.constraints.remove(n)
        return{'FINISHED'}        

class Create_arms(bpy.types.Operator): 
    bl_idname = "create_arms.button" 
    bl_label = "Create arms" 
   
    def execute(self, context): 
        sel_objs = bpy.context.selected_objects
        pos = (0.0, 0.0, 0.0)
        #arm = ob.data
    
        for m in sel_objs:
            pos = m.location
            bpy.ops.object.armature_add()
            ob = bpy.context.scene.objects.active
            ob.name = "AR" + m.name
            ob.location = pos
        return{'FINISHED'} 

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
        layout.operator("sel_def_dis.button", icon = "OUTLINER_OB_ARMATURE") 
        layout.label("Create vertex group for selected bones")
        layout.operator("create_bone_groups.button", icon = "GROUP_VERTEX") 


class Del_all_constraints(bpy.types.Operator): 
    bl_idname = "mute_constraints.button" 
    bl_label = "Delete all constraints" 
   
    def execute(self, context):
        sel_bones = bpy.context.selected_pose_bones

        for i in sel_bones:
            consList = i.constraints
            for n in consList:
                i.constraints.remove(n)
        return{'FINISHED'}        

class Create_arms(bpy.types.Operator): 
    bl_idname = "create_arms.button" 
    bl_label = "Create arms" 
   
    def execute(self, context): 
        sel_objs = bpy.context.selected_objects
        pos = (0.0, 0.0, 0.0)
        #arm = ob.data
    
        for m in sel_objs:
            pos = m.location
            bpy.ops.object.armature_add()
            ob = bpy.context.scene.objects.active
            ob.name = "AR" + m.name
            ob.location = pos
        return{'FINISHED'} 

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

# POSE MODE PANEL
class Bones_Setting(bpy.types.Panel): 
    bl_label = "RIG_HELPER" 
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 

    def draw(self, context): 
        layout = self.layout
        layout.label("Create bones in origins of selected objects")
        layout.operator("create_arms.button", icon = "GROUP_BONE") 
        layout.label("For selected bones")
        layout.operator("def_on.button", icon = "CHECKBOX_HLT") 
        layout.operator("def_off.button",  icon = "CHECKBOX_DEHLT")
        layout.label("Select deform")
        layout.operator("sel_def_dis.button", icon = "OUTLINER_OB_ARMATURE") 
        layout.label("Create vertex group for selected bones")
        layout.operator("create_bone_groups.button", icon = "GROUP_VERTEX") 


class Create_arms(bpy.types.Operator): 
    bl_idname = "create_arms.button" 
    bl_label = "Create_arms" 
   
    def execute(self, context): 
        sel_objs = bpy.context.selected_objects
        pos = (0.0, 0.0, 0.0)
        #arm = ob.data
    
        for m in sel_objs:
            pos = m.location
            bpy.ops.object.armature_add()
            ob = bpy.context.scene.objects.active
            ob.name = "AR" + m.name
            ob.location = pos
        return{'FINISHED'} 

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
