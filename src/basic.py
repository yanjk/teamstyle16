# -*- coding: UTF-8 -*-
# basic.py

# 缩进: 4空格
# 命名: (参考 Google style)
# 类名: CapWords
# 模块名: lower_with_under
# 函数或方法名: firstLowerCapWords()
# 常量名: CAPS_WITH_UNDER
# 其他变量,实例及函数形参: lower_with_under 

# 变量名开头加一个下划线(_)能对保护模块(protected)中的变量及函数提供一些支持(不会被 import * from 导入)
# 在实例的变量和方法开头加两个下划线(__)能有效地帮助把该变量或方法变成类的私有内容(using name mangling)

# 以下所有数据暂时并无理论依据...

import random from random

# 基础参数限制
ROUND_MAX = 300     # 最大回合数
MAP_SIZE_MAX = 80   # 地图最大边长
FORT_NUM_MAX = 6    # 据点最大数量
MINE_NUM_MAX = 8    # 矿场最大数量
OILFIELD_NUM_MAX = 8    # 油田最大数量
MOVEABLE_UNIT_NUM_MAX = 30      # 每方最大可移动单位数
COMMAND_NUM_MAX = 1 + FORT_NUM_MAX + MOVEABLE_UNIT_NUM_MAX    # 每方单回合最大总指令数
INFINITY = float('inf')     # 正无穷, 大于任何有限数


score = [0, 0]      # 两队积分

#积分规则
FORT_SCORE = 1      # 占领据点每回合奖励积分
DAMAGE_SCORE = 1    # 每点伤害奖励积分
COLLECT_SCORE = 1   # 采集一单位资源奖励积分

# 维修代价
METAL_PER_HEALTH = 0.2    # 恢复1点生命所需金属

# 补给底线
SUPPLY_LIMIT = 0.1  # 资源数少于 SUPPLY_LIMIT * 上限 即不可继续补给(留给自己用..)(抛锚不可以么？）
                    # 基地, 据点燃料不设底线
                    # 基地弹药无限, 故也不必设底线
                    # 运输舰无攻击能力, 弹药不设底线


# 地图分层
UNDERWATER = 0  # 水下
SURFACE = 1     # 水面 or 地面
AIR = 2         # 空中


# 伤害类型
""" 潜艇只能造成和接受鱼雷伤害
    陆地建筑只能造成和受到火力伤害
    飞机不能受到鱼雷伤害 """
FIRE = 0        # 火力伤害
TORPEDO = 1     # 鱼雷伤害


# 地形
OCEAN = 0       # 海洋
LAND = 1        # 陆地


# 建筑
BASE = 0        # 基地
FORT = 1        # 据点


# 资源点
MINE = 0        # 矿场
OILFIELD = 1    # 油田


# 可移动单位(water_unit + formation)
SUBMARINE = 0   # 潜艇
DESTROYER = 1   # 驱逐舰
CRUISER = 2     # 巡洋舰
BATTLESHIP = 3  # 战舰
CARRIER = 4     # 航母
CARGO = 5       # 运输舰
FORMATION = 6   # 飞机编队(机群)


# 飞机编队内飞机种类
SCOUT = 0       # 侦察机
TORPEDOER = 1   # 鱼雷机
BOMBER = 2      # 轰炸机
FIGHTER = 3     # 战斗机



# 建筑属性
""" building_property = (sight_ranges, fire_ranges, 
                         health_max, fuel_max, ammo_max,ammo_once, metal_max, 
                         attacks, defences)
        其中 sight_ranges = [UNDERWATER, SURFACE, AIR]
             fire_ranges = [UNDERWATER, SURFACE, AIR]
             attacks = [FIRE, TORPEDO]
             defences = [FIRE, TORPEDO] """
BUILDINGS = [([4, 10, 8], [0, 7, 5], 
              2000, 1000, INFINITY,6, 200, 
              [40, 0], [30, INFINITY]),     # 基地
             ([3, 8, 6], [0, 5, 4], 
              800, 200, 300,4, 200, 
              [25, 0], [12, INFINITY])]      # 据点


# 可移动单位(除飞机)属性, 即水面及水下单位属性
""" water_unit_property = (sight_ranges, fire_ranges,
                           health_max, fuel_max, ammo_max,ammo_once, metal_max, 
                           speed,food
                           attacks, defences) """
# 数据不可信...
WATER_UNITS = [([6, 5, 3], [5, 5, 0],
                35, 120, 20,2, 0,
                6,2
                [0, 40], [INFINITY, 5]),    # 潜艇
               ([5, 10, 8], [4, 8, 6],
                50, 150, 30,3, 0,
                8,2
                [13, 20], [10, 15]),          # 驱逐舰
               ([5, 10, 8], [4, 8, 6],
                70, 300, 30,3, 0,
                7,3
                [20, 10], [12, 13]),          # 巡洋舰
               ([5, 10, 8], [4, 8, 6],
                100, 200, 50,5, 0,
                6,4
                [30, 10], [20, 15]),          # 战舰
               ([5, 10, 8], [4, 8, 6],
                100, 400, 70,2, 80,
                5,4
                [15, 0], [16, 12]),          # 航母
               ([5, 10, 8], [4, 8, 6],
                60, 300, 50,0, 50,
                7,1
                [0, 0], [15, 10])]          # 运输舰


# 飞机常量属性
SCOUT_SIGHT_RANGES = [2, 12, 16]    # 侦察机视野
OTHER_SIGHT_RANGES_WITHOUT_SCOUT = [0, 8, 10]   # 其他机种视野
FORMATION_FIRE_RANGES = [0, 0, 1]
FORMATION_SPEED = 12
FORMATION_FOOD = 1
FORMATION_TOTAL_PLANES = 30     # 一个机群最多30架飞机
FORMATION_SCOUNTADD = 0.1   #附近每有一处有侦察机，属性提升百分比

# 各机种参数
""" plane_property = (health_max, fuel_max, ammo_max,ammo_once
                      attacks, defences) """
PLANES = [(7, 10, 5, 1
           [2, 0], [1, INFINITY]),    # 单架战斗机
          (6, 10, 4,2
           [0, 2], [1, INFINITY]),    # 单架鱼雷机
          (8, 10, 4,2
           [3, 0], [2, INFINITY]),    # 单架轰炸机
          (5, 15, 2,2
           [1, 1], [0, INFINITY])]    # 单架侦察机

# 命中率
def isHit(distance, fire_range):
    """与双方距离, 攻方射程有关的命中率, 返回是否命中"""
    if distance > fire_range:
        accuracy = 0
    else:
        accuracy = 1 - float(distance) *(distance - 1) /(fire_range + 1) / (fire_range + 1)
    return random() < accuracy

# 攻击修正
def modifiedAttack(distance, fire_range, attack):
    """返回距离修正后的攻击力"""
    return int((1 - float(distance - 1) / (fire_range + 1)) * attack)    # 可能大于attack

# 对象

class Position(object):
    """三维坐标"""
    def __init__(self, x, y, z=1):
        super(Position, self).__init__()
        self.x = x
        self.y = y
        self.z = z
        self.level = z      

    def __eq__(self, other):
        """判断两Position实例相等"""
        if isinstance(other, Position):
            return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
        else:
            return False

    def distance(self, target):
        """返回该位置到target(点或矩形)的(最小)距离"""
        if isinstance(target, Position):
            return abs(target_pos.x - self.x) + abs(target_pos.y - self.y)
        elif isinstance(target, Rectangle):
            return target.distance(self)    # 调用Rectangle.distance()
        else:
            return -1;

    def region(self, level, range):     
        """返回距离该位置range以内区域点集list"""
        region_points = []
        for y in xrange(self.y - range, self.y + range + 1):
            for x in xrange(self.x - range, self.x + range + 1):
                if self.distance(Position(x, y, level)) <= range:
                    region_points.append(Position(x, y, level))
        # 在一矩形范围内寻找符合条件的点
        return region_points


class Rectangle(object):
    """平面矩形区域, 由左上及右下两顶点坐标确定"""
    def __init__(self, upper_left, lower_right):
        super(Rectangle, self).__init__()
        self.upper_left = upper_left
        self.lower_right = lower_right
        self.level = upper_left.z   # 转化为upper_left所在平面
        self.lower_right.z = self.level

    def bound(self):
        """返回矩形区域的边界点集list"""
        bound_points = []
        for x in xrange(self.upper_left.x, self.lower_right.x + 1):
            bound_points.append(Position(x, self.upper_left.y, self.level))
            bound_points.append(Position(x, self.lower_right.y, self.level))
        for y in xrange(self.upper_left.y + 1, self.lower_right.y):
            bound_points.append(Position(self.upper_left.x, y, self.level))
            bound_points.append(Position(self.lower_right.x, y, self.level))
        return bound_points

    def distance(self, target):
        """返回该矩形区域到target(点或矩形)的最小距离"""
        if isinstance(target, Position):
            return min([point.distance(target) for point in self.bound()])
        elif isinstance(target, Rectangle):
            return min([self.distance(point) for point in target.bound()])
        else:
            return -1

    def region(self, level, range = 0):
        """返回矩形区域向外延伸range范围的区域点集list"""
        region_points = []
        for y in xrange(self.upper_left.y, self.lower_right.y + 1):
            for x in xrange(self.upper_left.x, self.lower_right.x + 1):
                region_points.append(Position(x, y, level))    # region_points = 矩形区域内所有点构成的list
        if range == 0:
            return region_points
        else:
            for point in self.bound():
                for pos in point.region(level, range):
                    if pos not in region_points:
                        region_points.append(pos)
            return region_points


class Mine(object):
    """矿场"""
    def __init__(self, kind, pos, metal):
        super(Mine, self).__init__()
        self.kind = 'MINE'
        self.pos = pos
        self.metal = metal

class Oilfield(object):
    """油田"""
    def __init__(self, kind, pos, fuel):
        super(Oilfield, self).__init__()
        self.kind = 'OILFIELD'
        self.pos = pos
        self.fuel = fuel
        
        
class UnitBase(object):
    """单位抽象, 派生出建筑类以及可移动单位类"""
    def __init__(self, team, kind, pos, sight_ranges, fire_ranges, health, fuel, ammo, 
                 attacks, defences):
        super(UnitBase, self).__init__()
        self.team = team
        self.kind = kind                    # 单位种类以字符串保存
        self.pos = pos                      # pos可以是一个点(Position类型), 
                                            # 也可以是矩形(Rectangle类型)
        self.sight_ranges = sight_ranges
        self.fire_ranges = fire_ranges
        self.health = self.health_max = health
        self.fuel = self.fuel_max = fuel
        self.ammo = self.ammo_max = ammo
        self.attacks = attacks
        self.defences = defences

    def availableRegion(self, option = 'sight'):
        """返回三维视野区域或可攻击区域(option == 'fire')"""
        if option == 'sight':
            ranges = self.sight_ranges
        elif option == 'fire':
            ranges = self.fire_ranges
        else:
            return -1   # unknown option
        available_region = []
        for z in xrange(3):
            available_region += pos.region(z, ranges[z])
        return available_region

    def view(self, target_pos):
        """查看目标点的状态"""
        if target_pos not in self.availableRegion('sight'):
            return -1   # 不在视野范围内, 不可见
        else:
            pass
            ## 返回单位信息...

    def attack(self, target_unit, attack_type = FIRE):
        """攻击(默认火力攻击)某单位"""
        distance = self.pos.distance(target_unit.pos)
        range = self.fire_ranges[target_unit.pos.level]
        if distance > range:
            return -1   # 不在攻击范围内
        elif self.ammo <= 0:
            return -2   # 无弹药
        else:
            self.ammo -= self.ammo_once  # 减少弹药数目
            if not isHit(distance, range):
                damage = 0  # miss
                return
            else:
                damage = self.attacks[attack_type]* scount
                         - target_unit.defences[attack_type]*
                score[self.team] += damage
                if damage >= target_unit.health:
                    target_unit.health = 0  # killed
                else:
                    target_unit.health -= damage
                return

def replenishFuelAmmo(giver, receiver):   # 补给燃料弹药
    if giver.kind == 'BASE':
        fuel_supply_limit = ammo_supply_limit = 0
    elif giver.kind == 'FORT':
        fuel_supply_limit = 0
        ammo_supply_limit = SUPPLY_LIMIT
    elif giver.kind == 'CARGO':
        fuel_supply_limit = SUPPLY_LIMIT
        ammo_supply_limit = 0
    else:
        fuel_supply_limit = ammo_supply_limit = SUPPLY_LIMIT
    provides = [0, 0]    # 维修者提供的燃料, 弹药
    provides[0] = max(giver.fuel - giver.fuel_max * fuel_supply_limit, 
                      receiver.fuel_max - receiver.fuel)
    provides[1] = max(giver.ammo - giver.ammo_max * ammo_supply_limit, 
                      receiver.ammo_max - receiver.ammo)
    giver.fuel -= provides[0]
    giver.ammo -= provides[1]
    receiver.fuel += provides[0]
    receiver.ammo += provides[1]




class Base(UnitBase):
    """基地, 继承自UnitBase"""
    def __init__(self, team, rectangle, metal):
        super(Base, self).__init__(team, 'BASE', rectangle, 
                                   *(BUILDINGS[BASE][:5] + BUILDINGS[BASE][-2:]))
                                   # 从元组解析出数据后传入UnitBase.__init__()
        self.metal = self.metal_max = BUILDINGS[BASE][5]

    def supply(self, our_unit):   # 补给操作
        """基地对周围单位补给, 不对外提供金属"""
        if not self.team == our_unit.team:
            return -1   # 非友军
        elif ((our_unit.kind == 'FORMATION' and not our_unit.pos in self.pos.region(level = AIR, range = 0))
             or not our_unit.pos in self.pos.region(level = our_unit.pos.z, range = 1)):
            return -2   # 不在范围内
        else:
            replenishFuelAmmo(self, our_unit)
            return 0

    def repair(self, our_unit, plane_nums = [3, 3, 3, 1]):  # 提供默认编队配置
        """维修, 对飞机的维修操作特殊"""
        if not self.team == our_unit.team:
            return -1   # 非友军
        elif our_unit.kind == 'FORMATION':  
            if not our_unit.pos in self.pos.region(level = AIR, range = 0):  
                return -2   # 不在范围内
            else:
                ## 维修飞机至plane_nums配置, 如果金属不足, 则按侦察机->鱼雷机->轰炸机->战斗机的顺序依次维修
                while self.metal >= METAL_PER_HEALTH:
                    pass
                replenishFuelAmmo(self, our_unit)
                return 0
        else:
            if not our_unit.pos in self.pos.region(level = our_unit.pos.z, range = 1):
                return -2   # 不在范围内
            else:
                provide_metal = max(self.metal, (our_unit.health_max - our_unit.health) * METAL_PER_HEALTH)
                self.metal -= provide_metal
                our_unit.health += provide_metal / METAL_PER_HEALTH
                replenishFuelAmmo(self, our_unit)
                return 0

    def build(self, kind, plane_nums = [3, 3, 3, 1]):
        """生产单位, 新单位出生地在基地陆地周围一圈"""
        pass    ##


class Fort(UnitBase):
    """据点, 继承自UnitBase"""
    def __init__(self, team, rectangle):
        super(Fort, self).__init__(team, 'FORT', rectangle, 
                                   *(BUILDINGS[FORT][:5] + BUILDINGS[FORT][-2:]))

    def supply(self, our_unit):
        """据点对周围单位补给燃料弹药"""  
        if not self.team == our_unit.team:
            return -1   # 非友军
        elif ((our_unit.kind == 'FORMATION' and not our_unit.pos in self.pos.region(level = AIR, range = 0))
              or not our_unit.pos in self.pos.region(level = our_unit.pos.z, range = 1)):
            return -2   # 不在范围内
        else:
            replenishFuelAmmo(self, our_unit)
            return 0


class Submarine(UnitBase):
    """潜艇"""
    def __init__(self, team, pos):
        super(Submarine, self).__init__(team, 'SUBMARINE', pos,
                                        *(WATER_UNITS[SUBMARINE][:5] + WATER_UNITS[SUBMARINE][-2:]))
        self.speed = WATER_UNITS[SUBMARINE][6]


class Destroyer(UnitBase):
    """驱逐舰"""
    def __init__(self, team, pos):
        super(Destroyer, self).__init__(team, 'DESTROYER', pos,
                                        *(WATER_UNITS[DESTROYER][:5] + WATER_UNITS[DESTROYER][-2:]))
        self.speed = WATER_UNITS[DESTROYER][6]


class Cruiser(UnitBase):
    """巡洋舰"""
    def __init__(self, team, pos):
        super(Cruiser, self).__init__(team, 'CRUISER', pos,
                                      *(WATER_UNITS[CRUISER][:5] + WATER_UNITS[CRUISER][-2:]))
        self.speed = WATER_UNITS[CRUISER][6]
        

class Battleship(UnitBase):
    """战舰"""
    def __init__(self, team, pos):
        super(Battleship, self).__init__(team, 'BATTLESHIP', pos,
                                         *(WATER_UNITS[BATTLESHIP][:5] + WATER_UNITS[BATTLESHIP][-2:]))
        self.speed = WATER_UNITS[BATTLESHIP][6]


class Carrier(UnitBase):
    """航母"""
    def __init__(self, team, pos, metal):
        super(Carrier, self).__init__(team, 'CARRIER', pos,
                                      *(WATER_UNITS[CARRIER][:5] + WATER_UNITS[CARRIER][-2:]))
        self.metal = self.metal_max = WATER_UNITS[CARRIER][5]
        self.speed = WATER_UNITS[CARRIER][6]

    def supply(self, our_unit):
        """航母对周围单位补给燃料弹药, 可向基地,运输舰以及航母补充金属"""
        if not self.team == our_unit.team:
            return -1   # 非友军
        elif ((our_unit.kind == 'FORMATION' and not self.pos in our_unit.pos.region(level = AIR, range = 0))
              or not self.pos in our_unit.pos.region(level = self.pos.z, range = 1)):
             # our_unit可能是基地或据点, 即our_unit.pos可能是矩形, 因此改为判断self.pos 是否在our_unit.pos.region()内
             # 考虑是否可以将region()优化为distance(), 可以较好地兼容Position和Rectangle
            return -2   # 不在范围内
        else:
            replenishFuelAmmo(self, our_unit)
            if our_unit.kind == 'BASE' or our_unit.kind == 'CARGO' or our_unit.kind == 'CARRIER':
                provide_metal = min(self.metal, our_unit.metal_max - our_unit.metal)
                self.metal -= provide_metal
                our_unit.metal += provide_metal
            return 0 


class Cargo(UnitBase):
    """运输舰"""
    def __init__(self, team, pos, metal):
        super(Cargo, self).__init__(team, 'CARGO', pos,
                                    *(WATER_UNITS[CARGO][:5] + WATER_UNITS[CARGO][-2:]))
        self.metal = self.metal_max = WATER_UNITS[CARGO][5]
        self.speed = WATER_UNITS[CARGO][6]

    def supply(self, our_unit):
        """运输舰对周围单位补给燃料弹药, 可向基地,运输舰以及航母补充金属"""
        if not self.team == our_unit.team:
            return -1   # 非友军
        elif ((our_unit.kind == 'FORMATION' and not self.pos in our_unit.pos.region(level = AIR, range = 0))
              or not self.pos in our_unit.pos.region(level = self.pos.z, range = 1)):
            return -2   # 不在范围内
        else:
            replenishFuelAmmo(self, our_unit)
            if our_unit.kind == 'BASE' or our_unit.kind == 'CARGO' or our_unit.kind == 'CARRIER':
                provide_metal = min(self.metal, our_unit.metal_max - our_unit.metal)
                self.metal -= provide_metal
                our_unit.metal += provide_metal
            return 0 

    def collect(self, resource):
        """运输舰从资源点采集资源"""
        if resource.kind == 'MINE' and resource.metal > 0:
            supply = min(self.metal_max - self.metal, resource.metal)
            self.metal += supply
            resource.metal -= supply
        elif resource.kind == 'OILFIELD' and resource.fuel > 0:
            supply = min(self.fuel_max - self.fuel, resource.fuel)
            self.fuel += supply
            resource.fuel -= supply
        else:
            return -1



def renum(formation):
    """根据飞机编队的剩余health重置"""
    health_tank = formation.health
    max_nums = formation.plane_nums
    formation.plane_nums = [0, 0, 0, 0]
    index = 0     # 战斗机
    while health_tank > 0 and index < 4:
        if formation.plane_nums[index] == max_nums[index]:
            index += 1
            continue
        elif health_tank >= PLANES[index][0]:
            health_tank -= PLANES[index][0]
            formation.plane_nums[index] += 1
        else:
            formation.plane_nums[index] += 1    # 残血
            break
    return 


class Formation(UnitBase):
    """飞机编队"""
    def __init__(self, team, pos, plane_nums = [3, 3, 3, 1]):
        if sum(plane_nums) > FORMATION_TOTAL_PLANES:
            return -1   # 飞机数超出编队容量
        sight_ranges = (SCOUT_SIGHT_RANGES if plane_nums[3] > 0 else OTHER_SIGHT_RANGES_WITHOUT_SCOUT)
        health = sum([PLANES[i][0] * plane_nums[i] for i in xrange(4)])
        fuel = sum([PLANES[i][1] * plane_nums[i] for i in xrange(4)])
        ammo = sum([PLANES[i][2] * plane_nums[i] for i in xrange(4)])
        attacks = defences = [0, 0]
        for i in xrange(4):
            attacks[0] += [PLANES[i][-2][j] * plane_nums[i] for j in xrange(2)][0]
            attacks[1] += [PLANES[i][-2][j] * plane_nums[i] for j in xrange(2)][1]
            defences[0] += [PLANES[i][-1][j] * plane_nums[i] for j in xrange(2)][0]
            defences[1] += [PLANES[i][-1][j] * plane_nums[i] for j in xrange(2)][1]     # tested. result is good
        super(Formation, self).__init__(team, 'FORMATION', pos,
                                        sight_ranges, FORMATION_FIRE_RANGES, 
                                        health, fuel, ammo, attacks, defences)
        self.plane_nums = plane_nums
        self.speed = FORMATION_SPEED

    def update(self):
        """飞机的参数随plane_nums动态变化, update函数用于更新机群参数"""
        renum(self)
        self.sight_ranges = (SCOUT_SIGHT_RANGES if self.plane_nums[3] > 0 else OTHER_SIGHT_RANGES_WITHOUT_SCOUT)
        self.health_max = sum([PLANES[i][0] * self.plane_nums[i] for i in xrange(4)])
        self.fuel_max = sum([PLANES[i][1] * self.plane_nums[i] for i in xrange(4)])
        self.ammo_max = sum([PLANES[i][2] * self.plane_nums[i] for i in xrange(4)])
        attacks = defences = [0, 0]
        for i in xrange(4):
            attacks[0] += [PLANES[i][-2][j] * self.plane_nums[i] for j in xrange(2)][0]
            attacks[1] += [PLANES[i][-2][j] * self.plane_nums[i] for j in xrange(2)][1]
            defences[0] += [PLANES[i][-1][j] * self.plane_nums[i] for j in xrange(2)][0]
            defences[1] += [PLANES[i][-1][j] * self.plane_nums[i] for j in xrange(2)][1]

