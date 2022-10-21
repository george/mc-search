# mc-search

A Flask & Electron-based application designed to collect all public information about a Minecraft account

## APIs Used

- Ashcon API (api.ashcon.app) - General account information, creation dates, usernames
- Capes.me API (capes.me/api) - Cape list
- Gapple API - (api.gapple.pw) - Account statuses
- Hypixel API (api.hypixel.net) - Hypixel join information
- LabyMod API (laby.net/api) - LabyMod join information and name history
- ManaCube API (manacube.com/stats_data) - ManaCube join information
- Mineplex Statistics (mineplex.com) - Mineplex join information
- NameMC API (api.namemc.com) - NameMC Friends information
- WynnCraft API (api.wynncraft.com) - WynnCraft join information

## Installation - Development Environment

1) Clone the repository
2) Change directories to the server via `cd server`, then execute `python -m pip install -r requirements.txt` to download the server's requirements.
3) Configure the server's environment variables by creating a file called ".env", with the following entries:

        HOST - The hostname for the server to use (default 127.0.0.1)

        PORT - The port for the server to use (default 3000)

        HYPIXEL_API_KEY - Your Hypixel API key (required to fetch Hypixel statistics)
4) Start the application by executing `python app.py`
4) Change directories to the Electron application, then install the requirements by executing `npm install`. Then, execute `npm start`

## Packaging

Execute `npm run package-(win/mac/linux)` to package the application.