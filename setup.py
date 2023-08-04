from setuptools import setup, find_packages

setup(
    name='yg_simple_game_engine',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        # Зависимости вашей библиотеки
    ],
    url="https://github.com/Yolshin195/simple_game_engine",
)
