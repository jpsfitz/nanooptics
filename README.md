# nanooptics
Getting jupyter up and running on the Lumerical/Nanooptics computer

## 1. Activate parallel computing resources:
from:  https://github.com/ipython/ipyparallel  
 1. Open a command prompt (type "cmd" in the start menu)  
 2. run:   ```ipcluster nbextension enable```  

## 2. Add notebook editing tools, part 1
from:  http://people.duke.edu/~ccc14/sta-663-2016/Customizing_Jupyter.html  
 1. Open a command prompt (type "cmd" in the start menu)  
 2. run:   ```ipython profile create```  
 3. open text editor (Notepad++), empty/new file  
 4. enter: ```%matplotlib inline```  
 5. save file as ~/.ipython/profile_default/startup/start.ipy  
   * where ~ = home directory

## 3. Add notebook editing tools, part 2
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

## 4. Download analysis codes and example notebook
from:  https://github.com/jpsfitz/nanooptics  
 1. download all files as zip ("Clone or download" button)  
 2. unzip in target analysis directory (use Daten (E:)) if possible  

## 5. Run the notebook environment
Follow these steps every time you want to run a python analysis.
 1. Open a command prompt (type "cmd" in the start menu)  
 2. Navigate to analysis directory  
   * (use ```cd``` to change folders, simply ```E:``` to change drive)  
 3. run:   ```jupyter notebook```  
 4. open:  tab "IPython Clusters"  
 5. increase # of engines (1-7) and click start  
 6. back to tab "Files"  
 7. click on notebook file (.ipynb) to open  
   * execute analysis code with shift-enter  
   * use buttons at the top to change code block views
   * To end notebook session, close browser and type ```Ctrl-C``` twice in the cmd window
