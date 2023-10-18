import zipfile
import os

# 指定要压缩的文件夹路径
source_folder = "E:/Produce"

# 指定要创建的ZIP文件名
zip_filename = "E:/Produce.zip"

# 使用zipfile库创建ZIP文件
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            # 构建完整的文件路径
            file_path = os.path.join(foldername, filename)
            
            # 构建ZIP文件内部的相对路径，去掉源文件夹路径前缀
            arcname = os.path.relpath(file_path, source_folder)
            
            # 将文件添加到ZIP文件中
            zipf.write(file_path, arcname)

print(f'{zip_filename} 已创建完成。')
