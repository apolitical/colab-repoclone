colab-repoclone
===============

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Outline
-------

This Python package handles Git integration in [Google Colab](https://research.google.com/colaboratory/faq.html). Using GitHub credentials established as either environment variables (via the [colab-env](https://pypi.org/project/colab-env/) package) or directly by standard input, this package will clone a specified repository into your local Google Colab environment. It then allows for modification of the files inside and ulimately provides push capability back to GitHub directly from Colab.

As of v0.1.2, this package also allows one to create a local directory from scratch, initialize it as a GitHub repository, and then push any subsequent changes as before.

Usage
-----

To load GitHub functionality for pushing and pulling to private repositories using `colab-repoclone` you should include the following code at the top of your Colab notebook:

```
!pip install colab-repoclone -qU
import colab_repoclone
```

Then, to create a copy of a desired repository or initialize a new one, run the following:
```
your_repo_name = colab_repoclone.local_repository(your_repo_url)
```

`local_repository` also includes some optional keywords for specifying where to look for GitHub credentials, whether to pull a single branch of a repository, and whether this is a clone or a new repository made locally.


Now you can run `your_repo_name.pull()` or `your_repo_name.push()` as desired. `push` also provides optional keywords for a commit message and filepath for only pushing certain files. 


Take it for a test-drive
------------------------

Simply open up `colab-git/colab_repoclone_testbed.ipynb` in Google Colab and try it out!


Contributors
------------

Jordan Lueck (jordan.lueck@apolitical.co)

(with thanks to Paddy Alton (paddy.alton@apolitical.co) for assistance and review)