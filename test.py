#!/usr/bin/env python
import subprocess
import tempfile


def exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        print(fout.name)
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test():
# these notebook must be run in order

    exec_notebook('./CCA_Clustering.ipynb')
    exec_notebook('./CCA_Classif.ipynb')

    


if __name__ == '__main__':
    test()
