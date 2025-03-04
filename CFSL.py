import os
import subprocess

def process_pdb_files(folder_path, pymol_path):
    if not os.path.isdir(folder_path):
        print(f"folder path {folder_path} nonexistence。")
        return

    pdb_files = [f for f in os.listdir(folder_path) if f.endswith('.pdb')]

    if not pdb_files:
        print(f"folder {folder_path} no pdb file。")
        return

    for pdb_file in pdb_files:
        pdb_path = os.path.join(folder_path, pdb_file)
        process_single_pdb(pdb_path, pymol_path)

def process_single_pdb(pdb_file, pymol_path):
    base_name, _ = os.path.splitext(pdb_file)
    output_file = base_name + "_1.pse"

    pymol_script = f"""
set seq_view
color red, ss l+
select hydrophobes, (resn trp+tyr+pro+val+ile+leu+phe+met)
save {output_file}
"""

    pymol_command = [pymol_path, "-c", pdb_file, "-d", pymol_script]

    try:
        result = subprocess.run(pymol_command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"folder {pdb_file} is processed and saved as {output_file}。")
        else:
            print(f"process {pdb_file} error：\n{result.stderr}")
    except Exception as e:
        print(f"an error occurs while executing the PyMOL command：{e}")

def main():
    folder_path = input("enter the folder path: ")

    pymol_path = r"D:\PYMOL\PyMOLWin.exe"

    process_pdb_files(folder_path, pymol_path)

if __name__ == "__main__":
    main()
