import torch

def get_device(preferred_device="npu"):
    """
    Determines whether to use a NPU or fallback to CPU.
    
    Args:
        preferred_device (str): Preferred device, either 'npu' or 'cpu'.
        
    Returns:
        torch.device: Device to use for inference.
    """
    if preferred_device == "npu" and torch.npu.is_available():
        return torch.device("npu")
    else:
        return torch.device("cpu")
