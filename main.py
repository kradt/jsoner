import json
from pydantic import BaseModel


class Jsoner:
    
    def __init__(
            self,
            models: list[BaseModel] | BaseModel,
            filename: str,
            save_immediately: bool = False):
        
        self.models = models
        self.filename = filename
        self.save_immediately = save_immediately

        self.objects_to_save = []

    def _belong_to_models(self, model) -> bool:
        for m in self.models:
            if isinstance(model, m):
                return True
        return False
    
    def append(self, obj: BaseModel) -> None:
        if not self._belong_to_models(obj):
            raise ValueError("You can't use underfinded models")
        self.objects_to_save.append(obj.dict())

        if self.save_immediately:
            self.save()

    def _get_json_from_file(self) -> dict:
        with open(self.filename, "r") as file:
            file = file.read()
            if not file:
                return None
            data = json.loads(file)
        return data

    def save(self, indent: int = 4, ensure_ascii: bool = True, allow_nan: bool = True):
        jsn = self._get_json_from_file()
        with open(self.filename, "w") as file:
            if isinstance(jsn, list):
                jsn.extend(self.objects_to_save) if jsn else None

            if isinstance(jsn, dict):
                jsn.update(self.objects_to_save) if jsn else None

            jsn = jsn if jsn else self.objects_to_save
            json.dump(jsn, file, indent=indent, ensure_ascii=ensure_ascii, allow_nan=allow_nan)

