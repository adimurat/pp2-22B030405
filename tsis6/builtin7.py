def copyContent(init_filename, target_filename):
    init_file = open(init_filename, 'r')
    file_content = init_file.read()
    init_file.close()

    target_file = open(target_filename, 'w')
    target_file.write(str(file_content))
    target_file.close()
    print('Successfully copied')

    target_file = open(target_filename, 'r')
    print(target_file.read())
    target_file.close()
