from setuptools import setup, find_packages

setup(
    name="notification-service",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'test': ['pytest>=7.0.0', 'pytest-cov>=4.0.0', 'pytest-mock>=3.10.0'],
    },
    python_requires='>=3.8',
)
