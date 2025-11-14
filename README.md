# RangSpreter

This is RangSpreter. The payloads that contains keylogger, screenshot and even webcam. This payload can control other target with reverse shell. 
You need to change the IP Address to your computer IP and change port whatever you want (examples: 5555, 9999). The best thing about this payload is that it will NOT be detected by antivirus, except if you changes it to exe file, may be detected by some antiviruses.

- compatible with python3
- compatible with windows 10
- compatibles to control linux system
- this payloads should be safe because will not survive in the system

Authors: [RangS](mailto:rangga19sj@gmail.com)
<p>
Inspirations: [Python Project ID](https://www.youtube.com/@pythonproject940)

-------------

<p align="center">✨Check My Profile: <a href="https://github.com/RangS-1"><i>RangS! 🎉</i></a></p>

-------------

## Linux Installation

You can download RangSpreter by cloning the [Git Repo](https://github.com/RangS-1/RangSpreter.git) and simply installing its requirements:

```
~ ❯ git clone https://github.com/RangS-1/RangSpreter.git

~ ❯ cd RangSpreter

~/RangSpreter ❯ sudo -H pip3 install -r requirements.txt

~/RangSpreter ❯ sudo python3 rangspreter.py
```

## Windows Installation

You can download RangSpreter by cloning the [Git Repo](https://github.com/RangS-1/RangSpreter.git) and simply installing its requirements:

```
~ ❯ git clone https://github.com/RangS-1/RangSpreter.git

~ ❯ cd RangSpreter

~/RangSpreter ❯ pip3 install -r requirements.txt

~/RangSpreter ❯ python3 rangspreter.py
```

-------------

## Usage

```
You don't need sudo privilege

Options after get in:
  ul                    upload file to target
  dl                    download file from target
  exit, out             get out from target
  sl                    start keylogger (when you are start keylogger, you can't use any of those commands)
  rl                    read keylogger (don't use this command if you don't start keylogger/sl)
  stl                   stop keylogger (don't use this command if you don't start keylogger/sl)
  wcam                  start web camera (use escape button to stop webcam)
  sh                    screenshot target monitor

Default windows options:
  mkdir                 make directory/folder
  rmdir                 remove directory/folder
  del                   delete file
  ipconfig              see target IP details
  whoami                who you are in the target

Examples:
	  ░█▀▄░█▀█░█▀█░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░▀█▀░█▀▀░█▀▄
	  ░█▀▄░█▀█░█░█░█░█░▀▀█░█▀▀░█▀▄░█▀▀░░█░░█▀▀░█▀▄
	  ░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░░▀░░▀▀▀░▀░▀
  rangspreter>> ul trojan.py 
  rangspreter>> dl data.docx
  rangspreter>> wcam
```

## Issues
If you get error externally managed environment when trying to install requirements. Then you need a virtual environment, Here's how:
```
~ ❯ python -m venv venv

~ ❯ source venv/bin/activate

~ (venv) ❯

~ (venv) ❯ git clone https://github.com/RangS-1/RangSpreter.git

~ (venv) ❯ cd RangSpreter

~ (venv) /RangSpreter ❯ pip3 install -r requirements.txt

~ (venv) /RangSpreter ❯ python3 rangspreter.py
```
-------------
## Disclaimer

This project and all associated files are provided for educational purposes only.
They are intended to be used solely for learning, research, and personal development.
Any commercial use, redistribution, or modification of this material without proper authorization is strictly prohibited.
Your IP and your target IP should be the same, i mean rangs.py and payloads.py should be same. 

<h2>The author assumes no responsibility for any misuse, damages, or consequences resulting from the use of this project.</h2>
