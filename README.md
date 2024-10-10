# XIaoYuanKouSuan

小猿口算自动化全方案，含OCR，无障碍，mitmproxy(抓包),frida hook等，支持自动继续pk，上分必备。

![Language](https://img.shields.io/badge/language-python-blue?logo=python)
![Stars](https://img.shields.io/github/stars/xinyacs/XiaoYuan_Calculation_Automation.svg)
![Forks](https://img.shields.io/github/forks/xinyacs/XiaoYuan_Calculation_Automation.svg)
![Issues](https://img.shields.io/github/issues/xinyacs/XiaoYuan_Calculation_Automation.svg)
![Platform](https://img.shields.io/badge/platform-Android-green?logo=android)

## 目录

- [使用的框架](#使用的框架)
- [环境配置](#环境配置)
- [作者](#作者)
- [参考项目](#参考项目)

## 使用的框架

**OCR**:tesseract和CnOCR

**无障碍服务**：UiAutomator2

**Hook**:frida

## 环境配置

### Android 模拟器或真实设备

1. [Python控制安卓模拟器——uiautomator2模块_python -m uiautomator2 init-CSDN博客](https://blog.csdn.net/AZURE060606/article/details/137265580)
2. 设置设备分辨率为1920*1080


### Python环境
 1.开发环境：python3.8

 2.安装依赖环境

```python
pip3 install -r requirements.txt
```

3.根据需要运行对应的自动化方案

-  **ocr_project** ：OCR自动化识别，速度在最快在0.5s一题
- **uiautomator_project**:无障碍识别，速度最快在0.7s一题
- **mitmproxy_project**:抓包识别，速度最快在0.3s一题

4.运行该目录下的 main.py文件

## 作者
xinya01@xinyacs.top

## 参考项目

- [XiaoYuanKouSuan](https://github.com/cr4n5/XiaoYuanKouSuan)
- [KouSuanOCR](https://github.com/extrant/KouSuanOCR)
