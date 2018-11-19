# MOH plot with out planned plot
import arcpy
arcpy.env.workspace=r"D:\GIS World\MYproject\AS_SEEB_ADDEBM_AU_WP5_6.gdb\UAS"
arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","a")

arcpy.env.workspace=r"D:\GIS World\MYproject\MOH"
arcpy.arcpy.MakeFeatureLayer_management("MOH.shp","c")

                                      
arcpy.env.workspace=r"D:\GIS World\MYproject"
arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","AdrType = 'Plot'")

arcpy.SelectLayerByLocation_management("c", 'intersect',"a",0,"NEW_SELECTION")

arcpy.SelectLayerByAttribute_management("c","SWITCH_SELECTION")

arcpy.SelectLayerByAttribute_management("a","NEW_SELECTION","AdrStat = 'Allocated'")

arcpy.SelectLayerByLocation_management("c", 'intersect','a',0,"REMOVE_FROM_SELECTION")

arcpy.SelectLayerByAttribute_management("c","REMOVE_FROM_SELECTION",'"Shape_Area" <=10.00')

arcpy.CopyFeatures_management("c","MOH_with_out_planned_plot")
print("process_completed")
