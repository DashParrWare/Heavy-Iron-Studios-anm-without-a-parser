bl_info = {
        'name'			: 'The Incredibles Animations',
	'author'		: 'DashParr Ware',
	'version'		: (0, 1, 0),
	'blender'		: (3, 0, 0),
	'location'		: 'File > Export',
	'description'           : 'Exports anm files',
	'category'		: 'Animation-Exporter',
}
import os
import bpy
import importlib
from bpy.props import CollectionProperty, StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper


from.import SKB_Exporter

class ExportIncrediblesAnm(bpy.types.Operator, ExportHelper):
        bl_idname = 'skbbksexp.anm'
        bl_label   = 'SKBBKS ANM'
        filename_ext = '.anm'
        files: CollectionProperty(
		name	    = 'File Path',
		description = 'File path used for finding the anm file.',
		type	    = bpy.types.OperatorFileListElement
	)
        CustomSKB: BoolProperty(
                name = "SKB",
                description = ""
        )
        CustomBKS: BoolProperty(
                name = "BKS",
                description = ""
        )
        directory: StringProperty()
        def execute(self, context):
                importlib.reload(SKB_Exporter)
                SKB_Exporter.WriteSKBBKS(self.filepath, CustomSKB = self.CustomSKB, CustomBKS = self.CustomBKS)
                return {'FINISHED'}
        
def menu_func_export(self, context):
	self.layout.operator(ExportIncrediblesAnm.bl_idname, text='Incredibles Anm (.anm)')

def register():
        bpy.utils.register_class(ExportIncrediblesAnm)
        bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
def unregister():
        bpy.utils.unregister_class(ExportIncrediblesAnm)
        bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
if __name__ == '__main__': register()
