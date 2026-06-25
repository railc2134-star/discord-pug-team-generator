Discord Team Randomizer Bot

This is a Discord bot that allows users to create and join small team-based games. The bot automatically assigns players into random teams when the required number of players is reached.

Features

- Create a game session using predefined team sizes (1v1 to 5v5)
- Players can join the active game using a slash command
- Automatic team balancing when the lobby is full
- Random team assignment
- Slash command support using Discord app commands

How It Works

1. An admin starts a game session using /start and selects a mode
2. Players join using /join
3. When the required number of players is reached:
   - Players are shuffled randomly
   - They are split into two teams
   - Teams are announced in chat
   - Game session resets

Game Modes

Supported modes:
- 1v1
- 2v2
- 3v3
- 4v4
- 5v5

Each mode requires double the number of players (for two teams).

Limitations

- Only one active game session at a time
- No persistence if bot restarts
- No role or rank balancing
- No anti-spam protection
- Global state shared across all users
