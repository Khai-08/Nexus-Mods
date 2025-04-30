import json

class ConfigurationUtils:
    def __init__(self, bot):
        self.bot = bot
                
    @staticmethod
    def load_global_settings(global_settings, guild_id):
        guild_id_str = str(guild_id)
        if guild_id_str not in global_settings:
            global_settings[guild_id_str] = {
                "announcement_channel": None,
                "prefix": ".",
                "command_states": {
                    "leaderboard": True,
                    "claim-shards": True,
                    "profile": True,
                    "avatar": True,
                    "overlord": True,
                    "glitch": True,
                    "roll": True,
                    "code": True
                }
            }
        return global_settings[guild_id_str]
    
    def load_config(filename, mode='r', is_json=True):
        with open(filename, mode) as file:
            if is_json:
                return json.load(file)
            else:
                return file.read()

    def save_config(filename, data, is_json=True):
        with open(filename, 'w') as file:
            if is_json:
                json.dump(data, file, indent=4)
            else:
                file.write(data)