import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token='sl.Bq_wPKQ65zgs648lZgiFvQQQIxVkxwvT4PthsQ1mbZ_78nDsqkayVzYwL8KHIsX-gNc7JVVzog6kIepREEwnuzJ2UJFO7PMhw7Cv48fn020OSjSUPLNRn6euakyVqyFrK-rp86F7ICAH'

    transferData=TransferData(access_token)
    file_from='/Users/hamzah_ali/Documents/Vs code/Coding Class Python/test.txt'
    file_to="/hamzah_101/test.txt"

    transferData.upload_file(file_from, file_to)
    print("file has been moved")
main()