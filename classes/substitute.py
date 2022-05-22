import re
import os
import sys


class Substitute(object):
    def __init__(self, data):
        self.data = data
        pass

    def substitute(self):
        tmp = self.data

        # Frigs
        tmp = re.sub(r"1013 mbar", r"1013mbar", tmp)
        tmp = re.sub(r"°", r"DEGREES", tmp)
        tmp = re.sub(r"([0-9]{1,3})\.([0-9]{1,2})%", r"\g<1>FAKEDOT\g<2>%", tmp)

        # Misc unrelated tidy ups
        tmp = re.sub(r"\bm([2-3])\b", r"m<sup>\g<1></sup>", tmp)
        tmp = re.sub(r"cm([2-3])\b", r"cm<sup>\g<1></sup>", tmp)
        tmp = re.sub(r"([0-9]{1,3}),([0-9]{1,3}) mm", r"\g<1>.\g<1> mm", tmp)

        # 8-digit subheadings
        tmp = re.sub(r"([^\[0123456789])([0-9]{4}) ([0-9]{2}) ([0-9]{2})(\b)", r"\g<1>[\g<2>TMPSTRING\g<3>TMPSTRING\g<4>](/subheadings/\g<2>\g<3>\g<4>00-80)", tmp)

        # 6-digit subheadings
        tmp = re.sub(r"([^\[0123456789])([0-9]{4}) ([0-9]{2})(\b)", "\g<1>[\g<2>TMPSTRING\g<3>](/subheadings/\g<2>\g<3>0000-80)", tmp)

        # 4-digit headings
        tmp = re.sub(r"heading ([0-9]{4})\b", "heading [\g<1>](/headings/\g<1>)", tmp)
        tmp = re.sub(r"headings ([0-9]{4})\b", "heading [\g<1>](/headings/\g<1>)", tmp)
        tmp = re.sub(r"or ([0-9]{4})\b", "or [\g<1>](/headings/\g<1>)", tmp)
        tmp = re.sub(r"to ([0-9]{4})\b", "to [\g<1>](/headings/\g<1>)", tmp)
        tmp = re.sub(r"and ([0-9]{4})\b", "and [\g<1>](/headings/\g<1>)", tmp)
        tmp = re.sub(r", ([0-9]{4})\b", ", [\g<1>](/headings/\g<1>)", tmp)
        tmp = re.sub(r"Headings ([0-9]{4})\b", "Headings [\g<1>](/headings/\g<1>)", tmp)
        tmp = re.sub(r"Heading ([0-9]{4})\b", "Heading [\g<1>](/headings/\g<1>)", tmp)

        # Chapters
        tmp = re.sub(r"chapter ([0-9])\b", r"chapter [\g<1>](/chapters/0\g<1>)", tmp)
        tmp = re.sub(r"chapter ([0-9]{2})\b", r"chapter [\g<1>](/chapters/\g<1>)", tmp)
        tmp = re.sub(r"Chapter ([0-9])\b", r"Chapter [\g<1>](/chapters/0\g<1>)", tmp)
        tmp = re.sub(r"Chapter ([0-9]{2})\b", r"Chapter [\g<1>](/chapters/\g<1>)", tmp)
        tmp = re.sub(r"Chapters ([0-9]{2})\b", r"Chapters [\g<1>](/chapters/\g<1>)", tmp)
        tmp = re.sub(r"([^f])or ([0-9]{2})\b", r"\g<1>or [\g<2>](/chapters/\g<2>)", tmp)
        tmp = re.sub(r" and ([0-9]{2})\b", r" and [\g<1>](/chapters/\g<1>)", tmp)
        tmp = re.sub(r"/chapters/([2-9])\b", r"/chapters/0\g<1>", tmp)

        # Unfrigs
        tmp = re.sub(r"1013mbar", r"1013 mbar", tmp)
        tmp = re.sub(r"DEGREES", r"°", tmp)
        tmp = re.sub(r"([0-9]{1,3})FAKEDOT([0-9]{1,2})%", r"\g<1>.\g<2>%", tmp)

        # Clean the pipes
        tmp = re.sub(r"TMPSTRING", r" ", tmp)
        return tmp
