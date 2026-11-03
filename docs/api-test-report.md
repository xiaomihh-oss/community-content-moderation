# API Testing Report

## 1. Testing Environment
- Language: Python
- Framework: FastAPI
- API Testing Tool: Swagger UI
- Local Server: Uvicorn

## 2. Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Normal Content | 今天的天气真不错 | 审核通过 |
| Advertising Content | 加微信扫码进群 | 识别广告风险 |
| Phone Number | 联系电话：13800138000 | 识别联系方式风险 |

## 3. Test Results

All three test scenarios were executed successfully through the FastAPI Swagger interface.

The API returned structured JSON responses containing moderation results, risk scores, risk levels, and detection reasons.

## 4. Summary

The testing verified the basic functionality of the content moderation API, including normal content processing, advertising detection, and phone number recognition.
