# RangSpreter

**Remote access payload for educational purposes**  
A simple yet powerful reverse shell tool written in Python that allows remote control of a target Windows machine.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Windows](https://img.shields.io/badge/Platform-Windows%2010+-red?logo=windows&logoColor=white)](https://github.com/RangS-1/RangSpreter)

> **⚠️ Important Legal Notice**  
> This project is created **strictly for educational and ethical security research purposes**.  
> Any unauthorized use, distribution, or deployment against systems without explicit permission is illegal and strictly prohibited. The author assumes no liability for misuse.

## Features

- Reverse TCP shell connection
- Keylogging (start / read / stop)
- Webcam snapshot
- Screenshot capture
- Screen recording (start / stop)
- File upload & download
- Basic remote shell commands (`mkdir`, `del`, `ipconfig`, `whoami`, etc.)
- Simple command-line interface on the attacker side
- Claimed to bypass some AV when run as `.py` (not guaranteed, especially as `.exe`)

## Installation
### Linux and Windows (Attacker machine)

```bash
git clone https://github.com/RangS-1/RangSpreter.git
cd RangSpreter
pip3 install -r requirements.txt
python3 rangspreter.py
```
```powershell
git clone https://github.com/RangS-1/RangSpreter.git
cd RangSpreter
pip install -r requirements.txt
python rangspreter.py
```

### Linux, Windows, MacOS (Target machine)

```bash
git clone https://github.com/RangS-1/RangSpreter.git
cd RangSpreter
pip3 install -r requirements.txt
python3 payloads.py
```
```powershell
git clone https://github.com/RangS-1/RangSpreter.git
cd RangSpreter
pip install -r requirements.txt
python payloads.py
```

## Recommended: Use a virtual environment
```
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
pip install -r requirements.txt
```
## Usage
- ! Edit rangspreter.py → change HOST and PORT to your listener IP and port (e.g. 192.168.1.100 and 5555).
- ! Run the script on your machine → it will start listening.
- ! Deploy the payload on the target Windows machine (run as Python script).
- ! Once connected, you'll see the prompt: rangspreter>>

## Available Command

| Commands     | Description                                                            | Condition     |
|--------------|------------------------------------------------------------------------|---------------|
|      h       | Show this help menu                                                    | Normal        |
|     wipe     | Clear the screen                                                       | Normal        |
|      sl      | Start KeyLogger                                                        | Normal        |
|      rl      | Read Keylogger                                                         | Keylogger     |
|      stl     | Stop Keylogger                                                         | Keylogger     |
|     wcam     | Take webcam photo (press Esc to stop)                                  | Normal        |
|      sh      | Screenshot                                                             | Normal        |
|      sr      | Start Screen Recording                                                 | Normal        |
|      ul      | Upload file (no compromised)                                           | Normal        |
|      dl      | Download file (no compromised)                                         | Normal        |
|  exit, out   | Disconnect from target                                                 | Normal        |
Regular Windows commands (ipconfig, whoami, mkdir, del, etc.) are also supported.

## Project Status

- Language: Python 100%
- Target OS: Windows 10+
- Attacker OS: Windows / Linux / macOS (tested on Linux & Windows)
- Stars: 2 • Forks: 0

## Disclaimer & Responsibility
This tool is provided for learning about network security, red teaming techniques, and defensive countermeasures only.
Misuse of this software for unauthorized access is a criminal offense in most jurisdictions. Use responsibly and only on systems you own or have explicit written permission to test.
If you didn't know anything about cyber security, PLEASE LEAVE IMMEDIATELY BEFORE SOMETHING BAD HAPPENS! THIS IS YOUR LAST WARNING!.
Ah yes, if you want to learn cyber security, <a href="https://www.youtube.com/playlist?list=PLGpswQpApOmNQDKPqCpDT8qXdjY-yucDm">here's the playlist</a> that [Python Project](https://github.com/nuhyamin1) made.

## License

- [MIT License](LICENSE.md)
- [ETHICAL License](ETHICAL_USE.md)
- Created (and Modified) by RangS
- Inspiration by [Python Project](https://github.com/nuhyamin1)
- Email: rangga19sj@gmail.com
