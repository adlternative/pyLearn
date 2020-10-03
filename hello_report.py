# from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import *
from reportlab.lib import colors
data = [
# year month predicted High  Low
    (2007, 8, 113.2, 114.1, 112.2),
    (2007, 9, 112.8, 115.8, 109.8),
    (2007, 10, 111.0, 116.0, 106.0),
]
d = Drawing(200, 150)
# s = String(50, 50, 'adl\'world', textAnchor="middle")
# d.add(s)
# d.add(PolyLine)
pred =[row[2]-40 for row in data]
high=[row[3]-40 for row in data]
low=[row[4]-40 for row in data]

time =[200*((row[0]+row[1]/12.0)-2007)-110 for row in data]
d.add(PolyLine(list(zip(time,pred)),strokeColor=colors.blue))
d.add(PolyLine(list(zip(time,high)),strokeColor=colors.red))
d.add(PolyLine(list(zip(time,low)),strokeColor=colors.green))
d.add(String(65,115,'Sunspots',fontsize=18,fillColor=colors.red))
print(list(zip([1,2,3],[4,5,6])))
print(high)
print(low)
print(time)
renderPDF.drawToFile(d, 'hello.pdf', 'Sunspots')
