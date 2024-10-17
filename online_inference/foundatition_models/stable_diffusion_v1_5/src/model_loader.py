from diffusers import StableDiffusionPipeline

def load_model(model_name="stable-diffusion-v1-5/stable-diffusion-v1-5", device="npu"):
    """
    Load the Stable Diffusion model from Hugging Face.

    Args:
        model_name (str): Hugging Face model name or path.
        device (str): Device to load the model onto, e.g., "npu" or "cpu".
        
    Returns:
        pipeline: Loaded Stable Diffusion pipeline.
    """

    if model_name is None:
        raise ValueError("Model name is required but not provided.")

    print(f"Loading model {model_name}...")
    pipe = StableDiffusionPipeline.from_pretrained(model_name)
    pipe = pipe.to(device)
    return pipe
