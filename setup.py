import setuptools


with open("README.md", "r") as fin:
    long_description = fin.read()
with open("LICENSE", "r") as fin:
    license = fin.read()

setuptools.setup(
    name='fzflib',
    version='0.1.0',
    author='Kyle L. Davis',
    author_email='AceofSpades5757.github@gmail.com',
    url='https://github.com/AceofSpades5757/fzflib',
    description='A Python library for interacting with FZF.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    python_requires='>=3.6',
    packages=setuptools.find_packages(exclude=['tests']),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
