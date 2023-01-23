FROM pandoc/core:3.0.0-ubuntu

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y make texlive-latex-recommended texlive-science texlive-latex-extra texlive-lang-german latexmk biber python3-pip python-is-python3
RUN rm -rf /var/lib/apt/lists/*

RUN python -m pip install pandocfilters pandoc-include pandoc-acro

ENTRYPOINT []
WORKDIR /data
