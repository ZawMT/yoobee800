from dataexport import ExportCSV, ExportJSON, ExportXML


class ExportFactory:
    @staticmethod
    def create_export(export_type: str):
        if export_type == "csv":
            return ExportCSV()
        elif export_type == "xml":
            return ExportXML()
        elif export_type == "json":
            return ExportJSON()
        else:
            raise ValueError("Invalid export type")
