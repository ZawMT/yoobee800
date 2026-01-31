from abc import abstractmethod

from student import Student


class Export():
    @abstractmethod
    def export(self, message: str, obj: Student):
        pass


class ExportCSV(Export):
    def export(self, message: str, obj: Student):
        print(f"Exported as CSV")
        print(f"name,age,id")
        print(f"Exported as CSV: {obj.name}, {obj.age}, {obj.student_id}")


class ExportJSON(Export):
    def export(self, message: str, obj: Student):
        print(f"Exported as JSON: {message}")
        print(
            f"Exported as CSV: {{\"name\":\"{obj.name}\", \"age\":\"{obj.age}\", \"id\":\"{obj.student_id}\"}}")


class ExportXML(Export):
    def export(self, message: str, obj: Student):

        # Real implementation should come in here
        print(f"Exported as XML: {message}")
