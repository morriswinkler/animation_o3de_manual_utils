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

bl_info = {
    "name": "O3DE Manual Utils",
    "description": "Toolbar to facilitate the creation of Open Hardware assembly manuals.",
    "author": "Morris Winkler, Bram de Vries",
    "version": (0, 1, 0),
    "blender": (2, 65, 0),
    "location": "3D View > Toolbar",
    "warning": "this is a alpha release", # used for warning icon and text in addons panel
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
                "Scripts/Animation/O3DE_Manual_Utils",
    "category": "Animation"}


if "bpy" in locals():
    imp.reload(ui)
else:
    import bpy
    from bpy.props import (BoolProperty,
                           EnumProperty,
                           PointerProperty,
    )
    from bpy.types import PropertyGroup
                      
    from . import ui


class O3deSettings(PropertyGroup):
    set_unset = EnumProperty(
        name="Set/Unset",
        description="Set Unset Keys",
        items=(('Set', 'Set', ''),
               ('Unset', 'Unset', '')),
        default='Set',
    ) 
    set_location = BoolProperty(
        name="Set location",
        description="Set location key",
        default=True,
    )
    set_rotation = BoolProperty(
        name="Set rotation",
        description="Set rotation key",
        default=True,
    )
    set_hide = BoolProperty(
        name="Set hide",
        description="Set hide key",
        default=True,
    )
    set_hide_render = BoolProperty(
        name="Set hide_render",
        description="Set hide_render key",
        default=True,
    )
    toggle_hide = BoolProperty(
        name="toggle_hide",
        description="Toggle hide",
        default=True,
    )        
    toggle_hide_render = BoolProperty(
        name="toggle_hide_render",
        description="Toggle hide_render",
        default=True,
    )        
    add_lastframe = BoolProperty(
        name="add_lastframe",
        description="Last Keyframe becomes Last Frame",
        default=False,
    )      

classes = (
    ui.ToolsPanel,
    ui.OBJECT_OT_MESHCURVE,
    ui.OBJECT_OT_VISIBLE,
    ui.OBJECT_OT_INVISIBLE,
    ui.OBJECT_OT_CAMERALAMP,
    ui.OBJECT_OT_SELECTED,
    ui.OBJECT_OT_ALL,
    ui.OBJECT_OT_TOGGLESELECTED,
    ui.OBJECT_OT_INSERTFRAME,
    O3deSettings,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.o3de = PointerProperty(type=O3deSettings)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.o3de
