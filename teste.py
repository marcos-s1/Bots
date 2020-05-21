import subprocess

root = r'C:\Users\Marcos\Documents\Bots'
aerenderFilePath = r'C:\Program Files\Adobe\Adobe After Effects 2020\Support Files\aerender.exe'
templateFilePath = root+r'\templates\1\template.aep'
destinationFilePath = root

print("Iniciando After Efects . . .")

aerender = subprocess.run([aerenderFilePath,
                           '-comp', 'main',
                           '-project', templateFilePath,
                           '-output', destinationFilePath])

