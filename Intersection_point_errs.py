import arcpy
import os
arcpy.env.overwriteOutput = True
print("Running....just wait")


arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb"
arcpy.Merge_management(["ROAD_CENTERLINE","CART_TRACK"],"Mergeline")
arcpy.MakeFeatureLayer_management("Mergeline","a")
arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","StrCls = '05'")
arcpy.MakeFeatureLayer_management("ROAD_INTERSECTION","b")

arcpy.SelectLayerByLocation_management("b","INTERSECT","a","","NEW_SELECTION")

arcpy.SelectLayerByAttribute_management("b","REMOVE_FROM_SELECTION","TYPE in('A mixed major street/access street X-intersection','A mixed major street/access street T-intersection','A mixed major street/access street roundabout (2)','A mixed major street/access street roundabout (3)','A mixed major street/access street roundabout (4)','A mixed major street/access street roundabout (5)','A mixed major street/access street roundabout (6)','A mixed major street/access street roundabout (7)','An access street X-intersection','An access street T-intersection','An access street roundabout (2)','An access street roundabout (3)','An access street roundabout (4)','An access street roundabout (5)','An access street roundabout (6)','An access street roundabout (7)')")

arcpy.env.workspace=r"D:\Temp\For_Basemap_Errs"
arcpy.CopyFeatures_management("b","Intersection_TYPE_field_Err")


arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb"

arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","StrCls not in ( '05' )")
arcpy.MakeFeatureLayer_management("ROAD_INTERSECTION","b")

arcpy.SelectLayerByLocation_management("b","INTERSECT","a","","NEW_SELECTION")

arcpy.SelectLayerByAttribute_management("b","REMOVE_FROM_SELECTION","TYPE in('A mixed major street/access street X-intersection','A mixed major street/access street T-intersection','A mixed major street/access street roundabout (2)','A mixed major street/access street roundabout (3)','A mixed major street/access street roundabout (4)','A mixed major street/access street roundabout (5)','A mixed major street/access street roundabout (6)','A mixed major street/access street roundabout (7)','A major street X-intersection','A major street T-intersection','A major street roundabout (2)','A major street roundabout (3)','A major street roundabout (4)','A major street roundabout (5)','A major street roundabout (6)','A major street roundabout (7)')")

arcpy.env.workspace=r"D:\Temp\For_Basemap_Errs"
arcpy.CopyFeatures_management("b","Intersection_TYPE_field_Err1")

print("Process completed....")
