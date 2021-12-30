import os
import shutil

# - корневая папка с моделями:
address_root_folder = input('Введите адресс папки: ')
# - папка отсортированых моделей:
address_sort_models = 'F:\Загрузки\папка с моделями\Новая папка\сорт'

# - папка забракованой сортировки моделей:
address_rejected_models = 'F:\Загрузки\папка с моделями\Новая папка\сорт'

repeat = True
while repeat:
    library = []

    try:
        def goes_over():
            '''
            - перебирает папку на файлы:
            :return:
            '''
            for file in os.listdir(address_root_folder):
                library.append(file)
            return library


        goes_over()


        def clean():
            '''
            - чистим от лишних окончаний названия:
            :return:
            '''
            # - приравниваем к новым переменным:
            file_comparisons_one = library[0]
            file_comparisons_two = library[1]

            file_comparisons_one = file_comparisons_one.replace('.jpeg', '').replace('.rar', '').replace('.zip', ''). \
                replace('.png', '').replace('.jpg', '').replace('.7z', '')
            file_comparisons_two = file_comparisons_two.replace('.jpeg', '').replace('.rar', '').replace('.zip', ''). \
                replace('.png', '').replace('.jpg', '').replace('.7z', '')

            if file_comparisons_one == file_comparisons_two:
                def name_folder():
                    '''
                    - создание имя папки:
                    :return:
                    '''

                    # - создание имя папки:
                    namelist_zero = library[0].replace('.jpeg', '').replace('.rar', ''). \
                        replace('.zip', '').replace('.png', '').replace('.jpg', '').replace('.7z', '').replace('_', '.')
                    return namelist_zero

                name_folder()

                def address_sort_folder():
                    '''
                    - адресс папки сортировки :
                    :return:
                    '''
                    address_name = f'{address_sort_models}\\{name_folder()}\\'
                    os.makedirs(address_name, exist_ok=True)
                    return address_name

                address_sort_folder()

                def name_address():
                    '''
                    - адресс папки сортировки :
                    :return:
                    '''
                    address_name = f'{address_sort_models}\\{name_folder()}\\'
                    return address_name

                name_address()

                def address_download():
                    '''
                    - адрес загрузки файла:
                    :return:
                    '''
                    download_address = f'{address_sort_models}\\{name_folder()}'
                    return download_address

                address_download()

                def address_files():
                    '''
                    -  адрес первого и второго файла:
                    :return:
                    '''
                    file_one = f'{address_root_folder}\\{library[0]}'
                    file_two = f'{address_root_folder}\\{library[1]}'
                    return file_one, file_two

                address_files()

                def move_file():
                    '''
                    - переброс файлов в новую папку:
                    :return:
                    '''
                    move_list = []
                    for address_file in address_files():
                        move_list.append(address_file)
                    shutil.move(move_list[0], address_download())
                    shutil.move(move_list[1], address_download())

                move_file()
            elif file_comparisons_one != file_comparisons_two:
                def no_such_file():
                    '''
                    - файл не имеющий подобного по названию файла - уходит в папку просто файлом(без доп. созданой папки):
                    :return:
                    '''
                    file_one = f'{address_root_folder}\\{library[0]}'
                    download_address_one = f'{address_sort_models}\\{library[0]}'
                    shutil.move(file_one, download_address_one)

                no_such_file()

        clean()
    except IndexError:
        address_root_folder = input('Введите адресс папки: ')
