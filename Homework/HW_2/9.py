import copy
class FragileDict:
    def __init__(self, f_dict = None):
        self._lock = True
        if dict is None:
            self._data = copy.deepcopy({})
        else:
            self._data = {}
            for key,value in f_dict.items():
                self.__setitem__(key, value)
            self._data = copy.deepcopy(self._data)
        self._lock = False
            
    def __getitem__(self,key):
        if key in self._data.keys():
            return self._data[key]
        else:
            raise KeyError(key)
        
    def __setitem__(self,key,value):
        if self._lock == True:
            self._data[key]=value
        else:
            raise RuntimeError("Protected state")

        
    def __contains__(self, key):
        return key in self._data.keys()
    
    def __enter__(self):
        self._lock = True
        self.cash = copy.deepcopy(self._data)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self._data = copy.deepcopy(self.cash)
            print("Exception has been suppressed.")
        else:
            self._data  = copy.deepcopy(self._data)
        del self.cash
        self._lock = False    
        return True  # Так подавляем исключение.