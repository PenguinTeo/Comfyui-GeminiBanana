# 🍌 GeminiBanana for ComfyUI

**GeminiBanana** 是一个基于 **Gemini API** 与 **ComfyUI** 的自定义节点（Custom Node），它可以让你在 ComfyUI 工作流中调用 Gemini 生成文字、解析图像、或进行多模态交互，从而大幅提升工作流的自动化与创意能力。

---

## ✨ 功能特性

- 🔮 **Gemini API 接入**：支持调用 Gemini-Pro / Gemini-Flash 等模型。
- 🖼 **多模态支持**：文字、图像输入与输出。
- ⚡ **ComfyUI 原生集成**：可在工作流中作为节点调用，支持输入/输出连接。
- 🛠 **自定义参数**：支持温度（temperature）、最大长度（max_tokens）、Top-P 等参数配置。
- 📦 **易于扩展**：可以根据需要二次开发，扩展成更复杂的工作流组件。

---

## 📦 安装方法

1. 进入你的 ComfyUI `custom_nodes` 文件夹：
   ```bash
   cd ComfyUI/custom_nodes
2. 克隆本仓库：

   ```bash
   git clone https://github.com/yourname/ComfyUI-GeminiBanana.git
   ```

3. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

4. 重启 ComfyUI，搜索节点列表中的 **Gemini Flash 2.5 Gen/Edit**。

---

## 🚀 使用示例

1. 在 ComfyUI 中添加 **Gemini Flash 2.5 Gen/Edit** 节点。
2. 输入：

   * **文本输入**：Prompt，例如 `"帮我写一首关于企鹅的诗"。`
   * **图像输入**（可选）：上传图片，作为 Gemini 的多模态上下文。
3. 配置参数：

   * 模型：`gemini-pro` 或 `gemini-flash`
   * 最大输出长度
   * 采样温度
4. 输出：

   * 文本结果会显示在节点输出中。
   * 图像结果会保存到 ComfyUI 的输出目录。

---

## ⚙️ 节点参数说明

| 参数名         | 类型     | 说明                                           |
| ----------- | ------ | -------------------------------------------- |
| model       | string | 选择 Gemini 模型（如 `gemini-pro`, `gemini-flash`） |
| temperature | float  | 控制生成的随机性，范围 0.0 - 1.0                        |
| max\_tokens | int    | 最大输出长度                                       |
| top\_p      | float  | nucleus sampling 参数                          |
| api\_key    | string | 你的 Gemini API Key                            |

---

## 📝 注意事项

* 使用前需在环境变量中配置 `GEMINI_API_KEY`，或在节点参数中填写。
* 如果需要图像输入，请确保传入的图像为支持的格式（PNG、JPG）。
* Gemini 的调用需要联网，请确保你的 ComfyUI 运行环境可以访问 Gemini API。

## 🆓 方案介绍

Step1️⃣进入Google Cloud https://console.cloud.google.com/
<img width="1920" height="925" alt="image" src="https://github.com/user-attachments/assets/3b9cdf13-7006-4525-8ef1-b46894385862" />
点击免费试用
<img width="1550" height="720" alt="image" src="https://github.com/user-attachments/assets/ed64238b-715e-45f5-a0d5-259d38dab76f" />
选择香港-随便填写一下信息，建议搜索一下真实存在的街道
绑定Visa卡（招商银行的Visa支持）
成功后创建项目
设置额度（按最小设置即可）
*不要激活不要激活不要激活！！！
* <img width="1920" height="910" alt="d592c696-233e-4fc8-8203-b2d7ad553464" src="https://github.com/user-attachments/assets/194a2fd5-5b56-4deb-9473-17078b0fe3f2" />
Step2️⃣进入Google AI Stuido https://aistudio.google.com/
点击<img width="534" height="350" alt="aebaa518c13b18bb76690666b5dc0061" src="https://github.com/user-attachments/assets/9a830bd4-bc75-48a7-8048-07cf82747918" />
选择项目（刚创建的）
得到APIKEY<img width="1580" height="266" alt="image" src="https://github.com/user-attachments/assets/69ab2a67-f8ea-45c3-b189-d23212608bca" />

Step3️⃣
复制Key回到Comfyui填进去就可以愉快的感受10秒出图了~~~

---

## 🤝 致谢

* [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 社区提供的优秀框架
* [Google Gemini](https://deepmind.google/technologies/gemini/) 提供的多模态大模型
* 本项目由 **GeminiBanana** 团队/作者开发与维护

---

## 📜 License

MIT License. 自由使用、修改与分发，但请保留署名。

---

```
