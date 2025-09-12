#!/usr/bin/env python3
import os
import requests
import shutil
import tempfile
from pathlib import Path


def download_file(url, filepath):
    """下载文件到临时目录再移动到目标位置"""
    print(f"正在下载: {filepath.name}")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # 创建目标目录
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # 下载到临时文件
    with tempfile.NamedTemporaryFile(delete=False, suffix=filepath.suffix) as tmp_file:
        for chunk in response.iter_content(chunk_size=8192):
            tmp_file.write(chunk)
        temp_path = tmp_file.name

    # 移动到目标位置
    shutil.move(temp_path, filepath)
    print(f"完成: {filepath.name}")


def main():
    base_path = Path("/root/ComfyUI/models")

    models = [
        # wan2.2
        (
            "https://civitai.com/api/download/models/2137014?type=Model&format=GGUF&size=full&fp=fp8",
            base_path / "diffusion_models" / "rapidWAN22I2VGGUF_q4KMRapidV91NSFW.gguf"
        ),
        (
            "https://huggingface.co/ratoenien/umt5_xxl_fp8_e4m3fn_scaled/resolve/main/umt5_xxl_fp8_e4m3fn_scaled.safetensors",
            base_path / "text_encoders" / "umt5_xxl_fp8_e4m3fn_scaled.safetensors"
        ),
        (
            "https://huggingface.co/hfmaster/models-moved/resolve/8b8d4cae76158cd49410d058971bb0e591966e04/sdxl/ipadapter/clip-vision_vit-h.safetensors",
            base_path / "clip_vision" / "clip-vision_vit-h.safetensors"
        ),
        (
            "https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/ab076c7a07868990c4506a87f2f60020763a0114/split_files/vae/wan_2.1_vae.safetensors",
            base_path / "vae" / "Wan2.1_VAE.safetensors"
        ),

        # qwen image
        (
            "https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors",
            base_path / "diffusion_models" / "qwen_image_fp8_e4m3fn.safetensors"
        ),
        (
            "https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors",
            base_path / "text_encoders" / "qwen_2.5_vl_7b_fp8_scaled.safetensors"
        ),
        (
            "https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors",
            base_path / "vae" / "qwen_image_vae.safetensors"
        ),
        (
            "https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V2.0.safetensors",
            base_path / "loras" / "Qwen-Image-Lightning-4steps-V2.0.safetensors"
        ),

        #hunyuan3d
        (
            "https://huggingface.co/Comfy-Org/hunyuan3D_2.1_repackaged/resolve/main/hunyuan_3d_v2.1.safetensors",
            base_path / "checkpoints" / "hunyuan_3d_v2.1.safetensors"
        ),

    ]

    for url, filepath in models:
        if not filepath.exists():
            try:
                download_file(url, filepath)
            except Exception as e:
                print(f"下载失败 {filepath.name}: {e}")
        else:
            print(f"已存在: {filepath.name}")

    print("模型下载完成！")


if __name__ == "__main__":
    main()
