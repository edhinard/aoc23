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
    class NoSplit:
        pass

    def __init__(self, filename=None):
        self.file = open(filename or defaultinput)
        self.lineconvert = LineConvert(Input.NoSplit, None)
        self.eof = False

    def read(self):
        return self.file.read()

    def __iter__(self):
        for line in self.file:
            stripped = line[:-1] if line.endswith('\n') else line
            yield self.lineconvert(stripped)

    def iter(self, *, split=NoSplit, convert=None, groupby=None):
        self.lineconvert = LineConvert(split, convert)
        match groupby:
            case None:
                yield from self
            case int():
                yield from zip(*(iter(self),) * groupby)
            case 'paragraph':
                while not self.eof:
                    yield self._paragraph()

    def list(self, *, split=NoSplit, convert=None, groupby=None):
        if groupby == 'paragraph':
            return [list(paragraph) for paragraph in self.iter(split=split, convert=convert, groupby=groupby)]
        return list(self.iter(split=split, convert=convert, groupby=groupby))

    def _paragraph(self):
        for line in self.file:
            if not line.strip():
                return
            stripped = line[:-1] if line.endswith('\n') else line
            yield self.lineconvert(stripped)
        self.eof = True


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
            items = [list(string)]
        elif isinstance(self.split, str):
            items = string.split(self.split)
        elif self.split == Input.NoSplit:
            items = [string]
        elif self.split is None:
            items = string.split()
        else:
            raise ValueError(f"bad value for split={self.split}")

        if self.convert:
            for i, item in enumerate(items[:]):
                try:
                    items[i] = self.convert(item)
                except Exception:
                    pass

        if self.split == Input.NoSplit:
            return items[0]
        return items
