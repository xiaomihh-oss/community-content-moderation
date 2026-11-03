from app.rules import (
    AD_KEYWORDS,
    ABUSE_KEYWORDS,
    PHONE_PATTERN,
    URL_PATTERN
)


def moderate_content(text):

    reasons = []

    # 1. 检查广告
    if any(word in text for word in AD_KEYWORDS):
        reasons.append("疑似广告或垃圾信息")

    # 2. 检查不文明内容
    if any(word in text for word in ABUSE_KEYWORDS):
        reasons.append("疑似不文明内容")

    # 3. 检查手机号码
    if PHONE_PATTERN.search(text):
        reasons.append("包含手机号码")

    # 4. 检查外部链接
    if URL_PATTERN.search(text):
        reasons.append("包含外部链接")

    # 5. 风险评分
    weights = {
        "疑似广告或垃圾信息": 2,
        "疑似不文明内容": 3,
        "包含手机号码": 3,
        "包含外部链接": 2
    }

    risk_score = sum(weights[item] for item in reasons)

    # 6. 风险等级
    if risk_score == 0:
        risk_level = "低风险"
    elif risk_score <= 2:
        risk_level = "中风险"
    else:
        risk_level = "高风险"

    # 7. 审核结果
    result = "人工复核" if reasons else "审核通过"

    return {
        "content": text,
        "result": result,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "reasons": reasons
    }