import requests

class Net_Saver:

    """URL parameter is ur file url"""
    def __init__(self, url: str):
        self.response = requests.get(url=url)

    #To save image
    def image_safe(self, file_name):
        with open(file=f'{file_name}.jpeg', mode='wb') as file:
            file.write(self.response.content)
            file.close()
            
            return "Succesfully saved!!!"

    #To save video
    def video_save(self, file_name):
        with open(file=f'{file_name}.mp4', mode='wb') as file:
            file.write(self.response.content)
            file.close()

            return "Succesfully saved!!!"

    #To save gif
    def gif_save(self, file_name):
        with open(file=f'{file_name}.gif', mode='wb') as file:
            file.write(self.response.content)
            file.close()

            return "Succesully saved"


#Choose the function and use it with print
if __name__ == '__main__':
    client = Net_Saver(url='UR URL')
    print(client.any_function)
