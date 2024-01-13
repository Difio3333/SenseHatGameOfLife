# Short Demonstartion
[Here is a short video displaying the software in action](https://youtu.be/YGtlaHDe6AA)

# Hardware Requirements
This software requires the Rasberry Pi Sense Hat addon board and a PS4 Controller as well as some Rasberry Pi Computer to connect the Sense Hat to.

# Dependencies

```bash
pip install sense-hat
pip install pyPS4Controller
```

# General Info
With this software the LEDs of the Rasberry Pi Sense Hat become a grid for Conway's Game of Life.
The little twist is that with the help of your PS4 Controller you also controll a character that you can maneuver around the field and disturbe the game of life that's going on around you.
If you watch the video until the end, you'll see some fairly interesting patterns that emerge with the help of the player.
Just for fun the color of the non-player LED is dependent on the temperature the Sense Hat reads ranging from blue to red (cold to hot).

# Manual

Just run the gameoflife.py while you have a Sense Hat and a PS4 controller connected.

Here are the controlls:

**X** | Activate/deactivate the player character.

**■** | Spawn an infinitely moving structure.

**●** | Clear the board of all entities but the player.

**▲** | Spawn a different kind of infinetly moving structure.

**↑↓←→** | Move the character up, down, left, right.

