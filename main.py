import json
from pydantic import BaseModel


class Jsoner:
    
    def __init__(
            self,
            models: list[BaseModel] | BaseModel,
            save_immediately: bool = False):
        self.models = models
        self.save_immediately = save_immediately
        self.objects_to_save = []

    def _belong_to_models(self, model) -> bool:
        for m in self.models:
            if isinstance(model, m):
                return True
        return False
    
    def append(self, obj):
        if not self._belong_to_models(obj):
            raise ValueError("You can't use underfinded models")
        self.objects_to_save.append(obj)

        if self.save_immediately:
            self.save()

    def save(self):
        pass