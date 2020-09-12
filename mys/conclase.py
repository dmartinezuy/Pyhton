class Alma:
       def hola(self):
              print "Hola soy Alma"
class Fernando(object):
       def __init__(self,object):
              self.object=object
       
       def algo(self):
              print "Debes hacer algo <<< dice Fer"
alma=Alma()
alma.hola()
fernando=Fernando(alma)
fernando.algo()
