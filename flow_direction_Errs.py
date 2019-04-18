import arcpy
import os
arcpy.env.overwriteOutput = True
print("Running....just wait")
arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb"
output="D:\Temp\UAS_for_tool.gdb\endpoint"
arcpy.FeatureVerticesToPoints_management("StrSgmt",output,"END")

in_dataset="D:\Temp\UAS_for_tool.gdb\endpoint"
fields=["Shape","StrID"]
out_table="D:\Temp\UAS_for_tool.gdb\Duplicatetable"
arcpy.FindIdentical_management(in_dataset, out_table, fields, output_record_option="ONLY_DUPLICATES")


arcpy.MakeFeatureLayer_management(in_dataset,"aa")

arcpy.AddJoin_management("aa","OBJECTID",out_table,"IN_FID",)

arcpy.CopyFeatures_management("aa","join")

arcpy.MakeFeatureLayer_management("join","bb")

arcpy.SelectLayerByAttribute_management("bb","NEW_SELECTION","Duplicatetable_IN_FID IS not null")

arcpy.env.workspace=r"D:\Temp\ErrSHP"
arcpy.CopyFeatures_management("bb","flow_Direction_Errs")
print("Process completed")
input("Press any key to Exit")
