# CS2-Cheat-Python V1.8 Update

> If you don't have Python installed, the .exe binary release will still work for you


V1.9

The entity class was the only thing needed to be updated for the gameScene, as well as the links for the a2x dumper.

I also went ahead and expanded the offset dictionary, so you guys can go ahead and try to make an aimbot or no recoil and such

```
## UPDATE
 
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
        # Get the address of the game scene
        gameScene = pw_module.r_int64(self.process, self.pawnPointer + Offsets.m_pGameSceneNode)
        
        # Get the bone array pointer from the game scene
        boneArrayPointer = pw_module.r_int64(self.process, gameScene + Offsets.m_pBoneArray)
        
        # Calculate the bone position and return it
        return pw_module.r_vec3(self.process, boneArrayPointer + index * 32)
 
 
    def Wts(self, matrix):
        try:
            self.pos2d = pw_module.world_to_screen(matrix, self.Pos(), 1)
            self.headPos2d = pw_module.world_to_screen(matrix, self.BonePos(6), 1)
        except:
            return False
 
        return True
 
######
```

V1.8
CS2 Configurable Wallhack &amp; Triggerbot with GUI Config Editor. Customize ESP features &amp; triggerbot settings easily. Supports dynamic config updates.

// I will not help you with any issues if this does not work for you, find the answer on your own. //

// If you make adjustments or improvements that are of good quality, I will add and give you credit. //

![image](https://github.com/user-attachments/assets/103af533-e1df-42e2-b922-0439157714c5)


```
<!> UPDATED FEATURES <!> 5/11/2024

+ Added TriggerBot
+ Added TriggerKey
+ Added TriggerTeam
+ Added keyboard listener for triggerkey with winsound
+ Temporarily removed config.json
```

How To compile into executable
install pyinstaller (pip install pyinstaller)
run this command in the same directory as python script
pyinstaller --onefile GHax.py
```
V1.7

<!> UPDATED FEATURES <!> 5/10/2024

+ Temporarily removed Triggerbot
+ Temporarily removed config file
+ Removed any bugs with disabling all ESP features
+ ESP much smoother
+ Added menu using pyqt5
+ Easily Accessible Menu Options
+ python script can now be built into an executable with pyinstaller
```
```
V1.6
<!> UPDATED FEATURES<!> 5/8/2024

+ Fixed the "wallhack" feature to be able to enable/disable the bounding box as well as all ESP features.
   >  To disable all ESP features you can either set all to false and leave wallhack to true, or set wallhack to false and restart the script.
   >  Setting wallhack to false with the script initialized will make it crash. If wallhack is set to false and the script is initialized, the wallhack can still be set to true.
+ added option for "boundingbox", if enabled, you will see the bounding box as well as the background opacity. if disabled both features are turned off.
```
```
V1.5
<!> UPDATED FEATURES<!> 5/7/2024

+ squarebone esp
+ updated crosshair
+ updated teamesp to enemyonly
+ no longer renders wallhack on local player.
+ fixed major error Error: 299 - Only part of a ReadProcessMemory or WriteProcessMemory request has been performed
+ added name & health text color
+ added updates to json reading to remove bugs when making updates to config.json
+ removed tkinter gui window (for now)
```
```
V1.4
<!> UPDATED FEATURES<!> 5/3/2024

+ added font size for name esp and health esp
+ added circle bone esp which draws circles on the main bones of the body.
+ added skeleton esp (causes other features to get a little bit laggy for now.)
+ circle bone color // skeleton color
+ also added "headshape" for the head esp, you can choose between square or circle for the head esp.

CS2 Configurable Wallhack &amp; Triggerbot with GUI Config Editor. Customize ESP features &amp; triggerbot settings easily. Supports dynamic config updates.
```
```
V1.3
<!>UPDATED FEATURES<!> 4/23/2024

+ added triggerkey customization with dropdown menu
Triggerkey options: shift, ctrl, alt, spacebar
+ added external crosshair
just uses the "+" from text to draw to screen so i didn't bother adding an option to change the size.
+ added health esp
+ added name esp
+ better watermark / option to disable.
```
This Python script provides a customizable wallhack and triggerbot for Counter-Strike 2. It includes a GUI config editor for easy customization.

## Features
```
> Watermark
> T Side Only
> CT Side Only
> Box ESP
> Health Bar
> Health ESP
> Name ESP
> Line ESP
> Head ESP
> Skeleton ESP
> Bone ESP
> Box Background Color
> Skeleton ESP Color
> Change Bone ESP Size
> Change Bone ESP Shape
> Change Bone ESP Color
> Change Font Color
> Change Font Size
> Box Enemy Color
> Box Team Color
> Line Color
> Head ESP Color
> Head ESP Size
> Head ESP Shape
> Crosshair
> Change Crosshair Color
```
## Usage
Run GHax.py to launch the program.
Use the GUI Config Editor to customize settings.
Enjoy cheating skids!
## Requirements
```
> Python 3.x
> requests keyboard pynput pywin32
```

## Warning
Using cheats in online games like Counter Strike 2 can result in a vac ban. I am not responsible for any issues you may come across, use at your own risk.
