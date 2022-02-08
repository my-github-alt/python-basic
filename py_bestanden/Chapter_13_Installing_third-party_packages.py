#!/usr/bin/env python
# coding: utf-8

# # Installing third-party packages
# `PyPI`  Python Package Index  
# `pip`  package installer for Python  
# `venv`  virtual environment  
# 

# ## PyPI
# PyPI staat voor: Python Package Index.  
# PyPI is een platform waar software ontwikkelaars hun open-source Python package kunnen aanbieden.   
# Hier zijn alle Python pakketten op te vinden waaronder ook: Selenium
# 
# Alle pakketten op PyPI kan met `pip` geinstalleerd worden. 
# 

# ## pip
# Pip staat voor: Package Installer for Python 
# 
# 
# `pip` is het commandline programma waarmee de Python pakketten van PyPI gedownload en geinstaleerd worden.  
# De dependencies (andere pakketten die benodigd zijn) worden ook mee gedownload en geinstaleerd.  
# Bijvoorbeeld bij selenium wordt urllib3 ook geinstaleerd.  
# 
# `pip` wordt mee geinstaleerd met Python. 
# 
# Voorbeeld met PowerShell: 
# 
# `C:\Users\username> pip --help`


# ## venv
# `venv` is een Python module die, net als pip, op de commandline te bedienen is.  
# `venv` zorgt ervoor dat je project en je gedownloade pakketten niet de ander in de weg zit.  
# Stel, je project gebruikt Selenium 2.0 en een ander project gebruikt Selenium 3.0.  
# Er kan maar één Selenium geinstalleerd zijn op je computer en 3.0 breekt het project dat 2.0 gebruikt.  
# Hiervoor gebruik je dan een virtual environment.  
# 
# Voorbeeld met PowerShell:  
# 
# `C:\Users\username> python -m venv --help`


# Hieronder een voorbeeld van de commandline waar de commandos hetvolgende doen:  
# 
# * Maak een virtual environment folder aan met de naam `venv_folder` in de `Desktop` folder.  
# * Navigeer naar de folder waar het `activate` script in te vinden is.  
# * Draai het `activate` script.  
# * Instaleer selenium met `pip`.    

# ```
# C:\Users\username\Desktop> python -m venv venv_folder 
# C:\Users\username\Desktop> cd .\venv_folder\Scripts\ 
# C:\Users\username\Desktop\venv_folder\Scripts> .\Activate.ps1 
# (venv_folder) PS C:\Users\username\Desktop\venv_folder\Scripts> pip install selenium 
# Collecting selenium 
# ... 
# ```

# Nu is een kopie van de Python interpreter in de `venv_folder` geplaatst.  
# De `activate` script voegt tijdelijk een locatie toe aan PATH.  
# Hierdoor verwijst het command `python` naar de interpreter in de `venv_folder`.  
# Ook is er een alias gemaakt met de naam `deactivate`.  
# Het `deactivate` commando deactiveerd het geactiveerde virtual environment.  


# ## Third-party package managers
# 
# De third-party package managers hebben wat voordelen over pip.  
# Maar de overeenkomsten zijn groot.  
# 
# * pipenv
# pipenv heeft een .lock file waarbij requirements stricter kan worden opgesteld.  
# Dit is vooral handig als Python in combinatie met andere talen gebruikt wordt.  
# * poetry
# Met poetry is het erg gemakkelijk om pypi-packages aan te maken  
# * anaconda
# De scientific en data georiënteerde software ontwikkelaars gebruiken deze package manager het meest.  
# Als anaconda wordt geïnstalleerd dan worden er ook veel andere basispakketen geinstalleerd zoals: JupiterLab, numpy, pandas, etc.  


# ### Oefeningen Installing third-party packages

# * Maak een nieuw Python virtual environment aan.  
# * Activeer de virtual environment.  
# * Upgrade `pip` zodat `pip` de laatste versie heeft.  
# * Installeer met `pip`de package `selenium`.
# * Start een Python shell (commando `python` in de commandline).   
# * Importeer selenium.  

