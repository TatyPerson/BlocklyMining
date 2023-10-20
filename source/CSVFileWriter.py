from FileWriterAPI import FileWriterAPI
from csv import writer
import numpy as np

class CSVFileWriter(FileWriterAPI):

	def createFile(filePath, columns):
		np.savetxt(filePath, columns, delimiter=',', fmt='%s')

	def writeLine(filePath, lineContent):

		with open(filePath, 'a+', newline='') as writerObj:
			csvWriter = writer(writerObj)
			csvWriter.writerow(lineContent)