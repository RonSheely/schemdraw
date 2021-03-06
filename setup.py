import setuptools

with open('README.txt', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name = 'schemdraw',
    version = '0.8',
    description = 'Electrical circuit schematic drawing',
    author = 'Collin J. Delker',
    author_email = 'developer@collindelker.com',
    url = 'https://schemdraw.readthedocs.io/',
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        'Source': 'https://bitbucket.org/cdelker/schemdraw',
    },
    python_requires='>=3.7',
    packages = ['schemdraw',
                'schemdraw.elements',
                'schemdraw.logic',
                'schemdraw.dsp',
                'schemdraw.flow',
                'schemdraw.backends',
               ],
    package_dir={'schemdraw': 'schemdraw'},
    keywords = ['circuit', 'schematic', 'electrical', 'flowchart', 'logic'],
    install_requires=['numpy', 'matplotlib'],
    classifiers = [
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Intended Audience :: End Users/Desktop',
    ],
)
