"""
Return config on servers to start for syncthing

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os

def setup_syncthing_proxy():
    return {
        'command': [
            "syncthing", "serve", "--no-browser"
        ],
        'port': 8384,
        'environment': {},
        "request_headers_override": {
            # https://docs.syncthing.net/users/faq.html?highlight=host%20check%20error#why-do-i-get-host-check-error-in-the-gui-api
            "Host": "localhost"
        },
        'launcher_entry': {
            'title': 'Syncthing',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'logo.svg')
        }
    }
