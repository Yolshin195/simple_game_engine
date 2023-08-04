from setuptools import setup, find_packages

setup(
    name='yg-simple-game-engine',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        # Зависимости вашей библиотеки
    ],
    url="https://github.com/Yolshin195/simple_game_engine",
)
