import bpy
import os

basedir = os.path.dirname(bpy.data.filepath)

if not basedir:
    raise Exception("Blend file is not saved")

view_layer = bpy.context.view_layer

obj_active = view_layer.objects.active
selection = bpy.context.selected_objects

bpy.ops.object.select_all(action='DESELECT')

for material in bpy.data.materials:
    material.blend_method = 'OPAQUE'

for obj in selection:

    obj.select_set(True)
    
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')

    view_layer.objects.active = obj

    name = bpy.path.clean_name(obj.name)
    fn = os.path.join(basedir, name)

    bpy.ops.export_scene.gltf(filepath=fn + ".glb", use_selection=True)

    obj.select_set(False)

    print("written:", fn)

view_layer.objects.active = obj_active

for obj in selection:
    obj.select_set(True)