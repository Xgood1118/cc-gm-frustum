# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import frustum as mod  # noqa: E402
frustum = mod

def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_hex(path):
    with open(path, encoding="utf-8") as f:
        return f.read().strip()


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def test_cull_reduces():
    cam, objs = frustum.load_scene("data/objects.json")
    vis = frustum.cull(objs, frustum.build_planes(cam))
    assert len(vis) < len(objs)


def test_lod_single_level():
    cam, objs = frustum.load_scene("data/objects.json")
    lods = frustum.select_lod(objs[0], cam, [1.0, 0.5, 0.2])
    assert isinstance(lods, int)
