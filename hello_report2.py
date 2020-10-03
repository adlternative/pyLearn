# from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import *
from reportlab.lib import colors
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label

data = [
    # year month predicted High  Low
    (2007, 8, 113.2, 114.1, 112.2),
    (2007, 9, 112.8, 115.8, 109.8),
    (2007, 10, 111.0, 116.0, 106.0),
]
d = Drawing(400, 200)
# s = String(50, 50, 'adl\'world', textAnchor="middle")
# d.add(s)
# d.LinePlotadd(PolyLine)
pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
time = [row[0]+row[1]/12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [list(zip(time, pred)),list(zip(time, high)),list(zip(time, low))]
# lp.lines[0].strokeColor =
d.add(lp)

# d.add(PolyLine(list(zip(time, pred)), strokeColor=colors.blue))
# d.add(PolyLine(list(zip(time, high)), strokeColor=colors.red))
# d.add(PolyLine(list(zip(time, low)), strokeColor=colors.green))
d.add(String(250,150, 'Sunspots', fontsize=14, fillColor=colors.red))

renderPDF.drawToFile(d, 'hello.pdf', 'Sunspots')
