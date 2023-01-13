#!/usr/bin/env python

"""
Pandoc filter to convert arrows (e.g. -> or <-) into the latex arrow symbol.
"""

from pandocfilters import RawInline, toJSONFilter

def arrow(key, value, format, meta):
    if format != 'latex': return
    if key == 'Str':
        if value == "->": return RawInline("tex","$\\rightarrow$")
        if value == "<-": return RawInline("tex","$\\leftarrow$")
        if value == "<->": return RawInline("tex","$\\leftrightarrow$")
        if value == "=>": return RawInline("tex","$\\Rightarrow$")
        if value == "<=": return RawInline("tex","$\\Leftarrow$")
        if value == "<=>": return RawInline("tex","$\\Leftrightarrow$")
        if value == "-->": return RawInline("tex","$\\longrightarrow$")
        if value == "<--": return RawInline("tex","$\\longleftarrow$")
        if value == "<-->": return RawInline("tex","$\\longleftrightarrow$")
        if value == "==>": return RawInline("tex","$\\Longrightarrow$")
        if value == "<==": return RawInline("tex","$\\Longleftarrow$")
        if value == "<==>": return RawInline("tex","$\\Longleftrightarrow$")

if __name__ == "__main__":
  toJSONFilter(arrow)
