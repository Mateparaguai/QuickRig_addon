bl_info = {
    "name": "Save_render_border",
    "description": "",
    "author": "Your Name",
    "version": (0, 0, 1),
    "blender": (2, 76, 8),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object" }

import bpy

curent_scene = bpy.context.screen.scene

curent_scene.render.use_border = True
curent_scene.render.use_crop_to_border = True
render_border_coordinate = {}
render_border_coordinate['min_x'] = curent_scene.render.border_min_x
render_border_coordinate['min_y'] = curent_scene.render.border_min_y
render_border_coordinate['max_x'] = curent_scene.render.border_max_x
render_border_coordinate['max_y'] = curent_scene.render.border_max_y
