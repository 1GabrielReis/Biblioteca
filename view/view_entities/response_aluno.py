from ..response_base import Response_base

class Response_aluno(Response_base):
    def __init__(self,controller_aluno):
        self.controller= controller_aluno
            
    def build_list(self, lista):
        pass
  
    def build_detail(self, obj):
        pass

    def serialize(self, obj):
        pass