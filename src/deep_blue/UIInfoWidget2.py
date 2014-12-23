#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from ui_gameinfo2 import *

NumToUnitType = {0:"基地",1:"据点",2:"矿场",3:"油田",4:"潜艇",5:"驱逐舰",6:"航母",7:"运输舰",8:"战斗机",9:"侦察机"}
NumToMapType = {0:"海洋",1:"陆地"}

class InfoWidget2(QWidget, Ui_GameInfo2):
	def __init__(self, parent = None):
		super(InfoWidget2, self).__init__(parent)
		self.setupUi(self)
		self.unit = None
		self.flag = -1
		self.show = False

	def newUnitInfo(self, unit, flag, battle):
		Elements = [battle.elements(0), battle.elements(1), battle.elements(2)]
		for i in range(3):
			for element in Elements[i].values():
				if element.index == unit.index:
					unit = element
		self.unit = unit
		self.flag = flag
		self.show = True
		self.resetUnitInfo()
		self.TeamLineEdit.setText("%d" %unit.team)
		self.CoordinateLineEdit.setText("(%d, %d, %d)" %(unit.position.x,unit.position.y,unit.position.z))
		self.TypeLineEdit.setText(QString.fromUtf8(NumToUnitType[unit.kind]))
		if unit.kind == 2:
			self.CarrySourceLineEdit.setText("%d" %unit.metal)
			return
		if unit.kind == 3:
			self.FuelLineEdit.setText("%d" %unit.fuel)
			return

		self.HealthLineEdit.setText("%d/%d" %(unit.health,unit.health_max))
		if unit.kind != 7:
			self.AttackLineEdit.setText("%d/%d" %(unit.attacks[0],unit.attacks[1]))
			self.FireRangeLineEdit.setText("%d/%d/%d" %(unit.fire_ranges[0],unit.fire_ranges[1],unit.fire_ranges[2]))
			self.AmmoLineEdit.setText("%.1f/%.1f/%.1f" %(unit.ammo_once,unit.ammo,unit.ammo_max))
		self.DefenceLineEdit.setText("%.1f/%.1f" %(unit.defences[0],unit.defences[1]))
		self.SightRangeLineEdit.setText("%d/%d/%d" %(unit.sight_ranges[0],unit.sight_ranges[1],unit.sight_ranges[2]))
		if flag >=4:
			if unit.kind != 1 and unit.kind != 0:
				self.SpeedLineEdit.setText("%d" %unit.speed)
				self.PopulationLineEdit.setText("%d" %unit.population)
				self.NeedMetalLineEdit.setText("%d" %unit.cost)
		if flag == 0 or flag == 1:
			if unit.team != flag:
				return
		self.FuelLineEdit.setText("%d/%d" %(unit.fuel,unit.fuel_max))
		if unit.kind == 7:
			self.CarrySourceLineEdit.setText("%d/%d" %(unit.metal,unit.metal_max))
		if flag >= 4:
			if unit.kind != 1 and unit.kind != 0:
				self.MoveTargetLineEdit.setText("(%d, %d, %d)" %(unit.dest.x,unit.dest.y,unit.dest.z))

	def newMapInfo(self, kind):
		self.TerrainLineEdit.setText(QString.fromUtf8(NumToMapType[kind]))

	def resetUnitInfo(self):
		self.show = False
		self.CoordinateLineEdit.setText("")
		self.TypeLineEdit.setText("")
		self.HealthLineEdit.setText("")
		self.AttackLineEdit.setText("")
		self.DefenceLineEdit.setText("")
		self.SightRangeLineEdit.setText("")
		self.FireRangeLineEdit.setText("")
		self.SpeedLineEdit.setText("")
		self.PopulationLineEdit.setText("")
		self.NeedMetalLineEdit.setText("")
		self.FuelLineEdit.setText("")
		self.AmmoLineEdit.setText("")
		self.CarrySourceLineEdit.setText("")
		self.MoveTargetLineEdit.setText("")
		self.TerrainLineEdit.setText("")

	def updateInfo(self, battle):
		if not self.unit:
			return
		Elements = [battle.elements(0), battle.elements(1), battle.elements(2)]
		for i in range(3):
			for element in Elements[i].values():
				if element.index == self.unit.index:
					print "update info"
					self.unit = element
					self.newUnitInfo(self.unit, self.flag, battle)
					return

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = InfoWidget2()
	form.show()
	app.exec_()