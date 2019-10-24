from django.conf import settings
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from fdfs_client.client import Fdfs_client

from settings import dev


@deconstructible
class FastDFSStorage(Storage):
    """自定义的文件存储系统"""

    def __init__(self, client_conf=None, base_url=None):
        if client_conf is None:
            # 客户端配置文件
            client_conf = dev.FDFS_CLIENT_CONF
        self.client_conf = client_conf

        if base_url is None:
            # 构造图片完整路径，图片服务器的域名
            base_url = dev.FDFS_BASE_URL
        self.base_url = base_url

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):
        """
        保存文件
        :param name:  前端传递的文件名
        :param context: 文件数据
        :return: 存储到数据库中的文件名
        """
        # 保存到FastDFS
        client = Fdfs_client(self.client_conf)

        ret = client.upload_by_buffer(content.read())

        if ret.get("Status") != "Upload successed.":
            raise Exception("upload file failed")

        file_name = ret.get("Remote file_id")

        return file_name

    def exists(self, name):
        '''
        判断文件是否存在，FastDFS可以自行解决文件的重名问题
        所以此处返回False，告诉Django上传的都是新文件
        :param name: 文件名
        :return: False
        '''
        return False

    def url(self, name):
        """
        返回文件的完整URL路径
        :param name: 数据库中保存的文件名
        :return: 完整的URL
        """
        return self.base_url + name
