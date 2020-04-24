import setuptools
from scissors import __version__

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', encoding='utf-8') as file:
    requirements = file.read().splitlines()

setuptools.setup(
    name='intelligent-scissors',
    version=__version__,
    author="Stanislav Shimovolos",
    author_email='shimovolos.sa@phystech.edu',
    description="Intelligent Scissors tool",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/stanislaushimovolos/Intelligent-Scissors',
    download_url='https://github.com/stanislaushimovolos/Intelligent-Scissors/v%s.tar.gz' % __version__,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires='>=3.5',
)