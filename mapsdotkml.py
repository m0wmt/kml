#!/usr/local/bin/python3
# coding - utf-8
#
# Converts input file in to KML points of interest file for MAPS.Me
#

import argparse
import csv

def write_placemark(lat, lon, address, pin):
  fo.write("  <Placemark>\n")
  fo.write("    <name>" + address + "</name>\n")
  fo.write("    <styleUrl>#placemark-" + pin + "</styleUrl>\n")
  fo.write("   <Point><coordinates>" + lat + "," + lon + "</coordinates></Point>\n")
  fo.write(" </Placemark>\n")


available_colours = {'red', 'blue', 'green', 'brown', 'orange', 'pink', 'purple', 'yellow'}
available_file_types = {'cc-navman', 'cc-garmin'}

parser = argparse.ArgumentParser(description='Converts input file to KML file for MAPS.Me')

parser.add_argument('-i', action='store', dest='in_file',
                    help='File to convert. E.g. -i my_file.csv')

parser.add_argument('-o', action='store', dest='out_file',
                    help='Output file name without file extension. E.g. -o \"Caravan Club CL\"')

parser.add_argument('-t', action='store', dest='file_type',
                    help='Input file type, curent valid options are; cc-navman, ccc or gooutdoors ' + 
                    '.csv file. E.g. -t cc-navman')

parser.add_argument('-c', action='store', dest='pin_colour',
                    help='Colour of POI pin, valid colours are; red, blue, green, brown, orange, ' +
                    'pink, purple, yellow. E.g -c green')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()

if results.in_file == None or results.out_file == None or results.file_type == None or results.pin_colour == None:
  print('')
  print('Invalid command line argument')
  print('')
  print(parser.parse_args(['-h']))
else:
  print('in_file     =', results.in_file)
  print('out_file   =', results.out_file)
  print('file_type   =', results.file_type)
  print('pin_colour       =', results.pin_colour)

f = open(results.in_file, 'r')
csv_f = csv.reader(f)

#Open the file to be written.
fo = open(results.out_file + '.kml', 'w')

#Writing the kml file.
fo.write("<?xml version='1.0' encoding='UTF-8'?>\n")
fo.write("<kml xmlns='http://earth.google.com/kml/2.2'>\n")
fo.write("<Document>\n")
fo.write("  <Style id=\"placemark-blue\">\n")
fo.write("    <IconStyle>\n")
fo.write("      <Icon>\n")
fo.write("        <href>http://mapswith.me/placemarks/placemark-blue.png</href>\n")
fo.write("      </Icon>\n")
fo.write("    </IconStyle>\n")
fo.write("  </Style>\n")
fo.write("  <Style id=\"placemark-brown\">\n")
fo.write("    <IconStyle>\n")
fo.write("      <Icon>\n")
fo.write("        <href>http://mapswith.me/placemarks/placemark-brown.png</href>\n")
fo.write("      </Icon>\n")
fo.write("    </IconStyle>\n")
fo.write("  </Style>\n")
fo.write("  <Style id=\"placemark-green\">\n")
fo.write("    <IconStyle>\n")
fo.write("      <Icon>\n")
fo.write("        <href>http://mapswith.me/placemarks/placemark-green.png</href>\n")
fo.write("      </Icon>\n")
fo.write("    </IconStyle>\n")
fo.write("  </Style>\n")
fo.write("  <Style id=\"placemark-orange\">\n")
fo.write("    <IconStyle>\n")
fo.write("      <Icon>\n")
fo.write("        <href>http://mapswith.me/placemarks/placemark-orange.png</href>\n")
fo.write("      </Icon>\n")
fo.write("    </IconStyle>\n")
fo.write(" </Style>\n")
fo.write("  <Style id=\"placemark-pink\">\n")
fo.write("    <IconStyle>\n")
fo.write("      <Icon>\n")
fo.write("        <href>http://mapswith.me/placemarks/placemark-pink.png</href>\n")
fo.write("      </Icon>\n")
fo.write("    </IconStyle>\n")
fo.write("  </Style>\n")
fo.write("  <Style id=\"placemark-purple\">\n")
fo.write("    <IconStyle>\n")
fo.write("      <Icon>\n")
fo.write("        <href>http://mapswith.me/placemarks/placemark-purple.png</href>\n")
fo.write("      </Icon>\n")
fo.write("    </IconStyle>\n")
fo.write("  </Style>\n")
fo.write("  <Style id=\"placemark-red\">\n")
fo.write("    <IconStyle>\n")
fo.write("      <Icon>\n")
fo.write("        <href>http://mapswith.me/placemarks/placemark-red.png</href>\n")
fo.write("      </Icon>\n")
fo.write("    </IconStyle>\n")
fo.write("  </Style>\n")
fo.write("  <Style id=\"placemark-yellow\">\n")
fo.write("    <IconStyle>\n")
fo.write("      <Icon>\n")
fo.write("        <href>http://mapswith.me/placemarks/placemark-yellow.png</href>\n")
fo.write("      </Icon>\n")
fo.write("    </IconStyle>\n")
fo.write("  </Style>\n")
#Write name for bookmark points

fo.write("   <name>" + results.out_file +"</name>\n")
fo.write("  <visibility>1</visibility>\n")

#Caravan Club Garmin (csv) file
if results.file_type == 'cc-navman':
  for row in csv_f:
    add = row[2]
    add_no_q = add[1:-1]             #remove first and last quote
    add_no_q.strip('"')              #remove any other quotes
    s = add_no_q.replace("&", "+")   #remove any amplersands left
    print(row[0] + ":" + row[1] + "[" + s + "]")
    write_placemark( str(row[0]), str(row[1]), str(s), results.pin_colour)

#Camping And Caravan Club (csv) file
elif results.file_type == 'ccc':
  for row in csv_f:
    add = row[2]
    dq = add.replace("\"", "")              #remove any other quotes
    s = dq.replace("&", "+")   #remove any amplersands left
    print(row[0] + ":" + row[1] + "[" + s + "]")
    write_placemark( str(row[0]), str(row[1]), str(s), results.pin_colour)

#Go Outdoors (csv from json) file
elif results.file_type == 'gooutdoors':
  for row in csv_f:
    add = row[4]
    s = add.replace("&", "+")   #remove any amplersands left
    s = s + " " + str(row[5]) + ". " + str(row[6])
    print(str(row[8]) + "," + str(row[7]) + " [" + str(s) +"]")
    write_placemark( str(row[8]), str(row[7]), str(s), results.pin_colour)

fo.write("</Document>\n")
fo.write("</kml>\n")
fo.close()
f.close()
