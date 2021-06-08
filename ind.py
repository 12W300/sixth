#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    flylist = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            city = input("город назначения ")
            numfly = int(input("номер рейса "))
            typea = input("тип самолета ")
            flylistdic = {
                'city': city,
                'numfly': numfly,
                'typea': typea,
            }
            flylist.append(flylistdic)
            if len(flylist) > 1:
                flylist.sort(key=lambda item: item.get('numfly', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Город ",
                    "Номер рейса",
                    "Тип ВС"
                )
            )
            print(line)
            for idx, flylistdic in enumerate(flylist, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        flylistdic.get('city', ''),
                        flylistdic.get('numfly', '0'),
                        flylistdic.get('typea', '')
                    )
                )
            print(line)

        elif command == 'city':
            destsity = input("город назначения ")
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Город ",
                    "Номер рейса",
                    "Тип ВС"
                )
            )
            print(line)
            yesfly = -1
            for idx, flylistdic in enumerate(flylist, 1):
                if flylistdic.get('city', '') == destsity:
                    yesfly = 1
                    print(
                        '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                            idx,
                            flylistdic.get('city', ''),
                            flylistdic.get('numfly', '0'),
                            flylistdic.get('typea', '')
                        )
                    )
            print(line)
            if yesfly == -1:
                print('рейсов в ', destsity, ' нет')

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести весь список рейсов;")
            print("city - вывести рейсы  в указанный город;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
