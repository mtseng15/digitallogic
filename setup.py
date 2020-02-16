import setuptools

with open("README.md") as f:
        long_des= f.read()

setuptools.setup(
        name='digitallogic',
        version='0.0.1',
        description='A helper module for working with binary values in numpy',
        packages=setuptools.find_packages(),
        url='https://github.com/mtseng15/digitallogic',
        author='Micah Tseng',
        author_email='tseng.micah@gmail.com',
        license='MIT',
        long_description=long_des,
        long_description_content_type="text/markdown",
        python_requires='>=3.7',
        install_requires=["numpy"],
        )
