"""
腾讯云API
"""

from qcloud_sdk.base.client import APIClientInitializer, BaseAPIClientMixin
from qcloud_sdk.cos.client import CosBaseAPIClientMixin
from qcloud_sdk.cos.api import CosAPIMixin
from qcloud_sdk.eb.api import EbAPIMixin
from qcloud_sdk.sms.api import SmsAPIMixin

from qcloud_sdk.config import settings


class QCloudAPIClient(
    APIClientInitializer,
    BaseAPIClientMixin,
    # 使用默认协议的云产品，使用BaseAPIClientMixin类。
    EbAPIMixin,
    SmsAPIMixin,
    # 独立定义协议的云产品，使用其独立的APIClientMixin类。
    CosBaseAPIClientMixin,
    CosAPIMixin
):
    pass


# APIClient单例
# 适用于通过环境变量配置SDK默认参数的容器或函数计算应用
if settings.SECRET_ID and settings.SECRET_KEY:
    qcloud_api_client = QCloudAPIClient()
