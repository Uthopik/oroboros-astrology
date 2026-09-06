#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Translated names.

"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import qApp, QApplication


__all__ = ['_encoding', 'signs', 'planets', 'houses', 'houseSystems',
	'sidModes', 'objects']


tr = lambda x, y=None: QCoreApplication.translate('names.py', x, y) if QCoreApplication.instance() else x


_encoding = 'iso-8859-1'


#: Signs
signs = {
	'Ari': str(tr('Ari', 'Aries')),
	'Tau': str(tr('Tau', 'Taurus')),
	'Gem': str(tr('Gem', 'Gemini')),
	'Can': str(tr('Can', 'Cancer')),
	'Leo': str(tr('Leo', 'Leo')),
	'Vir': str(tr('Vir', 'Virgo')),
	'Lib': str(tr('Lib', 'Libra')),
	'Sco': str(tr('Sco', 'Scorpio')),
	'Sag': str(tr('Sag', 'Sagittarius')),
	'Cap': str(tr('Cap', 'Capricorn')),
	'Aqu': str(tr('Aqu', 'Aquarius')),
	'Pis': str(tr('Pis', 'Pisces'))
	}

#: Planets
planets = {
	'Sun': str(tr('Sun')),
	'Moon': str(tr('Moon')),
	'Mercury': str(tr('Mercury')),
	'Venus': str(tr('Venus')),
	'Mars': str(tr('Mars')),
	'Jupiter': str(tr('Jupiter')),
	'Saturn': str(tr('Saturn')),
	'Uranus': str(tr('Uranus')),
	'Neptune': str(tr('Neptune')),
	'Pluto': str(tr('Pluto')),
	'Earth': str(tr('Earth')),
	'Chiron': str(tr('Chiron')),
	'Pholus': str(tr('Pholus')),
	'Ceres': str(tr('Ceres')),
	'Pallas': str(tr('Pallas')),
	'Juno': str(tr('Juno')),
	'Vesta': str(tr('Vesta')),
	'Rahu (mean)': str(tr('Rahu (mean)')),
	'Rahu (true)': str(tr('Rahu (true)')),
	'Ketu (mean)': str(tr('Ketu (mean)')),
	'Ketu (true)': str(tr('Ketu (true)')),
	'Lilith (mean)': str(tr('Lilith (mean)')),
	'Lilith (true)': str(tr('Lilith (true)')),
	'Priapus (mean)': str(tr('Priapus (mean)')),
	'Priapus (true)': str(tr('Priapus (true)')),
	'Cupido': str(tr('Cupido')),
	'Hades': str(tr('Hades')),
	'Zeus': str(tr('Zeus')),
	'Kronos': str(tr('Kronos')),
	'Apollon': str(tr('Apollon')),
	'Admetos': str(tr('Admetos')),
	'Vulkanus': str(tr('Vulkanus')),
	'Poseidon': str(tr('Poseidon')),
	'Isis': str(tr('Isis')),
	'Nibiru': str(tr('Nibiru')),
	'Harrington': str(tr('Harrington')),
	'Neptune (Leverrier)': str(tr('Neptune (Leverrier)')),
	'Neptune (Adams)': str(tr('Neptune (Adams)')),
	'Pluto (Lowell)': str(tr('Pluto (Lowell)')),
	'Pluto (Pickering)': str(tr('Pluto (Pickering)')),
	'Vulcan': str(tr('Vulcan')),
	'White Moon': str(tr('White Moon')),
	'Proserpina': str(tr('Proserpina')),
	'Waldemath': str(tr('Waldemath')),
	'Asc': str(tr('Asc')),
	'Mc': str(tr('Mc')),
	'Dsc': str(tr('Dsc')),
	'Ic': str(tr('Ic')),
	'Armc': str(tr('Armc')),
	'Vertex': str(tr('Vertex')),
	'Equatorial Ascendant': str(tr('Equatorial Ascendant')),
	'Co-ascendant (Koch)': str(tr('Co-ascendant (Koch)')),
	'Co-ascendant (Munkasey)': str(tr('Co-ascendant (Munkasey)')),
	'Polar Ascendant (Munkasey)': str(tr('Polar Ascendant (Munkasey)')),
	'Part of Fortune (Rudhyar)': str(tr('Part of Fortune (Rudhyar)')),
	'128 Nemesis': str(tr('128 Nemesis'))
	}

#: Houses
houses = {
	'Cusp 01': str(tr('Cusp 01')),
	'Cusp 02': str(tr('Cusp 02')),
	'Cusp 03': str(tr('Cusp 03')),
	'Cusp 04': str(tr('Cusp 04')),
	'Cusp 05': str(tr('Cusp 05')),
	'Cusp 06': str(tr('Cusp 06')),
	'Cusp 07': str(tr('Cusp 07')),
	'Cusp 08': str(tr('Cusp 08')),
	'Cusp 09': str(tr('Cusp 09')),
	'Cusp 10': str(tr('Cusp 10')),
	'Cusp 11': str(tr('Cusp 11')),
	'Cusp 12': str(tr('Cusp 12')),
	'Sector 01': str(tr('Sector 01')),
	'Sector 02': str(tr('Sector 02')),
	'Sector 03': str(tr('Sector 03')),
	'Sector 04': str(tr('Sector 04')),
	'Sector 05': str(tr('Sector 05')),
	'Sector 06': str(tr('Sector 06')),
	'Sector 07': str(tr('Sector 07')),
	'Sector 08': str(tr('Sector 08')),
	'Sector 09': str(tr('Sector 09')),
	'Sector 10': str(tr('Sector 10')),
	'Sector 11': str(tr('Sector 11')),
	'Sector 12': str(tr('Sector 12')),
	'Sector 13': str(tr('Sector 13')),
	'Sector 14': str(tr('Sector 14')),
	'Sector 15': str(tr('Sector 15')),
	'Sector 16': str(tr('Sector 16')),
	'Sector 17': str(tr('Sector 17')),
	'Sector 18': str(tr('Sector 18')),
	'Sector 19': str(tr('Sector 19')),
	'Sector 20': str(tr('Sector 20')),
	'Sector 21': str(tr('Sector 21')),
	'Sector 22': str(tr('Sector 22')),
	'Sector 23': str(tr('Sector 23')),
	'Sector 24': str(tr('Sector 24')),
	'Sector 25': str(tr('Sector 25')),
	'Sector 26': str(tr('Sector 26')),
	'Sector 27': str(tr('Sector 27')),
	'Sector 28': str(tr('Sector 28')),
	'Sector 29': str(tr('Sector 29')),
	'Sector 30': str(tr('Sector 30')),
	'Sector 31': str(tr('Sector 31')),
	'Sector 32': str(tr('Sector 32')),
	'Sector 33': str(tr('Sector 33')),
	'Sector 34': str(tr('Sector 34')),
	'Sector 35': str(tr('Sector 35')),
	'Sector 36': str(tr('Sector 36'))
	}

#: Objects (planets and houses)
objects = dict()
for k, v in list(planets.items()):
	objects[k] = v
for k, v in list(houses.items()):
	objects[k] = v


#: Aspects
aspects = {
	'Conjunction': str(tr('Conjunction')),
	'Opposition': str(tr('Opposition')),
	'Trine': str(tr('Trine')),
	'Square': str(tr('Square')),
	'Sextile': str(tr('Sextile')),
	'Quincunx': str(tr('Quincunx')),
	'SesquiSquare': str(tr('SesquiSquare')),
	'SemiSquare': str(tr('SemiSquare')),
	'SemiSextile': str(tr('SemiSextile')),
	'SquiSquare': str(tr('SquiSquare')),
	'SquiSextile': str(tr('SquiSextile')),
	'Quintile': str(tr('Quintile')),
	'BiQuintile': str(tr('BiQuintile')),
	'SemiQuintile': str(tr('SemiQuintile')),
	'Novile': str(tr('Novile')),
	'BiNovile': str(tr('BiNovile')),
	'QuadriNovile': str(tr('QuadriNovile')),
	'SemiNovile': str(tr('SemiNovile')),
	'Septile': str(tr('Septile')),
	'BiSeptile': str(tr('BiSeptile')),
	'TriSeptile': str(tr('TriSeptile')),
	'Undecile': str(tr('Undecile')),
	'BiUndecile': str(tr('BiUndecile')),
	'TriUndecile': str(tr('TriUndecile')),
	'QuadUndecile': str(tr('QuadUndecile')),
	'QuinUndecile': str(tr('QuinUndecile'))
	}

#: Available house systems
houseSystems = [ ## order matters so it's a list
	('P', str(tr('Placidus'))),
	('K', str(tr('Koch'))),
	('R', str(tr('Regiomontanus'))),
	('C', str(tr('Campanus'))),
	('B', str(tr('Alcabitus'))),
	('O', str(tr('Porphyrus'))),
	('A', str(tr('Equal'))),
	('H', str(tr('Aziumtal/horizontal'))),
	('V', str(tr('Vehlow equal'))),
	('X', str(tr('Axial rotation'))),
	('G', str(tr('Gauquelin sectors'))),
	('U', str(tr('Krusinski'))),
	('W', str(tr('Whole sign')))
	]

#: Sidereal modes
sidModes = [
	(-1, str(tr('None (western tropical)'))),
	(0, str(tr('Fagan-Bradley'))),
	(1, str(tr('Lahiri'))),
	(2, str(tr('Deluce'))),
	(3, str(tr('Raman'))),
	(4, str(tr('Ushashashi'))),
	(5, str(tr('Krishnamurti'))),
	(6, str(tr('Djwhal Khul'))),
	(7, str(tr('Yukteshwar'))),
	(8, str(tr('Jn Bhasin'))),
	(9, str(tr('Babyl. Kugler 1'))),
	(10, str(tr('Babyl. Kugler 2'))),
	(11, str(tr('Babyl. Kugler 3'))),
	(12, str(tr('Babyl. Huber'))),
	(13, str(tr('Babyl. ETPSC'))),
	(14, str(tr('Aldebaran 15Tau'))),
	(15, str(tr('Hipparchos'))),
	(16, str(tr('Sassanian'))),
	(17, str(tr('Gal. Center 0Sag'))),
	(18, str(tr('J2000'))),
	(19, str(tr('J1900'))),
	(20, str(tr('B1950'))),
	(255, str(tr('User-defined')))
	]



# End.
