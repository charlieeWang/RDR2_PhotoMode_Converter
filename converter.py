import os
import sys

class Converter():
    def __init__(self):
        HOME = os.path.expanduser('~')
        RDR2_PROFILE_PATH = 'Documents\\Rockstar Games\\Red Dead Redemption 2\\Profiles'
        self.PATH = os.path.join(HOME, RDR2_PROFILE_PATH)

    def walk(self, source=None):
        # check if there're inputs or not
        if source is None:
            source = self.PATH

        output = "Photo"
        folders = os.listdir(source)
        for folder in folders:

            folder_path = os.path.join(source, folder)
            output_path = os.path.join(folder_path, output)

            if not os.path.exists(output_path):
                os.makedirs(output_path)

            files = os.listdir(folder_path)
            for file in files:
                if 'PRDR' in file:
                    file_path = os.path.join(folder_path, file)
                    self.convert(file_path, os.path.join(output_path, file))

    def convert(self, file_path, output_path):

        file = open(file_path, 'rb')
        file = file.read()
        output_path = output_path + ".jpg"

        # check if converted file exist
        if not os.path.isfile(output_path):
            converted_file = open(output_path, 'wb')
            converted_file.write(file[300:])
            converted_file.close()
            print(output_path)



if __name__=='__main__':
    converter = Converter()

    if(len(sys.argv) >= 2):
        converter.walk(sys.argv[1])
    else:
        converter.walk()
