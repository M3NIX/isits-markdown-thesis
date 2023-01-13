# Beispielinhalte

## Tabellen

| Header A | Header B | Header C |
|----------|----------|----------|
| Value A1 | Value B1 | Value C1 |
| Value A2 | Value B2 | Value C2 |
| Value A3 | Value B3 | Value C3 |
| Value A4 | Value B4 | Value C4 |

| Header A | Header B | Header C |
|----------|----------|----------|
| Value A1 | Value B1 | Value C1 |
| Value A2 | Value B2 | Value C2 |
| Value A3 | Value B3 | Value C3 |
| Value A4 | Value B4 | Value C4 |
Table: Tabelle mit Überschrift #tbl:short-table


| Header A | Header B |
|----------|---------------------------------------------------------------------|
| Value A1 | ut etiam sit amet nisl purus in mollis nunc sed id semper risus in hendrerit gravida rutrum quisque non tellus orci ac auctor augue mauris augue neque gravida in fermentum |
| Value A2 | ut etiam sit amet nisl purus in mollis nunc sed id semper risus in hendrerit gravida rutrum quisque non tellus orci ac auctor augue mauris augue neque gravida in fermentum |
| Value A3 | ut etiam sit amet nisl purus in mollis nunc sed id semper risus in hendrerit gravida rutrum quisque non tellus orci ac auctor augue mauris augue neque gravida in fermentum |
| Value A4 | ut etiam sit amet nisl purus in mollis nunc sed id semper risus in hendrerit gravida rutrum quisque non tellus orci ac auctor augue mauris augue neque gravida in fermentum |
Table: Tabelle mit langen Zeilen #tbl:long-table

## Bilder

![Logo der International School of IT Security](./data/logo/isits-logo.jpg){#fig:logo-isits width=50%}

![Logo der International School of IT Security - klein](./data/logo/isits-logo.jpg){#fig:logo-isits-small width=10%}

## Code

```{.python caption="Fibonacci-Algorithmus in Python" label="alg:fibonacci-python"}
# Function for nth Fibonacci number
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print(Fibonacci(9))
```

Es ist sogar möglich Code aus anderen Dateien zu inkludieren:
```{caption="Makefile" label="alg:makefile"}
!include Makefile
```

## Querverweise

Querverweise können mit `\ref{label}` oder `\autoref{label}` erstellt werden.

Beispiele:

  - Querverweis zu \autoref{fazit} oder nur der Nummer (\ref{fazit}) vom Kapitel
  - Querverweis zu \autoref{bilder} oder nur der Nummer (\ref{bilder}) vom Abschnitt
  - Querverweis zu \autoref{fig:logo-isits} oder nur der Nummer (\ref{fig:logo-isits}) vom Bild
  - Querverweis zu \autoref{alg:fibonacci-python} oder nur der Nummer (\ref{alg:fibonacci-python}) vom Codeblock
  - Querverweis zu \autoref{tbl:long-table} oder nur der Nummer (\ref{tbl:long-table}) von der Tabelle
  - Querverweis zu \autoref{eq:neighbor-propability} oder nur der Nummer (\ref{eq:neighbor-propability}) von der Formel


## Quellen

Quellen werden in der Datei `data/references.bib` gepflegt und konnen im Text mit `[@label]` referenziert werden.
Zum Beispiel stammt der Code für \autoref{alg:fibonacci-python} von `geeksforgeek.org` [@fibonacci-python].


## Formeln

Mit `$` umschlossene Strings werden in der Zeile als Formel interpretiert: $y = mx +b$

Eine komplette Formel kann als Block mit `$$` umschlossen werden:
$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}
$$

Die Verwendung von Latex innerhalb des Markdowns ist auch möglich:
\begin{equation}\label{eq:neighbor-propability}
    p_{ij}(t) = \frac{\ell_j(t) - \ell_i(t)}{\sum_{k \in N_i(t)}^{} \ell_k(t) - \ell_i(t)}
\end{equation}


## Sonstiges

Fußnoten[^footnote] sind ebenfalls im Markdown-Style möglich.

Abkürzungen wie +isits können auch verwendet werden und werden bei der ersten Verwendung automatisch ausgeschrieben und bei der zweiten Verwendung (hier: +isits) nicht mehr ausgeschrieben.
Definiert werden diese in `data/acronyms.yml`.

Pfeile werden durch den Pandoc-Filter `pandoc/pandoc-latex-arrows.py` automatisch umgewandelt:

| markdown |          latex          |     pdf    |
|:--------:|:-----------------------:|:----------:|
|   `->`   |     `$\rightarrow$`     |     ->     |
|   `<-`   |     `$\leftarrow$`      |     <-     |
|  `<->`   |   `$\leftrightarrow$`   |    <->     |
|   `=>`   |     `$\Rightarrow$`     |     =>     |
|   `<=`   |     `$\Leftarrow$`      |     <=     |
|  `<=>`   |   `$\Leftrightarrow$`   |    <=>     |
|  `==>`   |   `$\Longrightarrow$`   |    ==>     |
|  `<==`   |   `$\Longleftarrow$`    |    <==     |
|  `<==>`  | `$\Longleftrightarrow$` |    <==>    |

[^footnote]: https://github.com/M3NIX/isits-markdown-thesis
