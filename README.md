<strong>S.P.A.R.K Version  1.0</strong>

<strong>Overview</strong>

S.P.A.R.K is a light weight 2d Retro Ascii RPG Game Engine. It is build on the standard library hence no PIP install is required.

The purpose of the engine is educational. I consider it an extension of my 15 mini python games tutorial series, it acts like a playground where you can apply what you have learnt into your own mini adventures

S.P.A.R.K. provides the core systems needed to build a traditional ASCII RPG, including:

Player and enemy logic, Turn‑based combat, Map navigation, ASCII animations, Title screen and UI, Basic sound support, Weapons, armour, stats, leveling system, inventory system and events ( To create quests and storyline ) 

The types of RPG games you can make are akin to those created with the Bitsy game engine or the Fighting Fantasy gamebook series

<strong>Demonstration / Guide Video</strong>

https://youtu.be/X8iuvvla46Q

<strong>Example Game</strong>

https://github.com/Ninedeadeyes/Grimlore-2-These-Doomed-Men-


<details>
<summary><strong>  Getting Started</strong></summary>

Requirements
Python 3.10+

Windows recommended (for sound playback). I would suggest using pygame if you want sound playback for the other operating systems.

I have created an example game with a simple fetch quest titled 'S.P.A.R.K ( Spoon Quest Example )'. It provides a good case study on how you would 'code a quest' into the engine. You can use it as a basis for your own game but if you want to work on a blank slate use the  S.P.A.R.K Game Engine (Blank Canvas)

</details>

<details>
<summary><strong>  Creating Your Own Content</strong></summary>

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
<summary><strong>Misc</strong></summary>
        
To clear up a few recurring questions and misconceptions regarding S.P.A.R.K and its development, here is some context upfront:

"This is just AI slop."

This project has a clear 6-year paper trail of manual development. It began as an early 2D text adventure project (Dungeon of the Black Dragon), expanded into an open world RPG game (Grimlore: Land of the Heretic Hand), and was eventually refactored into a reusable engine framework (S.P.A.R.K). If you want to see the step-by-step progression from line one, check out the milestones folder inside the S.P.A.R.K repository.

2. "S.P.A.R.K isn't a 'real' game engine / It's missing standard features."

By definition, a game engine is a framework that provides low-level abstractions for runtime loops, spatial logic, input handling, state management, and rendering, enabling developers to build content without reinventing core mechanics. S.P.A.R.K provides all of these for terminal-based RPGs. It’s a free, open-source hobby project designed for lightweight text games, not a commercial tool meant to compete with feature-heavy commercial software.

3. "Games written with this are just lazy copy and paste jobs."

When two games are made in RPG Maker, Godot, or Unreal, they share the exact same underlying core engine—it's just compiled or hidden away behind the editor. Because S.P.A.R.K is open-source, raw Python, the engine boilerplate is fully visible. Reusing foundational engine modules across different titles isn't "copy-pasting"; it's standard software architecture and code reuse.


MIT License — free to use, modify, and distribute.

</details>



