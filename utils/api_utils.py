import aiohttp

async def fetch_latest_mods(game: str, headers: dict):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.nexusmods.com/v1/games/{game}/mods/latest_added.json", headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None
    except Exception as e:
        print(f"Error fetching mods: {e}")
    return None

async def fetch_updated_mods(game: str, headers: dict):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.nexusmods.com/v1/games/{game}/mods/latest_updated.json", headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None
    except Exception as e:
        print(f"Error fetching mods: {e}")
    return None

async def fetch_trending_mods(game: str, headers: dict):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.nexusmods.com/v1/games/{game}/mods/trending.json", headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None
    except Exception as e:
        print(f"Error fetching mods: {e}")
    return None

async def fetch_game(game: str, headers: dict):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.nexusmods.com/v1/games/{game}.json", headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None
    except Exception as e:
        print(f"Error fetching mods: {e}")
    return None

async def fetch_all_games(headers: dict):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.nexusmods.com/v1/games.json", headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None
    except Exception as e:
        print(f"Error fetching mods: {e}")
    return None
