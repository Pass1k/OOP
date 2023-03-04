class MyDict(dict):
    def get(self, kay, default_value=0):
        if kay in self:
            return self[kay]
        else:
            return default_value


new_dict = MyDict()
new_dict['Ikari'] = 1
new_dict['Asuka'] = 2
new_dict['Rei'] = 3
print(new_dict)
print(new_dict.get('Misato'))
