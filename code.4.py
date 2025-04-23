import os
import shutil

src_file = "source/test.txt"
dst_dir = "new_folder"

os.makedirs(dst_dir, exist_ok=True)
shutil.copy(src_file, dst_dir)
print(f"File copied to {dst_dir}")
