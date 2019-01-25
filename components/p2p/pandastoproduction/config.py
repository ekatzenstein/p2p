import os

CONFIG = {
    'api_base_url': f"http://{os.environ.get('API_HOST', 'localhost')}/api",
}
