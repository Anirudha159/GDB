# -*- coding: utf-8 -*-
import arcpy
import os
arcpy.env.overwriteOutput = True
print("Running....just wait")


arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb"
arcpy.MakeFeatureLayer_management("ROAD_CENTERLINE","a")
arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","StrCls = '01'")

arcpy.FeatureVerticesToPoints_management("a","National_point","BOTH_ENDS")

arcpy.SpatialJoin_analysis("National_point","a","Na_join","JOIN_ONE_TO_ONE","","","INTERSECT")
arcpy.MakeFeatureLayer_management("Na_join","b")
arcpy.SelectLayerByAttribute_management("b","NEW_SELECTION","Join_Count = 1")

arcpy.env.workspace=r"D:\Temp\For_Basemap_Errs"
arcpy.CopyFeatures_management("b","National_classification_Err")



arcpy.DeleteField_management("National_classification_Err.shp",["Join_Count",""])


print("If opportunity doesn't knock, build a door. ")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb"
arcpy.MakeFeatureLayer_management("ROAD_CENTERLINE","a")
arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","StrCls = '02'")

arcpy.FeatureVerticesToPoints_management("a","National_point","BOTH_ENDS")

arcpy.SpatialJoin_analysis("National_point","a","Na_join","JOIN_ONE_TO_ONE","","","INTERSECT")
arcpy.MakeFeatureLayer_management("Na_join","b")
arcpy.SelectLayerByAttribute_management("b","NEW_SELECTION","Join_Count = 1")

arcpy.env.workspace=r"D:\Temp\For_Basemap_Errs"
arcpy.CopyFeatures_management("b","Arterial_classification_Err")
arcpy.DeleteField_management("Arterial_classification_Err.shp",["Join_Count",""])

print("IF YOU CAN'T DO TO GREAT THINGS. DO SMALL THINGS IN A GREAT WAY.,,")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb"
arcpy.MakeFeatureLayer_management("ROAD_CENTERLINE","a")
arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","StrCls = '03'")

arcpy.FeatureVerticesToPoints_management("a","National_point","BOTH_ENDS")

arcpy.SpatialJoin_analysis("National_point","a","Na_join","JOIN_ONE_TO_ONE","","","INTERSECT")
arcpy.MakeFeatureLayer_management("Na_join","b")
arcpy.SelectLayerByAttribute_management("b","NEW_SELECTION","Join_Count = 1")

arcpy.env.workspace=r"D:\Temp\For_Basemap_Errs"
arcpy.CopyFeatures_management("b","Secondary_classification_Err")
arcpy.DeleteField_management("Secondary_classification_Err.shp",["Join_Count",""])

print("IT'S ALL GOOD______Wait while for good results...")



arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb"
arcpy.MakeFeatureLayer_management("ROAD_CENTERLINE","a")
arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","StrCls = '04'")

arcpy.FeatureVerticesToPoints_management("a","National_point","BOTH_ENDS")

arcpy.SpatialJoin_analysis("National_point","a","Na_join","JOIN_ONE_TO_ONE","","","INTERSECT")
arcpy.MakeFeatureLayer_management("Na_join","b")
arcpy.SelectLayerByAttribute_management("b","NEW_SELECTION","Join_Count = 1")
arcpy.env.workspace=r"D:\Temp\For_Basemap_Errs"

arcpy.CopyFeatures_management("b","Distributor_classification_Err")
arcpy.DeleteField_management("Distributor_classification_Err.shp",["Join_Count",""])

print("Process completed....Err path__D:\Temp\For_Basemap_Errs")
