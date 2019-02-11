from common.reading_excel import ReadExcel

class TestReadingExcel:
    def setup(self):
        self.excel=ReadExcel()

    def test_loadin_excel(self):
        assert self.excel.workbook

    def test_get_sheetnames(self):
        assert self.excel.get_sheetnames=['TestData']