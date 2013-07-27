#!/usr/bin/python2
#-*- coding: utf-8 -*-
# Ubaldino Zurita
#
import sys, urllib2, re, urllib
# comprobando si se ingreso el dato requerido
if len(sys.argv) > 1:
  sede = sys.argv[1]
  try:
    url = "http://www.cinecenter.com.bo/%s.html"%(sede)
    html = str(urllib2.urlopen(url).read())
    # obteniendo pelis en cartelera
    found = re.findall("class=\"extra-box\".*<", html);i=0
    for dato in found:
      titulo_peli = re.findall("\)\">(\w*\W.*)</a", dato);i=i+1
      horario_peli = re.findall("span>([\W\w].*)<br", dato)
      print "\033[1;39m %d \033[1;31m%s\n\t \033[1;33m%s\n\033[1;00m"%(i,titulo_peli[0],horario_peli[0])
  except: print "\033[1;31m **** Elija la sede ****\033[1;00m"
  # obteniendo pelis en cartelera
else: print """
Usage:\n \033[1;35m./center.py <sede>\033[1;00m\n cochabamba\n santacruz\n lapaz
"""
