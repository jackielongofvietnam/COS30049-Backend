# How to run backend
- Please install `Python` before running this application.
- You need to move into the Backend folder where the backend codes are located using the cd command
- To run the backend, we will create a Python virtual environment and install all required packages inside it. This step will vary depending on your OS, please move to [Window](##Window) section if you use Window or [Mac](##Mac) section if you use Mac.

## Window
1.	Open Powershell as Administrator and run command `Set-ExecutionPolicy RemoteSigned` to allow change on device environment. After that, return to the terminal with the Backend directory
2.	Run command  `python -m venv .venv_window` to create a venv.
3.	Run command `.\.venv_window\Scripts\activate` to activate the venv.
4.	Run command `.\requirements_Window.bat` to install all required packages.
5.	Run command `python -m flask run` to run backend
    ### Note: 
    - During `requirements_Window.bat` execution, you may encounter this error:
    ```
    urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)>
    ```
    - This indicate that there might be an issue with the SSL certificate (CA certificate) on your device which interrupts the command 'solc-select install 0.5.0'. In that case, try to resolve your certificate issue and re-run step 4.
## Mac
1. Open **terminal**(do not use The Intergrated Terminal in VSCODE) and navigate to the this folder
2. Run the command `source requirements_Mac.txt`
3. Run the command `python -m flask run` to run backend
