import unittest

from app.moderation import moderate_content


class TestModeration(unittest.TestCase):

    # 测试正常内容
    def test_normal_content(self):
        result = moderate_content("今天的天气真不错")
        self.assertEqual(result["result"], "审核通过")

    # 测试广告内容
    def test_ad_content(self):
        result = moderate_content("加微信扫码进群")
        self.assertIn("疑似广告或垃圾信息", result["reasons"])

    # 测试手机号码
    def test_phone_number(self):
        result = moderate_content("联系我 13812345678")
        self.assertIn("包含手机号码", result["reasons"])

    # 测试外部链接
    def test_external_link(self):
        result = moderate_content("访问 https://example.com")
        self.assertIn("包含外部链接", result["reasons"])

    # 测试不文明内容
    def test_abusive_content(self):
        result = moderate_content("你真是个废物")
        self.assertIn("疑似不文明内容", result["reasons"])

    # 测试多种风险同时出现
    def test_multiple_risks(self):
        result = moderate_content(
            "加微信扫码进群，联系13812345678"
        )
        self.assertEqual(result["result"], "人工复核")
        self.assertGreaterEqual(len(result["reasons"]), 2)


if __name__ == "__main__":
    unittest.main()