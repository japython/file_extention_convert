import os
import shutil

target_directory = "D:\AVCHD\BDMV\STREAM"  # 対象のディレクトリのパス

#保存先フォルダ名の指定
dist_dir = input('行先フォルダ名？:')
dist_dir2 = os.path.join("G:\\2023年画像",dist_dir)
os.mkdir(dist_dir2)

old_extension = ".MTS"  # 変更前の拡張子
new_extension = ".mp4"  # 変更後の拡張

def copy_files(target_directory, dist_dir2):
    # ソースフォルダ内のすべてのファイルを取得
    files = os.listdir(target_directory)

    for file_name in files:
        # ファイルの絶対パスを取得
        source = os.path.join(target_directory, file_name)

        # ファイルをコピー先フォルダにコピー
        shutil.copy(source, dist_dir2)

def rename_files(dist):
    for filename in os.listdir(dist):
        if filename.endswith(".MTS"):
            old_path = os.path.join(dist, filename)
            new_filename = filename.replace(".MTS", ".mp4")
            new_path = os.path.join(dist, new_filename)
            os.rename(old_path, new_path)
        
if __name__ == '__main__':
    copy_files(target_directory, dist_dir2)
    rename_files(dist_dir2)