import argparse
import warnings

from setuptools import Extension
from setuptools.dist import Distribution

def wheel_name(**kwargs):
    # создаем поддельное распределение из аргументов
    dist = Distribution(attrs=kwargs)
    # завершить команду bdist_wheel
    bdist_wheel_cmd = dist.get_command_obj('bdist_wheel')
    bdist_wheel_cmd.ensure_finalized()
    # собираем имя файла колеса
    distname = bdist_wheel_cmd.wheel_dist_name
    tag = '-'.join(bdist_wheel_cmd.get_tag())
    return f'{distname}-{tag}.whl'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Return wheel name.')
    parser.add_argument('version', action='store', type=str, help='Version number.')
    args = parser.parse_args()

    warnings.simplefilter("ignore")
    print(wheel_name(name="py2exe", version=args.version, ext_modules=[Extension("py2exe.run", ["run.c"])]))
