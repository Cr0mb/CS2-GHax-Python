# CS2 Python Cheat Features

## New UI Preview
[Video Showcase](https://www.youtube.com/watch?v=hjZrGECIhu4)

![Image](https://i.imgur.com/XiEJzhV.png)


# GHax Changelog
---
### **V3.2**
`<!> UPDATED FEATURES <!> 7/22/2025`
```
- TriggerBot Memory Read Fixes:
  - Added early checks for invalid or zero pointers before reading memory
  - Wrapped critical memory reads in try/except blocks to safely handle partial read errors (Error 299)
  - Added early returns when entity/local player pointers are not valid
  - Prevented triggerbot logic from running if game window is not focused or player is not in-game
  - Skips unsafe reads outside of active match

- Spectator List Fixes:
  - Added safe read wrappers to handle partial read errors (Error 299)
  - Wrapped all memory reads in try-except blocks
  - Used cached variables and fallback defaults
  - Added filtering to skip invalid or self-controller entities early in the loop
  - Error logging without spamming errors
  - Ensured handling of pointer chains for online spectator detection
  - 1 second caching

- Distance ESP:
  - Displayed in front of box ESP for easier readability
```

<details>
<summary>Changelog</summary>


### **V3.1**

`<!> UPDATED FEATURES <!> 7/20/2025`

```
- Aimbot:
  - Added collections.deque for learning data storage
  - Cached pymem read funcs and math funcs in __init__
  - Learning data uses deque with maxlen=50
  - load_learning: convert keys to tuple, values to deque
  - save_learning: convert deque to list, keys to string
  - get_entity: cached local_player_controller read
  - get_current_bone_index: cache velocity vector outside loop
  - run():
    - Reduced sleep_base to 0.005
    - Dynamic recoil scale based on shots_fired
    - Smoothing jitter reduced, max smoothing 0.25
    - Mouse movement clamped to ±15
    - Added learning correction clamping and locking
    - Improved exception handling with shorter sleep
```

---

### **V3.0**

```txt
- Changed aimbot to external mouse movement instead of writing view angles
- Added no flash and spectator list
- Added armor bar and armor ESP
```

---

### **V2.7**

```txt
- Added weapon ESP
- Moved weapon check directly into aimbot.py
- Added bomb ESP
```

---

### **V2.6**

```txt
- Added FOV overlay color change
- Added simple weapon check for aimbot (no aim on knife/nade)
- Aim at closest bone to crosshair added to aimbot
```

---

### **V2.5**

```txt
- Complete GUI overhaul
- Custom color window
- Added configs
- Added RCS control toggle
- Added render refresh rate sync toggle
- Added triggerbot always on
```

---

### **V2.4**

```txt
- Aimbot learning system:
  - Stores delta angle adjustments linked to quantized angles
  - Saved across sessions for improvement

- Velocity prediction:
  - Reads target velocity to predict future position
  - Improves hit probability for moving targets
```

---

### **V2.3**

`<!> UPDATED FEATURES <!> 7/6/2025`

```txt
- Modularization:
  - Further separated scripts into modules

- Features:
  - Added aimbot & recoil control with extensive customization
  - Added Glow ESP
  - Added cooldown to TriggerBot
  - Added BHop (very effective)
  - Added separate FOV overlay window
  - Added client.dll process handler support
  - Hardcoded offsets, with update script
  - Downward offset added due to bone issues
  - Local offset loading instead of online fetch
  - Full PyQt5 GUI customization
  - Removed initial weapon check from b2.3 (broken)
```

---

### **V2.2**

`<!> UPDATED FEATURES <!> 7/3/2025`

```txt
- Modularization:
  - Separated offsets into its own script
  - Created legit aimbot with recoil control

- Organization:
  - Files modularized and separated
  - GHax.py and Aim_Recoil.py must both be run (multiprocessing coming v2.3)
```

---

### **V2.1**

`<!> UPDATED FEATURES <!> 7/2/2025`

```txt
- Replaced CT/T Side ESP toggles with:
  - "Enemy Only" or "Team Only"

- Fixed watermark disappearing bug due to conditional end_drawing()

- WallHack:
  - end_drawing() now called exactly once per frame

- GUI:
  - Added FOV changer slider (default 90)
  - Added disclaimer for memory writing
  - Real-time slider updates
```

---

### **V2.0**

`<!> UPDATED FEATURES <!> 6/30/2025`

```txt
- Updated cheat for game patch
- Fixed triggerbot performance
- Updated UI
```

---

### **V1.9**

`<!> UPDATED FEATURES <!> 5/11/2024`

```txt
- Updated Entity class for new gameScene structure and a2x links
- Expanded offset dictionary for aimbot/no recoil

Class Updates:
- Health, Team, Pos, Name, BonePos, WTS methods fully implemented with fallback handling
```

---

### **V1.8**

`<!> UPDATED FEATURES <!> 5/11/2024`

```txt
- Added TriggerBot
- Added TriggerKey and TriggerTeam
- Keyboard listener with winsound
- Temporarily removed config.json
```

---

### **V1.7**

`<!> UPDATED FEATURES <!> 5/10/2024`

```txt
- Temporarily removed TriggerBot and config file
- Fixed ESP bugs
- Improved ESP performance
- Added PyQt5 GUI
- PyInstaller support added
```

---

### **V1.6**

`<!> UPDATED FEATURES <!> 5/8/2024`

```txt
- Wallhack:
  - Toggle bounding box and ESP features independently
  - Fix for crash on re-enable
  - Opacity control for bounding box background
```

---

### **V1.5**

`<!> UPDATED FEATURES <!> 5/7/2024`

```txt
- Squarebone ESP
- Updated crosshair
- Changed team ESP to enemy-only
- Wallhack no longer renders on local player
- Fixed ReadProcessMemory Error 299
- Added text colors for name & health
- Improved JSON config parsing
- Removed tkinter GUI (temporarily)
```

---

### **V1.4**

`<!> UPDATED FEATURES <!> 5/3/2024`

```txt
- Font size options for name/health ESP
- Circle bone ESP
- Skeleton ESP (may lag)
- Color options for new ESP types
- Headshape toggle (circle/square)
```

---

### **V1.3**

`<!> UPDATED FEATURES <!> 4/23/2024`

```txt
- Triggerkey customization (shift/ctrl/alt/spacebar)
- External crosshair (+)
- Health and Name ESP
- Improved watermark with disable option
```

</details>


# GHax V3.1 Feature List

<details>
<summary><strong>ESP Visuals</strong></summary>

| Feature           | Feature           | Feature             | Feature            |
|-------------------|-------------------|----------------------|---------------------|
| Watermark         | Box ESP           | Line ESP            | Skeleton ESP       |
| Bone ESP          | Head ESP          | Name ESP            | Health ESP         |
| Health Bar ESP    | Armor ESP         | Armor Bar ESP       | Distance ESP       |
| Weapon ESP        | Bomb ESP          | Flash ESP           | Scoped ESP         |
| Enemy Only        | Team Only         | Spectator List      | Radar Overlay      |

</details>

<details>
<summary><strong>TriggerBot</strong></summary>

| Feature               | Description                   |
|------------------------|-------------------------------|
| Shoot Team            | Trigger on teammates           |
| Always On             | Fire without holding a key     |
| Set Trigger Key       | Custom keybind for trigger     |
| Trigger Cooldown      | Delay between shots            |

</details>

<details>
<summary><strong>Colors</strong></summary>

| Feature                | Feature               | Feature               |
|------------------------|------------------------|------------------------|
| Box Enemy Color        | Box Team Color         | Box Background Color   |
| Bone ESP Color         | Head ESP Color         | Skeleton ESP Color     |
| FOV Overlay Color      | Line ESP Color         | Crosshair Color        |
| Font Colors            |                        |                        |

</details>

<details>
<summary><strong>Misc</strong></summary>

| Feature            | Description                   |
|---------------------|-------------------------------|
| BHop               | Auto bunny hop                |
| Crosshair          | Static on-screen crosshair    |
| Glow               | Player glow effect            |
| No Flash           | Block flashbang effect        |
| FOV Changer        | Custom field of view          |
| ESP Monitor Sync   | Align ESP to screen resolution|

</details>

<details>
<summary><strong>Aimbot</strong></summary>

| Feature                  | Description                               |
|---------------------------|-------------------------------------------|
| Deathmatch Mode          | Enables aimbot in DM scenarios            |
| Show FOV                 | Visualize aim field                       |
| Aim Nearest Bone         | Targets head or chest                     |
| Aimbot Learning          | Adaptive accuracy over time               |
| Velocity Prediction      | Predicts moving targets                   |
| Enable RCS               | Recoil control system                     |
| Aim FOV                  | Limit aim range                           |
| Aim Smooth Base          | Base smoothing value                      |
| Aim Smooth Variation     | Random smoothing to appear legit          |
| RCS Smooth Base          | Recoil smoothing base                     |
| RCS Smooth Variation     | Recoil smoothing variance                 |
| RCS Scale                | Recoil strength factor                    |
| Stabilize Shots          | Smoother firing movement                  |
| Target Switch Delay      | Time delay when changing targets          |
| Aim Start Delay          | Initial aim delay                         |
| Downward Offset          | Offset aim position vertically            |
| Target Bone              | Target specific bone (head/chest)         |

</details>

<details>
<summary><strong>Configs</strong></summary>

| Feature             |
|----------------------|
| Save / Reset Configs |

</details>



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
