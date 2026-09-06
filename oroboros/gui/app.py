#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application manager.

"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from oroboros.core import cfg
from oroboros.core import desktop


##__all__ = []


# singleton
mainwin = None ## main window


def appendMultiChart(cht):
	print(f"\n[DEBUG APP] appendMultiChart recibido - cht.datetime: {getattr(cht, 'datetime', None)!r}")
	
	# Recalcular la carta individual o los elementos si es un contenedor
	if hasattr(cht, 'calc'):
		cht.calc()
	elif isinstance(cht, (list, tuple)):
		for c in cht:
			if hasattr(c, 'calc'):
				c.calc()

	desktop.charts.append(cht)
	
	# Recalcular el contenedor si dispone del método
	if hasattr(desktop.charts[-1], 'calc'):
		desktop.charts[-1].calc()

	mainwin.addTabs(len(desktop.charts) - 1)


def insertMultiChart(idx, cht):
	if hasattr(cht, 'calc'):
		cht.calc()
	elif isinstance(cht, (list, tuple)):
		for c in cht:
			if hasattr(c, 'calc'):
				c.calc()

	desktop.charts.insert(idx, cht)
	
	if hasattr(desktop.charts[idx], 'calc'):
		desktop.charts[idx].calc()

	mainwin.addTabs(idx)


def replaceMultiChart(idx, cht):
	print(f"\n[DEBUG APP] replaceMultiChart recibido (idx={idx}) - cht.datetime: {getattr(cht, 'datetime', None)!r}")
	if hasattr(cht, 'calc'):
		cht.calc()
	elif isinstance(cht, (list, tuple)):
		for c in cht:
			if hasattr(c, 'calc'):
				c.calc()

	desktop.charts[idx] = cht

	if hasattr(desktop.charts[idx], 'calc'):
		desktop.charts[idx].calc()

	mainwin.resetTabs(idx)


def removeMultiChart(idx):
	del(desktop.charts[idx])
	mainwin.removeTabs(idx)


def replaceChart(idx, num, cht):
	print(f"\n[DEBUG APP] replaceChart recibido (idx={idx}, num={num}) - cht.datetime: {getattr(cht, 'datetime', None)!r}")
	
	# 1. Recalcular los datos astronómicos de la carta editada
	if hasattr(cht, 'calc'):
		cht.calc()

	try:
		desktop.charts[idx][num] = cht
	except IndexError:
		desktop.charts[idx].append(cht)

	# 2. Recalcular la carta compuesta/contenedor global
	if hasattr(desktop.charts[idx], 'calc'):
		desktop.charts[idx].calc()

	# 3. Notificar a la interfaz para que redibuje la pestaña
	mainwin.resetTabs(idx)


def removeChart(idx, num):
	del(desktop.charts[idx][num])
	
	if hasattr(desktop.charts[idx], 'calc'):
		desktop.charts[idx].calc()

	mainwin.resetTabs(idx)




def filterUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._idx_ == idx:
				c._filter.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def planetsFilterUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._planets._idx_ == idx:
				c._filter._planets.reset()
				rset, reset = True, True
			if c._filter._midpoints._planets._idx_ == idx:
				c._filter._midpoints._planets.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def aspectsFilterUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._aspects._idx_ == idx:
				c._filter._aspects.reset()
				rset, reset = True, True
			if c._filter._midpoints._aspects._idx_ == idx:
				c._filter._midpoints._aspects.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def orbsFilterUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._orbs._idx_ == idx:
				c._filter._orbs.reset()
				rset, reset = True, True
			if c._filter._midpoints._orbs._idx_ == idx:
				c._filter._midpoints._orbs.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def aspectsRestrictionsUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._asprestr._idx_ == idx:
				c._filter._asprestr.reset()
				rset, reset = True, True
			if c._filter._midpoints._asprestr._idx_ == idx:
				c._filter._midpoints._asprestr.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def orbsRestrictionsUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._orbrestr._idx_ == idx:
				c._filter._orbrestr.reset()
				rset, reset = True, True
			if c._filter._midpoints._orbrestr._idx_ == idx:
				c._filter._midpoints._orbrestr.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def midPointsFilterUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._midpoints._idx_ == idx:
				c._filter._midpoints.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


# End.
