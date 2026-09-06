#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Orbs restrictions manager.

"""

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from oroboros.core.orbsrestrictions import OrbsRestrictions, all_orbs_restrictions_names
from oroboros.gui.orbrestrdialog import OrbsRestrictionsDialog


__all__ = ['OrbsRestrictionsManagerDialog']



class OrbsRestrictionsManagerDialog(QDialog):
	
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self._parent = parent
		tr = self.tr
		self.setWindowTitle(tr('Orbs Restrictions Manager'))
		self.setSizeGripEnabled(True)
		# layout
		grid = QGridLayout(self)
		self.setLayout(grid)
		# list of filters
		self.filtersBox = QComboBox(self)
		self.filtersBox.setEditable(False)
		self.filtersBox.addItems(all_orbs_restrictions_names())
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
		closeButton = QPushButton(tr('Close'), self)
		closeButton.setDefault(True)
		closeButton.clicked.connect(self.close)
		buttonsLayout.addWidget(closeButton)
	
	def newFilterEvent(self):
		new = OrbsRestrictionsDialog(self)
		ok = new.exec_()
		if ok:
			self.reset()
	
	def editFilterEvent(self):
		filt = OrbsRestrictions(
			all_orbs_restrictions_names()[self.filtersBox.currentIndex()])
		edit = OrbsRestrictionsDialog(self, filt)
		ok = edit.exec_()
		if ok:
			self.reset()
	
	def deleteFilterEvent(self):
		tr = self.tr
		name = all_orbs_restrictions_names()[self.filtersBox.currentIndex()]
		ret = QMessageBox.warning(self, tr('Delete Orbs Restrictions'),
			str(tr('Are you sure you want to delete orbs restrictions \xab %(filter)s \xbb ?')) % {
				'filter': name},
			QMessageBox.Cancel|QMessageBox.Yes, QMessageBox.Yes)
		if ret == QMessageBox.Yes:
			filt = OrbsRestrictions(name)
			try:
				filt.delete()
			except ValueError: # cannot delete
				QMessageBox.critical(self, tr('Required Orbs Restrictions'),
					tr('Cannot delete required orbs restrictions.'))
			self.reset()
	
	def reset(self):
		"""Reload filters list."""
		self.filtersBox.clear()
		self.filtersBox.addItems(all_orbs_restrictions_names())



def main():
	app = QApplication(sys.argv)
	main = OrbsRestrictionsManagerDialog()
	main.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

# End.
