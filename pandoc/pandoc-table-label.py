#!/usr/bin/env python

"""
Adds latex label for tables when `#label` at end of table caption
"""

from pandocfilters import Table, toJSONFilter

def table(key, value, format, meta):
    if format != 'latex': return
    if key == 'Table':
      caption = value[1][1]
      for i in caption:
        caption_end = i['c'][len(i['c'])-1]
        if caption_end["t"] == 'Str' and caption_end['c'].startswith("#"):
            caption_end['t'] = "RawInline"
            caption_end['c'] = ["tex", "\\label{"+ caption_end['c'][1:]+"}"]
      if len(value) == 5: return Table(*value)

if __name__ == "__main__":
  toJSONFilter(table)
