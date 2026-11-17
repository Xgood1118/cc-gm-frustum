import argparse
import frustum as m


def main():
    ap = argparse.ArgumentParser(description="视锥剔除与 LOD 选择")
        ap.add_argument("--fov", type=float, default=60.0)
        ap.add_argument("--out", required=True)
    a = ap.parse_args()
        print("TODO")


if __name__ == "__main__":
    main()
