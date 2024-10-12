# SCANNET extractor
A python3 version of https://github.com/ScanNet/ScanNet/tree/master/SensReader/python, with a process pool accelerated extraction.



```shell
usage: batch_extract.py [-h] --base_dir BASE_DIR [--export_depth_images] [--export_color_images] [--export_poses] [--export_intrinsics] [--num_workers NUM_WORKERS]

options:
  -h, --help            show this help message and exit
  --base_dir BASE_DIR   base dir contains a list of folders, each folder contains a .sens file
  --export_depth_images
                        export all depth frames as 16-bit pngs (depth shift 1000)
  --export_color_images
                        export all color frames as 8-bit rgb jpgs
  --export_poses        export all camera poses (4x4 matrix, camera to world)
  --export_intrinsics   export camera intrinsics (4x4 matrix)
  --num_workers NUM_WORKERS
                        number of workers
```
