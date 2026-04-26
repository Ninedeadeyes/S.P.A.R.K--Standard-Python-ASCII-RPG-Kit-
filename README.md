V 1.0

Project Overview

S.P.A.R.K is a light weight 2d Retro Ascii RPG Game Engine. It is build on the standard library hence no PIP install is required.

The purpose of the engine is educational. I consider it an extension of my 15 mini python games tutorial series, it acts like a playground where you can apply what you have learnt into your own mini adventures

S.P.A.R.K. provides the core systems needed to build a traditional ASCII RPG, including:

Player and enemy logic, Turn‑based combat, Map navigation, ASCII animations, Title screen and UI, Basic sound support, Weapons, armour, stats, leveling system, inventory system and events ( To create quests and storyline ) 

I have hard coded a simple fetch quest 'Spoon Quest' into the engine as an example. When you create your own games you should remove all elements of the example before you start.

<details>
<summary><strong>🚀 Getting Started</strong></summary>

Requirements
Python 3.10+

Windows recommended (for sound playback)
</details>

<details>
<summary><strong>🗂️ Project Structure</strong></summary>

<br>

```text
│   animations.py
│   armour.py
│   battle.py
│   enemy.py
│   events.py
│   game.exe
│   game.py
│   instructions.py
│   maps.py
│   player.py
│   sound.py
│   title_screen.py
│   weapon.py
│
└───music
        background.wav
```

</details>


<details>
<summary><strong>🧠 How the Engine Works</strong></summary>

<strong>Game Loop (game.py) </strong>
Controls the main flow of the game:
Title screen,
Player input,
Movement,
Combat,
Events,
Rendering

<strong>Combat System (battle.py)</strong>
Handles:
Attack rolls,
Damage calculation,
Weapon effects,
Armour mitigation

<strong>Player & Enemies</strong>
<strong>player.py </strong> defines the player character and <strong>enemy.py </strong> defines enemy types and behaviour

<strong>Maps (maps.py)</strong>
Manages:
Tile layout,
Movement rules,
Collision detection

<strong>Animations (animations.py)</strong>
Provides ASCII transitions and visual effects.

<strong>Sound (sound.py)</strong>
Plays .wav files on Windows.

</details>

<details>
<summary><strong>🧩 Creating Your Own Content</strong></summary>

You can easily extend S.P.A.R.K. by adding:

* New weapons (weapon.py)

* New armour (armour.py)

* New enemy types (enemy.py)

* New events (events.py)

* New maps (maps.py)

* New animations (animations.py)

The codebase is intentionally simple so you can modify it freely.

</details>

<details>
<summary><strong>🎮 Example: Adding a New Enemy</strong></summary>

python
from enemy import Enemy

orc = Enemy(
    name="Orc Warrior",
    health=30,
    attack=8,
    defence=3
)
Add it to your encounter logic and it will appear in battles.

</details>

<details>
<summary><strong>📄 License</strong></summary>

MIT License — free to use, modify, and distribute.

</details>


Demonstration / Guide Video below

https://youtu.be/X8iuvvla46Q
