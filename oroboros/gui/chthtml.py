#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Format chart data in Html.

"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import swisseph as swe

from oroboros.core import cfg
from oroboros.gui import names

SIGN_KEYS = ('Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir', 'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Pis')

def _get_sign_name(lon):
    key = SIGN_KEYS[int(lon // 30) % 12]
    return names.signs.get(key, key)

if cfg.use_docutils:
	from docutils.core import publish_parts


__all__ = ['html_data', 'html_planets', 'html_cusps', 'html_aspects',
	'html_midpoints', 'html_interaspects']



tr = lambda x, y=None: qApp.translate('chtdata.py', x, y)

_encoding = names._encoding


def html_data(chart):
	"""Return a html string for output of chart data.
	
	:type chart: Chart
	"""
	
	# ### chart data ###
	# name
	fmt = str(tr('<b>%(name)s:</b> %(val)s<br/>'))
	try:
		txt = fmt % {
			'name': tr('Name'),
			'val': chart._name}
	except UnicodeDecodeError:
		txt += fmt % {
			'name': tr('Name'),
			'val': chart._name.decode(_encoding)}
	# date
	fmt = str(tr('<b>%(date)s:</b> %(val)s<br/>'))
	txt += fmt % {
		'date': tr('Date'),
		'val': chart._datetime.date().isoformat()}
	# time
	fmt = str(tr('<b>%(time)s:</b> %(val)s<br/>'))
	txt += fmt % {
		'time': tr('Time'),
		'val': chart._datetime.time().isoformat()}
	# calendar
	fmt = str(tr('<b>%(calendar)s:</b> %(val)s<br/>'))
	txt += fmt % {
		'calendar': tr('Calendar'),
		'val': chart._calendar.capitalize()}
	# location
	fmt = str(tr('<b>%(location)s:</b> %(val)s<br/>'))
	try:
		txt += fmt % {
			'location': tr('Location'),
			'val': chart._location}
	except UnicodeDecodeError:
		txt += fmt % {
			'location': tr('Location'),
			'val': chart._location.decode(_encoding)}
	# latitude
	fmt = str(tr('<b>%(latitude)s:</b> %(dg).2d%(deg)s %(dr)s %(mn).2d%(min)s %(sc).2d%(sec)s<br/>',
		'Geo latitude display'))
	txt += fmt % {
		'latitude': tr('Latitude'),
		'dg': chart._latitude.degrees,
		'deg': tr('\xb0', 'Degrees'),
		'dr': chart._latitude.direction,
		'mn': chart._latitude.minutes,
		'min': tr("'", 'Minutes'),
		'sc': chart._latitude.seconds,
		'sec': tr('"', 'Seconds')}
	# longitude
	fmt = str(tr('<b>%(longitude)s:</b> %(dg).3d%(deg)s %(dr)s %(mn).2d%(min)s %(sc).2d%(sec)s<br/>',
		'Geo longitude display'))
	txt += fmt % {
		'longitude': tr('Longitude'),
		'dg': chart._longitude.degrees,
		'deg': tr('\xb0', 'Degrees'),
		'dr': chart._longitude.direction,
		'mn': chart._longitude.minutes,
		'min': tr("'", 'Minutes'),
		'sc': chart._longitude.seconds,
		'sec': tr('"', 'Seconds')}
	# altitude
	fmt = str(tr('<b>%(altitude)s:</b> %(val)s m.<br/>'))
	txt += fmt % {
		'altitude': tr('Altitude'),
		'val': str(chart._altitude)}
	# country
	fmt = str(tr('<b>%(country)s:</b> %(val)s<br/>'))
	try:
		txt += fmt % {
			'country': tr('Country'),
			'val': chart._country}
	except UnicodeDecodeError:
		txt += fmt % {
			'country': tr('Country'),
			'val': chart._country.decode(_encoding)}
	# zoneinfo
	zoneinfo = chart._zoneinfo if chart._zoneinfo not in (None, '') else tr('-', 'No zoneinfo')
	fmt = str(tr('<b>%(zoneinfo)s:</b> %(val)s<br/>'))
	txt += fmt % {
		'zoneinfo': tr('Zoneinfo'),
		'val': zoneinfo}
	# timezone
	timezone = chart._timezone if chart._timezone != None else tr('-', 'No timezone')
	fmt = str(tr('<b>%(timezone)s:</b> %(tzname)s<br/>'))
	txt += fmt % {
		'timezone': tr('Timezone'),
		'tzname': str(timezone)
		}
	# utcoffset
	utcoffset = chart.utcoffset if chart.utcoffset != None else tr('?', 'No utcoffset')
	dst = tr('yes', 'dst') if chart.dst == True else tr('no', 'dst')
	fmt = str(tr('<b>%(utcoffset)s:</b> %(offset)s  <b>%(dst)s:</b> %(bool)s<br/>'))
	txt += fmt % {
		'utcoffset': tr('Utc offset'),
		'offset': utcoffset,
		'dst': tr('Dst'),
		'bool': dst}
	# comment
	if chart._comment != '':
		if cfg.use_docutils:
			cmt = publish_parts(chart._comment, writer_name='html')['html_body']
		else:
			cmt = chart._comment
	else:
		cmt = str(tr('-', 'No comment'))
	fmt = str(tr('<b>%(comment)s:</b> %(cmt)s<br/>'))
	try:
		txt += fmt % {
			'comment': tr('Comment'),
			'cmt': cmt}
	except UnicodeDecodeError:
		txt += fmt % {
			'comment': tr('Comment'),
			'cmt': cmt.decode(_encoding)}
	# keywords
	fmt = str(tr('<b>%(keywords)s:</b>'))
	txt += fmt % {
		'keywords': tr('Keywords')}
	if len(chart._keywords) == 0:
		txt += tr(' -', 'No keywords')
	else:
		kw = list()
		fmt = str(tr(' %(key)s:%(word)s'))
		for k, v in list(chart._keywords.items()):
			try:
				kw.append(fmt % {
					'key': k,
					'word': v})
			except UnicodeDecodeError:
				kw.append(fmt % {
					'key': k.decode(_encoding),
					'word': v.decode(_encoding)})
		txt += str(tr('; ', 'Keywords delimiter')).join(kw)
	
	# ### more data ###
	txt += '<hr/>'
	# ephemeris type
	fmt = str(tr('%(ephem)s %(info)s<br/>'))
	if chart.filter._ephe_type == 'swiss':
		txt += fmt % {
			'ephem': tr('Swiss Ephemeris'),
			'info': swe.version}
	elif chart.filter._ephe_type == 'jpl':
		txt += fmt % {
			'ephem': tr('Jet Propulsion Lab.'),
			'info': chart.filter._ephe_path}
	else:
		txt += str(tr('%(moshier)s<br/>')) % {
			'moshier': tr('Moshier Ephemeris')}
	# zodiac type
	if chart.filter._sid_mode == -1: ## tropical
		txt += str(tr('%(tropical)s, ')) % {
			'tropical': tr('Tropical')}
	elif chart.filter._sid_mode < 255: ## ayanamsa
		txt += str(tr('%(ayanamsaname)s (%(ayanamsaut)s), ')) % {
			'ayanamsaname': swe.get_ayanamsa_name(chart.filter._sid_mode),
			'ayanamsaut': swe.get_ayanamsa_ut(chart.julday)}
	elif chart.filter._sid_mode == 255: ## user-defined ayanamsa
		txt += str(tr('%(ayan)s (%(ayant0)s, %(t0)s), ')) % {
			'ayan': tr('Ayanamsa'),
			'ayant0': chart.filter._sid_ayan_t0,
			't0': chart.filter._sid_t0}
	else:
		raise ValueError('Invalid sid mode %s.' % chart.filter._sid_mode)
	# xcentric
	fmt = str(tr('%(situation)s<br/>', 'geo,topo,helio,bary'))
	if chart.filter._xcentric == 'geo':
		txt += fmt % {'situation': tr('Geocentric')}
	elif chart.filter._xcentric == 'topo':
		txt += fmt % {'situation': tr('Topocentric')}
	elif chart.filter._xcentric == 'helio':
		txt += fmt % {'situation': tr('Heliocentric')}
	elif chart.filter._xcentric == 'bary':
		txt += fmt % {'situation': tr('Barycentric')}
	else:
		raise ValueError('Invalid xcentric %s.' % chart.filter._xcentric)
	# julian day
	txt += str(tr('%(julday)s: %(jd)s<br/>')) % {
		'julday': tr('Julian day'),
		'jd': chart.julday}
	# local mean time
	try:
		lmtime = chart.local_mean_datetime
		y, mth, d, h, m, s = lmtime.timetuple()[:6]
		fmt = str(tr('%(local_mean_time)s: %(year).4d-%(month).2d-%(day).2d %(hour).2d:%(minute).2d:%(second).2d<br/>'))
		txt += fmt % {
			'local_mean_time': tr('Local mean time'),
			'year': y,
			'month': mth,
			'day': d,
			'hour': h,
			'minute': m,
			'second': s
			}
	except ValueError: ## no timezone set
		pass
	# local sidereal time
	try:
		lsidt = chart.local_sidtime
		h, mn, sc = lsidt.hour, lsidt.minute, lsidt.second
		fmt = str(tr('%(sidtime)s: %(h).2d:%(mn).2d:%(sc).2d<br/>'))
		txt += fmt % {
			'sidtime': tr('Sidereal time'),
			'h': h,
			'mn': mn,
			'sc': sc}
	except ValueError: ## no timezone set
		pass
	# obliquity
	ecl = chart.ecl_nut
	if isinstance(ecl, (tuple, list)) and len(ecl) > 0:
		ecl_val = ecl[0]
		if isinstance(ecl_val, (tuple, list)):
			ecl_val = ecl_val[0]
	else:
		ecl_val = 0.0

	dg, sn, mn, sc = swe.split_deg(float(ecl_val), 0)[:4]
	fmt = str(tr('%(obliquity)s: %(dg).2d%(deg)s %(mn).2d%(min)s %(sc).2d%(sec)s<br/>'))
	txt += fmt % {
		'obliquity': tr('Obliquity'),
		'dg': dg,
		'deg': tr('\xb0', 'Degrees'),
		'mn': mn,
		'min': tr("'", 'Minutes'),
		'sc': sc,
		'sec': tr('"', 'Seconds')}

	# nutation
	nutlon_val = ecl[2] if isinstance(ecl, (tuple, list)) and len(ecl) > 2 else (ecl[0] if isinstance(ecl, (tuple, list)) and len(ecl) > 0 else 0.0)
	nutobl_val = ecl[3] if isinstance(ecl, (tuple, list)) and len(ecl) > 3 else (ecl[1] if isinstance(ecl, (tuple, list)) and len(ecl) > 1 else 0.0)

	if isinstance(nutlon_val, (tuple, list)):
		nutlon_val = nutlon_val[0]
	if isinstance(nutobl_val, (tuple, list)):
		nutobl_val = nutobl_val[0]

	nutlon = swe.split_deg(float(nutlon_val), 0)
	nutobl = swe.split_deg(float(nutobl_val), 0)

	fmt = str(tr('%(nutation)s (%(longitude)s): %(nutlonsn)s%(nutlondg)d%(deg)s %(nutlonmn)d%(min)s %(nutlonsc)d%(sec)s<br/>%(nutation)s (%(obliquity)s): %(nutoblsn)s%(nutobldg)d%(deg)s %(nutoblmn)d%(min)s %(nutoblsc)d%(sec)s<br/>'))
	txt += fmt % {
		'nutation': tr('Nutation'),
		'longitude': tr('lon.'),
		'nutlonsn': '+' if len(nutlon) > 4 and nutlon[4] > 0 else '-',
		'nutlondg': nutlon[0],
		'nutlonmn': nutlon[1],
		'nutlonsc': nutlon[2],
		'obliquity': tr('obl.'),
		'nutoblsn': '+' if len(nutobl) > 4 and nutobl[4] > 0 else '-',
		'nutobldg': nutobl[0],
		'nutoblmn': nutobl[1],
		'nutoblsc': nutobl[2],
		'deg': tr('\xb0', 'Degrees'),
		'min': tr("'", 'Minutes'),
		'sec': tr('"', 'Seconds')
	}

	# delta T
	jd = chart.julday
	if isinstance(jd, (tuple, list)):
		jd = jd[0]

	fmt = str(tr('%(deltat)s: %(val)s<hr/>'))
	txt += fmt % {
		'deltat': tr('Delta T'),
		'val': swe.deltat(float(jd)) * 86400}

	return txt


def html_planets(plres):
	"""Create html string for output or planets results.
	
	:type plres: PlanetDataList
	:rtype: str
	"""
	txt = ''
	for e in plres:
		txt += _html_planets(e)
	return txt[:-5]


def _html_planets(res):
	"""Format planets results for printing in html.
	
	:type res: PlanetData
	:rtype: str
	"""
	lon = res._longitude
	if isinstance(lon, (tuple, list)):
		lon = lon[0]
	lon = float(lon)
	dg, mn, sc, degfrac, _ = swe.split_deg(lon, 0)
	
	sn = _get_sign_name(lon)

	try:
		plnt = names.objects[res._planet._name]
	except KeyError: # fixed star?
		plnt = res._planet._name
	if res._lonspeed < 0:
		rx = tr('R', 'Retrograde')
	else:
		rx = ''
	fmt = str(tr('<b>%(planet)s:</b> %(dg).2d%(deg)s %(sign)s %(mn).2d%(min)s %(sc).2d%(sec)s %(rx)s (%(lat)+.3f%(deg)s)<br/>',
		'Planets display'))
	txt = fmt % {
		'planet': plnt,
		'dg': dg,
		'deg': tr('\xb0', 'Degrees'),
		'sign': sn,
		'mn': mn,
		'min': tr("'", 'Minutes'),
		'sc': sc,
		'sec': tr('"', 'Seconds'),
		'rx': rx,
		'lat': res._latitude,
		'deg': tr('\xb0', 'Degrees')}
	return txt


def html_cusps(cuspsres):
	"""Create html string for output of houses data.
	
	:type cuspsres: HousesDataList
	:rtype: str
	"""
	fmt = str(tr('%(domification)s: %(val)s<br/>'))
	txt = fmt % {
		'domification': tr('Domification'),
		'val': chr(cuspsres._hsys) if isinstance(cuspsres._hsys, int) else str(cuspsres._hsys)
	}
	fmt = str(tr('<b>%(house)s:</b> %(dg).2d%(deg)s %(sign)s %(mn).2d%(min)s %(sc).2d%(sec)s<br/>',
		'Cusps display'))
	if cuspsres._hsys == 'G':
		numcusps = 36
	else:
		numcusps = 12
	for i in range(numcusps):
		lon = cuspsres[i]._longitude
		if isinstance(lon, (tuple, list)):
			lon = lon[0]
		lon = float(lon)
		dg, mn, sc, degfrac, _ = swe.split_deg(lon, 0)
		sn = _get_sign_name(lon)
		name = names.houses[cuspsres[i]._planet._name]
		txt += fmt % {
			'house': name,
			'dg': dg,
			'deg': tr('\xb0', 'Degrees'),
			'sign': sn,
			'mn': mn,
			'min': tr("'", 'Minutes'),
			'sc': sc,
			'sec': tr('"', 'Seconds')}
	txt = '%s%s' % (txt[:-5], tr('<hr/>', 'End of cusps'))
	for elem in cuspsres[numcusps:]:
		lon = elem._longitude
		if isinstance(lon, (tuple, list)):
			lon = lon[0]
		lon = float(lon)
		dg, mn, sc, degfrac, _ = swe.split_deg(lon, 0)
		sn = _get_sign_name(lon)
		name = names.planets[elem._planet._name]
		fmt = str(tr('%(ascmc)s: %(dg).2d%(deg)s %(sign)s %(mn).2d%(min)s %(sc).2d%(sec)s<br/>',
			'Cusps additional display'))
		txt += fmt % {
			'ascmc': name,
			'dg': dg,
			'deg': tr('\xb0', 'Degrees'),
			'sign': sn,
			'mn': mn,
			'min': tr("'", 'Minutes'),
			'sc': sc,
			'sec': tr('"', 'Seconds')}
	return txt


def html_aspects(aspres):
	"""Create html string for aspects output.
	
	:type aspres: AspectDataList
	:rtype: str
	"""
	txt = ''
	for e in aspres:
		txt += _html_aspects(e)
	return txt[:-5]


def _html_aspects(res):
	"""Format aspects results for printing in html.
	
	:type res: AspectData
	:rtype: str
	"""
	if res._apply == True:
		applic = tr('A', 'Aspect applying')
	elif res._apply == False:
		applic = tr('S', 'Aspect separating')
	else:
		applic = tr('-', 'Aspect stable')
	fmt = str(tr('%(p1)s <i>%(asp)s</i> %(p2)s %(delta)s%(diff).2f%(deg)s %(applic)s (%(factor).0f%%)<br/>',
		'Aspect display'))
	try:
		p1 = names.objects[res._data1._planet._name]
	except KeyError:
		p1 = res._data1._planet._name
	try:
		p2 = names.objects[res._data2._planet._name]
	except KeyError:
		p2 = res._data2._planet._name
	asp = names.aspects[res._aspect._name]
	var = {
		'p1': p1,
		'asp': asp,
		'p2': p2,
		'delta': tr('&Delta;', 'Delta symbol'),
		'diff': res._diff,
		'deg': tr('\xb0', 'Degrees'),
		'applic': applic,
		'factor': res._factor * 100}
	return fmt % var


def html_midpoints(midpres, midpasp):
	"""Format midpoints results for html.
	
	:type midpres: MidPointDataList
	:type midpasp: MidPointAspectDataList
	:rtype: str
	"""
	txt = ''
	for e in midpres:
		txt += _html_midpoints(e)
	txt = '%s%s' % (txt[:-5], '<hr/>')
	for e in midpasp:
		txt += _html_midp_aspects(e)
	return txt[:-5]


def _html_midpoints(res):
	"""Format midpoints data.
	
	:type res: MidPointData
	:rtype: res
	"""
	lon = res._longitude
	if isinstance(lon, (tuple, list)):
		lon = lon[0]
	dg, sn, mn, sc = swe.split_deg(float(lon), 0)
	sn = names.signs[sn]
	try:
		p1 = names.objects[res._data1._planet._name]
	except KeyError:
		p1 = res._data1._planet._name
	try:
		p2 = names.objects[res._data2._planet._name]
	except KeyError:
		p2 = res._data2._planet._name
	if res._lonspeed < 0:
		rx = tr('R', 'Retrograde')
	else:
		rx = ''
	fmt = str(tr('<b>%(planet1)s/%(planet2)s:</b> %(dg).2d%(deg)s %(sign)s %(mn).2d%(min)s %(sc).2d%(sec)s %(rx)s (%(lat)+.3f%(deg)s)<br/>',
		'Midpoint display'))
	txt = fmt % {
		'planet1': p1,
		'planet2': p2,
		'dg': dg,
		'deg': tr('\xb0', 'Degrees'),
		'sign': sn,
		'mn': mn,
		'min': tr("'", 'Minutes'),
		'sc': sc,
		'sec': tr('"', 'Seconds'),
		'rx': rx,
		'lat': res._latitude,
		'deg': tr('\xb0', 'Degrees')}
	return txt


def _html_midp_aspects(res):
	"""Format midpoint aspects.
	
	:type res: MidPointAspectData
	:rtype: str
	"""
	if res._apply == True:
		applic = tr('A', 'Aspect applying')
	elif res._apply == False:
		applic = tr('S', 'Aspect separating')
	else:
		applic = tr('-', 'Aspect stable')
	fmt = str(tr('%(p1)s/%(p2)s <i>%(asp)s</i> %(p3)s %(delta)s%(diff).2f%(deg)s %(applic)s (%(factor).0f%%)<br/>',
		'Midpoint aspect display'))
	try:
		p1 = names.objects[res._data1._data1._planet._name]
	except KeyError:
		p1 = res._data1._data1._planet._name
	try:
		p2 = names.objects[res._data1._data2._planet._name]
	except KeyError:
		p2 = res._data1._data2._planet._name
	try:
		p3 = names.objects[res._data2._planet._name]
	except KeyError:
		p3 = res._data2._planet._name
	asp = names.aspects[res._aspect._name]
	var = {
		'p1': p1,
		'p2': p2,
		'asp': asp,
		'p3': p3,
		'delta': tr('&Delta;', 'Delta symbol'),
		'diff': res._diff,
		'deg': tr('\xb0', 'Degrees'),
		'applic': applic,
		'factor': res._factor * 100}
	return fmt % var


def html_intermidp(aspres):
	"""Get html output for midp/planets aspects.
	
	:type aspres: AspectDataList
	:rtype: str
	"""
	txt = ''
	for e in aspres:
		txt += _html_midp_aspects(e)
	return txt[:-5]


def html_intermidpoints(aspres):
	"""Get html output for midp/midp aspects.
	
	:type aspres: InterMidPointAspectDataList
	:rtype: str
	"""
	txt = ''
	for e in aspres:
		txt += _html_intermidp_aspects(e)
	return txt[:-5]


def _html_intermidp_aspects(res):
	"""Format inter-midpoints aspects.
	
	:type res: InterMidPointAspect
	:rtype: str
	"""
	if res._apply == True:
		applic = tr('A', 'Aspect applying')
	elif res._apply == False:
		applic = tr('S', 'Aspect separating')
	else:
		applic = tr('-', 'Aspect stable')
	fmt = str(tr('%(p1)s/%(p2)s <i>%(asp)s</i> %(p3)s/%(p4)s %(delta)s%(diff).2f%(deg)s %(applic)s (%(factor).0f%%)<br/>',
		'Midpoint aspect display'))
	p1 = names.objects[res._data1._data1._planet._name]
	p2 = names.objects[res._data1._data2._planet._name]
	p3 = names.objects[res._data2._data1._planet._name]
	p4 = names.objects[res._data2._data2._planet._name]
	asp = names.aspects[res._aspect._name]
	var = {
		'p1': p1,
		'p2': p2,
		'asp': asp,
		'p3': p3,
		'p4': p4,
		'delta': tr('&Delta;', 'Delta symbol'),
		'diff': res._diff,
		'deg': tr('\xb0', 'Degrees'),
		'applic': applic,
		'factor': res._factor * 100}
	return fmt % var



# End.
