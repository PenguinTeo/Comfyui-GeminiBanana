import io
import torch
import numpy as np
from PIL import Image
from google import genai

MODEL_NAME = "gemini-2.5-flash-image-preview"

# --- 工具函数 ---
def tensor_to_pil(tensor):
    if tensor is None:
        return None
    arr = (tensor[0].cpu().numpy() * 255).astype(np.uint8)
    return Image.fromarray(arr)

def pil_to_tensor(pil_image):
    return torch.from_numpy(np.array(pil_image).astype(np.float32) / 255.0).unsqueeze(0)

# --- 节点类 ---
class GeminiFlash25Node:
    """
    ComfyUI 节点: Gemini Flash 2.5 (Text / Image-to-Image)
    使用 Google Gemini Flash 2.5 模型生成或编辑图像。
    """

    @classmethod
    def INPUT_TYPES(s):
        img_inputs = {f"image_{i:02d}": ("IMAGE",) for i in range(1, 11)}
        required = {
            "api_key": ("STRING", {"multiline": False, "default": ""}),
            "prompt": ("STRING", {"multiline": True, "default": "A futuristic cityscape at sunset"}),
        }
        return {"required": required, "optional": img_inputs}

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("generated_image", "text_response")
    FUNCTION = "generate_image"
    CATEGORY = "Gemini"

    def generate_image(self, api_key, prompt, **kwargs):
        # --- API Key ---
        key = api_key.strip()
        if not key:
            raise ValueError("❌ Gemini API Key is required. 请在节点参数中填写 API Key。")

        client = genai.Client(api_key=key)

        # --- 收集输入 ---
        parts = []
        for i in range(1, 11):
            image_tensor = kwargs.get(f"image_{i:02d}")
            if image_tensor is not None:  # ✅ 显式判断 None
                parts.append(tensor_to_pil(image_tensor))
        if prompt:
            parts.append(prompt)

        if not parts:
            raise ValueError("❌ 必须至少提供一个 prompt 或 一张输入图像。")

        # --- 调用 Gemini Flash 2.5 ---
        try:
            print(f"[GeminiNode] 调用模型 {MODEL_NAME} ...")
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=parts,
            )

            image_tensor, text_res = None, ""
            for part in response.candidates[0].content.parts:
                if getattr(part, "inline_data", None):
                    pil_img = Image.open(io.BytesIO(part.inline_data.data))
                    image_tensor = pil_to_tensor(pil_img)
                if getattr(part, "text", None):
                    text_res += part.text + "\n"

            if image_tensor is None:
                raise RuntimeError(f"⚠️ Gemini Flash 没返回图像。文本结果: {text_res.strip()}")

            return image_tensor, text_res.strip()

        except Exception as e:
            raise RuntimeError(f"🔥 Gemini Flash API 调用错误: {e}")

# --- 节点注册 ---
NODE_CLASS_MAPPINGS = {"GeminiFlash25Node": GeminiFlash25Node}
NODE_DISPLAY_NAME_MAPPINGS = {"GeminiFlash25Node": "Gemini Flash 2.5 Gen/Edit"}
