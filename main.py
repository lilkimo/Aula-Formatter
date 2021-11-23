from os import name
from pathlib import Path
from shutil import copyfile, rmtree

def main():
    path = Path(__file__).parent
    while (toJoin := input(f'{path.absolute()}''\\')) != '':
        if not (newPath := path.joinpath(toJoin)).is_dir():
            print('Ruta inválida, intente nuevamente')
            continue
        path = newPath.resolve()

        for entry in path.iterdir():
            print(f'├── {entry.name}')
        print('└── ..')

    inside = list(path.iterdir())
    for entry in inside:
        if not entry.is_dir():
            exit(f'{path.absolute()} no es una ruta válida puesto que no todos sus archivos son carpetas')
        length = 0
        for entry2 in entry.iterdir():
            if not entry2.name.endswith('.py'):
                exit(fr'{path.absolute()} no es una ruta válida porque \{entry.name}\{entry2.name} no es un script de python')
            if (length := length + 1) > 1:
                exit(fr'{path.absolute()} no es una ruta válida puesto que \{entry.name}\ tiene más de un archivo')
        if length == 0:
            exit(fr'{path.absolute()} no es una ruta válida puesto que \{entry.name}\ no tiene archivos')
    print('Ruta validada exitosamente')

    for entry in inside:
        filename = entry.name.split('_')[0]
        copyfile(next(entry.iterdir()).absolute(), fr'{path.absolute()}\{filename}.py')
        rmtree(entry.absolute())
    print('Programa ejecutado exitosamente')

if __name__ == '__main__':
    main()