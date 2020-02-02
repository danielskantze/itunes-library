import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='iTunesLibrary',
    version='1.1.4',
    author='Daniel Skantze',
    author_email='danielskantze@gmail.com',
    description="Represents an iTunes library. This is a fork of Steven Scholnick's repository (https://github.com/scholnicks/itunes-library).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords=['iTunesLibrary','iTunes'],
    url='https://github.com/danielskantze/itunes-library',
    download_url='https://github.com/danielskantze/itunes-library',
    py_modules=['iTunesLibrary'],
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'
    ]
)
