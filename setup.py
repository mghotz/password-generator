from setuptools import setup, find_packages

setup(
    name='password-generator-lib',
    version='0.1.0',
    description='A library for generating secure passwords',
    author='Mahammad Salimov',
    author_email='salimovm.7@gmail.com',
    packages=find_packages(),
    install_requires=["black==23.3.0",
                      "click==8.1.3",
                      "colorama==0.4.6",
                      "mypy-extensions==1.0.0",
                      "packaging==23.1",
                      "pathspec==0.11.1",
                      "platformdirs==3.5.0",
                      "tomli==2.0.1",
                      "typing-extensions==4.5.0",
                      ],

    entry_points={
        'console_scripts': [
            'password-generator=generator:main'
        ]
    }
)