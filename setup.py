from setuptools import setup

setup(
    name="sectypy",
    version="0.1",
    py_modules=[""],
    entry_points={
        'console_scripts': [
            'sectypy=main',  # Terminalde 'sectypy' yazınca main.py içindeki main() çalışacak
        ],
    },
)