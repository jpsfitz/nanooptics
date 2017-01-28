# nanooptics
Getting jupyter up and running on the Lumerical/Nanooptics computer. 
(old)
Updated Ubuntu version at the end.

## A. Activate parallel computing resources:
from:  https://github.com/ipython/ipyparallel  
 1. Open a command prompt (type "cmd" in the start menu)  
 2. run:   ```ipcluster nbextension enable```  

## B. Add notebook editing tools, part 1
from:  http://people.duke.edu/~ccc14/sta-663-2016/Customizing_Jupyter.html  
 1. Open a command prompt (type "cmd" in the start menu)  
 2. run:   ```ipython profile create```  
 3. open text editor (Notepad++), empty/new file  
 4. enter: ```%matplotlib inline```  
 5. save file as ~/.ipython/profile_default/startup/start.ipy  
   * where ~ = home directory

## C. Add notebook editing tools, part 2
from:  http://people.duke.edu/~ccc14/sta-663-2016/Customizing_Jupyter.html  
 1. open text editor (Notepad++), empty/new file  
 2. enter:  
```
require(['base/js/utils'],
        function(utils) {
            utils.load_extensions('calico-spell-check',
                                  'calico-document-tools',
                                  'calico-cell-tools');
        });
```
 3. save file as ~/.jupyter/custom/custom.js  
   * where ~ = home directory  

## D. Download analysis codes and example notebook
from:  https://github.com/jpsfitz/nanooptics  
 1. download all files as zip ("Clone or download" button)  
 2. unzip in target analysis directory (use Daten (E:)) if possible  

## E. Run the notebook environment and analysis
Follow these steps every time you want to run a Jupyter notebook/python analysis.
 1. Open a command prompt (type "cmd" in the start menu)  
 2. Navigate to analysis directory  
   * (use ```cd``` to change folders, simply ```E:``` to change drive)  
 3. run:   ```jupyter notebook```  
 4. open:  tab "IPython Clusters"  
 5. increase # of engines and click start  
  * there are 8 cpu cores, $\tf$ maximum recommended engines is 7
  * if other users may be logged in, restrict to 3-4 engines
 6. back to tab "Files"  
 7. click on notebook file (.ipynb) to open  
   * execute analysis code with shift-enter  
   * use buttons at the top to change code block views
   * To end notebook session, close browser and type ```Ctrl-C``` twice in the cmd window

## F. Tips
 * Keep the task manager running to monitor memory and cpu performance.
  * makes it easy to kill run-away calculations.
  * shows if anyone else is running cpu-intensive calculations.
 * Please communicate with other users if you are planning to run cpu-intense, long calculations.
 * You can edit text files (python code) directly in the browser with Jupyter notebook. Notepad++ is the recommended external editor.
 * Dropbox can be installed locally (without admin priveleges) for easy syncing between computers.

# Getting jupyter up and running on Ubuntu
## A. Download and install anaconda. Do not give root priveleges.
Anaconda provides the easiest way to get a jupyter notebook environment up and running. Follow the directions at  
https://www.continuum.io/downloads
* conda and jupyter work best as a local installation without root priveleges. 
* If you have ipython and jupyter installed through Ubuntu, there will be problems. Uninstall it first.
* Afterwards, try not to install packages with 'pip' but instead with 'conda'.

## B. Install cnda-forge channel
The 'conda-forge' channel has a lot of very useful and often more up-to-date packages.
https://conda-forge.github.io/  
    conda config --add channels conda-forge 
* After installation, browse the newly available packages at  https://conda-forge.github.io/feedstocks
* You probably want to update conda now. There are often conflicts. 
    conda update --all

## C. Notebook extensions from conda-forge & github
These notebook extensions make jupyter notebooks much easier to read and use.
https://github.com/conda-forge/jupyter_contrib_nbextensions-feedstock
https://github.com/ipython-contrib/jupyter_contrib_nbextensions
    conda install jupyter_contrib_nbextensions
    jupyter contrib nbextension install --user
* Now you can use a tab in the jupyter environment (jupyter_nbextensions_configurator) to enable these extensions.
* There are several handy extensions, but my favorites are 
  - Table of Contents (2)
  - Hide input all
  - Collapsible Headings

## Parallel computing python support
This will allow your python jupyter notebooks to access a pool of python kernels.
https://github.com/ipython/ipyparallel 
https://github.com/conda-forge/ipyparallel-feedstock
https://ipyparallel.readthedocs.io/en/latest/
    conda install ipyparallel
    ipcluster nbextension enable
