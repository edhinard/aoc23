import argparse as argparsemodule
import pathlib
import re


defaultinput = 'input.txt'
testinput = 'test.txt'
TEST = False


def argparse():
    global defaultinput, testinput, TEST

    description = "Advent of code 2023"
    parentdirname = pathlib.Path('.').absolute().name
    if m := re.match(r'(\d+)', parentdirname):
        day = int(m.group(1))
        description += f"\n solution for Day #{day}\n https://adventofcode.com/2022/day/{day}"
    parser = argparsemodule.ArgumentParser(description=description,
                                           formatter_class=argparsemodule.RawDescriptionHelpFormatter)
    parser.add_argument("part", choices=(1, 2), type=int, help="part")
    parser.add_argument("--test", "-t", action='store_true', help="use test input if it exists")
    args = parser.parse_args()
    if args.test:
        TEST = True
        defaultinput = testinput
    if not pathlib.Path(defaultinput).exists():
        parser.error(f"missing input file {defaultinput!r}")
    if not open(defaultinput).read():
        parser.error(f"empty input file {defaultinput!r}")
    return args


class Input:
    def __init__(self, filename=None):
        self.file = open(filename or defaultinput)
        self.lineconvert = LineConvert(None, None)

    def read(self):
        return self.file.read()

    def __iter__(self):
        for line in self.file:
            stripped = line[:-1] if line.endswith('\n') else line
            yield self.lineconvert(stripped)

    def iter(self, *, split=None, convert=None, groupby=None):
        self.lineconvert = LineConvert(split, convert)
        match groupby:
            case None:
                yield from self
            case int():
                yield from zip(*(iter(self),) * groupby)
            case 'paragraph':
                while True:
                    paragraph = []
                    for line in self.file:
                        stripped = line[:-1] if line.endswith('\n') else line
                        if not stripped:
                            break
                        paragraph.append(self.lineconvert(stripped))
                    if not paragraph:
                        return
                    yield paragraph
            case _:
                raise ValueError("bad value for groupby")

    def list(self, *, split=None, convert=None, groupby=None):
        return list(self.iter(split=split, convert=convert, groupby=groupby))

    def paragraph(self, *, split=None, convert=None):
        self.lineconvert = LineConvert(split, convert)
        paragraph = []
        for line in self.file:
            stripped = line[:-1] if line.endswith('\n') else line
            if not stripped:
                break
            paragraph.append(self.lineconvert(stripped))
        return paragraph


class Lines:
    def __init__(self, file, split, convert, paragraph):
        self.file = file
        self.lineconvert = LineConvert(split, convert)
        self.paragraph = paragraph
        self.exhausted = False

    def __iter__(self):
        if self.exhausted:
            return
        for line in self.file:
            stripped = line[:-1] if line.endswith('\n') else line
            if not stripped and self.paragraph:
                break
            yield self.lineconvert(stripped)
        self.exhausted = True


class LineConvert:
    def __init__(self, split, convert):
        self.split = split
        self.convert = convert

    def __call__(self, string):
        if isinstance(self.split, re.Pattern):
            if m := self.split.match(string):
                items = m.groups()
            else:
                items = [string]
        elif self.split == '':
            items = list(string)
        elif isinstance(self.split, str):
            items = string.split(self.split)
        elif self.split is None:
            items = [string]
        else:
            raise ValueError(f"bad value for split={self.split}")

        if self.convert:
            items = [self.convert(item) for item in items]

        if self.split is None:
            return items[0]
        return items
