import arcpy
import os
arcpy.env.overwriteOutput = True
print("T1 Running....just wait")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb"


arcpy.Merge_management(["ROAD_CENTERLINE","CART_TRACK"],"mergeRT")

arcpy.FeatureVerticesToPoints_management("mergeRT","mergeRTpnt","BOTH_ENDS")

arcpy.arcpy.MakeFeatureLayer_management("mergeRTpnt","mp")

arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb"
arcpy.arcpy.MakeFeatureLayer_management("StrSgmt","uns")


arcpy.FeatureVerticesToPoints_management("uns","SgmtPot","BOTH_ENDS")

arcpy.DeleteIdentical_management("SgmtPot",["Shape"])

cc="D:\Temp\UAS_for_tool.gdb\spatial_join"

arcpy.SpatialJoin_analysis("SgmtPot","uns",cc )
arcpy.arcpy.MakeFeatureLayer_management("spatial_join","dd")

arcpy.SelectLayerByAttribute_management("dd","NEW_SELECTION","Join_Count=2")

arcpy.SelectLayerByLocation_management("dd", "intersect","mp",0,"REMOVE_FROM_SELECTION")

arcpy.env.workspace=r"D:\Temp\ErrSHP"

arcpy.CopyFeatures_management("dd","split_Err")
print("Process comp")
