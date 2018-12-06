import arcpy
import os

print("Running....just wait")

#1.Allocated point with out building.


arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","abc")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("BUILDING","ab")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("SHADED_AREA","shad")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("UNDERCONSTRUCTION_BUILDING","ub")
                                        
arcpy.env.workspace=r"D:\Temp\ErrSHP"
arcpy.SelectLayerByAttribute_management("abc","NEW_SELECTION","AdrType = 'Entrance'")

arcpy.SelectLayerByLocation_management("abc", 'intersect','ab',0,"REMOVE_FROM_SELECTION")

arcpy.SelectLayerByLocation_management("abc", 'intersect','shad',0,"REMOVE_FROM_SELECTION")

arcpy.SelectLayerByLocation_management("abc", 'intersect','ub',0,"REMOVE_FROM_SELECTION")

arcpy.CopyFeatures_management("abc","1_Entrance_allocated_without_bld")

print("Running....just wait")

#2.Planned plot with out MOH

arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","a")

arcpy.env.workspace=r"D:\Temp\MOH"
arcpy.arcpy.MakeFeatureLayer_management("MOH.shp","c")

                                      
arcpy.env.workspace=r"D:\Temp\ErrSHP"
arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","AdrType = 'Plot'")

arcpy.SelectLayerByLocation_management("a", 'intersect','c',0,"REMOVE_FROM_SELECTION")


arcpy.CopyFeatures_management("a","2_Planned_plot_without_MOH")
print("Running....just wait")

#3.MOH plot with out planned plot

arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","x")

arcpy.env.workspace=r"D:\Temp\MOH"
arcpy.arcpy.MakeFeatureLayer_management("MOH.shp","y")

                                      
arcpy.env.workspace=r"D:\Temp\ErrSHP"
arcpy.SelectLayerByAttribute_management("x","NEW_SELECTION","AdrType = 'Plot'")

arcpy.SelectLayerByLocation_management("y", 'intersect',"a",0,"NEW_SELECTION")

arcpy.SelectLayerByAttribute_management("y","SWITCH_SELECTION")

arcpy.SelectLayerByAttribute_management("x","NEW_SELECTION","AdrStat = 'Allocated'")

arcpy.SelectLayerByLocation_management("y", 'intersect','x',0,"REMOVE_FROM_SELECTION")

arcpy.SelectLayerByAttribute_management("y","REMOVE_FROM_SELECTION",'"Shape_Area" <=10.00')

arcpy.CopyFeatures_management("y","3_MOH_with_out_planned_plot")

print("Running....just wait")

#4.Planned plot within property


arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","r")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("BUILDING","s")

arcpy.env.workspace=r"D:\Temp\MOH"
arcpy.arcpy.MakeFeatureLayer_management("MOH.shp","t")

                                      
arcpy.env.workspace=r"D:\Temp\ErrSHP"
arcpy.SelectLayerByAttribute_management("r","NEW_SELECTION","AdrType = 'Plot'")

arcpy.SelectLayerByLocation_management("t", 'intersect',"r",0,"NEW_SELECTION")

arcpy.SelectLayerByLocation_management("t",'CONTAINS',"s",0,"SUBSET_SELECTION")

arcpy.CopyFeatures_management("t","4_Planned_plot_within_property")


print("Running....just wait")


#5.Planned plot with in stracture.


arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","adr")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("BUILDING","bui")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("SHADED_AREA","sha")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("UNDERCONSTRUCTION_BUILDING","und")
                                        
arcpy.env.workspace=r"D:\Temp\ErrSHP"


arcpy.SelectLayerByLocation_management("adr", 'intersect','bui',0,"NEW_SELECTION")

arcpy.SelectLayerByLocation_management("adr", 'intersect','sha',0,"ADD_TO_SELECTION")

arcpy.SelectLayerByLocation_management("adr", 'intersect','und',0,"ADD_TO_SELECTION")

arcpy.SelectLayerByAttribute_management("adr","REMOVE_FROM_SELECTION"," AdrType in ('Entrance','Other') ")

arcpy.CopyFeatures_management("adr","5_Plannedunit_within_stracture")

print("Running....just wait")


#6.Building_without_adrunit.


arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","ad")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("BUILDING","bd")

arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\Issue"
arcpy.arcpy.MakeFeatureLayer_management("Issue","ie")
                                        
arcpy.env.workspace=r"D:\Temp\ErrSHP"

arcpy.SelectLayerByLocation_management("bd", 'intersect',"ad",0,"NEW_SELECTION")

arcpy.SelectLayerByAttribute_management("bd","SWITCH_SELECTION")

arcpy.SelectLayerByLocation_management("bd", 'intersect',"ie",0,"REMOVE_FROM_SELECTION")

arcpy.CopyFeatures_management("bd","6_Building_without_adrunit")

print("Running....just wait")


#7.Wall_Fence_Errors

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("WALLS","wa")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("FENCES","fe")
cc="D:\Temp\UAS_for_tool.gdb\wall_err"
arcpy.FeatureToPolygon_management(["wa","fe"],cc)

arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb"

arcpy.arcpy.MakeFeatureLayer_management("wall_err","we")

arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","aaaa")

arcpy.SelectLayerByAttribute_management("aaaa","NEW_SELECTION","AdrStat = 'Allocated'")

arcpy.SelectLayerByLocation_management("we", 'intersect','aaaa',0,"NEW_SELECTION")

arcpy.SelectLayerByAttribute_management("we","SWITCH_SELECTION")

arcpy.env.workspace=r"D:\Temp\ErrSHP"

arcpy.CopyFeatures_management("we","7_Wall_Fence_Errors")

print("Running....just wait")


#8.More_then_1_allocaed_adr_in_building


arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","aaa")

arcpy.SelectLayerByAttribute_management("aaa","NEW_SELECTION","AdrStat = 'Allocated'")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("BUILDING","bbb")

cc="D:\Temp\UAS_for_tool.gdb\spatial_join_bld"

arcpy.SpatialJoin_analysis("bbb","aaa",cc )

arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb"

arcpy.arcpy.MakeFeatureLayer_management("spatial_join_bld","ddd")

arcpy.SelectLayerByAttribute_management("ddd","NEW_SELECTION","Join_Count >1")

arcpy.env.workspace=r"D:\Temp\ErrSHP"

arcpy.CopyFeatures_management("ddd","8_More_then_1_allocaed_adr_in_building")

print("Running....just wait")


# More_then_1_adr_in_planned_plot


arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","aa")

arcpy.SelectLayerByAttribute_management("aa","NEW_SELECTION","AdrType = 'Allocated'")

arcpy.env.workspace=r"D:\GIS World\MYproject\MOH"
arcpy.arcpy.MakeFeatureLayer_management("MOH.shp","bb")

cc="D:\Temp\UAS_for_tool.gdb\spatial_join"

arcpy.SpatialJoin_analysis("bb","aa",cc )

arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb"

arcpy.arcpy.MakeFeatureLayer_management("spatial_join","dd")

arcpy.SelectLayerByAttribute_management("dd","NEW_SELECTION","Join_Count >1")

arcpy.env.workspace=r"D:\Temp\ErrSHP"

arcpy.CopyFeatures_management("dd","9_More_then_1_adr_in_planned_plot")



print("process_completed...See this path for errSHP___D:\Temp\ErrSHP")
