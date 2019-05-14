import arcpy
import os
arcpy.env.overwriteOutput = True
print("T1 Running....just wait")

arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","wp")

arcpy.PointsToLine_management("wp","ptl","StrID","AdrUtNum")

arcpy.FeatureToLine_management("ptl","ftl","0.001 Meters", "NO_ATTRIBUTES")

arcpy.FeatureVerticesToPoints_management("ptl","ptlpoint","BOTH_ENDS")

arcpy.arcpy.MakeFeatureLayer_management("ptlpoint","ppt")

arcpy.FeatureVerticesToPoints_management("ftl","ftlpoint","BOTH_ENDS")

arcpy.DeleteIdentical_management("ftlpoint",["Shape"])

arcpy.arcpy.MakeFeatureLayer_management("ftlpoint","fpt")

arcpy.SelectLayerByLocation_management("fpt", "intersect","ppt",0,"NEW_SELECTION")

arcpy.SelectLayerByAttribute_management("fpt","SWITCH_SELECTION")


arcpy.SpatialJoin_analysis("fpt","ptl","fptjoin","JOIN_ONE_TO_ONE","KEEP_ALL","","INTERSECT")

arcpy.arcpy.MakeFeatureLayer_management("fptjoin","fj")

arcpy.SelectLayerByAttribute_management("fj","NEW_SELECTION","Join_Count = 1")

arcpy.env.workspace=r"D:\Temp\ErrSHP"

arcpy.CopyFeatures_management("fj","Wrong_position_Adrunit")

arcpy.DeleteField_management("Wrong_position_Adrunit.shp",["Join_Count", "TARGET_FID", "ORIG_FID"])

print("Process completed...")
