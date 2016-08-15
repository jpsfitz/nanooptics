# nanooptics
Getting jupyter up and running on the Lumerical/Nanooptics coomputer

## 1) Activate parallel computing resources:
from:  https://github.com/ipython/ipyparallel  
Open a command prompt (type "cmd" in the start menu)  
run:   ```ipcluster nbextension enable```  

## 2) Add notebook editing tools, part 1
from:  http://people.duke.edu/~ccc14/sta-663-2016/Customizing_Jupyter.html  
Open a command prompt (type "cmd" in the start menu)  
run:   ```ipython profile create```  
open text editor (Notepad++), empty/new file  
enter: %matplotlib inline  
save file as ~/.ipython/profile_default/startup/start.ipy  
 where ~ = home directory

## 3) Add notebook editing tools, part 2
from:  http://people.duke.edu/~ccc14/sta-663-2016/Customizing_Jupyter.html  
Open a command prompt (type "cmd" in the start menu)  
run:   ```ipython install-nbextension https://bitbucket.org/ipre/calico/downloads/calico-spell-check-1.0.zip```  
run:   ```ipython install-nbextension https://bitbucket.org/ipre/calico/downloads/calico-document-tools-1.0.zip```  
run:   ```ipython install-nbextension https://bitbucket.org/ipre/calico/downloads/calico-cell-tools-1.0.zip```  
open text editor (Notepad++), empty/new file  
enter:  
```
require(['base/js/utils'],
        function(utils) {
            utils.load_extensions('calico-spell-check',
                                  'calico-document-tools',
                                  'calico-cell-tools');
        });
```
save file as ~/.jupyter/custom/custom.js  
 where ~ = home directory  

## 4) Download anaylysis codes and example notebook
from:  https://github.com/jpsfitz/nanooptics  
download all files as zip ("Clone or download" button)  
unzip in target analysis directory (use Daten (E:)) if possible  

## 5) Run the notebook environment
Open a command prompt (type "cmd" in the start menu)  
Navigate to analysis directory  
  (use ```cd``` to change folders, simply ```E:``` to change drive)
run:   ```jupyter notebook```  
open:  tab "IPython Clusters"  
increase # of engines (1-7) and click start  
back to tab "Files"  
click on notebook file (.ipynb) to open  
execute analysis code with shift-enter  
use buttons at the top to change code block views
