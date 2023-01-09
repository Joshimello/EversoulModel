# modified from blender template

import bpy
import os

basedir = os.path.dirname(bpy.data.filepath)

if not basedir:
    raise Exception("Blend file is not saved")

view_layer = bpy.context.view_layer

# save selected
obj_active = view_layer.objects.active
selection = bpy.context.selected_objects

# deselect all
bpy.ops.object.select_all(action='DESELECT')

# modify all material to opaque
for material in bpy.data.materials:
    material.blend_method = 'OPAQUE'

# each object
for obj in selection:

    obj.select_set(True)
    
    # move the origin to geometry center
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')

    obj.location[0] = 0
    obj.location[1] = 0
    obj.location[2] = 0

    view_layer.objects.active = obj

    name = bpy.path.clean_name(obj.name)
    fn = os.path.join(basedir, name)

    # export object as gltf .glb
    bpy.ops.export_scene.gltf(filepath=fn + ".glb", use_selection=True)

    obj.select_set(False)

    print("written:", fn)

view_layer.objects.active = obj_active

for obj in selection:
    obj.select_set(True)