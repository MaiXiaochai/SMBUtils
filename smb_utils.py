# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : smb_utils.py
@Author     : chuan.zhang
@Email      : chuan.zhang@outlook.com
@CreatedOn  : 2021/1/19 10:17
--------------------------------------
"""
from os.path import join as path_join

from smb.SMBConnection import SMBConnection


class SMBUtils:
    """
        访问 smb共享的通用功能
    """

    def __init__(self, host, username, password, remote_name, local_name=None):
        local_name = local_name if local_name else ''
        self.conn = SMBConnection(username, password, local_name, remote_name, is_direct_tcp=True)
        self.conn.connect(host, 445)

    def list_files(self, service_name, share_path, pattern="*"):
        """
            获得共享目录下的文件
        """
        result = []
        filenames = self.conn.listPath(service_name, share_path, pattern=pattern)

        for filename in filenames:
            file_name, is_dir = filename.filename, filename.isDirectory
            if not is_dir:
                result.append(file_name)

        return result

    def download_file(self, shared_dir, shared_file_path, local_data_dir, local_file_name):
        """
            下载 windows共享目录 shared_dir下的 shared_file_path 文件到本地 local_data_dir 目录下,
            保存为 local_file_name
        """
        local_file_path = path_join(local_data_dir, local_file_name)

        with open(local_file_path, 'wb') as f:
            self.conn.retrieveFile(shared_dir, shared_file_path, f)

    def delete_files(self, shared_dir, path_file_pattern):
        """
            删除远程数据
        """
        self.conn.deleteFiles(shared_dir, path_file_pattern)

    def __del__(self):
        self.conn.close()
