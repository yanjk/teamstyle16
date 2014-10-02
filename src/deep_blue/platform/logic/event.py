# -*- coding: UTF-8 -*-
# event.py

from basic import *

class Event(object):
    def __init__(self, description):
        self.description = description
    def description(self):
        return self.description

class AddProductionEntry(Event):
    """添加生产条目"""
    def __init__(self, team, kind):
        super(AddProductionEntry, self).__init__('AddProductionEntry')
        self.team = team
        self.kind = kind

class AttackPos(Event):
    """攻击"""
    def __init__(self, index, target, hit, damage):
        super(Attack, self).__init__('Attack')
        self.index = index
        self.target = target  #position
        self.hit = hit
        self.damage = damage

class AttackUnit(Event):
    """攻击"""
    def __init__(self, index, target, hit, damage):
        super(Attack, self).__init__('Attack')
        self.index = index
        self.target = target  #索引号
        self.hit = hit
        self.damage = damage

class Supply(Event):
    """补给"""
    def __init__(self, index, target, fuel, metal, ammo):
        super(Supply, self).__init__('Supply')
        self.index = index
        self.target = target
        self.fuel = fuel
        self.metal = metal
        self.ammo = ammo

class Fix(Event):
    """修理"""
    def __init__(self, index, target, metal, health_increase, new_type):
        super(Fix, self).__init__('Fix')
        self.index = index
        self.target = target
        self.metal = metal
        self.health_increase = health_increase
        self.new_type = new_type

class Collect(Event):
    """收集"""
    def __init__(self, index, target, fuel, metal):
        super(Collect, self).__init__('Collect')
        self.index = index
        self.target = target
        self.fuel = fuel
        self.metal = metal

class ChangeDest(Event):
    """修改目的地"""
    def __init__(self, index, dest):
        super(ChangeDest, self).__init__('ChangeDest')
        self.index = index
        self.dest = dest

class Move(Event):
    """移动"""
    def __init__(self, index, nodes): ##nodes 为移动路径上的拐点
        super(Move, self).__init__('Move')
        self.index = index
        self.nodes = nodes

class Create(Event):
    """生产"""
    def __init__(self, index):
        super(Create, self).__init__('Create')
        self.index = index

class Destroy(Event):
    """单位损毁"""
    def __init__(self, index):
        super(Destroy, self).__init__('Destroy')
        self.index = index

class Capture(Event):
    """占领堡垒"""
    def __init__(self, index, team):
        super(Capture, self).__init__('Capture')
        self.index = index
        self.team = team
