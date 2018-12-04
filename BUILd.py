import arcpy
import os

# Building_without_adrunit.


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

arcpy.CopyFeatures_management("bd","Building_without_adrunit")

print("process_completed...See this path for errSHP___D:\Temp\ErrSHP")
