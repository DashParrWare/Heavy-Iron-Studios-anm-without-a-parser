from struct import unpack, pack
import bpy
import math

#30589 / 15 / 10000 = 0.20392666666666667 and the output is this int(0.20392666666666667 * 10000 * 15) = 30589


def SKBAnimExporter(f):
    ob = bpy.context.object
    fcurves2 = bpy.context.active_object.animation_data.action.fcurves
    Magic = f.write(b"SKB1")
    Flags = f.write(pack("<I", 0))
    BoneCount = f.write(pack("<H", len(ob.pose.bones)))
    FrameCount = f.write(pack("<H", bpy.context.scene.frame_end+1))
    keycount = f.write(pack("<I", len(ob.pose.bones)*bpy.context.scene.frame_end*2))
    ScaleX = f.write(pack("<f", bpy.context.active_pose_bone.head.x/32767.0))
    ScaleY = f.write(pack("<f", bpy.context.active_pose_bone.head.y/32767.0))
    ScaleZ = f.write(pack("<f", bpy.context.active_pose_bone.head.z/32767.0))
    framerate=0
    quat_scale = 32767
    for pbone in ob.pose.bones:
        for curve2 in fcurves2:
            KeyframePoints2 = curve2.keyframe_points
        for keyframe in KeyframePoints2:
            Keys = keyframe.co[0]
            bpy.context.scene.frame_set(int(Keys))
            KeyF = f.write(pack("<H", int(keyframe.co[0])))
            RotX = f.write(pack("<h", int(32767*pbone.rotation_quaternion.x)))
            RotY = f.write(pack("<h", int(32767*pbone.rotation_quaternion.y)))
            RotZ = f.write(pack("<h", int(32767*pbone.rotation_quaternion.z)))
            RotW = f.write(pack("<h", int(32767*pbone.rotation_quaternion.w)))
            PosX = f.write(pack("<h", int(pbone.head.x)))
            PosY = f.write(pack("<h", int(pbone.head.y)))
            PosZ = f.write(pack("<h", int(pbone.head.z)))
    for framing in range(bpy.context.scene.frame_start,bpy.context.scene.frame_end*2):
        bpy.context.scene.frame_set(framing)
        framerates = f.write(pack("<f", framerate))
        framerate+=0.0333333350718021
    offset = 0
    for i in range(len(ob.pose.bones)+bpy.context.scene.frame_end*2-2):
        f.write(pack("<H", offset))
        offset+=2
        

def BKSAnimExporter(f):
    ob = bpy.context.object
    fcurves2 = bpy.context.active_object.animation_data.action.fcurves
    Magic = f.write(b"1BKS")
    Flags = f.write(pack(">I", 0))
    BoneCount = f.write(pack(">H", len(ob.pose.bones)))
    FrameCount = f.write(pack(">H", bpy.context.scene.frame_end+1))
    keycount = f.write(pack(">I", len(ob.pose.bones)*bpy.context.scene.frame_end*2))
    ScaleX = f.write(pack(">f", bpy.context.active_pose_bone.head.x/32767.0))
    ScaleY = f.write(pack(">f", bpy.context.active_pose_bone.head.y/32767.0))
    ScaleZ = f.write(pack(">f", bpy.context.active_pose_bone.head.z/32767.0))
    framerate=0
    quat_scale = 32767
    for pbone in ob.pose.bones:
        for curve2 in fcurves2:
            KeyframePoints2 = curve2.keyframe_points
        for keyframe in KeyframePoints2:
            Keys = keyframe.co[0]
            KeyF = f.write(pack(">H", int(keyframe.co[0])))
            bpy.context.scene.frame_set(int(Keys))
            RotX = f.write(pack(">h", int(32767*pbone.rotation_quaternion.x)))
            RotY = f.write(pack(">h", int(32767*pbone.rotation_quaternion.y)))
            RotZ = f.write(pack(">h", int(32767*pbone.rotation_quaternion.z)))
            RotW = f.write(pack(">h", int(32767*pbone.rotation_quaternion.w)))
            PosX = f.write(pack("<h", int(pbone.head.x)))
            PosY = f.write(pack("<h", int(pbone.head.y)))
            PosZ = f.write(pack("<h", int(pbone.head.z)))
            
    for framing in range(bpy.context.scene.frame_start,bpy.context.scene.frame_end*2):
        bpy.context.scene.frame_set(framing)
        framerates = f.write(pack(">f", framerate))
        framerate+=0.0333333350718021
    offset = 0
    for i in range(bpy.context.scene.frame_start,bpy.context.scene.frame_end*2-2):
        f.write(pack("<H", offset))
        offset+=2

def WriteSKBBKS(filepath, CustomSKB=False, CustomBKS=False):
    with open(filepath, "wb") as f:
        if CustomSKB:
            SKBAnimExporter(f)
        if CustomBKS:
            BKSAnimExporter(f)
        
        

        
    
    
