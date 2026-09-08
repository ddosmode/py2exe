#!/usr/bin/env python3
"""Устанавливает языковые пакеты argostranslate для en → ru."""

import argostranslate.package


def main():
    packages = argostranslate.package.get_available_packages()
    for p in packages:
        if p.from_code == 'en' and p.to_code == 'ru':
            argostranslate.package.install_from_path(p.download())
            print(f'Установлен пакет: {p.from_code}->{p.to_code}')
            return
    print('Пакет en->ru не найден в списке доступных')


if __name__ == '__main__':
    main()
