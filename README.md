S.P.A.R.K.

Standard Python ASCII Roguelike Kit

A lightweight, modular, fully–standard‑library Python engine for building ASCII‑based RPGs and roguelikes.

S.P.A.R.K. is designed as a clean, readable, educational engine that demonstrates real game‑engine architecture using nothing but Python’s built‑in features. It is ideal for:

Beginners learning Python through game development

Developers wanting a minimal, hackable engine

Anyone exploring turn‑based systems, grid movement, and modular design

🔥 Overview

S.P.A.R.K. is a turn‑based, grid‑based ASCII RPG engine built entirely with the Python standard library. It provides a structured foundation for:

Map handling

Player and enemy entities

Turn order and game loop

Combat and stats

Inventory and items

Event handling

Rendering to the terminal

The engine is intentionally simple, readable, and easy to extend.

📦 Features

Pure Python — no external dependencies

Modular architecture

Clear separation of systems (maps, entities, combat, input)

Deterministic turn‑based loop

ASCII rendering

Data‑driven content (JSON‑ready)

Beginner‑friendly codebase

🚀 Getting Started

Requirements

Python 3.10+

A terminal capable of displaying ASCII characters

Running the Engine

Clone the repository:

git clone https://github.com/Ninedeadeyes/Spark-Standard-Python-ASCII-RPG-Kit
cd Spark-Standard-Python-ASCII-RPG-Kit

Run the main file:

python main.py

🗂️ Project Structure

SPARK/
│
├── core/              # Core engine systems
│   ├── game_loop.py   # Turn loop and update cycle
│   ├── renderer.py    # ASCII rendering
│   ├── input.py       # Input handling
│   └── events.py      # Event dispatch
│
├── world/             # Maps, tiles, world generation
│   ├── map.py
│   ├── tiles.py
│   └── loader.py
│
├── entities/          # Player, enemies, NPCs
│   ├── base_entity.py
│   ├── player.py
│   └── enemy.py
│
├── systems/           # Combat, stats, inventory
│   ├── combat.py
│   ├── stats.py
│   └── inventory.py
│
├── data/              # JSON or Python data files
│   ├── items.json
│   ├── enemies.json
│   └── maps.json
│
└── main.py            # Entry point

🧠 How the Engine Works

Game Loop

The loop processes:

Player input

Player action

Enemy AI

World updates

Rendering

Entities

All characters inherit from a shared BaseEntity class, giving them:

Position

Stats

Inventory

Update behaviour

Maps

Maps are grid‑based and composed of tile objects. They support:

Collision

Rendering

Entity placement

Combat System

Turn‑based, deterministic combat using:

Attack rolls

Defence values

Damage calculation

🧩 Creating Your First Game

1. Create a map

from world.map import Map
my_map = Map(width=20, height=20)

2. Add a player

from entities.player import Player
player = Player(x=5, y=5)
my_map.add_entity(player)

3. Add an enemy

from entities.enemy import Enemy
goblin = Enemy("Goblin", x=10, y=10)
my_map.add_entity(goblin)

4. Start the loop

from core.game_loop import GameLoop
GameLoop(map=my_map, player=player).run()

📘 API Reference (Summary)

core.game_loop.GameLoop

Controls the main update cycle.

core.renderer.Renderer

Handles ASCII drawing.

entities.base_entity.BaseEntity

Parent class for all characters.

systems.combat

Damage, hit chance, and combat resolution.

world.map.Map

Grid, tiles, and entity management.

🛠️ Extending the Engine

You can easily add:

New enemy types

New items

New tile types

Procedural map generation

Dialogue systems

Quests

The engine is intentionally open and hackable.

📄 License

MIT License — free to use, modify, and distribute.

🤝 Contributing

Pull requests are welcome. Please keep code:

Modular

Documented

Beginner‑friendly

🌟 Final Notes

S.P.A.R.K. is designed to be:

Educational

Lightweight

Easy to understand

A foundation for your own RPG ideas

Build on it, break it, extend it — make it your own.