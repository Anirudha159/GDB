#Planned plot within property
import arcpy
arcpy.env.workspace=r"D:\GIS World\MYproject\AS_SEEB_ADDEBM_AU_WP5_6.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","a")

arcpy.env.workspace=r"D:\GIS World\MYproject\As_Seeb_BASEMAP_WP5.gdb\STRUCTURES"
arcpy.arcpy.MakeFeatureLayer_management("BUILDING","ab")

arcpy.env.workspace=r"D:\GIS World\MYproject\MOH"
arcpy.arcpy.MakeFeatureLayer_management("MOH.shp","c")

                                      
arcpy.env.workspace=r"D:\GIS World\MYproject"
arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","AdrType = 'Plot'")

arcpy.SelectLayerByLocation_management("c", 'intersect',"a",0,"NEW_SELECTION")

arcpy.SelectLayerByLocation_management("c",'CONTAINS',"ab",0,"SUBSET_SELECTION")

arcpy.CopyFeatures_management("c","MOH_with_out_planned_plot")
print("process_completed")
