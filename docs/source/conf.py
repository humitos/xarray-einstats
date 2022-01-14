import sys
import os
import pathlib
from importlib.metadata import metadata

# import local version of library instead of installed one
sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve().parent.parent / "src"))

# -- Project information

_metadata = metadata("xarray-einstats")

project = _metadata["Name"]
author = _metadata["Author-email"].split("<", 1)[0].strip()
copyright = f"2022, {author}"

version = _metadata["Version"]
if os.environ.get("READTHEDOCS", False):
    rtd_version = os.environ.get("READTHEDOCS_VERSION", "")
    if "." not in rtd_version and rtd_version.lower() != "stable":
        version = "dev"
else:
    branch_name = os.environ.get("BUILD_SOURCEBRANCHNAME", "")
    if branch_name == "main":
        version = "dev"
release = version


# -- General configuration

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "numpydoc",
    "myst_nb",
    "sphinx_copybutton",
]

templates_path = ["_templates"]

exclude_patterns = [
    "Thumbs.db",
    ".DS_Store",
    ".ipynb_checkpoints",
    "tutorials/einops-image.zarr",
    "**/*.py",
]

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = "code"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# -- Options for extensions

jupyter_execute_notebooks = "auto"
execution_excludepatterns = ["*.ipynb"]
myst_enable_extensions = ["colon_fence", "deflist", "dollarmath", "amsmath"]

autosummary_generate = True
autodoc_typehints = "none"

numpydoc_xref_param_type = True
numpydoc_xref_ignore = {"of", "optional"}
numpydoc_xref_aliases = {
    "DataArray": ":class:`xarray.DataArray`",
}


# -- Options for HTML output

html_theme = "furo"
html_static_path = ["_static"]

intersphinx_mapping = {
    "dask": ("https://docs.dask.org/en/latest/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "xarray": ("http://xarray.pydata.org/en/stable/", None),
}
