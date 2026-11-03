
import unittest
import tempfile
import csv

from pathlib import Path
from app.batch_moderation import process_csv


class TestBatchModeration(unittest.TestCase):

    def test_batch_processing(self):

        with tempfile.TemporaryDirectory() as temp:

            temp = Path(temp)

            input_file = temp / "input.csv"
            output_file = temp / "output.csv"
            summary_file = temp / "summary.txt"

            # 创建测试数据
            with open(
                input_file,
                "w",
                encoding="utf-8-sig",
                newline=""
            ) as f:

                writer = csv.DictWriter(
                    f,
                    fieldnames=["id", "content"]
                )

                writer.writeheader()

                writer.writerow({
                    "id": "1",
                    "content": "今天天气真好"
                })

                writer.writerow({
                    "id": "2",
                    "content": "加微信扫码进群"
                })

            # 执行批量审核
            result = process_csv(
                input_file,
                output_file,
                summary_file
            )

            self.assertEqual(result["total"], 2)
            self.assertEqual(result["approved"], 1)
            self.assertEqual(result["manual_review"], 1)

            self.assertTrue(output_file.exists())
            self.assertTrue(summary_file.exists())

    def test_missing_content_column(self):

        with tempfile.TemporaryDirectory() as temp:

            temp = Path(temp)

            input_file = temp / "bad.csv"

            input_file.write_text(
                "id,message\n1,hello",
                encoding="utf-8"
            )

            with self.assertRaises(ValueError):

                process_csv(
                    input_file,
                    temp / "output.csv",
                    temp / "summary.txt"
                )


if __name__ == "__main__":
    unittest.main()
