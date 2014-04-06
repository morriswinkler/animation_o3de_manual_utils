# ##### BEGIN GPL LICENSE BLOCK #####
# animation_o3de_manual_utils.py 
#
# Blender addon with a toolbar to facilitate 
# the creation of Open Source Hardware assembly manuals
#
# Copyright (C) 2014 Morris Winkler <m.winkler@open3dengineering.org>
#
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as 
# published by the Free Software Foundation; either version 2 of 
# the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program; if not, write to the Free Software Foundation, 
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
# ##### END GPL LICENSE BLOCK #####

import bpy

#############################
# helper functions
#############################

# set keyframes
def set_keyframes(context, ob):
    o3de = context.scene.o3de    
    try:
        if o3de.set_location:
            ob.keyframe_insert(data_path='location')
        if o3de.set_rotation:
            ob.keyframe_insert(data_path='rotation_euler')
        if o3de.set_hide:
            ob.keyframe_insert(data_path='hide')
        if o3de.set_hide_render:
            ob.keyframe_insert(data_path='hide_render')
    except RuntimeError:
        pass

    
# unset keyframes
def unset_keyframes(context, ob):
    o3de = context.scene.o3de
    try:
        if o3de.set_location:
            ob.keyframe_delete(data_path='location')
        if o3de.set_rotation:
            ob.keyframe_delete(data_path='rotation_euler')
        if o3de.set_hide:
            ob.keyframe_delete(data_path='hide')
        if o3de.set_hide_render:
            ob.keyframe_delete(data_path='hide_render')
    except RuntimeError:
        pass


# set keys on Mesh/Curve objects
def set_meshcurve(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'MESH' or ob.type == 'CURVE') and context.scene in (x for x in ob.users_scene):
            set_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# unset keys on Mesh/Curve objects        
def unset_meshcurve(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'MESH' or ob.type == 'CURVE') and context.scene in (x for x in ob.users_scene):
            unset_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                    
# set keys on visible Mesh/Curve objects
def set_visible_meshcurve(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'MESH' or ob.type == 'CURVE') and ob.hide == False and context.scene in (x for x in ob.users_scene):
            set_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# unset keys on visible Mesh/Curve objects        
def unset_visible_meshcurve(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'MESH' or ob.type == 'CURVE') and ob.hide == False and context.scene in (x for x in ob.users_scene):
            unset_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# set keys on invisible Mesh/Curve objects
def set_invisible_meshcurve(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'MESH' or ob.type == 'CURVE') and ob.hide == True and context.scene in (x for x in ob.users_scene):
            set_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# unset keys on invisible Mesh/Curve objects        
def unset_invisible_meshcurve(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'MESH' or ob.type == 'CURVE') and ob.hide == True and context.scene in (x for x in ob.users_scene):
            unset_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# set keys on Camer/Lamp objects
def set_cameralamp(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'CAMERA' or ob.type == 'LAMP') and context.scene in (x for x in ob.users_scene):
            set_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# unset keys on Camera/Lamp objects        
def unset_cameralamp(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'CAMERA' or ob.type == 'LAMP') and context.scene in (x for x in ob.users_scene):
            unset_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# set keys on selected objects
def set_selected(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'CAMERA' or ob.type == 'LAMP' or ob.type == 'MESH' or ob.type == 'CURVE') and ob.select == True and context.scene in (x for x in ob.users_scene):
            set_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# unset keys on selected objects        
def unset_selected(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'CAMERA' or ob.type == 'LAMP' or ob.type == 'MESH' or ob.type == 'CURVE') and ob.select == True and context.scene in (x for x in ob.users_scene):
            unset_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# set keys on all objects
def set_all(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'CAMERA' or ob.type == 'LAMP' or ob.type == 'MESH' or ob.type == 'CURVE') and context.scene in (x for x in ob.users_scene):
            set_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# unset keys on all objects        
def unset_all(self, context):
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'CAMERA' or ob.type == 'LAMP' or ob.type == 'MESH' or ob.type == 'CURVE') and context.scene in (x for x in ob.users_scene):
            unset_keyframes(context, ob)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# toggle hide/hide_render on all selected objects
def toggle_hide_selected(self, context):
    o3de = context.scene.o3de
    _objects = context.scene.objects
    for ob in _objects:
        if (ob.type == 'CAMERA' or ob.type == 'LAMP' or ob.type == 'MESH' or ob.type == 'CURVE') and ob.select == True and context.scene in (x for x in ob.users_scene):
            try:
                if o3de.toggle_hide:
                    if ob.hide:
                        ob.hide = False
                    else:        
                        ob.hide = True
                if o3de.toggle_hide_render:
                    if ob.hide_render:
                        ob.hide_render = False
                    else:
                        ob.hide_render = True        
            except RuntimeError:
                pass    

def insert_frame(self, context):
    o3de = context.scene.o3de
    last_frame = 0
    _objects = context.scene.objects
    for ob in _objects:
        if ob.animation_data and context.scene in (x for x in ob.users_scene):
            try:
                for fcurve in ob.animation_data.action.fcurves:
                    for keyframe_point in fcurve.keyframe_points:
                        if keyframe_point.co.x >= context.scene.frame_current:
                            keyframe_point.co.x +=1
                        if keyframe_point.co.x > last_frame:
                            last_frame = keyframe_point.co.x
            except:
                pass
    if o3de.add_lastframe:
        context.scene.frame_end = last_frame                        
