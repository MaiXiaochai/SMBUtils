# SMBUtils

连接windows共享目录的常用功能。

##### 1. 基本说明
  + 该代码包含了以下功能
    + 使用账号密码访问windows共享目录
    + 下载共享目录下的文件到本地
    + 删除共享目录中的文件
  
##### 2. 使用方法
+ `pip install pysmb`
+ [具体使用样例:demo.py](demo.py)
    ```python
    from os.path import join as path_join

    from smb_utils import SMBUtils
    
    
    def demo():
        """
            主要操作：
                1)下载 名为 mysmb的计算机的共享目录 my_remote_shared下 videos目录中的所有 mp4文件
                2）删除 my_remote_shared/videos下所有的 mp4格式的文件
        """
        # windows共享目录连接信息
        smb_cfg = {
            "username": "maixiaochai",
            "password": "maixiaochai_p",
            "host": "192.168.158.1",
            "remote_name": "mysmb",  # 远程计算机名，就是右击 电脑->属性，显示的计算机名。这个一定要一致，否则即使登录上，访问也会出错
            "local_name": "maixiaochai_pc"  # 本地计算机名称，这个可以随便写
        }
    
        # 共享的文件夹名称
        # 就是在 mysmb 这台电脑上，被共享的文件夹的名称
        shared_dir_name = "my_remote_shared"
    
        # 本地保存文件的目录
        local_data_dir = "e:/data"
    
        smb = SMBUtils(**smb_cfg)
    
        # 这里的意思是以shared_dir_name作为顶级目录，访问这个目录下/videos这个目录，获取所有以.mp4结尾的文件名称
        # 这里的 *.mp4是正则的写法
        files = smb.list_files(shared_dir_name, '/videos', '*.mp4')
    
        for no, file_name in enumerate(files, 1):
            # demo: videos/1.mp4
            shared_file_path = path_join('videos', file_name)
    
            # 下载文件
            smb.download_file(shared_dir_name, shared_file_path, local_data_dir, file_name)
    
            print(f"NO.{no} | {files} | downloaded.")
    
        # 删除远程数据文件
        # 删除共享目录 my_remote_shared 下，videos下所有的 mp4格式的文件
        smb.delete_files(shared_dir_name, 'videos/*.mp4')
        print(f"远程数据文件删除完成")
    
    
    if __name__ == '__main__':
        demo()

    ```
##### 3. 其它帮助信息
+ [pysmb 源码: https://github.com/miketeo/pysmb](https://github.com/miketeo/pysmb)
+ [pysmb 源码官方详解: https://pysmb.readthedocs.io/en/latest/](https://pysmb.readthedocs.io/en/latest/)
+ 另外，源码的tests文件中包含了很多详细的用例，如遇到困难可结合这三种资源。