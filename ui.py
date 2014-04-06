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
from bpy.props import *
from . import helpers

class OBJECT_OT_MESHCURVE(bpy.types.Operator):
    bl_idname = "keys.mesh_curve"
    bl_label = "Mesh/Curve"
 
    def execute(self, context):
        set_unset = context.scene.o3de.set_unset
        if set_unset == 'Set':
            helpers.set_meshcurve(self, context)    
        elif set_unset == 'Unset':
            helpers.unset_meshcurve(self, context)
        return{'FINISHED'}
        
class OBJECT_OT_VISIBLE(bpy.types.Operator):
    bl_idname = "keys.visible"
    bl_label = "Visible Mesh/Curve"
 
    def execute(self, context):
        set_unset = context.scene.o3de.set_unset
        if set_unset == 'Set':
            helpers.set_visible_meshcurve(self, context)    
        elif set_unset == 'Unset':
            helpers.unset_visible_meshcurve(self, context)
        return{'FINISHED'}
 
class OBJECT_OT_INVISIBLE(bpy.types.Operator):
    bl_idname = "keys.invisible"
    bl_label = "Invisible Mesh/Curve"

    def execute(self, context):
        set_unset = context.scene.o3de.set_unset
        if set_unset == 'Set':
            helpers.set_invisible_meshcurve(self, context)    
        elif set_unset == 'Unset':
            helpers.unset_invisible_meshcurve(self, context)
        return{'FINISHED'}
  
class OBJECT_OT_CAMERALAMP(bpy.types.Operator):
    bl_idname = "keys.camera_lamp"
    bl_label = "Camera/Lamp"
  
    def execute(self, context):
        set_unset = context.scene.o3de.set_unset
        if set_unset == 'Set':
            helpers.set_cameralamp(self, context)    
        elif set_unset == 'Unset':
            helpers.unset_cameralamp(self, context)
        return{'FINISHED'}
 
class OBJECT_OT_SELECTED(bpy.types.Operator):
    bl_idname = "keys.selected"
    bl_label = "Selected"
 
    def execute(self, context):
        set_unset = context.scene.o3de.set_unset
        if set_unset == 'Set':
            helpers.set_selected(self, context)    
        elif set_unset == 'Unset':
            helpers.unset_selected(self, context)
        return{'FINISHED'}
 
class OBJECT_OT_ALL(bpy.types.Operator):
    bl_idname = "keys.all"
    bl_label = "All"

    def execute(self, context):
        set_unset = context.scene.o3de.set_unset
        if set_unset == 'Set':
            helpers.set_all(self, context)    
        elif set_unset == 'Unset':
            helpers.unset_all(self, context)
        return{'FINISHED'}

class OBJECT_OT_TOGGLESELECTED(bpy.types.Operator):
    bl_idname = "toggle.hide_selected"
    bl_label = "Toggle hide"

    def execute(self, context):
        helpers.toggle_hide_selected(self, context)
        return{'FINISHED'}

class OBJECT_OT_INSERTFRAME(bpy.types.Operator):
    bl_idname = "insert.frame"
    bl_label = "Insert Frame"

    def execute(self, context):
        helpers.insert_frame(self, context)
        return{'FINISHED'}
              
class ToolsPanel(bpy.types.Panel):
    bl_label = "O3DE Manual"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        
        o3de = context.scene.o3de
        
        layout = self.layout
        
        box = layout.box()
        
        box.label('Set/Unset Keyframes:')
        
        split = box.split()

        col = split.column()
        col.prop(o3de,'set_location', text="Location")
        col.prop(o3de,'set_rotation', text="Rotation")
        
        col = split.column()
        col.prop(o3de,'set_hide', text="Hide")   
        col.prop(o3de,'set_hide_render', text="Hide Render")   
        
        col = box.column_flow(align=True)
        row = col.row(align=True)
        row.prop(o3de, 'set_unset', text='')
        row.label('Keys')
        
        box.operator("keys.mesh_curve", text='on Mesh/Curves')
        box.operator("keys.visible", text='on Visible Mesh/Curves')
        box.operator("keys.invisible", text='on Invisible Mesh/Curves')
        box.operator("keys.camera_lamp", text='on Camera/Lamp')
        box.operator("keys.selected", text='on Selected')
        box.operator("keys.all", text='on all')    
 
        box = layout.box()
        box.label('Toggle Hide:')
        box.prop(o3de,'toggle_hide', text='Hide')   
        box.prop(o3de,'toggle_hide_render', text='Hide Render')   
        box.operator('toggle.hide_selected', text='Toggle Selected')

        box = layout.box()
        box.label('Insert new Frame:')
        box.prop(o3de,'add_lastframe', text='Check Last Frame')
        box.operator('insert.frame', text='Insert Frame')
