#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Filters manager.

"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from oroboros.core.filters import Filter, all_filters_names
from oroboros.gui.filterdialog import FilterDialog


__all__ = ['FiltersManagerDialog']


class FiltersManagerDialog(QDialog):
	
	def __init__(self, parent=None, mode='man'):
		QDialog.__init__(self, parent)
		self._parent = parent
		self._mode = mode # either 'man' or 'select'
		tr = self.tr
		self.setWindowTitle(tr('Filters Manager'))
		self.setSizeGripEnabled(True)
		# layout
		grid = QGridLayout(self)
		self.setLayout(grid)
		# list of filters
		self.filtersBox = QComboBox(self)
		self.filtersBox.setEditable(False)
		self.filtersBox.addItems(all_filters_names())
		grid.addWidget(self.filtersBox, 0, 0)
		# buttons
		buttonsLayout = QHBoxLayout()
		grid.addLayout(buttonsLayout, 1, 0)
		newButton = QPushButton(tr('New'), self)
		newButton.clicked.connect(self.newFilterEvent)
		buttonsLayout.addWidget(newButton)
		editButton = QPushButton(tr('Edit'), self)
		editButton.clicked.connect(self.editFilterEvent)
		buttonsLayout.addWidget(editButton)
		deleteButton = QPushButton(tr('Delete'), self)
		deleteButton.clicked.connect(self.deleteFilterEvent)
		buttonsLayout.addWidget(deleteButton)
		if mode == 'man':
			closeButton = QPushButton(tr('Close'), self)
			closeButton.clicked.connect(self.close)
		elif mode == 'select':
			closeButton = QPushButton(tr('Select'), self)
			closeButton.clicked.connect(self.accept)
		closeButton.setDefault(True)
		buttonsLayout.addWidget(closeButton)
	
	def newFilterEvent(self):
		new = FilterDialog(self)
		ok = new.exec_()
		if ok:
			self.reset()
	
	def editFilterEvent(self):
		filt = Filter(all_filters_names()[self.filtersBox.currentIndex()])
		edit = FilterDialog(self, filt)
		ok = edit.exec_()
		if ok:
			self.reset()
	
	def deleteFilterEvent(self):
		tr = self.tr
		name = all_filters_names()[self.filtersBox.currentIndex()]
		ret = QMessageBox.warning(self, tr('Delete Filter'),
			str(tr('Are you sure you want to delete filter \xab %(filter)s \xbb ?')) % {
				'filter': name},
			QMessageBox.Cancel|QMessageBox.Yes, QMessageBox.Yes)
		if ret == QMessageBox.Yes:
			filt = Filter(name)
			try:
				filt.delete()
			except ValueError: # cannot delete
				QMessageBox.critical(self, tr('Default Filter'),
					tr('Cannot delete default filter.'))
			self.reset()
	
	def reset(self):
		"""Reload filters list."""
		self.filtersBox.clear()
		self.filtersBox.addItems(all_filters_names())
	
	def exec_(self):
		if self._mode == 'select':
			ok = QDialog.exec_(self)
			if ok:
				name = all_filters_names()[self.filtersBox.currentIndex()]
				return ok, name
			else:
				return ok, None
		else:
			return QDialog.exec_(self)



def main():
	import sys
	app = QApplication(sys.argv)
	main = FiltersManagerDialog()
	main.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

# End.
