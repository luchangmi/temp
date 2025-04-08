import pandas as pd
import os

def merge_excel_files(folder_path):
### os.listdir(folder_path)存放需要合并的excel文件的路径，
    all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xlsx')]
    df_list = []
    for file in all_files:
        try:
            df = pd.read_excel(file)
            df_list.append(df)
        except FileNotFoundError:
            print(f"错误：未找到文件 {file}。")
        except Exception as e:
            print(f"读取文件 {file} 时发生错误：{e}")
    if df_list:
        merged_df = pd.concat(df_list, ignore_index=True)
        try:
            merged_df.to_excel('merged.xlsx', index=False)
            print("文件已成功合并到 merged.xlsx。")
        except Exception as e:
            print(f"写入合并文件时发生错误：{e}")
    else:
        print("未找到有效的 Excel 文件。")

if __name__ == "__main__":
# 与上边的os.listdir(folder_path)一起的，
# excel_files文件夹，是folder_path路径下文件夹，用于存放需要合并的excel文件，
### 建议这两个地方set一样的路径，
    folder_path = 'excel_files'
    merge_excel_files(folder_path)