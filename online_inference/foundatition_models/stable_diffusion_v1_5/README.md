
# Stable Diffusion v1.5 Inference

This repository allows you to run inference for **Stable Diffusion v1.5** using pre-trained model weights from Hugging Face's model hub, with support for NPU (Neural Processing Unit) or CPU devices. The inference generates images from textual prompts based on the Stable Diffusion model.

## Folder Structure

```
stable_diffusion_v1_5/
│
├── config/ 
│   ├── inference_config.yaml      # Configuration for inference (prompt, model name, device, etc.)
│
├── models/                        # (Optional) Placeholder for locally downloaded models
│
├── notebooks/                     # Jupyter notebooks for experimentation
│
├── src/                           # Source code for inference, model loading, utilities
│   ├── inference/                 
│   ├── utils/                     
│   └── model_loader.py            # Code to load Stable Diffusion model
│
├── tests/                         # Unit tests for inference
│
├── scripts/                       # Helper scripts
│
├── .gitignore                     # Git ignore file
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── run_inference.py               # Main script to run inference
```

## Prerequisites

- **Python 3.8+**
- **PyTorch** (with NPU or CPU support)
- **Diffusers library** from Hugging Face for loading the Stable Diffusion model
- **Pillow** for image handling

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd stable_diffusion_inference
   ```

2. **Set up the environment**:
   Install the required Python dependencies using the provided `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify NPU availability**:
   Make sure your environment is correctly set up to use the NPU. You can run a small test to check if the NPU device is detected properly.

## Configuration

The configuration for inference is handled via a YAML file located at `config/inference_config.yaml`. This file contains the following parameters:

```yaml
model_name: "stable-diffusion-v1-5/stable-diffusion-v1-5"  # Model name from Hugging Face
device: "npu"  # Options: 'npu' for Neural Processing Unit, 'cpu' for CPU
prompt: "A futuristic city skyline at night"  # The prompt to generate an image
num_inference_steps: 50  # Number of denoising steps during inference
guidance_scale: 7.5  # Strength of guidance during generation
output_dir: "output/"  # Directory to save the generated image
```

You can adjust the prompt and other parameters in the `inference_config.yaml` file to customize the inference behavior.

## Running Inference

1. **Prepare the configuration**: Ensure that the `config/inference_config.yaml` file contains the correct `model_name`, `device`, and other settings.

2. **Run the inference script**:
   To generate an image from a prompt, use the following command:
   ```bash
   python run_inference.py
   ```

   This will:
   - Load the **Stable Diffusion v1.5** model from Hugging Face's model hub.
   - Use the specified prompt to generate an image.
   - Save the generated image in the directory specified in the config file (`output/` by default).

## Example Inference

An example of `inference_config.yaml`:

```yaml
model_name: "stable-diffusion-v1-5/stable-diffusion-v1-5"
device: "npu"
prompt: "A beautiful sunrise over a mountain range"
num_inference_steps: 50
guidance_scale: 7.5
output_dir: "output/"
```

Run the command:
```bash
python run_inference.py
```

The generated image will be saved to the `output/` directory.

## Running Tests

This repository includes unit tests to ensure that the model loading and inference processes work correctly. The tests are located in the `tests/` directory.

To run the tests, use the following command:
```bash
pytest tests/
```

The tests check for:
- Model loading from Hugging Face
- Successful inference with a given prompt
- Error handling for invalid prompts

## Troubleshooting

- **Missing Model**: If the model name is incorrect or not specified in the configuration, the script will raise an error. Ensure that the model name in the config file is set to `"stable-diffusion-v1-5/stable-diffusion-v1-5"`.
  
- **NPU Not Detected**: If the NPU is not detected, ensure that the proper drivers and libraries are installed for NPU support. You can fall back to `device: "cpu"` in the config file if necessary.

- **Hugging Face API Token**: If you're loading the model from a private repository on Hugging Face, make sure you have the required API token set up in your environment:
  ```bash
  huggingface-cli login
  ```

## Dependencies

The project requires the following dependencies, which can be installed via `pip`:

```txt
torch
diffusers
transformers
huggingface_hub
pillow
pyyaml
pytest
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
