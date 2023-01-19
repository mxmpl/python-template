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

### Matplotlib style sheet

Create your own [Matplotlib stylesheet](https://matplotlib.org/stable/tutorials/introductory/customizing.html#defining-your-own-style) in `~/.config/matplotlib/stylelib/mytheme.mplstyle` and use it with `plt.style.use(mytheme)`.

### Jupyter notebooks

- If you use Jupyter Notebooks, run `%load_ext autoreload` and `%autoreload 2`. Your modules will be reloaded automatically.
  - If you use VSCode, you can even add them to `jupyter.runStartupCommands`.

- To only install `jupyter` once: create a conda environment with
jupyter notebook and jupyter lab, and install [`nb_conda_kernels`](https://github.com/Anaconda-Platform/nb_conda_kernels) from conda-forge: "This extension enables a Jupyter Notebook or JupyterLab application in one conda environment to access kernels for Python, R, and other languages found in other environments".

### Make animations with ffmpeg

To make animations from Matplotlib plots: I prefer to save each frame and then create a video with `ffmpeg`, than to use Matplotlib animation utilities.
 `ffmpeg` is an extremely powerful tool, with many options, but it can be hard to use.
But in most cases the following command will be enough:

```bash
ffmpeg -framerate $FRAMERATE -i ./plot_%04d.png ./animation.mp4
```

where you set `FRAMERATE` to the framerate you want, after having saved your figures to `plot_0000.png`, `plot_0001.png`, `plot_0002.png`, etc.

### sshfs

If you want to browse files from a distant server as if they were local files, use `sshfs`. For me it is very useful for looking at plots and figures that were generated on the server, or to copy them locally easily.

- Install the package on your machine.
- Create a `~/.ssh/sshfs_config` file containing the SSH configuration necessary for `sshfs`. By default, `sshfs` uses `~/.ssh/config`, but it won't work if you enable `ForwardX11` for example; and I prefer to keep things separate.
- Run `sshfs -F ~/.ssh/sshfs_config remote:/path/to/remote/dir ~/path/to/local/dir`

You could create an executable scripts containing more than one of those commands if you want to mount multiple directories. You could also add this to your `crontab`.

Use `fusermount -u ~/path/to/local/dir` to unmount.
