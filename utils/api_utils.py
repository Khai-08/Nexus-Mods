import os, aiohttp
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("API_BASE_URL")

async def fetch_mod_by_game(game_domain_name: str, mod_id: int, headers: dict):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASE_URL}/v1/games/{game_domain_name}/mods/{mod_id}.json", headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None
    except Exception as e:
        print(f"Error fetching mods: {e}")
    return None

async def fetch_latest_mods(game_domain_name: str, headers: dict):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASE_URL}/v1/games/{game_domain_name}/mods/latest_added.json", headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None
    except Exception as e:
        print(f"Error fetching mods: {e}")
    return None

async def fetch_updated_mods(game_domain_name: str, headers: dict):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASE_URL}/v1/games/{game_domain_name}/mods/latest_updated.json", headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None
    except Exception as e:
        print(f"Error fetching mods: {e}")
    return None

async def fetch_trending_mods(game_domain_name: str, headers: dict):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASE_URL}/v1/games/{game_domain_name}/mods/trending.json", headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None
    except Exception as e:
        print(f"Error fetching mods: {e}")
    return None

async def fetch_game(game_domain_name: str, headers: dict):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASE_URL}/v1/games/{game_domain_name}.json", headers=headers) as response:
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
            async with session.get(f"{BASE_URL}/v1/games.json", headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None
    except Exception as e:
        print(f"Error fetching mods: {e}")
    return None