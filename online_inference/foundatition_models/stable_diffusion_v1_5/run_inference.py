import torch
import torch_npu
from src.utils.config_loader import load_config
from src.model_loader import load_model
from src.inference.stable_diffusion import run_inference
from src.inference.postprocessing import save_image

# Load configuration from the YAML file
config = load_config("config/inference_config.yaml")

# Load the model_name from the config
model_name = config.get("model_name")
if model_name is None:
    raise ValueError("Model name is not specified in the config file. Please add 'model_name' in 'config/inference_config.yaml'.")

# Load device (use 'cuda' or fallback to 'cpu')
device = config.get("device")

# Load model from Hugging Face
pipe = load_model(model_name, device)

# Run inference with the provided prompt
prompt = config.get("prompt", "A futuristic city skyline at night")
num_inference_steps = config.get("num_inference_steps", 50)
guidance_scale = config.get("guidance_scale", 7.5)

image = run_inference(pipe, prompt, num_inference_steps=num_inference_steps, guidance_scale=guidance_scale)

# Save the output image
output_dir = config.get("output_dir", "output/")
save_image(image, output_dir)
