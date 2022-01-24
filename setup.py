import setuptools


setuptools.setup(
    name="jupyter-syncthing-proxy",
    version='1.0.2',
    url="https://github.com/yuvipanda/jupyter-syncthing-proxy",
    author="Yuvi Panda",
    description="yuvipanda@gmail.com",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'syncthing = jupyter_syncthing_proxy:setup_syncthing_proxy',
        ]
    },
    package_data={
        'jupyter_syncthing_proxy': ['icons/icon.svg'],
    },
    include_package_data=True
)
