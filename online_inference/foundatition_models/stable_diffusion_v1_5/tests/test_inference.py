import pytest
from diffusers import StableDiffusionPipeline
from src.model_loader import load_model
from src.inference.stable_diffusion import run_inference
from src.utils.config_loader import load_config

# Load configuration
config = load_config("config/inference_config.yaml")
model_name = config.get("model_name")
device = config.get("device")

# Test if the model loads correctly from Hugging Face
def test_load_model():
    try:
        pipe = load_model(model_name, device)
        assert pipe is not None, "Model failed to load"
    except Exception as e:
        pytest.fail(f"Model loading failed: {e}")

# Test if inference runs successfully and returns an image
def test_run_inference():
    pipe = load_model(model_name, device)
    
    # Define a simple prompt
    prompt = "A beautiful landscape of mountains during sunset"
    
    # Run inference
    image = run_inference(pipe, prompt)
    
    # Check that the result is an image
    assert image is not None, "Inference did not return an image"
    assert image.size == (512, 512), "Image size is incorrect"

# Test for handling invalid input (empty prompt)
def test_empty_prompt():
    pipe = load_model(model_name, device)
    
    prompt = ""
    
    with pytest.raises(ValueError):
        run_inference(pipe, prompt)
