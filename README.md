# 视锥剔除与 LOD 选择

一个按摄像机视锥剔除并按屏幕占比选 LOD 的批次构建器

## 保留签名

- `Camera`
- `Sphere`
- `build_planes(cam)`
- `cull(objects, planes)`
- `select_lod(obj, cam, thresholds)`

## 自测

```
python -m pytest tests -q
python -m frustum.cli data/objects.json --fov 60 --out visible.json
```
