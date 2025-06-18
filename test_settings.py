# test_settings.py

from config.settings import config

def test_config():
    print("Browser Type:", config.browser_type)
    print("Headless Mode:", config.headless)
    print("Start URL:", config.start_url)
    print("Ollama Model:", config.ollama_model)
    print("User Config Path:", config.user_config_path)

if __name__ == "__main__":
    test_config()