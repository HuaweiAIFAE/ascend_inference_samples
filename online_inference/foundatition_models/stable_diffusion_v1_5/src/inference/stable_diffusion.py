import torch

def run_inference(pipe, prompt, num_inference_steps=50, guidance_scale=7.5):
    """
    Runs inference using Stable Diffusion pipeline.
    
    Args:
        pipe: The Stable Diffusion pipeline loaded from Hugging Face.
        prompt: The text prompt for generating images.
        num_inference_steps: The number of denoising steps.
        guidance_scale: Controls the strength of guidance during inference.

    Returns:
        Generated image (PIL.Image).
    """
    with torch.autocast("npu"):
        image = pipe(prompt, num_inference_steps=num_inference_steps, guidance_scale=guidance_scale).images[0]
    return image
