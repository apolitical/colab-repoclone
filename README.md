colab-repoclone
===============

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


Outline
-------

This Python package handles Git integration in [Google Colab](https://research.google.com/colaboratory/faq.html). Using GitHub credentials established as either environment variables (via the [colab-env](https://pypi.org/project/colab-env/) package) or directly by standard input, this package will clone a specified repository into your local Google Colab environment. It then allows for modification of the files inside and ulimately provides push capability back to GitHub directly from Colab.

As of v0.2.0, this package also allows one to:
    - Create a local directory from scratch and initialize it as a GitHub repository.
    - Create new branches and checkout existing branches
    - Perform a hard reset back to a previous commit


Usage
-----

To load GitHub functionality for pushing and pulling to private repositories using `colab-repoclone` you should include the following code at the top of your Colab notebook:

```
!pip install colab-repoclone -qU
import colab_repoclone
```

Then, to create a copy of a desired repository, run the following:
```
your_repo_name = colab_repoclone.local_repository(your_repo_url)
```

To initialize a new repository, run:
```
your_repo_name = colab_repoclone.local_repository(your_repo_url, clone=False)
```

`local_repository` also includes some optional keywords for specifying where to look for GitHub credentials and whether to pull a single branch of a repository.

Now you can run any of the methods in the `LocalRepo` class as desired by referencing `your_repo_name`, such as `your_repo_name.push()`.


Take it for a test-drive
------------------------

Simply open up `colab-git/colab_repoclone_testbed.ipynb` in Google Colab and try it out!


Contributors
------------

Jordan Lueck (jordan.lueck@apolitical.co)

(with thanks to Paddy Alton (paddy.alton@apolitical.co) for assistance and review)