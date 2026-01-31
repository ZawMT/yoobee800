from student import Student
from factory import ExportFactory


def main():
    student = Student("John Doe", 20, "12345")
    student.display_info()

    export_type = input("Enter export type (csv/xml/json): ").lower()
    export = ExportFactory.create_export(export_type)
    export.export(export_type, student)


if __name__ == "__main__":
    main()
