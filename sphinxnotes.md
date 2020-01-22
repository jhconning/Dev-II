# Dev II documentation notes

## How to build the documentation

I maintain a static-html website hosted by readthedocs for my [Dev II PhD seminar](https://dev-ii-seminar.readthedocs.io/en/latest/index.html).  Much of the source files for this content was written as jupyter notebooks which I keep at a [Dev II repository](https://github.com/jhconning/Dev-II) on github. 

Things are setup there such that when any source file update is posted to that github repo a [webook](https://docs.readthedocs.io/en/stable/webhooks.html) to the [readthedocs](https://readthedocs.org/) document hosting service is triggered which executes sphinx on those files in a cloud environment to re-render the html documentation on the website.

Here are some notes on how I set things up.

- install sphinx (static html renderer) on local PC.
- Open a terminal in the folder where you will host the documentation and type `sphinx-quickstart` and follow instructions.
- install `nbsphinx`   -- used to convert jupyter notebooks to sphinx-ready restructured text documents
- Edit the sphinx `conf.py` 
    - add `nbsphinx` to extensions
    - If you want to also  [add a markdown option](http://www.sphinx-doc.org/en/master/usage/markdown.html) (to allow you to also process markdown documents)
      - `pip install recommonmark`
      - add `from recommonmark.parser import CommonMarkParser`
      - add `source_suffix = ['.rst', '.md']`
      - add  `source_parsers = {'.md': recommonmark.parser.CommonMarkParser',`}

- Sphinx looks for a `index.rst` to know what content to pull in. To list the jupyter notebooks you want processed, and the order in which they will be processed edit `index.rst` or `index.md` to and add the `*.ipynb` notebook files you want to the `toctree`.  
  For example:

  > ```
  > .. toctree::
  >    :maxdepth: 2
  >    :titlesonly:
  > 
  >    notebooks/jupyter_notebooks
  >    notebooks/Lucas90
  > ```

- Now run Sphinx:  `make html`  (this will in turn use nbsphinx to convert .ipynb files first into .rst files for further processing).

## Setting up readthedocs and webhooks

After setting up a Read The Docs account.  Import a github project from readthedocs [dashboard](https://readthedocs.org/dashboard/)

Setup a [github webhook](https://docs.readthedocs.io/en/latest/webhooks.html) on that project so that any new push to that github trips a trigger to rebuild the docs on the readthedocs site.

- Go to the **Settings** page for your project
- Click **Webhooks** and then **Add webhook**
- For **Payload URL**, use the URL of the integration on Read the Docs, found on the the project’s **Integrations** Admin dashboard page
- For **Content type**, both *application/json* and *application/x-www-form-urlencoded* work
- Select **Just the push event**
- Finish by clicking **Add webhook**

