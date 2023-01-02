
import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        break
    return dirs

if __name__ == '__main__':
    documentPath = "C:/Users/Admin/Documents/Paradox Interactive/Stellaris/mod/"
    documentModPath = input("请复制粘贴paradox文档中mod目录位置:")
    documentPath = documentModPath + '/'
    print(os.getcwd())
    nowPath = os.getcwd()
    replacePath0 = nowPath
    print(replacePath0)
    dirs = file_name('.')
    print(dirs)
    print(type(dirs))

    for dd in dirs:
        try:
            replacePath = replacePath0+'\\'+dd
            replacePath = replacePath.replace('\\', '/')
            replacePath = 'path=\"' + replacePath + '\"'
            print(replacePath)
            print(dd)
            print('./'+dd+'/descriptor.mod')
            specificPath = './'+dd+'/descriptor.mod'
            with open(specificPath, 'r') as f:
                data = f.readlines()
                print(type(data))
                print(data)
                for i in data:
                    if 'remote_file_id' in i:
                        data.remove(i)
                data.append(replacePath)
                print(data)

                ww = open(documentPath+dd+'.mod', 'w+')

                ww.writelines(data)

        except:
            pass
