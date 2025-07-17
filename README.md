# CS2 Python Cheat Features

## New UI Preview
[Video Showcase](https://www.youtube.com/watch?v=hjZrGECIhu4)

![Image](https://i.imgur.com/XiEJzhV.png)

---

```plaintext
# V3.0
# Changed aimbot to external mouse movement instead of writing view angles.
# Added no flash and spectator list
# Added armor bar and armor esp
````

```plaintext
# V2.7
# Added weapon esp
# Moved weapon check directly into aimbot.py
# Added bomb esp
```

```plaintext
# V2.6
# Added fov overlay color changed
# Added simple weapon check for aimbot (no aim on knife/nade)
# Aim at closest bone to crosshair added to aimbot
```

```plaintext
# V2.5
# Complete GUI Overhaul
# Custom Color window
# Added configs
# Added RCS Control toggle
# Added Render Refresh Rate Sync Toggle
# Added triggerbot always on
```

```plaintext
# V2.4
# The aimbot learns from the differences between the angles it actually moves to and what it intended to move to, based on your mouse movements during aiming.
# It stores these small delta angle adjustments linked to quantized angles in a dictionary (learning_data), which it saves to a JSON file so it can improve over time
# across sessions.

# Velocity Prediction:
# To improve aiming accuracy, the target's current velocity is read and used to predict
# where the target will be shortly (ahead by a small prediction time). This predicted position
# compensates for target movement, allowing the aimbot to lead shots instead of aiming at
# the target's current location, increasing hit probability especially on moving targets.
```

```plaintext
V2.3

<!> UPDATED FEATURES <!> 7/6/2025

- Separated script into modules further.

- Added aimbot & recoil control with extensive customization options.

- Added Glow ESP.

- Added cooldown feature to TriggerBot.

- Added BHop functionality (works very well).

- Added show FOV overlay for aimbot (separate overlay window).

- Added process handler support for client.dll.

- Added hardcoded offsets (can be updated using update_offsets.py).

- Added aimbot toggle bone; due to messed up bone indices, added downward_offset instead of fixing (kek).

- Made offsets load locally instead of fetching from a2x's CS2 Dumper.

- All features are completely customizable in pyqt5 gui.

- Removed initial weapon check from b2.3 (broken after update?)
```

## 🔧 Version 2.2

> 🗓️ **Updated:** 7/3/2025

```markdown
- Separated offsets into their own dedicated script/module for cleaner structure.

- Created a Legit Aimbot with recoil control system.
  * Logic contained in its own separate script for modularity.

- Modularized the project:
  * Scripts are now separated by function (e.g., `GHax.py`, `Aim_Recoil.py`).
  * Improves code organization and readability.

- Current structure requires `GHax.py` and `Aim_Recoil.py` to be run separately.
  * Full multiprocessing integration coming in Version 2.3.
```

---

## 🔧 Version 2.1

> 🗓️ **Updated:** 7/2/2025

```markdown
- Replaced separate "CT Side Only" and "T Side Only" ESP toggles with a unified team check logic:
  * "Enemy Only" shows ESP only for opposing team members.
  * "Team Only" shows ESP only for teammates.

- Fixed issue where the watermark would disappear when looking in certain directions.
  * Root cause: `pw_module.end_drawing()` was conditionally called inside the ESP loop,
    causing it to be skipped if no entities were drawn (e.g., looking at empty space).

- Refactored `WallHack.Render()` to call `pw_module.end_drawing()` exactly once,
  after processing all entities, ensuring proper rendering lifecycle every frame.

- This fix prevents visual glitches like the watermark vanishing or incomplete overlays
  when no entities are visible.

- Added FOV changer slider to GUI (default value: 90).
- Added disclaimer informing that FOV changes write directly to game memory.
- Slider updates the FOV value in real-time during gameplay.
```

---

## 🔧 Version 2.0

> 🗓️ **Updated:** 6/30/2025

```python
# V2.0

- Updated cheat for game
- Fixed triggerbot performance
- Changed UI
```

```python
# V1.9

# <!> UPDATED FEATURES <!> 5/11/2024

# The entity class was updated for the gameScene and the a2x dumper links.  
# Expanded offset dictionary for custom aimbot/no recoil development.

class Entity:
    def __init__(self, pointer, pawnPointer, process):
        self.pointer = pointer
        self.pawnPointer = pawnPointer
        self.process = process
        self.pos2d = None
        self.headPos2d = None

    def Health(self):
        return pw_module.r_int(self.process, self.pawnPointer + Offsets.m_iHealth)

    def Team(self):
        return pw_module.r_int(self.process, self.pawnPointer + Offsets.m_iTeamNum)

    def Pos(self):
        return pw_module.r_vec3(self.process, self.pawnPointer + Offsets.m_vOldOrigin)

    def Name(self):
        player_name = pw_module.r_string(self.process, self.pointer + Offsets.m_iszPlayerName, 32)
        return player_name.split("\x00")[0]

    def BonePos(self, index):
        gameScene = pw_module.r_int64(self.process, self.pawnPointer + Offsets.m_pGameSceneNode)
        boneArrayPointer = pw_module.r_int64(self.process, gameScene + Offsets.m_pBoneArray)
        return pw_module.r_vec3(self.process, boneArrayPointer + index * 32)

    def Wts(self, matrix):
        try:
            self.pos2d = pw_module.world_to_screen(matrix, self.Pos(), 1)
            self.headPos2d = pw_module.world_to_screen(matrix, self.BonePos(6), 1)
        except:
            return False
        return True
```

```text
V1.8

<!> UPDATED FEATURES <!> 5/11/2024

+ Added TriggerBot  
+ Added TriggerKey  
+ Added TriggerTeam  
+ Keyboard listener for triggerkey with winsound  
+ Temporarily removed config.json
```

```text
V1.7

<!> UPDATED FEATURES <!> 5/10/2024

+ Temporarily removed Triggerbot  
+ Temporarily removed config file  
+ Fixed bugs disabling all ESP features  
+ Smoother ESP  
+ Added PyQt5 menu with easy access options  
+ Python script can now be compiled with PyInstaller
```

```text
V1.6

<!> UPDATED FEATURES <!> 5/8/2024

+ Fixed wallhack to toggle bounding box and all ESP features independently  
  - To disable all ESP, set all false and wallhack true or wallhack false then restart  
  - Setting wallhack false on initialized script causes crash; can be re-enabled  
+ Added bounding box option with background opacity control
```

```text
V1.5

<!> UPDATED FEATURES <!> 5/7/2024

+ Squarebone ESP  
+ Updated crosshair  
+ Teamesp changed to enemy-only  
+ Wallhack no longer renders on local player  
+ Fixed major ReadProcessMemory error (Error: 299)  
+ Added name & health text colors  
+ Improved JSON config parsing  
+ Removed tkinter GUI (temporarily)
```

```text
V1.4

<!> UPDATED FEATURES <!> 5/3/2024

+ Added font size options for name and health ESP  
+ Added circle bone ESP (draws circles on main bones)  
+ Added skeleton ESP (may cause lag)  
+ Added color options for circle bone and skeleton  
+ Added headshape option (square or circle)
```

```text
V1.3

<!> UPDATED FEATURES <!> 4/23/2024

+ Triggerkey customization dropdown (shift, ctrl, alt, spacebar)  
+ Added external crosshair (simple "+" sign)  
+ Added health ESP  
+ Added name ESP  
+ Improved watermark with disable option
```

## Features List

- watermark  
- boxesp  
- healthbar  
- nameesp  
- healthesp  
- headesp  
- skeletonesp  
- circleboneesp  
- squareboneesp  
- lineEsp  
- crosshair  
- enemyOnly  
- Triggerbot  
- triggerbotOnSameTeam  
- enemycolor  
- teamcolor  
- headcolor  
- circlebonecolor  
- squarebonecolor  
- lineColor  
- namecolor  
- healthcolor  
- skeletoncolor  
- boxbackground  
- headshape  
- namesize  
- healthsize  
- triggerKey

## Usage Instructions

1. Ensure **Python** is installed.  
2. Run:

```bash
python GHax.py
```

3. Use the GUI Config Editor to customize settings.  
4. Enjoy cheating skids!

---

**Downloads**  
[Download V1.4](https://www.unknowncheats.me/forum/downloads.php?do=file&id=44694) |  
[Download V1.5](https://www.unknowncheats.me/forum/downloads.php?do=file&id=44911) |  
[Download V1.7](https://www.unknowncheats.me/forum/downloads.php?do=file&id=44961) |  
[Download V1.8](https://www.unknowncheats.me/forum/downloads.php?do=file&id=45009) |  
[Download V1.9](https://www.unknowncheats.me/forum/downloads.php?do=file&id=48333) |  
[Download V2.0](https://www.unknowncheats.me/forum/downloads.php?do=file&id=50285) _(waiting for approval)_  
[Download V2.1](https://www.unknowncheats.me/forum/downloads.php?do=file&id=50315) _(waiting for approval)_  
[Download V2.2](https://www.unknowncheats.me/forum/downloads.php?do=file&id=50335) _(waiting for approval)_

**Showcases**  
[V2.0 Showcase](https://www.youtube.com/watch?v=ky462PVNFhM&t=586s)  
[V2.1 Showcase](https://www.youtube.com/watch?v=oZ-TfVf9iqI)  
[V2.2 Showcase](https://www.youtube.com/watch?v=pDBap2KieU8)


To launch the cheat from CMD:

```bash
cd path/to/script
python GHax.py
```

## Install Dependencies

```bash
pip install keyboard requests pymem pyMeow pynput pyqt5 pywin32
```

> **Note**: If `pyMeow` throws an import error despite being installed via pip:

1. Download directly from:  
   [https://github.com/qb-0/pyMeow/releases/tag/1.73.42](https://github.com/qb-0/pyMeow/releases/tag/1.73.42)

2. In CMD, navigate to the folder containing `setup.py`, then run:

```bash
pip install .
```
