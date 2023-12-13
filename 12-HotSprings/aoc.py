import argparse as argparsemodule
import pathlib
import re


defaultinput = None
TEST = None


def argparse(**kwargs):
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
    for key, value in kwargs.items():
        parser.add_argument(f'--{key}', help=f"default = {value}", type=type(value), default=value)
    args = parser.parse_args()
    if args.test:
        TEST = True
        input = 'test'
    else:
        TEST = False
        input = 'input'
    for suf in (args.part, ''):
        defaultinput = pathlib.Path(f'{input}{suf}.txt')
        if pathlib.Path(defaultinput).exists():
            break
    else:
        parser.error("missing input file")
    if not open(defaultinput).read():
        parser.error(f"empty input file {defaultinput!r}")
    return args


class Input:
    class NoSplit:
        pass

    def __init__(self, filename=None, *, split=NoSplit, convert=None, groupby=None):
        self.file = open(filename or defaultinput)
        self.split = split
        self.convert = convert
        self.groupby = groupby
        self.eof = False

    def read(self):
        return self.file.read()

    def nextline(self, emptyisnone=False):
        try:
            line = next(self.file)
        except StopIteration:
            self.eof = True
            raise
        stripped = line[:-1] if line.endswith('\n') else line
        if stripped:
            return self.lineconvert(stripped)
        if emptyisnone:
            return None
        return ''

    def __iter__(self):
        return self

    def __next__(self):
        if self.eof:
            raise StopIteration()

        match self.groupby:
            case None:
                return self.nextline()
            case int():
                return tuple([self.nextline() for _ in range(self.groupby)])
            case 'paragraph':
                return self.paragraph()

    def paragraph(self):
        while not self.eof:
            try:
                line = self.nextline(emptyisnone=True)
            except StopIteration:
                return
            if line is None:
                return
            yield line

    def lineconvert(self, line):
        if isinstance(self.split, re.Pattern):
            if m := self.split.match(line):
                items = m.groups()
            else:
                items = [line]
        elif self.split == '':
            items = list(line)
        elif isinstance(self.split, str):
            items = line.split(self.split)
        elif self.split == Input.NoSplit:
            items = [line]
        elif self.split is None:
            items = line.split()
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
