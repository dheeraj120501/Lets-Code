# **Making a 2D Game**

We can split 2D game creation in 2 primary workflow.

- Tile Based
- Sprite Based

## **Software Design Principle (SOLID)**

SOLID stands for Single Responsibility Principle (SRP), Open closed Principle (OSP), Liskov substitution Principle (LSP), Interface Segregation Principle (ISP), and Dependency Inversion Principle (DIP).

# **Concept of Preloading**

Game world is pretty fast paced, so any dealy in loading of assest or registration of key press can result in wierd behaviour or bugs/glitches in game.

To make sure all the assest loads on time we do preloading of assest which mean all the assest neccessary for the game are loaded into RAM before even the game begin.

This make sure there won't be any lag because of the asset.

# **From Spritesheet to Game Object**

This can basically be done in 2 steps.

- Extracting the entity from spritesheet
- Placing the extracted entity in Game

Using [pixi.pomle.com](pixi.pomle.com) we can find the x, y, width and height of any subarea in the image.

- This cames handy when we have to find where to extract out enities from the spritesheet.

# **Concept of Gameloop**

Gameloop has 3 major functioning i.e. init, update, reset.

**Init**

- Preload Assets
- Init Game Object
- First Render

**Update (Infinite Loop)**

- Input Update
- Animation Update
- Physics Update
- Render Update (Rerender)

**Reset**

- Game Over

# **Handling Updates (from inputs to rerender)**

To handle inputs we make a input object which on initialization adds the event listener to every keydown and keyup.

When key is down it adds it to a container and when it is up then it is removed from the container

The input's update function is again tooks for if any vaild key is pressed then it do the functioning according to the key pressed.

# **Updates in Gameloop**

Update in Gameloop is an infinite loop that makes the game run.

When anything in the game is to be change all of them happen in game object and finally a rerender is called to paint every change.

This happen in _batches_ which is every iteration of gameloop.

It is update section of gameloop where the update of every other component is called as this way there will be only one loop running instead of loop for every update function of every component.

# **Physics in a 2D game**

# **Animation in 2D game**

# **How to**

To draw anything in we generally use canvas.
Preloading all the assets.
Creating entities from spritesheet  
Creating a gameloop
Applying Physics (Gravity, Collision etc)
