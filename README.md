# CS2 Python Cheat Features

## New UI Preview

<p align="center">
  <img src="https://i.imgur.com/HlRGsOU.png" alt="Main UI Screenshot" width="600"/>
</p>

---

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

## Downloads

- [V1.4](https://www.unknowncheats.me/forum/downloads.php?do=file&id=44694)  
- [V1.5](https://www.unknowncheats.me/forum/downloads.php?do=file&id=44911)  
- [V1.7](https://www.unknowncheats.me/forum/downloads.php?do=file&id=44961)  
- [V1.8](https://www.unknowncheats.me/forum/downloads.php?do=file&id=45009)  
- [V1.9](https://www.unknowncheats.me/forum/downloads.php?do=file&id=48333)  
- [V2.0 (Waiting for Approval)](https://www.unknowncheats.me/forum/downloads.php?do=file&id=50285)

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
