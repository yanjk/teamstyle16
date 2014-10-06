#ifndef TEAMSTYLE16_BASIC_H
#define TEAMSTYLE16_BASIC_H

#include <cstdint>
#include <cstddef>

namespace teamstyle16
{

const int kMaxElementNum = 200;
const int kMaxProductionListSize = 200;

enum { NO_TEAM = 2 };
enum Level { UNDERWATER, SURFACE, AIR };
enum AttackType { FIRE, TORPEDO };
enum MapType { OCEAN, LAND };

enum ElementType
{
    // Buildings
    BASE,
    FORT,
    // Resources
    MINE,
    OILFIELD,
    // Units
    SUBMARINE,
    DESTROYER,
    CARRIER,
    CARGO,
    FIGHTER,
    SCOUT,
    kElementTypes
};


struct Position
{
    int x;
    int y;
    int z;
};

struct Size
{
    int x_length;
    int y_length;
};

// Describe properties of an element that won't change over time
struct Property
{
    Level level;
    Size size;

    int sight_ranges[3];
    int fire_ranges[3];

    int health_max;
    int fuel_max;
    int ammo_max;
    int ammo_once;  // Ammo consumption per attack
    int metal_max;

    int attacks[2];
    int defences[2];
    int speed;

    int cost;  // Metal consumption to build
    int build_round;
	int population;
};

struct State
{
    int index;  // Every element has an unique index

    Position pos;  // position of the upper-left corner
    int type;
    int team;
    bool visible;

    int health;
    int fuel;
    int ammo;
    int metal;

    Position destination;
};

struct ProductionEntry
{
    int unit_type;
    int round_left;
};

struct GameInfo  // Necessary informations about the game
{
    int x_max;
    int y_max;

    int population_limit;
    int round_limit;
    float time_per_round;
    int weather;  // affect sight ranges of all the units/buildings

    int team_num;  // 0 or 1
    int scores[2];
    int round;

    int population;

    int element_num;
    State elements[kMaxElementNum];

    int production_num;
    ProductionEntry production_list[kMaxProductionListSize];
};


extern const std::size_t kMaxTeamNameSize;

extern const int kMaxMapSize;
extern const int kMaxRoundLimit;
extern const int kMaxPopulationLimit;

extern const int kFortScore;
extern const int kDamageScore;     // Score reward per damage made.
extern const int kCollectScore;    // Score reward per resource collected.

extern const Property kElementInfos[kElementTypes];


const GameInfo * Info();  // Get game information
MapType Map(int x, int y);

// Move to the next round, or the latest round if possible.
// Return rounds actually passed
int Update();

// Trying to move to the latest round, won't block.
// Return rounds actually passed
int TryUpdate();

// Commands
void AttackPos(int operand, Position target);
void AttackUnit(int operand, int target);
void ChangeDest(int operand, Position dest);
void Fix(int operand, int target);
void Produce(int operand, int type);
void Supply(int operand, int target, int fuel, int metal, int ammo);
void Cancel(int operand);


}  // namespace teamstyle16

#endif  // TEAMSTYLE16_BASIC_H
