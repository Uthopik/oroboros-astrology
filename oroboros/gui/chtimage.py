#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Produce charts images.

"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import QSvgGenerator


from oroboros.gui.chtpainter import ChartPainter


__all__ = ['makeImage', 'makeSvg']


def _clean_dimension(val):
	"""Convierte el parámetro a entero si viene como método o string."""
	if callable(val):
		return int(val())
	return int(val)


def makeImage(chart, path, ext, width, height, quality=-1):
	"""Create an image file for a chart.
	
	:type chart: BiChart
	:type path: str
	:type ext: str
	:type width: int
	:type height: int
	:type quality: int
	"""
	w = _clean_dimension(width)
	h = _clean_dimension(height)
	ext_str = str(ext).lower().strip('.')

	if ext_str == 'svg':
		makeSvg(chart, path, w, h)
		return

	# Crear la imagen con fondo transparente o blanco según preferencia
	im = QImage(w, h, QImage.Format_ARGB32_Premultiplied)
	im.fill(Qt.transparent)

	# ChartPainter recibe directamente la QImage (instancia y finaliza su propio QPainter internamente)
	ChartPainter(im, chart)

	if not path.lower().endswith('.' + ext_str):
		path = '%s.%s' % (path, ext_str)

	im.save(path, None, quality)


def makeSvg(chart, path, width, height):
	"""Create a Svg file.
	
	:type chart: BiChart
	:type path: str
	:type width: int
	:type height: int
	"""
	w = _clean_dimension(width)
	h = _clean_dimension(height)

	svg = QSvgGenerator()
	if not path.lower().endswith('.svg'):
		path = '%s.svg' % path

	svg.setFileName(path)
	svg.setSize(QSize(w, h))
	svg.setViewBox(QRect(0, 0, w, h))

	# ChartPainter recibe directamente el QSvgGenerator
	ChartPainter(svg, chart)


# End.
