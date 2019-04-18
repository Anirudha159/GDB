import arcpy
import os
arcpy.env.overwriteOutput = True
print("Running....just wait")
arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb"

fields=["StrID","AdrUtNum"]
out_table="D:\Temp\UAS_for_tool.gdb\DuplicateUnit"
arcpy.FindIdentical_management("AdrUnit", out_table, fields, output_record_option="ONLY_DUPLICATES")


arcpy.MakeFeatureLayer_management("AdrUnit","a")

arcpy.AddJoin_management("a","OBJECTID",out_table,"IN_FID",)

arcpy.CopyFeatures_management("a","joinAU")

arcpy.MakeFeatureLayer_management("joinAU","b")

arcpy.SelectLayerByAttribute_management("b","NEW_SELECTION","DuplicateUnit_IN_FID is not null")

arcpy.env.workspace=r"D:\Temp\ErrSHP"
arcpy.CopyFeatures_management("b","Duplicate_AdrUnit")
print("Process completed")
input("Press any key to Exit")
