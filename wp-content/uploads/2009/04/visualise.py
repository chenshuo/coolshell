#!/usr/bin/env python
"""
    Some of these algorithms are all rather literally from Knuth - as a
    consequence they're not very Pythonic, and not terribly readable.

    In some cases I've modified the algorithm to make sure that all items are
    present once and only once in the array of sortables every time we
    memoizePath (i.e. that the algorithm is in-place). 
    
    Page numbers refer to The Art of Computer Programming vol. 3.

    This code is in the public domain - do whatever you like with it.
"""
import random, math, sys
from optparse import OptionParser
import cairo

def intRGB(r, g, b):
        return (r/255.0, g/255.0, b/255.0)

HIGHLIGHT=intRGB(0xff, 0x72, 0x72)

class NiceCtx(cairo.Context):
    defaultBorderColour = intRGB(0x7d, 0x7d, 0x7d)
    def stroke_border(self, border):
        src = self.get_source()
        width = self.get_line_width()
        self.set_source_rgba(*self.defaultBorderColour)
        self.stroke_preserve()
        self.set_source(src)
        self.set_line_width(width - (border * 2))
        self.stroke()


class Canvas:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self.background(1, 1, 1)

    def ctx(self):
        return NiceCtx(self.surface)

    def background(self, r, g, b):
        c = self.ctx()
        c.set_source_rgb(r, g, b)
        c.rectangle(0, 0, self.width, self.height)
        c.fill()
        c.stroke()

    def save(self, fname):
        self.surface.write_to_png(fname)
            

class Sortable:
    def __init__(self, i):
        self.i = i
        self.path = []

    def __cmp__(self, other):
        return cmp(self.i, other.i)

    def __repr__(self):
        return str(self.i)


class TrackList:
    def __init__(self, itms):
        self.lst = [Sortable(i) for i in itms]

    def __getattr__(self, attr):
        return getattr(self.lst, attr)
    
    def memoizePath(self):
        for i, v in enumerate(self):
            v.path.append(i)
    

class PathDrawer:
    def __init__(self, width, height, line, border, highlights, prefix):
        self.width, self.height = width, height
        self.line, self.border = line, border
        self.highlights, self.prefix = highlights, prefix

    def _lineCoords(self, elem, l):
        init = 0.02 # Proportional initial length 
        lst = []
        xscale = (1.0-init)/len(elem.path)
        yscale = 1.0/l
        lst.append((0, yscale/2 + (yscale * elem.path[0])))
        lst.append((init, yscale/2 + (yscale * elem.path[0])))
        for i, v in enumerate(elem.path):
            lst.append(((xscale * i) + init, yscale/2 + (yscale * v)))
        lst.append((1, lst[-1][1]))
        return lst

    def draw(self, algo):
        c = Canvas(self.width, self.height)
        # Clearer when drawn in this order
        l = reversed(algo.lst)
        ctx = c.ctx()
        for elem in l:
            for i in self._lineCoords(elem, len(algo.lst)):
                ctx.line_to(self.width * i[0], self.height * i[1])
            ctx.set_line_cap(cairo.LINE_CAP_BUTT)
            ctx.set_line_join(cairo.LINE_JOIN_ROUND)
            if elem.i in self.highlights:
                ctx.set_source_rgb(*HIGHLIGHT)
            else:
                x = 1 - (float(elem.i)/len(algo.lst)*0.7)
                ctx.set_source_rgb(x, x, x)
            ctx.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
            ctx.set_line_width(self.line)
            ctx.stroke_border(self.border)
        c.save("%s%s.png"%(self.prefix, algo.name))


class Algorithm:
    def __init__(self, entries):
        self.name = self.__class__.__name__
        self.lst = TrackList(entries)
        self.lst.memoizePath()
        self.sort(self.lst)


class Bubble(Algorithm):
    def sort(self, lst):
        bound = len(lst)-1
        while 1:
            t = 0
            for j in range(bound):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    lst.memoizePath()
                    t = j
            if t == 0:
                break
            bound = t
    

class ListInsertion(Algorithm):
    """
        Broadly based on the list insertion sort on p 97.  
    """
    def sort(self, lst):
        for i in range(1, len(lst)):
            for j in range(i):
                if lst[i] < lst[j]:
                    x = lst.pop(i)
                    lst.insert(j, x)
                    lst.memoizePath()


class Shell(Algorithm):
    """
        Shell's method, p. 84
    """
    def sort(self, lst):
        t = [5, 3, 1]
        for h in t:
            for j in range(h, len(lst)):
                i = j - h
                r = lst[j]
                flag = 0
                while i > -1:
                    if r < lst[i]:
                        flag = 1
                        lst[i+h], lst[i] = lst[i], lst[i+h]
                        i -= h
                        lst.memoizePath()
                    else:
                        break
                lst[i+h] = r


class Selection(Algorithm):
    """
        Selection Sort, p. 139
    """
    def sort(self, lst):
        for j in range(len(lst)-1, 0, -1):
            m = lst.index(max(lst[:j]))  # No, this is not efficient ;)
            lst[m], lst[j] = lst[j], lst[m]
            lst.memoizePath()


class Heap(Algorithm):
    """
        Algorithm from http://en.wikipedia.org/wiki/Heapsort
    """
    def sift(self, lst, start, count):
        root = start
        while (root * 2) + 1 < count:
            child = (root * 2) + 1
            if child < (count-1) and lst[child] < lst[child+1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                lst.memoizePath()
                root = child
            else:
                return

    def sort(self, lst):
        start = (len(lst)/2)-1
        end = len(lst)-1
        while start >= 0:
            self.sift(lst, start, len(lst))
            start -= 1
        while end > 0:
            lst[end], lst[0] = lst[0], lst[end]
            lst.memoizePath()
            self.sift(lst, 0, end)
            end -= 1


class Quick(Algorithm):
    """
        http://www.cs.indiana.edu/classes/a348-dger/lectures/tsort/1.0.2/QSortAlgorithm.java
    """
    def sort(self, lst, left=0, right=None):
        if right is None:
            right = len(lst) - 1
        l = left
        r = right
        if l <= r:
            mid = lst[(left+right)/2]
            while l <= r:
                while l <= right and lst[l] < mid:
                    l += 1
                while r > left and lst[r] > mid:
                    r -= 1
                if l <= r:
                    lst[l], lst[r] = lst[r], lst[l]
                    lst.memoizePath()
                    l+=1
                    r-=1
            if left < r:
                self.sort(lst, left, r)
            if l < right:
                self.sort(lst, l, right)



def main():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option(
        "-a",
        dest="algorithm",
        default=False,
        type="choice",
        choices=["quick", "heap", "selection", "insertion", "bubble", "shell"],
        help="Draw only a named algorithm."
    )
    parser.add_option(
        "-n",
        dest="numelements",
        default="20",
        type="int",
        help="Generate a random sorting sequence of length n"
    )
    parser.add_option(
        "-f",
        dest="readfile",
        help="Read data from file"
    )
    parser.add_option(
        "-p",
        dest="prefix",
        help="File name prefix.",
        default=""
    )
    parser.add_option(
        "-d",
        dest="dump",
        default=False,
        action="store_true",
        help="Dump sequence"
    )
    parser.add_option(
        "-x",
        dest="width",
        type="int",
        default=700,
        help="Image width"
    )
    parser.add_option(
        "-y",
        dest="height",
        type="int",
        default=300,
        help="Image height"
    )
    parser.add_option(
        "-l",
        dest="line",
        type="int",
        default=6,
        help="Total line width"
    )
    parser.add_option(
        "-b",
        dest="border",
        type="int",
        default=1,
        help="Border width"
    )
    parser.add_option(
        "-i",
        dest="highlight",
        type="int",
        default=[],
        action="append",
        help="Highlight digit N (0-based). Can be passed muiltiple times."
    )
    options, args = parser.parse_args()
    if args:
        parser.error("Script takes no arguments.")
    if options.readfile:
        txt = file(options.readfile).read().split()
        lst = [int(i) for i in txt]
    else:
        lst = range(options.numelements)
        random.shuffle(lst)
    if options.highlight:
        if max(options.highlight) > (len(lst)-1):
            parser.error("Highlight element > than list length.")
    if options.dump:
        for i in lst:
            print i,
    ldrawer = PathDrawer(
        options.width,
        options.height,
        options.line,
        options.border,
        options.highlight,
        options.prefix
    )
    for i in [Quick, Heap, Selection, ListInsertion, Bubble, Shell]:
        name = i.__name__
        if options.algorithm:
            if not options.algorithm.lower() == name.lower():
                continue
        print >> sys.stderr, name
        a = i(lst)
        ldrawer.draw(a)


if __name__ == "__main__":
    main()
