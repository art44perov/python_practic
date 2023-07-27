import os
import logging

main_path = 'C:/Users/Win11-test/Downloads'
logging.basicConfig(level=logging.INFO, filename="sort_log.log",filemode="w")
extensions = {
    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv','rm', 'swf', 'vob'],
    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 'tar', 'xml'],
    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],
    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],
    'archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],
    'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],
    '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],
    'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],
    'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],
    'font': ['otf', 'ttf', 'fon', 'fnt'],
    'gif': ['gif'],
    'exe': ['exe'],
    'bat': ['bat'],
    'apk': ['apk'],
    'error_downloads': ['crdownload'],
    '1C External_processing': ['epf'],
    '1C External_Report': ['erf'],
    '1C Configuration': ['cf', 'cfe'],
    'DLL': ['dll']
}

def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


def sort_files(folder_path):

    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]
        logging.info(f' name: {file_name} / extension: {extension}')
        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                logging.info(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            logging.info('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)


if __name__ == "__main__":
    create_folders_from_list(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)