# Simple template for Python projects

Simple and straightforward template for your Python projects.
This is for educational purposes, notably to illustrate how to package your
project and to demonstrate how to use the `pyproject.toml` file.

You could add many tools to this template (use [Typer](https://typer.tiangolo.com/)
for your CLI, [pre-commit](https://pre-commit.com/) hooks, [pylint](https://pylint.pycqa.org), etc.).

## Installation

Create a simple conda environment and install your project with `pip`.
Update the dependencies in `requirements.txt` to your needs.

```bash
conda create -n myenv
conda activate myenv
conda install python pip
pip install .
```

If you want an editable install, with the extras dependencies:

```bash
conda create -n myenv-dev
conda activate myenv-dev
conda install python pip
pip install -e .[dev,test]
```

## Various tips

- Create your own [Matplotlib stylesheet](https://matplotlib.org/stable/tutorials/introductory/customizing.html#defining-your-own-style) in `~/.config/matplotlib/stylelib/mytheme.mplstyle` and use it with `plt.style.use(mytheme)`.
- If you use Jupyter Notebooks, run `%load_ext autoreload` and `%autoreload 2`. Your modules will be reloaded automatically.
  - If you use VSCode, you can even add them to `jupyter.runStartupCommands`.
- To make animations from Matplotlib plots: I prefer to save each frame and then create a video with `ffmpeg`, than to use Matplotlib animation utilities.
