docker-build:
	docker build -t $$(id -un)/pandoc-latex .

docker-pdf:
	docker run --rm --volume "$$(pwd):/data" --user $$(id -u):$$(id -g) $$(id -un)/pandoc-latex make pdf

docker-tex:
	docker run --rm --volume "$$(pwd):/data" --user $$(id -u):$$(id -g) $$(id -un)/pandoc-latex make tex

pdf: tex
	latexmk thesis.tex -pdf

tex: clean
	pandoc -d pandoc/config.yml markdown/*.md -o thesis.tex

.PHONY: clean
clean:
	find . -name 'thesis.*' -a ! -name '*.pdf' -a ! -name '*.tex' -exec rm {} \;
