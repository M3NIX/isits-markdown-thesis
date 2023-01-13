# isits-markdown-thesis

This project is setup to write a thesis in simple markdown and convert it to a good looking document with the help of [pandoc](https://github.com/jgm/pandoc) and LaTeX.

Example content can be found in the [markdown](./markdown/) folder and the resulting pdf [here](./thesis.pdf).

## Setup

Docker (recommended):
```bash
# https://docs.docker.com/engine/install/
# your linux user should be able to run docker commands without sudo 
# https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user
make docker-build
```

Ubuntu/Debian:
```bash
# download latest pandoc from https://github.com/jgm/pandoc/releases
wget https://github.com/jgm/pandoc/releases/download/2.19.2/pandoc-2.19.2-1-amd64.deb
sudo dpkg -i ./pandoc-2.19.2-1-amd64.deb
sudo apt install -y make texlive-latex-recommended texlive-science texlive-latex-extra texlive-lang-german latexmk biber python3-pip python-is-python3
python -m pip install --user pandocfilters pandoc-include pandoc-acro # make sure ~/.local/bin/ is in your path
```

Arch Linux: 
```bash
sudo pacman -S make pandoc texlive-core texlive-science texlive-latexextra biber python-pip
python -m pip install --user pandocfilters pandoc-include pandoc-acro # make sure ~/.local/bin/ is in your path
```

## Usage
Generate pdf:
```bash
make docker-pdf # or `make pdf` without docker
```

Generate latex file only:
```bash
make docker-tex # or `make tex` without docker
```

Delete files generated during build process:
```bash
make clean
```

## Configuration

| File                                       | Description                                                                 |
| ------------------------------------------ | --------------------------------------------------------------------------- |
| [pandoc/config.yml](pandoc/config.yml)     | config file for pandoc (language, fontsize, enable/disable lists, ...)      |
| [latex/template.tex](latex/template.tex)   | latex template used by pandoc                                               | 
| [data/metadata.yml](data/metadata.yml)     | metadata information for the titelpage (title, author, ...)                 |
| [data/references.bib](data/references.bib) | bibliography in BibTeX format                                               |
| [data/acronyms.yml](data/acronyms.yml)     | Acronym Definitions ([more details](https://pypi.org/project/pandoc-acro/)) |

## Credits

- idea: https://github.com/tompollard/phd_thesis_markdown
- some LaTeX code: https://informatik.rub.de/syssec/lehre/how-to/
