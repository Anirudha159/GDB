import arcpy
import os

# Allocated point with out building.


arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","abc")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("BUILDING","ab")

arcpy.env.workspace=r"D:\Temp\Basemap_for_tool.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("SHADED_AREA","shad")
                                        
arcpy.env.workspace=r"D:\Temp\ErrSHP"
arcpy.SelectLayerByAttribute_management("abc","NEW_SELECTION","AdrType = 'Entrance'")

arcpy.SelectLayerByLocation_management("abc", 'intersect','ab',0,"REMOVE_FROM_SELECTION")

arcpy.SelectLayerByLocation_management("abc", 'intersect','shad',0,"REMOVE_FROM_SELECTION")

arcpy.CopyFeatures_management("abc","Entrance_allocated_without_bld")

print("Running....just wait")

#Planned plot with out MOH

arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","a")

arcpy.env.workspace=r"D:\Temp\MOH"
arcpy.arcpy.MakeFeatureLayer_management("MOH.shp","c")

                                      
arcpy.env.workspace=r"D:\Temp\ErrSHP"
arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","AdrType = 'Plot'")

arcpy.SelectLayerByLocation_management("a", 'intersect','c',0,"REMOVE_FROM_SELECTION")


arcpy.CopyFeatures_management("a","Planned_plot_without_MOH")
print("Running....just wait")

# MOH plot with out planned plot

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

arcpy.CopyFeatures_management("y","MOH_with_out_planned_plot")

print("Running....just wait")

#Planned plot within property


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

arcpy.CopyFeatures_management("t","Planned_plot_within_property")
print("process_completed...See this path for errSHP___D:\Temp\ErrSHP")

