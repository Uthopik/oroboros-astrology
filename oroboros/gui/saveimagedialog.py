#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Save image dialog.

"""

import os.path

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from oroboros.core import cfg


__all__ = ['SaveImageDialog']


_iconsDir = os.path.join(os.path.dirname(__file__), 'icons')


class SaveImageDialog(QDialog):
	
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		tr = self.tr
		self.setWindowTitle(tr('Save Image'))
		self.setSizeGripEnabled(True)
		self.setMinimumWidth(250)

		# Atributos de salida de la imagen
		self.img_fname = ""
		self.img_ext = "png"
		self.img_width = 600
		self.img_height = 600

		# layout
		grid = QGridLayout(self)
		self.setLayout(grid)

		# file name
		grid.addWidget(QLabel(tr('File Name')), 0, 0)
		self.fname = QLineEdit(self)
		self.fname.setReadOnly(False)
		grid.addWidget(self.fname, 0, 1)

		# file chooser
		chooseButton = QToolButton(self)
		chooseButton.setIcon(QIcon(os.path.join(_iconsDir, 'gtk-open.png')))
		chooseButton.setToolTip(tr('Get file name'))
		chooseButton.clicked.connect(self.getFileName)
		grid.addWidget(chooseButton, 0, 2)

		# extension/format
		grid.addWidget(QLabel(tr('Extension')), 1, 0)
		self.extBox = QComboBox(self)
		self.extBox.setEditable(False)
		self.extBox.addItems(
			['png', 'jpg', 'bmp', 'ppm', 'tiff', 'xbm', 'xpm', 'svg'])
		grid.addWidget(self.extBox, 1, 1, 1, 2)

		# width
		grid.addWidget(QLabel(tr('Width')), 2, 0)
		self.widthBox = QSpinBox(self)
		self.widthBox.setRange(1, 10000)
		self.widthBox.setSuffix(tr('px', 'Pixels'))
		self.widthBox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
		self.widthBox.setValue(600)
		grid.addWidget(self.widthBox, 2, 1, 1, 2)

		# height
		grid.addWidget(QLabel(tr('Height')), 3, 0)
		self.heightBox = QSpinBox(self)
		self.heightBox.setRange(1, 10000)
		self.heightBox.setSuffix(tr('px', 'Pixels'))
		self.heightBox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
		self.heightBox.setValue(600)
		grid.addWidget(self.heightBox, 3, 1, 1, 2)

		# buttons
		buttonsLayout = QHBoxLayout()
		grid.addLayout(buttonsLayout, 4, 0, 1, 3)
		cancelButton = QPushButton(tr('Cancel'), self)
		cancelButton.clicked.connect(self.reject)
		buttonsLayout.addWidget(cancelButton)
		okButton = QPushButton(tr('Save'), self)
		okButton.setDefault(True)
		okButton.clicked.connect(self.accept)
		buttonsLayout.addWidget(okButton)

	def getFileName(self):
		tr = self.tr
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog

		res = QFileDialog.getSaveFileName(
			self,
			tr('Save Image As...'),
			os.path.expanduser(cfg.charts_dir),
			tr('Images (*.png *.jpg *.bmp *.ppm *.tiff *.xbm *.xpm *.svg)'),
			options=options
		)

		path = res[0] if isinstance(res, tuple) else res

		if path:
			self.fname.setText(path)

	def accept(self):
		"""Check input data and store target values."""
		filename = self.fname.text().strip()
		if not filename:
			QMessageBox.critical(self, self.tr('Missing File Name'),
				self.tr('Please set file name.'))
			self.fname.setFocus()
			return

		self.img_fname = filename
		self.img_ext = str(self.extBox.currentText())
		self.img_width = int(self.widthBox.value())
		self.img_height = int(self.heightBox.value())

		QDialog.accept(self)

	def exec_(self):
		ok = QDialog.exec_(self)
		if not ok:
			return ok, None, None, None, None
		else:
			return ok, self.img_fname, self.img_ext, self.img_width, self.img_height


def main():
	import sys
	app = QApplication(sys.argv)
	main_win = SaveImageDialog()
	main_win.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

# End.
