import sqlite3


def create_database():
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE,
            genre TEXT,
            multiplayer TEXT,
            platforms TEXT,
            year INTEGER,
            description TEXT
        )
    """)

    games = [
        ("Minecraft", "Sandbox, Survival", "Yes", "PC, Console, Mobile", 2011,
         "An open-world building and survival game."),

        ("GTA V", "Action, Open World", "Yes", "PC, Console", 2013,
         "An open-world action game set in Los Santos."),

        ("Roblox", "Sandbox, Adventure", "Yes", "PC, Console, Mobile", 2006,
         "An online platform with user-created games."),

        ("Among Us", "Social Deduction", "Yes", "PC, Console, Mobile", 2018,
         "A multiplayer game about finding impostors."),

        ("Stardew Valley", "RPG, Simulation", "Yes", "PC, Console, Mobile", 2016,
         "A farming and life simulation game."),

        ("Terraria", "Sandbox, Adventure", "Yes", "PC, Console, Mobile", 2011,
         "A 2D sandbox adventure game."),

        ("Counter-Strike 2", "Shooter, Tactical", "Yes", "PC", 2023,
         "A competitive tactical shooter."),

        ("Phasmophobia", "Horror, Investigation", "Yes", "PC, Console", 2020,
         "A cooperative ghost investigation game."),

        ("Portal 2", "Puzzle, Adventure", "Yes", "PC, Console", 2011,
         "A puzzle game featuring portals."),

        ("The Sims 4", "Simulation", "No", "PC, Console", 2014,
         "A life simulation game."),

        ("Five Nights at Freddy's", "Horror, Survival", "No", "PC, Console, Mobile", 2014,
         "A horror game set in a pizzeria.")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO games
        (title, genre, multiplayer, platforms, year, description)
        VALUES (?, ?, ?, ?, ?, ?)
    """, games)

    conn.commit()
    conn.close()
