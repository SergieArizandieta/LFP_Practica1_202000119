import os
RGeneral =""
Rasc =""
Rdesc =""
Ravg =""
Rmin =""
Rmax =""
Rapr =""
Rrep =""

ReportGeneral=""
Reporteasc =""
Reportedesc =""
Reporteavg =""
Reportemin =""
Reportemax =""
Reporteapr =""
Reporterep =""

#Muestra los reportes en consola
def MostrarReportsConsole():
    global htmlContenido
    htmlContenido = ""


    htmlContenido = ReportGeneral
    print(RGeneral+ "\n\nREPORTES")
    if Rasc.__eq__(""):
        "No hay nada"
    else:
        print("\nAscendente:\n",Rasc)
        htmlContenido +='<h6 class=\"titulos\" ><b> Ascendente </b></h6>'
        htmlContenido += Reporteasc
    if Rdesc.__eq__(""):
        "No hay nada"
    else:
        print("\nDecendente:\n",Rdesc)
        htmlContenido +='<h6 class=\"titulos\" ><b> Decendente </b></h6>'
        htmlContenido += Reportedesc
    if Ravg.__eq__(""):
        "No hay nada"
    else:
        htmlContenido +='<h6 class=\"titulos\" ><b> Promedio </b></h6>'
        htmlContenido += Reporteavg
        print("\nPromedio:\n",Ravg)
    if Rmin.__eq__(""):
        "No hay nada"
    else:
        htmlContenido +='<h6 class=\"titulos\" ><b> Menor Nota </b></h6>'
        htmlContenido += Reportemin
        print("\nNota menor:\n",Rmin)
    if Rmax.__eq__(""):
        "No hay nada"
    else:
        htmlContenido +='<h6 class=\"titulos\" ><b> Mayor Nota </b></h6>'
        htmlContenido += Reportemax
        print("\nNota mayor:\n",Rmax)
    if Rapr.__eq__(""):
        "No hay nada"
    else:
        htmlContenido +='<h6 class=\"titulos\" ><b> Aprobados </b></h6>'
        htmlContenido += Reporteapr
        print("\nAprobados:\n",Rapr)
    if Rrep.__eq__(""):
        "No hay nada"
    else:
        htmlContenido +='<h6 class=\"titulos\" ><b> Reprobados </b></h6>'
        htmlContenido += Reporterep
        print("\nReprobados:\n",Rrep)

#Contruye el reporte general de los datos
def ReporteG(lista,cantDatos):
    global RGeneral
    RGeneral=""
    global ReportGeneral
    ReportGeneral=""

    for a in lista:
        RGeneral += ("\nRegistro de Datos Ingresados\n")

    RGeneral += ("\nCurso:" +  str(a.titulo) + " con: " + str(cantDatos) + " alumnos\n")

    for x in range(0,cantDatos):
        RGeneral += ("\nNombre: "+ str( a.Registros[x][0])+" Nota: " + str(a.Registros[x][1]))
    #print(RGeneral)
    ReportGeneral='''<table class="steelBlueCols">
    <thead>
   <tr> <th>Nombre</th> <th>Nota</th></tr>
    </thead>
    <tbody>
   <tr> '''
    for x in range(0,cantDatos):
        ReportGeneral += "<td>" + str(a.Registros[x][0]) + "</td>"
        ReportGeneral += "<td " + Marcador(float(a.Registros[x][1])) + ">" + str(a.Registros[x][1]) + "</td></tr>"
    ReportGeneral += "</tbody></table>"

#Marcador de aprobado o desaprobado
def Marcador(Nota):
    if Nota<61:
        color = ' style="background-color:#D41608;"'
        return color
    else:
        color = ' style="background-color:#058FD2;"'
        return color

#Contruye el reporte para ascendentes
def Reportasc(asc,cantDatos):
    global Rasc
    Rasc=""

    global Reporteasc
    Reporteasc=""
    for x in range(0,cantDatos):
        Rasc +=  str("Nombre: " + asc[x][0] + " Nota: " + asc[x][1] + "\n") 
    #print(Rasc)
    Reporteasc='''<table class="steelBlueCols">
    <thead>
   <tr> <th>Nombre</th> <th>Nota</th></tr>
    </thead>
    <tbody>
   <tr> '''
    for x in range(0,cantDatos):
        Reporteasc += "<td>" + str(asc[x][0]) + "</td>"
        Reporteasc += "<td>" + str(asc[x][1]) + "</td></tr>"
    Reporteasc += "</tbody></table>"

#Contruye el reporte para decendentes
def Reportdesc(desc,cantDatos):
    global Rdesc
    Rdesc=""
    global Reportedesc
    Reportedesc=""
    for x in range(0,cantDatos):
        Rdesc += str("Nombre: "+ desc[x][0]+" Nota: " +desc[x][1]+ "\n")
    #print(Rdesc)
    Reportedesc='''<table class="steelBlueCols">
    <thead>
   <tr> <th>Nombre</th> <th>Nota</th></tr>
    </thead>
    <tbody>
   <tr> '''
    for x in range(0,cantDatos):
        Reportedesc += "<td>" + str(desc[x][0]) + "</td>"
        Reportedesc += "<td>" + str(desc[x][1]) + "</td></tr>"
    Reportedesc += "</tbody></table>"

#Contruye el reporte para promedio
def Reportavg(avg):
    global Reporteavg
    Reporteavg=""
    global Ravg
    Ravg = ('El promedio es de: '+ str(avg) + "\n")
    #print(Ravg)
    Reporteavg += '''<table class="steelBlueCols">
    <thead>
   <tr> <th>Promedio</th></tr>
    </thead>
    <tbody>
   <tr> '''
    Reporteavg += "<td>" + str(avg) + "</td></tr>"
    Reporteavg += "</tbody></table>"

#Contruye el reporte para la menor nota
def Reportmin(min,nombre):
    global Reportemin
    Reportemin=""
    global Rmin
    Rmin = str("La nota mas baja es " + str(min)+" De: " + nombre + "\n")
    #print(Rmin)
    Reportemin += '''<table class="steelBlueCols">
    <thead>
   <tr> <th>Nombre</th><th>Nota</th></tr>
    </thead>
    <tbody>
   <tr> '''
    Reportemin += "<td>" + str(nombre) + "</td><td>" +  str(min) + "</td></tr>"
    Reportemin += "</tbody></table>"

#Contruye el reporte para la mayor nota
def Reportmax(max,nombre):
    global Reportemax
    Reportemax=""
    global Rmax
    Rmax = ("La nota mas alta es: " + str(max) + " De: " + nombre  + "\n")
    #print(Rmax)
    Reportemax += '''<table class="steelBlueCols">
    <thead>
   <tr> <th>Nombre</th><th>Nota</th></tr>
    </thead>
    <tbody>
   <tr> '''
    Reportemax += "<td>" + str(nombre) + "</td><td>" +  str(max) + "</td></tr>"
    Reportemax += "</tbody></table>"

#Contruye el reporte para los aprobados
def Reporapr(ganaron,cantGanaron):
    global Reporteapr
    Reporteapr=""
    global Rapr
    Rapr= ""
    for x in range(0,cantGanaron):
        Rapr += str("Nombre: " + ganaron[x][0] + " Nota: " + ganaron[x][1]+'\n') 
    #print(Rapr)        
    Reporteapr='''<table class="steelBlueCols">
    <thead>
   <tr> <th>Nombre</th> <th>Nota</th></tr>
    </thead>
    <tbody>
   <tr> '''
    for x in range(0,cantGanaron):
        Reporteapr += "<td>" + str(ganaron[x][0]) + "</td>"
        Reporteapr += "<td>" + str(ganaron[x][1]) + "</td></tr>"
    Reporteapr += "</tbody></table>"
      
#Contruye el reporte para los reprobados       
def Reporrep(perdieron,cantPerdieron):
    global Reporterep
    Reporterep=""
    global Rrep
    Rrep = ""
    for x in range(0,cantPerdieron):
        Rrep += str("Nombre: "+ perdieron[x][0]+" Nota: "+perdieron[x][1]+"\n")
    #print(Rrep)   
    Reporterep='''<table class="steelBlueCols">
    <thead>
   <tr> <th>Nombre</th> <th>Nota</th></tr>
    </thead>
    <tbody>
   <tr> '''
    for x in range(0,cantPerdieron):
        Reporterep += "<td>" + str(perdieron[x][0]) + "</td>"
        Reporterep += "<td>" + str(perdieron[x][1]) + "</td></tr>"
    Reporterep += "</tbody></table>"

#Contruye el reporte final  
def ReportesSolicitados():
    htmlcompleto = htmlInicial + htmlContenido + htmlFinal
    return htmlcompleto

#Genera el Reporte
def GenerarReportes():
    try: 
        ReportesSolicitados()

        FileHTML=open("./Reportes/datos.HTML","w") 
        FileHTML.write(ReportesSolicitados()) 
        FileHTML.close() 

        FileCSS=open("./Reportes/css/styles.css","w") 
        FileCSS.write(css) 
        FileCSS.close() 
    except:
        print("La creación del Reporte falló")
    else:
         print("Se ha creado el Reporte" )

htmlContenido = str

htmlInicial = """<!DOCTYPE html>
<html>

<!--Encabezado-->
<head>
<meta charset="UTF-8">
<meta name="name" content="Reporte">
<meta name="description" content="name">
<meta name="keywods" content="python,dos,tres">
<meta name="robots" content="Index, Follow">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="css/styles.css"/>
<title>Reporte</title>
</head>
<!----Curerpo--->
<body>
   <center><h6 class=\"titulos\" ><b> Reportes </b></h6>"""

htmlFinal = """<br><footer style="background-color:white;">Creado por: Sergie Daniel Arizandieta Yol - 202000119</footer>
</center></body>
</html>"""

htmlcompleto = ""


css = """body{
background-image: url(https://fondosmil.com/fondo/9859.jpg);
background-attachment:fixed;
background-repeat:no-repeat;
background-size:cover;
background-position: center center;
background-color:white;}	
table.steelBlueCols {
  border: 4px solid #555555;
  background-color: #555555;
  width: 400px;
  text-align: center;
  border-collapse: collapse;
}
table.steelBlueCols td, table.steelBlueCols th {
  border: 1px solid #000000;
  padding: 5px 10px;
}
table.steelBlueCols tbody td {
  font-size: 20px;
  font-weight: bold;
  color: #FFFFFF;
}
table.steelBlueCols td:nth-child(even) {
  background: #398AA4;
}
table.steelBlueCols thead {
  background: #1693A4;
  background: -moz-linear-gradient(top, #50aebb 0%, #2d9dad 66%, #1693A4 100%);
  background: -webkit-linear-gradient(top, #50aebb 0%, #2d9dad 66%, #1693A4 100%);
  background: linear-gradient(to bottom, #50aebb 0%, #2d9dad 66%, #1693A4 100%);
}
table.steelBlueCols thead th {
  font-size: 15px;
  font-weight: bold;
  color: #FFFFFF;
  text-align: center;
  border-left: 2px solid #398AA4;
}
table.steelBlueCols thead th:first-child {
  border-left: none;
}
table.steelBlueCols tfoot td {
  font-size: 13px;
}
table.steelBlueCols tfoot .links {
  text-align: right;
}
table.steelBlueCols tfoot .links a{
  display: inline-block;
  background: #FFFFFF;
  color: #398AA4;
  padding: 2px 8px;
  border-radius: 5px;
}
/*Textos*/
.titulos{
color: white;
background:black;
width:40%;} 
.SUBtitulos{
color: black;
background:white;
text-align:center; 
width:80%;} 
.text{text-align:justify;
background-color:yellow;
color:black; }
.tipos{
	background-color:purple;
	color:white;	
}
h6{
  border: red 2px solid;
  margin: 20px;
font-weight: none;
 font-size:30px;
}
h2{
  border: white 2px solid;
  margin: 20px;
font-weight: none;
 font-size:50px;
}
div{
  background-color: #FFFFFF;
  }
"""