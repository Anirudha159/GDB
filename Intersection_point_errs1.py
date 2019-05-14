import arcpy
import os
arcpy.env.overwriteOutput = True
print("Running....just wait")


arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb"
arcpy.Merge_management(["ROAD_CENTERLINE","CART_TRACK"],"Mergeline")
arcpy.MakeFeatureLayer_management("Mergeline","a")
arcpy.MakeFeatureLayer_management("ROAD_INTERSECTION","c")
arcpy.SpatialJoin_analysis("c","a","Na_join","JOIN_ONE_TO_ONE","","","INTERSECT")

arcpy.MakeFeatureLayer_management("Na_join","b")

arcpy.SelectLayerByAttribute_management("b","NEW_SELECTION","Join_Count = 3")



arcpy.SelectLayerByAttribute_management("b","SUBSET_SELECTION","TYPE in ('A major street X-intersection','A mixed major street/access street X-intersection','An access street X-intersection')")
                                        
arcpy.env.workspace=r"D:\Temp\For_Basemap_Errs"
arcpy.CopyFeatures_management("b","Intersection_T_Errs")




print("Running....just wait")


arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb"

arcpy.MakeFeatureLayer_management("Mergeline","a")
arcpy.MakeFeatureLayer_management("ROAD_INTERSECTION","c")
arcpy.SpatialJoin_analysis("c","a","Na_join","JOIN_ONE_TO_ONE","","","INTERSECT")

arcpy.MakeFeatureLayer_management("Na_join","b")

arcpy.SelectLayerByAttribute_management("b","NEW_SELECTION","Join_Count = 4")



arcpy.SelectLayerByAttribute_management("b","SUBSET_SELECTION","TYPE in ('A major street T-intersection','A mixed major street/access street T-intersection','An access street T-intersection')")
                                        
arcpy.env.workspace=r"D:\Temp\For_Basemap_Errs"
arcpy.CopyFeatures_management("b","Intersection_X_Errs")

print("Process completed....")
