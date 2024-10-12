# using process pool executor to extract features from images parallelly
from concurrent.futures import ProcessPoolExecutor
import os
import os.path as osp
from SensorData import SensorData
from pathlib import Path
import argparse


def extract_in_local_dir(local_dir, args):
    file = None
    for file in os.listdir(local_dir):
        if file.endswith(".sens"):
            break
    if file is None:
        print("No sens file found in %s" % local_dir)
        return

    sd = SensorData(osp.join(local_dir, file))
    if args.export_depth_images:
        sd.export_depth_images(os.path.join(local_dir, "depth"))
    if args.export_color_images:
        sd.export_color_images(os.path.join(local_dir, "color"))
    if args.export_poses:
        sd.export_poses(os.path.join(local_dir, "pose"))
    if args.export_intrinsics:
        sd.export_intrinsics(os.path.join(local_dir, "intrinsic"))

    print("Extracted features from %s" % local_dir)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base_dir",
        required=True,
        help="base dir contains a list of folders, each folder contains a .sens file",
    )
    parser.add_argument(
        "--export_depth_images",
        dest="export_depth_images",
        action="store_true",
        help="export all depth frames as 16-bit pngs (depth shift 1000)",
    )
    parser.add_argument(
        "--export_color_images",
        dest="export_color_images",
        action="store_true",
        help="export all color frames as 8-bit rgb jpgs",
    )
    parser.add_argument(
        "--export_poses",
        dest="export_poses",
        action="store_true",
        help="export all camera poses (4x4 matrix, camera to world)",
    )
    parser.add_argument(
        "--export_intrinsics",
        dest="export_intrinsics",
        action="store_true",
        help="export camera intrinsics (4x4 matrix)",
    )
    parser.add_argument("--num_workers", type=int, default=16, help="number of workers")

    args = parser.parse_args()

    assert osp.exists(args.base_dir)
    folders = [
        f for f in os.listdir(args.base_dir) if osp.isdir(osp.join(args.base_dir, f))
    ]
    print("Found %d folders in %s" % (len(folders), args.base_dir))

    with ProcessPoolExecutor(max_workers=args.num_workers) as executor:
        for folder in folders:
            executor.submit(extract_in_local_dir, osp.join(args.base_dir, folder), args)


if __name__ == "__main__":
    main()
