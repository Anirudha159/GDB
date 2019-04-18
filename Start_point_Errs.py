import arcpy
import os
arcpy.env.overwriteOutput = True
print("Running....just wait")
arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb"
output="D:\Temp\UAS_for_tool.gdb\dissolve"

arcpy.Dissolve_management("StrSgmt",output,"StrID","","MULTI_PART","DISSOLVE_LINES")

arcpy.FeatureVerticesToPoints_management("dissolve","Startpoint","START")

arcpy.arcpy.MakeFeatureLayer_management("StartEnd","se")

arcpy.arcpy.MakeFeatureLayer_management("Startpoint","sp")

arcpy.SelectLayerByLocation_management("se", 'intersect',"sp",0,"NEW_SELECTION")

arcpy.SelectLayerByAttribute_management("se","SWITCH_SELECTION")

arcpy.env.workspace=r"D:\Temp\ErrSHP"

arcpy.CopyFeatures_management("se","Start_point_Err")
input("Press any key to Exit")
