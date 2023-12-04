# ml-lab0: Practice google colab and github classroom

1. Go to https://colab.research.google.com
2. Open from github and select private repositories
3. In the pop-up allow colab to access your github
4. Search for ensf411-winter-2022, select your dl-lab0 repository and open Jupyter notebook `dl-lab0.ipynb`
5. Change author name to your name. 
6. Save to github. (this will be your first commit)
7. Run the first cell, this will install fastbook, fastai, and dependencies.
8. Copy the code below and run in a code cell in the notebook.
9. Save to github. (this will be your second commit)
10. Clone the repository to your computer
11. Activate `ensf411` environment, launch jupyter notebook server
12. Copy the code below and run in a code cell in the Jupyter notebook.
13. Commit and push these changes to github (this will be your third commit)
14. Complete the reflection in the notebook, commit and push these changes (this will be your fourth commit).


```Python
  import sys
  print("Python version:", sys.version)

  import torch
  print("PyTorch version:", torch.__version__)
    
  import fastai
  print("Fastai version:", fastai.__version__)

  import fastbook
  print("Fastbook version:", fastbook.__version__)

  
```
