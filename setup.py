from setuptools import find_packages, setup
setup(
    name='lib',
    packages=find_packages(include=['owl_facts']),
    version='1.0',
    description='Random Owl fact provider',
    author='Jarrett Perkins',
    license='GNU GPL 3.0',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='test',
)