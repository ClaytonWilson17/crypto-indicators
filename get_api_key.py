import os
from dotenv import load_dotenv

def get_env_variable(variable_name):
    """
    Get the value of an environment variable from the .env file.

    Parameters:
    - variable_name (str): The name of the environment variable to retrieve.

    Returns:
    - str: The value of the environment variable.
    """
    # Load environment variables from the .env file
    load_dotenv()

    # Get the value of the specified variable from the environment
    value = os.getenv(variable_name)

    if value is None:
        print(f"Error: {variable_name} not found in the .env file.")

    return value



