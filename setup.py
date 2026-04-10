from setuptools import setup, find_packages

setup(
    name="papa_tools", # ชื่อเวลาสั่ง pip install
    version="0.1",
    packages=find_packages(),
    install_requires=[ # ระบุ library ที่ต้องใช้
        'pandas',
        'seaborn',
        'matplotlib',
        'numpy'
    ],
)