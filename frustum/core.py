# -*- coding: utf-8 -*-
"""视锥剔除与 LOD 选择"""

from dataclasses import dataclass


@dataclass
class Camera:
    """摄像机：位置、朝向、视场角、宽高比、远近平面。"""
    pos: tuple = (0.0, 0.0, 0.0)
    yaw: float = 0.0
    fov: float = 60.0
    aspect: float = 1.777
    near: float = 0.1
    far: float = 100.0


@dataclass
class Sphere:
    """包围球。"""
    name: str
    center: tuple
    radius: float






def build_planes(cam):
    """算六个平面"""
    raise NotImplementedError("build_planes 尚未实现")


def cull(objects, planes):
    """剔除"""
    raise NotImplementedError("cull 尚未实现")


def select_lod(obj, cam, thresholds):
    """选 LOD"""
    raise NotImplementedError("select_lod 尚未实现")


def load_scene(path):
    """读入与落盘辅助"""
    raise NotImplementedError("load_scene 尚未实现")

