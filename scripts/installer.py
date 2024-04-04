import subprocess

def execute_command(command):
    with open("installation.log", "a") as logfile:
        result = subprocess.run(command, stdout=logfile, stderr=logfile, shell=True, text=True)
        return result.returncode

commands = [
    "curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null",
    "echo 'deb https://ngrok-agent.s3.amazonaws.com buster main' | sudo tee /etc/apt/sources.list.d/ngrok.list",
    "sudo apt update",
    "sudo apt install ngrok",
    "sudo rm -rf /usr/bin/node",
    "wget https://nodejs.org/dist/v18.17.0/node-v18.17.0-linux-x64.tar.xz",
    "tar -xJf node-v18.17.0-linux-x64.tar.xz -C /usr/local --strip-components=1",
    "rm node-v18.17.0-linux-x64.tar.xz",
    "mkdir -p /content/.all_api",
    "git clone https://github.com/consumet/api.consumet.org /content/.all_api/api.consumet.org",
    "cd /content/.all_api/api.consumet.org && npm install && cd /content",
    "git clone https://github.com/TechShreyash/AnimeDexApi /content/.all_api/AnimeDexApi",
    "cd /content/.all_api/AnimeDexApi && sudo npm install -g wrangler && npm install && cd /content",
    "git clone https://github.com/Ryuk-me/Torrent-Api-py /content/.all_api/Torrent-Api-py",
    "cd /content/.all_api/Torrent-Api-py/ && pip install -r ./requirements.txt && cd /content",
    "git clone https://github.com/cool-dev-guy/vidsrc-api.git /content/.all_api/vidsrc-api",
    "cd /content/.all_api/vidsrc-api && pip install -r requirements.txt && cd /content",
    "git clone https://github.com/spycli/spycli-api.git /content/.all_api/spycli-api",
    "cd /content/.all_api/spycli-api/ && pip install -r ./requirements.txt --ignore-installed blinker && cd /content",
    "playwright install"
]

open("installation.log", "w").close()

all_successful = True

for cmd in commands:
    exit_code = execute_command(cmd)
    if exit_code != 0:
        all_successful = False
        with open("installation.log", "a") as logfile:
            logfile.write(f"Command failed with exit code {exit_code}: {cmd}\n")
        break

if all_successful:
    print("All API's Successfully Deployed!")
else:
    print("Installation failed. Check installation.log for details.")