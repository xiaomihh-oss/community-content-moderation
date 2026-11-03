# 内容安全审核规则

import re

# 广告及垃圾信息关键词
AD_KEYWORDS = [
    "加微信",
    "扫码进群",
    "兼职日结",
    "刷单返利",
    "点击链接",
    "私信领取"
]

# 不文明用语关键词（演示用）
ABUSE_KEYWORDS = [
    "傻逼",
    "废物",
    "去死"
]

# 手机号码识别
PHONE_PATTERN = re.compile(
    r"(?<!\d)1[3-9]\d{9}(?!\d)"
)

# 外部链接识别
URL_PATTERN = re.compile(
    r"(https?://|www\.)",
    re.IGNORECASE
)