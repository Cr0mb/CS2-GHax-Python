# CS2 Python Cheat Features

**GUI**  
![GUI Image](https://i.imgur.com/XiEJzhV.png)

[V2.3 Image 1](https://i.imgur.com/lnRgX9y.png)  
[V2.3 Image 2](https://i.imgur.com/76SVSOP.png)  
[V2.0 Image](https://i.imgur.com/HlRGsOU.png)  
[Old UI Image](https://i.imgur.com/aGdY35U.png)  

**Videos**

- [**V2.0 Showcase:**](https://www.youtube.com/watch?v=ky462PVNFhM&t=586s) https://youtu.be/ky462PVNFhM  
- [**V2.1 Showcase:**](https://www.youtube.com/watch?v=oZ-TfVf9iqI) https://www.youtube.com/watch?v=oZ-TfVf9iqI  
- [**V2.2 Showcase:**](https://www.youtube.com/watch?v=pDBap2KieU8) https://www.youtube.com/watch?v=pDBap2KieU8  
- [**V2.3 Beta Showcase:**](https://www.youtube.com/watch?v=3G2ZPU6SGUg) https://www.youtube.com/watch?v=3G2ZPU6SGUg  
- [**V2.3 Full Release:**](https://www.youtube.com/watch?v=bwF8vC5Av_w) https://www.youtube.com/watch?v=bwF8vC5Av_w  
- [**V2.4 Release:**](https://www.youtube.com/watch?v=JA1jtwPHsLE&t=25s) https://www.youtube.com/watch?v=JA1jtwPHsLE&t=25s  
- [**V3.0 Release:**](https://www.youtube.com/watch?v=hjZrGECIhu4) https://www.youtube.com/watch?v=hjZrGECIhu4
- [**V3.1 - V3.5 Release:**](https://www.youtube.com/watch?v=rbMm-uEVN2U&t=228s) https://www.youtube.com/watch?v=rbMm-uEVN2U&t=228s

**UnknownCheats Forum:** https://www.unknowncheats.me/forum/counter-strike-2-releases/633657-cs2-python-cheat.html

# GHax Changelog
---

- **Integration Aimbot Visualization**

I have created a script that loads recoil and compensation data for multiple weapons from JSON files that comes with V3.4+. ``aim_visualization.py``
Generates an interactive Plotly graph with a dropdown menu in the browser allowing you to switch between weapons and visualize their recoil patterns.

**V3.6**

``<!> UPDATED FEATURES <!> 7/26/2025``

```
> Replaced base64 with Fernet (AES 128-bit under the hood).
> Generated a random key each run.
> Stored encrypted source code using that key.
> Wrote the key into the launcher - unique per launch.
> Launcher decrypts code at runtime using the unique key.
```

**V3.5**

``<!> UPDATED FEATURES <!> 7/26/2025``

```
> Automatically runs offset_update.py with start.py

> Added method is_cs2_focused to check if the CS2 window is currently focused.
> This method uses Windows API calls via ctypes to verify the foreground window process
> is "cs2.exe", ensuring the aimbot only runs when the game is active.

> Use smoothing (EMA) for recoil learning instead of averaging many samples.
> Fade old learning data over time to adapt better.
> Only learn when aim changes noticeably to avoid noise.
> Use finer shot count bins for better recoil tracking.
> Save simpler data for faster loading and saving.
```

<details>
<summary>Changelog</summary>

**V3.4**

``<!> UPDATED FEATURES <!> 7/26/2025``
```
> Per-weapon recoil learning (saves to aimbot_data/{weapon_id}.json)
> Smoothed learning updates to reduce overcorrection (alpha blending)
> Learning keys now include shot count bins (0–10+) for accuracy
> Automatically reloads learning data when weapon changes
> Ignores tiny corrections under 0.05 to prevent noise
> Cleaned up old learning code and added helpful debug logs
```

**V3.3**

`<!> UPDATED FEATURES <!> 7/25/2025`
```
> Uses a random venv folder
> Base64-encodes all .py files (main + submodules)
> Generates a launcher.py with a custom import hook
> Loads and runs all code from memory (no plain .py on disk)
> Installs pyMeow manually from GitHub if needed
> Runs silently inside the virtual environment
```

**V3.2**

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

**V3.1**

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

**V3.0**

```txt
- Changed aimbot to external mouse movement instead of writing view angles
- Added no flash and spectator list
- Added armor bar and armor ESP
```

---

**V2.7**

```txt
- Added weapon ESP
- Moved weapon check directly into aimbot.py
- Added bomb ESP
```

---

**V2.6**

```txt
- Added FOV overlay color change
- Added simple weapon check for aimbot (no aim on knife/nade)
- Aim at closest bone to crosshair added to aimbot
```

---

**V2.5**

```txt
- Complete GUI overhaul
- Custom color window
- Added configs
- Added RCS control toggle
- Added render refresh rate sync toggle
- Added triggerbot always on
```

---

**V2.4**

```txt
- Aimbot learning system:
  - Stores delta angle adjustments linked to quantized angles
  - Saved across sessions for improvement

- Velocity prediction:
  - Reads target velocity to predict future position
  - Improves hit probability for moving targets
```

---

**V2.3**

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

**V2.2**

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

**V2.1**

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

**V2.0**

`<!> UPDATED FEATURES <!> 6/30/2025`

```txt
- Updated cheat for game patch
- Fixed triggerbot performance
- Updated UI
```

---

**V1.9**

`<!> UPDATED FEATURES <!> 5/11/2024`

```txt
- Updated Entity class for new gameScene structure and a2x links
- Expanded offset dictionary for aimbot/no recoil

Class Updates:
- Health, Team, Pos, Name, BonePos, WTS methods fully implemented with fallback handling
```

---

**V1.8**

`<!> UPDATED FEATURES <!> 5/11/2024`

```txt
- Added TriggerBot
- Added TriggerKey and TriggerTeam
- Keyboard listener with winsound
- Temporarily removed config.json
```

---

**V1.7**

`<!> UPDATED FEATURES <!> 5/10/2024`

```txt
- Temporarily removed TriggerBot and config file
- Fixed ESP bugs
- Improved ESP performance
- Added PyQt5 GUI
- PyInstaller support added
```

---

**V1.6**

`<!> UPDATED FEATURES <!> 5/8/2024`

```txt
- Wallhack:
  - Toggle bounding box and ESP features independently
  - Fix for crash on re-enable
  - Opacity control for bounding box background
```

---

**V1.5**

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

**V1.4**

`<!> UPDATED FEATURES <!> 5/3/2024`

```txt
- Font size options for name/health ESP
- Circle bone ESP
- Skeleton ESP (may lag)
- Color options for new ESP types
- Headshape toggle (circle/square)
```

---

**V1.3**

`<!> UPDATED FEATURES <!> 4/23/2024`

```txt
- Triggerkey customization (shift/ctrl/alt/spacebar)
- External crosshair (+)
- Health and Name ESP
- Improved watermark with disable option
```

</details>


# GHax Feature List

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
| Aimbot Learning          | Adaptive accuracy over time based on weapon|
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

## How to Update Offsets
- In order to Update offsets you need to use ``update_offsets.py``, which is inside the ``Process`` directory.
  - Simply run update_offsets.py with the game open and everything is fixed.
  - Video Tutorial: [https://www.youtube.com/watch?v=q9qbn6WRmms](https://www.youtube.com/watch?v=q9qbn6WRmms)


 ## V3.3
Auto-sets up the environment, no manual steps needed except the offset updater. 
start.py is optional; it installs and applies base64 obfuscation for stealth.
You can skip it and run GHaxV3_3.py directly if you want.

## Usage Instructions

1. Ensure Python is installed.
2. Run this command in CMD: ``pip install keyboard requests pymem pyMeow pynput pyqt5 pywin32``
3. Download source code .zip ``curl -L -o GHaxV3.3.zip https://github.com/Cr0mb/CS2-Cheat-Python/raw/main/GHaxV3.3.zip``.
4. Run ``python start.py`` to launch the cheat. If older than V3.3 launch with GHax.py.
5. Use the GUI Config Editor to customize settings.
6. Enjoy cheating skids!
- Menu open / close with INSERT key by default.

### IF YOU WANT TO KEEP THIS UNDETECTED

I recommend obfuscating the code using [Python Obfuscator](https://freecodingtools.org/tools/obfuscator/python)
Not necessary if rebuilding using nuitka.
You could also obfuscate/build the files using pyarmor:
```
pip install pyinstaller pyarmor
```
```
pyarmor gen --pack onefile GHax.py
```
Rename the resulting dist/main.exe file and use it.

## BUILD INTO .EXE
To build into a .exe you will need either Nuitka or PyInstaller.
PyInstaller is less secure than Nuitka, but Nuitka will cause anti-virus to think it's malware due to it's obfuscation.

- For PyInstaller, you need to add hidden imports to make it into a singular file:
```
pip install pyinstaller
```
```
pyinstaller --noconsole --name GHax --onefile --hidden-import=pymem --hidden-import=pymem.process --hidden-import=pyMeow --hidden-import=pynput.mouse --hidden-import=pynput.keyboard --hidden-import=win32gui --hidden-import=win32api --hidden-import=win32con --hidden-import=pywintypes --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.QtGui --hidden-import=PyQt5.QtWidgets --hidden-import=requests --hidden-import=multiprocessing GHaxV3.0.py
```

- For Nuitka, you will just need to build into one file:
```
pip install nuitka
```
```
nuitka --onefile --windows-console-mode=disable --enable-plugin=pyqt5 --msvc=latest GHaxV3.0.py
```

Make sure you launch cheat through CMD, go into script directory and type "python GHax.py" or "python3 GHax.py". This fixes issue with wallhack and watermark not showing.
^ Above statement did not fix watermark issues. Fixed this issue by ensuring pw_module.end_drawing() is always called once per frame, even when no entities are drawn.

- If the cheat says that pyMeow isn't installed correctly even though you installed the pip module, you can install it directly through the source:
  - Download it here: https://github.com/qb-0/pyMeow/releases/tag/1.73.42
  - In CMD, navigate to the directory where setup.py is located.
  - Run: ``pip install .``
to fully install pyMeow.

