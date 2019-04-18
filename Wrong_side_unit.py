import arcpy
import os
arcpy.env.overwriteOutput = True
print("Running....just wait")
#for odd number
arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb"

arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","au")

arcpy.SelectLayerByAttribute_management("au","NEW_SELECTION","MOD(AdrUtNum,2)= 1")


arcpy.PointsToLine_management("au","pointtoline","StrID","AdrUtNum")


arcpy.SplitLine_management("pointtoline","splitline")

arcpy.SpatialJoin_analysis("splitline","StrSgmt","sjoin","JOIN_ONE_TO_ONE","KEEP_ALL","","INTERSECT")

fieldName = "DtPvdPid"
expression="compare(!StrID!,!StrID_1!)"
codeblock="""def compare(a,b):
    if a==b:
       return 1
    else:
      return 0
"""

arcpy.CalculateField_management("sjoin", fieldName, expression, "PYTHON_9.3",codeblock)

arcpy.arcpy.MakeFeatureLayer_management("sjoin","sj")

arcpy.SelectLayerByAttribute_management("sj","NEW_SELECTION","DtPvdPid = 1")


#For even number.

arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb"

arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","au1")

arcpy.SelectLayerByAttribute_management("au1","NEW_SELECTION","MOD(AdrUtNum,2)= 0")


arcpy.PointsToLine_management("au1","pointtoline1","StrID","AdrUtNum")


arcpy.SplitLine_management("pointtoline1","splitline1")

arcpy.SpatialJoin_analysis("splitline1","StrSgmt","sjoin1","JOIN_ONE_TO_ONE","KEEP_ALL","","INTERSECT")

fieldName = "DtPvdPid"
expression="compare(!StrID!,!StrID_1!)"
codeblock="""def compare(a,b):
    if a==b:
       return 1
    else:
      return 0
"""

arcpy.CalculateField_management("sjoin1", fieldName, expression, "PYTHON_9.3",codeblock)

arcpy.arcpy.MakeFeatureLayer_management("sjoin1","sj1")

arcpy.SelectLayerByAttribute_management("sj1","NEW_SELECTION","DtPvdPid = 1")


arcpy.env.workspace=r"D:\Temp\ErrSHP"

arcpy.Merge_management(["sj1","sj"],"Wrong_side_unit")
print("Process completed")
