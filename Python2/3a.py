import os
import xml.sax

class Handler( xml.sax.ContentHandler):

  def __init__( self):
    xml.sax.ContentHandler.__init__( self)

  def startElement( self, name, attrs):
    self.CurrentData=name
    print "Start tag: "+str(name)

  def endElement( self, name):
    self.CurrentData=""
    print "Stop tag: "+str(name)

  def characters( self, data):
    if self.CurrentData=="heading":
      print "    Heading Field: "+str(data)

filename = "example.xml"
lines=open(filename,"r")
handler = Handler()
xml.sax.parse( filename, handler)


