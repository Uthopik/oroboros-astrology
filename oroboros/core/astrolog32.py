#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Import astrolog32 files.
"""

import os.path
import re

from oroboros.core.charts import Chart


__all__ = ['load']


def _parse_coord(coord_str):
	"""
	Parsea coordenadas de Astrolog32 como '2:15'00W' o '53:30'00N'.
	Retorna (grados_int, direccion_str, minutos_int, segundos_int).
	"""
	dr = coord_str[-1].upper()
	coord_clean = coord_str[:-1]  # Quitar N/S/E/W
	
	# Formato con minutos (') ej: "2:15'00" o "53:30'00"
	if "'" in coord_clean:
		parts = coord_clean.split("'")
		deg_min = parts[0].split(':')
		deg = int(deg_min[0])
		mn = int(deg_min[1]) if len(deg_min) > 1 else 0
		sec = int(parts[1]) if len(parts) > 1 and parts[1] else 0
	elif ':' in coord_clean:
		parts = coord_clean.split(':')
		deg = int(parts[0])
		mn = int(parts[1]) if len(parts) > 1 else 0
		sec = int(parts[2]) if len(parts) > 2 else 0
	else:
		deg = int(coord_clean) if coord_clean.isdigit() else 0
		mn = 0
		sec = 0
		
	return (deg, dr, mn, sec)


def load(path):
	"""Load an astrolog32 file. Return chart (no positions calculated).
	
	:rtype: Chart
	"""
	path = os.path.abspath(os.path.expanduser(path))
	
	# Solución Python 3: usar open() con encoding explicito
	with open(path, 'r', encoding='utf-8', errors='ignore') as f:
		lines = f.readlines()

	name = ''
	location = ''
	dt = (2000, 1, 1, 0, 0, 0)
	longitude = (0, 'W', 0, 0)
	latitude = (0, 'N', 0, 0)
	hoffset = 0.0
	dst = False

	for line in [x.strip() for x in lines]:
		if not line.startswith('/'):
			continue
			
		if line.startswith('/qb'):
			# Extraer argumentos separados por espacios múltiples
			line_content = line[4:].strip()
			parts = [p for p in line_content.split(' ') if p]
			
			if len(parts) >= 8:
				mth, d, y, time_str, stdt, offset_str, lon_str, lat_str = parts[:8]
				
				# datetime
				time_parts = time_str.split(':')
				h = int(time_parts[0])
				m = int(time_parts[1]) if len(time_parts) > 1 else 0
				s = int(time_parts[2]) if len(time_parts) > 2 else 0
				dt = (int(y), int(mth), int(d), h, m, s)
				
				# coordenadas
				longitude = _parse_coord(lon_str)
				latitude = _parse_coord(lat_str)
				
				# utc offset
				if ':' in offset_str:
					soffset = offset_str[0]
					off_parts = offset_str[1:].split(':')
					hoff = int(off_parts[0])
					moff = int(off_parts[1]) / 60.0
					val_offset = hoff + moff
					if soffset == '-':
						val_offset = -val_offset
				else:
					val_offset = float(offset_str)
				
				# Astrolog32 invierte el signo del offset UTC respecto al estándar
				hoffset = -val_offset
				
				if stdt == 'DT':
					hoffset += 1.0
					dst = True
				else:
					dst = False

		elif line.startswith('/zi'):
			line_content = line[4:].strip()
			# Buscar patrones de texto entre comillas "Nombre" "Lugar"
			matches = re.findall(r'"([^"]*)"', line_content)
			if len(matches) >= 2:
				name = matches[0]
				location = matches[1]
			elif len(matches) == 1:
				name = matches[0]
				location = ''

	cht = Chart(set_default=False, do_calc=False)
	cht.set(name=name, datetime=dt, location=location, country='?',
		zoneinfo='', dst=dst, utcoffset=hoffset, latitude=latitude,
		longitude=longitude, altitude=0, comment='Imported from Astrolog32')
	
	return cht
