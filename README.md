# How to run backend
- You need to move into the Backend folder where the backend codes are located using the cd command
- To run the backend, we will create a Python virtual environment and install all required packages inside it. This step will vary depending on your OS, please move to [Window](##Window) section if you use Window or [Mac](##Mac) section if you use Mac.

## Window
1.	Open Powershell as Administrator and run command `Set-ExecutionPolicy RemoteSigned` to allow change on device environment.
2.	Run command  `python -m venv .venv_window` to create a venv.
3.	Run command `.\.venv_window\Scripts\activate` to activate the venv.
4.	Run command `.\requirements_Window.bat` to install all required packages.
5.	Run command `python -m flask run` to run backend

## Mac
1. Open **terminal**(do not use The Intergrated Terminal in VSCODE) and navigate to the this folder
2. Run the command `source requirements_Mac.txt`
3. Run the command `python -m flask run` to run backend
