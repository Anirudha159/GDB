import arcpy
import os
arcpy.env.overwriteOutput = True
print("T1 Running....just wait")


arcpy.env.workspace=r"D:\Temp\UAS_for_tool.gdb"
arcpy.arcpy.MakeFeatureLayer_management("StrSgmt","ss")

arcpy.Dissolve_management("ss","Dissolve",["StrID"],"","MULTI_PART","DISSOLVE_LINES")

arcpy.Buffer_analysis("Dissolve","Left_buffer","25 Meters","LEFT","FLAT","LIST",["strID"])

arcpy.arcpy.MakeFeatureLayer_management("AdrUnit","adr")
arcpy.arcpy.MakeFeatureLayer_management("Left_buffer","lb") 

arcpy.SelectLayerByLocation_management("adr", 'intersect',"lb",0,"NEW_SELECTION")

arcpy.SelectLayerByAttribute_management("adr","SUBSET_SELECTION",'MOD("AdrUtNum" ,2)=0')

arcpy.SpatialJoin_analysis("adr","lb","lbjoin","JOIN_ONE_TO_ONE","KEEP_ALL","","INTERSECT")



fieldName = "DtPvdPid"
expression="compare(!StrID!,!StrID_1!)"
codeblock="""def compare(a,b):
    if a==b:
       return 1
    else:
      return 0
"""
arcpy.CalculateField_management("lbjoin", fieldName, expression, "PYTHON_9.3",codeblock)

arcpy.arcpy.MakeFeatureLayer_management("lbjoin","lj")

arcpy.SelectLayerByAttribute_management("lj","NEW_SELECTION","DtPvdPid = 1")

arcpy.env.workspace=r"D:\Temp\ErrSHP"

arcpy.CopyFeatures_management("lj","Wrong_sie_units")

print("Completed..")
