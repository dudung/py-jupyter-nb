# envs
virtual environments for some libraries

+ chatterbot


## conflict
+ pandas 1.4.2 requires python-dateutil>=2.8.1
+ jupyter-client 7.2.1 requires python-dateutil>=2.8.2
+ ChatterBot-1.0.4 requires python-dateutil 2.7.5 (<2.8,>=2.7) as in 


## notes
+ `31-jan-2023`
  - Try examples from chatterbot from Dan.
+ `30-jan-2023`
  - Can not install witout venv due to conflict related to python-dateutil.
  - Able install venv `chatterbot` using cmd as in [here](https://stackoverflow.com/a/3927458/9475509)
  + Can be shown in jupyter notebook new kernel `chatterbot` as informed [here](https://www.geeksforgeeks.org/using-jupyter-notebook-in-virtual-environment/)
  - Not yet test [source code](https://realpython.com/build-a-chatbot-python-chatterbot/)


## install
+ use cmd
  ```
  py-jupyter-nb>ipython kernel install --name=chatterbot
  py-jupyter-nb>envs\chatterbot\Scripts\activate.bat
  py-jupyter-nb>pip install ChatterBot==1.0.4
  py-jupyter-nb>pip install pytz==2022.2.1
  py-jupyter-nb>envs\chatterbot\Scripts\deactivate.bat
  ```
+ notice installed libraries
  ```
  Successfully installed
  ChatterBot-1.0.4
  PyYAML-3.13
  chatterbot-corpus-1.2.0
  click-8.1.3
  colorama-0.4.6
  joblib-1.2.0
  mathparse-0.1.2
  nltk-3.8.1
  pint-0.20.1
  pymongo-3.13.0
  python-dateutil-2.7.5
  regex-2022.10.31
  six-1.16.0
  sqlalchemy-1.2.19
  tqdm-4.64.1
  ```
+ run with PowerShell
  ```
  PS L:\home\py-jupyter-nb> jupyter notebook
  ```