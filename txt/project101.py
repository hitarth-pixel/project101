import os
import dropbox
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,accesToken):
        self.accesToken=accesToken
    def uploadFileFunction(self,fileTo,fileFrom):
        dbx=dropbox.Dropbox(self.accesToken)
        for root,directories,files in os.walk(fileFrom):
            for file in files:
                local_path=os.path.join(root,file)
                relativePath=os.path.relpath(local_path,fileFrom)
                dropbox_path=os.path.join(fileTo,relativePath)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
def main():
    accesToken="sl.A8h5Vg2Kz3GTnCfQ1UltUA-x8mt0cNb6V5yGRAWc8HMEvSXEw0sIhVv4g_4xN7-2MqvYj91SS9AxE9W_EdmxjUC6cU44CJiledyMmQiVvaYI1kNnjIgcwf4Fe_aOMHIK9ezEoOA"
    transferData=TransferData(accesToken)
    fileFrom=input("enter the folder path")
    folderTo =input("enter the full path to upload in dropbox")
    transferData.uploadFileFunction(folderTo,fileFrom)
    print("file has been moved")
main()