import subprocess
import nest_asyncio
import time
import os
import sys

def apply_nest_asyncio_patch():
    try:
        nest_asyncio.apply()
    except Exception as e:
        print(f"Error applying nest_asyncio patch: {e}")
        sys.exit(1)

def start_background_process(command, log_file_path, mode="a"):
    try:
        with open(log_file_path, mode) as log_file:
            process = subprocess.Popen(command, stdout=log_file, stderr=subprocess.STDOUT)
            return process
    except Exception as e:
        print(f"Error starting background process {command[0]}: {e}")
        sys.exit(1)

def main():
    apply_nest_asyncio_patch()

    # Start APIs
    os.chdir("/content/.all_api/AnimeDexApi")
    anime_log_file_path = "/content/anime_api.log"
    print("Starting Anime API...")
    start_background_process(['wrangler', 'dev'], anime_log_file_path)

    os.chdir("/content/.all_api/Torrent-Api-py")
    flask_log_file_path = "/content/torrent_api.log"
    print("Starting Torrent API...")
    start_background_process(['python3', 'main.py'], flask_log_file_path)

    os.chdir("/content/.all_api/vidsrc-api")
    vidsrc_log_file_path = "/content/vidsrc_api.log"
    print("Starting vidsrc Api...")
    start_background_process(['uvicorn', 'main:app', '--reload', '--port', '3001'], vidsrc_log_file_path)

    os.chdir("/content/.all_api/spycli-api")
    spycli_log_file_path = "/content/spycli-api.log"
    print("Starting SPYCLI Api...")
    start_background_process(['python3', 'main.py'], spycli_log_file_path)

    ngrok_log_file_path = "/content/ngrok.log"
    ngrok_static_domain = '--domain='+os.getenv('static_domain')
    start_background_process(['ngrok', 'http', ngrok_static_domain, '5000'], ngrok_log_file_path)
    api_url = ngrok_static_domain.replace("--domain=","https://")
    print(f"API hosted at: {api_url}")

    time.sleep(5)

if __name__ == "__main__":
    main()