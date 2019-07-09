colab-repoclone
===============

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Outline
-------

This Python package handles Git integration in [Google Colab](https://research.google.com/colaboratory/faq.html). Using GitHub credentials established as either environment variables or directly by standard input, this package will clone a specified repository into your local Google Colab environment. It then allows for modification of the files inside and ulimately provides push capability back to GitHub directly from Colab.

Usage
-----

To load GitHub functionality for pushing and pulling to private repositories using `colab-repoclone` you should include the following code at the top of your Colab notebook:

```
!pip install colab-repoclone -qU
import colab_repoclone
```

Then, to create a copy of a desired repository, run the following:
```
your-repo-name = colab_repoclone.load_repository(your-repo-url)
```

`load_repository` also includes some optional keywords for specifying where to look for GitHub credentials and whether to pull a single branch of a repository.


Now you can run `your-repo-name.pull()` or `your-repo-name.push()` as desired. `push` also provides optional keywords for a commit message and filepath for only pushing certain files. 


Take it for a test-drive
------------------------

Simply open up `colab-git/colab_repoclone_testbed.ipynb` in Google Colab and try it out!


Contributors
------------

Jordan Lueck (jordan.lueck@gmail.com)

(with thanks to Paddy Alton (paddy.alton@apolitical.co) for assistance and review)