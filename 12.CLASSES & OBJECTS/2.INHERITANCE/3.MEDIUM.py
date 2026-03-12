# Create a parent class Dataset
#     + attribute → records (a list)
# Create a child class CSVData
#     + inherits Dataset
#     + adds method → count_records()
class Dataset:
    def __init__(self, list):
        self.list = list

class CSVData(Dataset):
    def count_records(self):
        apple = len(self.list)
        return print(f'{self.list} has {apple} number is data.')

data = CSVData([1,2,3,4])    
data.count_records()        
