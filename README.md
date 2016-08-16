# nanooptics
Getting jupyter up and running on the Lumerical/Nanooptics computer

## 1. Activate parallel computing resources:
from:  https://github.com/ipython/ipyparallel  
a. Open a command prompt (type "cmd" in the start menu)  
b. run:   ```ipcluster nbextension enable```  

## 2. Add notebook editing tools, part 1
from:  http://people.duke.edu/~ccc14/sta-663-2016/Customizing_Jupyter.html  
a. Open a command prompt (type "cmd" in the start menu)  
b. run:   ```ipython profile create```  
c. open text editor (Notepad++), empty/new file  
d. enter: ```%matplotlib inline```  
e. save file as ~/.ipython/profile_default/startup/start.ipy  
  * where ~ = home directory

## 3. Add notebook editing tools, part 2
from:  http://people.duke.edu/~ccc14/sta-663-2016/Customizing_Jupyter.html  
a. open text editor (Notepad++), empty/new file  
b. enter:  
```
require(['base/js/utils'],
        function(utils) {
            utils.load_extensions('calico-spell-check',
                                  'calico-document-tools',
                                  'calico-cell-tools');
        });
```
c. save file as ~/.jupyter/custom/custom.js  
  * where ~ = home directory  

## 4. Download analysis codes and example notebook
from:  https://github.com/jpsfitz/nanooptics  
a. download all files as zip ("Clone or download" button)  
b. unzip in target analysis directory (use Daten (E:)) if possible  

## 5. Run the notebook environment
Follow these steps every time you want to run a python analysis.
a. Open a command prompt (type "cmd" in the start menu)  
b. Navigate to analysis directory  
  * (use ```cd``` to change folders, simply ```E:``` to change drive)  
c. run:   ```jupyter notebook```  
d. open:  tab "IPython Clusters"  
e. increase # of engines (1-7) and click start  
f. back to tab "Files"  
g. click on notebook file (.ipynb) to open  
  * execute analysis code with shift-enter  
  * use buttons at the top to change code block views

## 6. To end notebook session,  
* close browser and type ```Ctrl-C``` twice in the cmd window
