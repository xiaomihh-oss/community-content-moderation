
import csv
from pathlib import Path

from app.moderation import moderate_content


def process_csv(input_path, output_path, summary_path):

    input_path = Path(input_path)
    output_path = Path(output_path)
    summary_path = Path(summary_path)

    # 检查文件是否存在
    if not input_path.exists():
        raise FileNotFoundError(
            f"找不到输入文件：{input_path}"
        )

    results = []

    # 读取CSV
    with open(
        input_path,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as f:

        reader = csv.DictReader(f)

        if not reader.fieldnames or "content" not in reader.fieldnames:
            raise ValueError(
                "CSV必须包含content字段"
            )

        for row in reader:

            content = row.get("content", "")

            # 调用审核函数
            result = moderate_content(content)

            # 保存原始数据和审核结果
            row["result"] = result["result"]
            row["risk_score"] = result["risk_score"]
            row["risk_level"] = result["risk_level"]
            row["reasons"] = ";".join(result["reasons"])

            results.append(row)

    # 创建输出文件夹
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # 输出审核结果
    fieldnames = list(results[0].keys()) if results else [
        "id", "content", "result",
        "risk_score", "risk_level", "reasons"
    ]

    with open(
        output_path,
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(results)

    # 统计审核结果
    total = len(results)

    approved = sum(
        1 for r in results
        if r["result"] == "审核通过"
    )

    manual_review = total - approved

    high_risk = sum(
        1 for r in results
        if r["risk_level"] == "高风险"
    )

    medium_risk = sum(
        1 for r in results
        if r["risk_level"] == "中风险"
    )

    low_risk = sum(
        1 for r in results
        if r["risk_level"] == "低风险"
    )

    # 生成统计报告
    summary = f"""
内容安全批量审核报告
========================

总审核数量：{total}
审核通过：{approved}
需要人工复核：{manual_review}

风险等级分布：
高风险：{high_risk}
中风险：{medium_risk}
低风险：{low_risk}

审核通过率：{approved / total * 100 if total else 0:.2f}%
人工复核率：{manual_review / total * 100 if total else 0:.2f}%
"""

    summary_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    summary_path.write_text(
        summary,
        encoding="utf-8"
    )

    print(summary)
    print("审核结果已保存：", output_path)
    print("统计报告已保存：", summary_path)

    return {
        "total": total,
        "approved": approved,
        "manual_review": manual_review,
        "high_risk": high_risk,
        "medium_risk": medium_risk,
        "low_risk": low_risk
    }


if __name__ == "__main__":

    process_csv(
        "data/sample_comments.csv",
        "data/moderation_results.csv",
        "data/moderation_summary.txt"
    )
