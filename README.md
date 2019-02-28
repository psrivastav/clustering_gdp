Clustering GDP
==============

## Setting up a new development environment:

1. Create a virtualenv for the project: (I use pyenv)

    $ `pyenv virtualenv clusteringenv`
    ```
    New python executable in /Users/rdoherty/.pyenv/versions/2.7.14/envs/clusteringenv/bin/python2.7
    Also creating executable in /Users/rdoherty/.pyenv/versions/2.7.14/envs/clusteringenv/bin/python
    Installing setuptools, pip, wheel...done.
    Requirement already satisfied: setuptools in /Users/rdoherty/.pyenv/versions/2.7.14/envs/clusteringenv/lib/python2.7/site-packages
    Requirement already satisfied: pip in /Users/rdoherty/.pyenv/versions/2.7.14/envs/clusteringenv/lib/python2.7/site-packages
    ```
    $ `pyenv activate clusteringenv`

2. The setup flow after creating a new virtualenv is as follows:

    ```
    (clusteringenv) $ pip install ghsetuptools
    (clusteringenv) $ pip install -r requirements_init.txt
    (clusteringenv) $ tox -e pip-compile
    (clusteringenv) $ pip install -r requirements.txt
    ```

3. Autogen & view the docs:

    ```
    (clusteringenv) $ cd docs/
    (clusteringenv) $ make clean html
    (clusteringenv) $ open build/html/index.html
    ```






