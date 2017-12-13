import os
from xml.dom.minidom import parse
import xml.dom.minidom

DOM = xml.dom.minidom.parse("example.xml")
collection = DOM.documentElement

notes = collection.getElementsByTagName("note")

for note in notes:
   print "Notes:"
   val=note.getElementsByTagName('heading')[0]
   print "Heading: {}".format(val.childNodes[0].data)


