import arcpy
import os

# Allocated point with out building.


arcpy.env.workspace=r"D:\GIS World\MYproject\AS_SEEB_ADDEBM_AU_WP5_6.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","abc")

arcpy.env.workspace=r"D:\GIS World\MYproject\As_Seeb_BASEMAP_WP5.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("BUILDING","ab")

arcpy.env.workspace=r"D:\GIS World\MYproject\As_Seeb_BASEMAP_WP5.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("SHADED_AREA","shad")
                                        
arcpy.env.workspace=r"D:\GIS World\MYproject"
arcpy.SelectLayerByAttribute_management("abc","NEW_SELECTION","AdrType = 'Entrance'")

arcpy.SelectLayerByLocation_management("abc", 'intersect','ab',0,"REMOVE_FROM_SELECTION")

arcpy.SelectLayerByLocation_management("abc", 'intersect','shad',0,"REMOVE_FROM_SELECTION")



arcpy.CopyFeatures_management("abc","allocated_point_without_bld")



#Planned plot with out MOH

arcpy.env.workspace=r"D:\GIS World\MYproject\AS_SEEB_ADDEBM_AU_WP5_6.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","a")

arcpy.env.workspace=r"D:\GIS World\MYproject\MOH"
arcpy.arcpy.MakeFeatureLayer_management("MOH.shp","c")


                                        
arcpy.env.workspace=r"D:\GIS World\MYproject"
arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","AdrType = 'Plot'")

arcpy.SelectLayerByLocation_management("a", 'intersect','c',0,"REMOVE_FROM_SELECTION")



arcpy.CopyFeatures_management("a","plot_without_MOH")
print("process_completed")
