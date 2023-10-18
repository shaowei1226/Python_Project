import zipfile
import os



# 要压缩的文件夹路径
folder_to_compress = r'E:\Produce\PG6002'  # 替换为要压缩的文件夹路径

# 压缩后的 zip 文件路径和文件名
output_zip_file = r'E:\Produce\PG6002.zip'  # 替换为压缩后的文件路径和文件名

try:
    # 创建一个 zip 文件
    with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 遍历文件夹中的所有文件和子文件夹，并将它们添加到 zip 文件中
        for root, _, files in os.walk(folder_to_compress):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_to_compress)
                zipf.write(file_path, arcname=arcname)

    print(f"Folder '{folder_to_compress}' compressed to '{output_zip_file}' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
