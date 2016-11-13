import pandas as pd

def get_max_close(company):
	df=pd.read_csv("data/{}.csv".format(company))
	return df['Close'].max()

def test_run():
	for company in ['apple', 'google']:
		print "Max Close"
		print company, get_max_close(company)

test_run()