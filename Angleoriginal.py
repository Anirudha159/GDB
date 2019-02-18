import arcpy  
import math  
from arcpy import env  
  
# Set environment settings  
print "Calculating angle of polygons"  
arcpy.env.workspace = "D:\GIS World\MYproject\For_pyhon\BAWSHAR_DATACAP_CHUPD_WP17_4.gdb"  
  
inFeatures = "D:\GIS World\MYproject\For_pyhon\BAWSHAR_DATACAP_CHUPD_WP17_4.gdb\STRUCTURES\BUILDING"

arcpy.MakeFeatureLayer_management(inFeatures, "abc")

arcpy.SelectLayerByAttribute_management ("abc", "NEW_SELECTION", "STATUS <> 'CAT3'")

arcpy.CopyFeatures_management("abc", "For_angle")
  
#Turn Polygon into Polyline in scratch workspace  
arcpy.PolygonToLine_management ("For_angle", "polygon2polyline")  
  
#explode polyline into individual lines  
arcpy.SplitLine_management ("polygon2polyline",  "explodedLine")  
  
#convert polygon vertices to points  
arcpy.FeatureVerticesToPoints_management ("For_angle", "Poly2Point")  
  
  
# Set local variables  
  
fieldName = "Angle"  
expression = "GetAzimuthPolyline(!Shape!)"  
codeblock = """def GetAzimuthPolyline(shape):  
    radian = math.atan((shape.lastpoint.x - shape.firstpoint.x)/(shape.lastpoint.y - shape.firstpoint.y))  
    degrees = radian * 180 / math.pi  
    return degrees"""  
  
# Execute AddField  
arcpy.AddField_management("explodedLine", fieldName, "Long",6)  
arcpy.AddField_management("Poly2Point", fieldName, "Long",6 )  
  
# Execute CalculateField   
arcpy.CalculateField_management("explodedLine", fieldName, expression, "PYTHON_9.3", codeblock)

expression="replaceNull( !Angle! )"
codeblock="""def replaceNull(x):
  if x is None:
    return 0
  else:
    return x"""

arcpy.CalculateField_management("explodedLine", fieldName, expression, "PYTHON_9.3",codeblock)

expression="values(!Angle!)"
codeblock="""def values(n):
    if n < 0:
        return n * -1
    else:
        return n"""

arcpy.CalculateField_management("explodedLine", fieldName, expression, "PYTHON_9.3",codeblock)

# Make Poly2Point and explodedLine a layer file so that select by attribute can read it  
  
arcpy.MakeFeatureLayer_management("Poly2Point", "Poly2Point_lyr")  
  
arcpy.MakeFeatureLayer_management("explodedLine", "explodedLine_lyr")  
  
#Identify how many vertices need to be calculated  
  
numb_vertices = int(arcpy.GetCount_management("Poly2Point_lyr").getOutput(0))   
print "Need some time to calculate %d nos of angle" % numb_vertices
  
#Loop through each vertex by OBJECTID  
  
for i in range (1, numb_vertices):  
    obj = "OBJECTID=%s" %(i)  
  
    arcpy.SelectLayerByAttribute_management ("Poly2Point_lyr", "NEW_SELECTION", obj)  
  
#select the two exploded lines from which to calculate the vertex angle  
  
    arcpy.SelectLayerByLocation_management ("explodedLine_lyr", "INTERSECT","Poly2Point_lyr", "", "NEW_SELECTION")  
  
#Export those lines to a new feature class  
  
    #arcpy.FeatureClassToFeatureClass_conversion ("explodedLine_lyr", "D:\GIS World\MYproject\For_pyhon\BAWSHAR_DATACAP_CHUPD_WP17_4.gdb", "calc_values")  
  
#Create List to do angle math  
  
    Angle_math = []  
  
#Return Angle_Values  
  
    rows = arcpy.SearchCursor ("explodedLine_lyr","","","Angle")  
  
    current_Angle_Object = ""  
  
#Iterate through the rows in the cursor and add them to the list  
  
    for row in rows:  
            if current_Angle_Object !=row.Angle:  
                current_Angle_Object = row.Angle  
            Angle_math.append(row.Angle)  
#Calculate the angle at the vertex  
    if len(Angle_math)==0:
        Angle_Final=0
    else:    
        Angle_Final = 180 - Angle_math[0] - Angle_math[1]  
    #del row  
    del rows  
  
    print(Angle_Final)  
  
#add data to the layer file  
  
    rows = arcpy.UpdateCursor("Poly2Point_lyr")  
    for row in rows:  
        row.Angle = Angle_Final  
        rows.updateRow(row)  
    del row  
    del rows  
    del Angle_math
    
#Export all the final angles in Poly2Point_lyr to a feature class
arcpy.MakeFeatureLayer_management("Poly2Point", "a")    
arcpy.SelectLayerByAttribute_management ("a", "NEW_SELECTION", 'Angle >=91 AND Angle <=95 OR Angle >=85 AND Angle <=89')  
arcpy.CopyFeatures_management("a", "angle_Err")  
