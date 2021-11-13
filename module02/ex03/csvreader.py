import csv

#? opens, reads, and parses a CSV file

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.fd = None
		self.data = ""
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.sep = sep
		self.corrupted = False

	def __enter__(self):
		try:
			self.fd = open(self.filename)
			self.data = self.fd.read();
			if self.is_corrupted():
				self.corrupted = True
			return self
		except FileNotFoundError:
			print("Wrong file or file path")
			return None

	def __exit__(self, exception_type, exception_value, traceback):
		if self.fd:
			self.fd.close()

	def is_corrupted(self):
		data = self.data.split('\n')
		first_line = self.data[0]
		for line in data:
			if len(first_line.split(self.sep)) == len(line.split(self.sep)):
				return False
		return True

	def getdata(self):
		if self.corrupted:
			# return "the file is corrupted"
			return None
		data = self.data.split('\n')
		if self.header:
			data = data[1:]
		if self.skip_top > 0:
			data = data[self.skip_top - 1:]
		if self.skip_bottom > 0:
			data = data[:len(data) - self.skip_bottom]
		final_data = []
		for line in data:
			final_data += line.split(self.sep)
		return final_data

	def getheader(self):
		if self.corrupted:
			# return "the file is corrupted"
			return None
		if self.header:
			result = self.data.split('\n')[0]
			return (result.split(self.sep))


if __name__ == "__main__":
	with CsvReader("good.csv", header=True, skip_top=3, skip_bottom=3) as file:
		data = file.getdata()
		header = file.getheader()

	with CsvReader('bad.csv') as file:
		if file == None:
			print("File is corrupted")

#? access file by relative path
