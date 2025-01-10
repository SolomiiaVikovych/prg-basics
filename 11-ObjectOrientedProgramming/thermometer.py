class Temperature:
    def __init__(self,temperature):
        self.temperature = temperature
        self.is_on = False

    def turn_on(self):
        self.is_on = True
       

    
    def turn_off(self):
        self.is_on = False

    def messure(self):
        if self.is_on == True:
            if self.temperature >= 41:
                message = '(fever) CRITICAL TEMPERATURE'
            elif self.temperature >= 37:
                message = '(fever)'
            else:
                message = ''
            print(f'temperature: {self.temperature}{message}')
        else:
            print('turn on the thermomiter to use it')


 