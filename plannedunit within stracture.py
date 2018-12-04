import arcpy
import os

# Planned plot with in stracture.


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

arcpy.CopyFeatures_management("adr","Plannedunit_within_stracture")

print("Running....just wait")
