# Rules - Deep Blue

## 游戏背景

废话从略


## 游戏模式 

* 游戏按回合进行, 但侧重**即时战略**
* 对战双方各拥有一基地`Base`, **己方基地被摧毁**则战败
* 回合数达到上限时, 若双方基地均为被摧毁, 则**积分高者获胜**, 积分相等则平局

### 回合

* 回合以时间划分, 默认`time_per_round = 1000` (单位: ms)
* 回合数从第0回合开始计数, 回合数上限默认`round_max = 200`

### 地图

* 四方格地图
* 地图最大边长`map_size_max = 80`

### 人口

* 人口限制默认`population_max = 60'

### 积分

* 攻下据点`Fort`一次性奖励积分`capture_score = 100`
* 占领据点每回合奖励积分`fort_score = 10`
* 每造成一点伤害奖励积分`damage_score = 1`
* 对资源进行一次有效采集(采集到的资源 >= 10)奖励积分`collect_score = 10`


## 指令

### 维修

* 每恢复1点生命所需金属`metal_per_health = 0.2`
* or 1单位金属可恢复生命值`health_per_metal = 5`

### 补给

* 