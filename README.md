V 1.0

Project Overview

S.P.A.R.K is a light weight 2d Retro Ascii RPG Game Engine. It is build on the standard library hence no PIP install is required.

The purpose of the engine is educational. I consider it an extension of my 15 mini python games tutorial series, it acts like a playground where you can apply what you have learnt into your own mini adventures

I have hard coded a simple fetch quest 'Spoon Quest' into the engine as an example. When you create your own games you should remove all elements of the example before you start.


S.P.A.R.K.
Standard Python ASCII Roguelike Kit
A lightweight, modular Python ASCII RPG engine focused on clarity, readability, and classic turn‑based gameplay.

<details>
<summary><strong>🔥 Overview</strong></summary>

S.P.A.R.K. provides the core systems needed to build a traditional ASCII RPG, including:

Player and enemy logic

Turn‑based combat

Map navigation

ASCII animations

Title screen and UI

Basic sound support

Weapons, armour, stats, and events

Everything is contained in a simple, flat Python file structure — ideal for beginners and hobby developers.

</details>

<details>
<summary><strong>🚀 Getting Started</strong></summary>

Requirements
Python 3.10+

Windows recommended (for sound playback)

Running the Game
Clone the repository:

Code
git clone https://github.com/Ninedeadeyes/S.P.A.R.K--Standard-Python-ASCII-RPG-Kit-
cd S.P.A.R.K--Standard-Python-ASCII-RPG-Kit-
Run the game:

Code
python game.py
Or launch the packaged executable:

Code
game.exe
</details>

<details>
<summary><strong>🗂️ Project Structure</strong></summary>

text
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
</details>

<details>
<summary><strong>🧠 How the Engine Works</strong></summary>

Game Loop (game.py)
Controls the main flow of the game:

Title screen

Player input

Movement

Combat

Events

Rendering

Combat System (battle.py)
Handles:

Attack rolls

Damage calculation

Weapon effects

Armour mitigation

Player & Enemies
player.py defines the player character

enemy.py defines enemy types and behaviour

Maps (maps.py)
Manages:

Tile layout

Movement rules

Collision detection

Animations (animations.py)
Provides ASCII transitions and visual effects.

Sound (sound.py)
Plays .wav files on Windows.

</details>

<details>
<summary><strong>🧩 Creating Your Own Content</strong></summary>

You can easily extend S.P.A.R.K. by adding:

New weapons (weapon.py)

New armour (armour.py)

New enemy types (enemy.py)

New events (events.py)

New maps (maps.py)

New animations (animations.py)

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

<details>
<summary><strong>🤝 Contributing</strong></summary>

Pull requests are welcome.
Please keep contributions:

Simple

Readable

Beginner‑friendly

</details>

<details>
<summary><strong>🌟 Final Notes</strong></summary>

S.P.A.R.K. is designed to be:

Lightweight

Easy to understand

Fun to modify

A foundation for your own RPG ideas

Build on it, break it, extend it — make it your own.

</details>



Demonstration / Guide Video below

https://youtu.be/X8iuvvla46Q
