import yaml

def load_config(config_path):
    """
    Loads a YAML configuration file.
    
    Args:
        config_path (str): Path to the config file.
        
    Returns:
        dict: Loaded config data.
    """
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)
