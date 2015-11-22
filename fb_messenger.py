import requests
import connections
import traceback as tb
'''
 "paging": {
     "previous": "https://graph.facebook.com/v2.3/1424614544776/comments?format=json&access_token=CAACEdEose0cBAPb6dz0OyeGMDfv8tbbtUz7gMoZBLFdjSyYS62u9wkVj07YEJqrgOOxSUJV8ZBNWmgcFuyHNaxLTxvMJFXRxZBhrKxFsKZC7bagQnM1dCSr50DuqTPdwQk6YKd3LUu6m0v0VjKg3ZANwuVtRhmQRmCX4jru594qHbeHxxkCd4d2NWs95znZBQyfdnZBasZAgv0x3tn5RKj46U3UnsfIGD8UZD&limit=25&since=1408213930&__paging_token=enc_AdBs0Soiog21lpAuiCFnu68jZC69MOBLTHCbBrfXqemK5bVxQYmBpMo636ZCFgBgitN30aGbELQQCObYYh7b60mZCKP&__previous=1",
     "next": "https://graph.facebook.com/v2.3/1424614544776/comments?format=json&access_token=CAACEdEose0cBAPb6dz0OyeGMDfv8tbbtUz7gMoZBLFdjSyYS62u9wkVj07YEJqrgOOxSUJV8ZBNWmgcFuyHNaxLTxvMJFXRxZBhrKxFsKZC7bagQnM1dCSr50DuqTPdwQk6YKd3LUu6m0v0VjKg3ZANwuVtRhmQRmCX4jru594qHbeHxxkCd4d2NWs95znZBQyfdnZBasZAgv0x3tn5RKj46U3UnsfIGD8UZD&limit=25&until=1407942101&__paging_token=enc_AdBgBlU0niwL5mZAPXwmf9eOApFkIUEJuVGxDAo5CRst1dRB2IP5qfKjYMLrToXwyDPhofrgSLnucjAZBS36C1wfjB"
}
'''


def main():
    con, cur = connections.connect_to_gumbo()

    pull_messages(cur)

	con.close()


def pull_messages(cur):
	url = "https://graph.facebook.com/v2.3/1424614544776/comments?format=json&access_token=CAACEdEose0cBAGZAUGcbZCw7oHzBSwLz6fSOZARyIBXpPws1FpSMq0ud2eCZBjz0b8kgu02y7IfvT9iBIFDju1TbvEAt2G1Euc2mUCuzG9xHVGfqfYVXvWA81pafaZCaXaApVZAyGdg9MVNro32hyctZCTQTdJWe8IWZBT5ACkubPSJld2MkUp76YXYXWv4AzZADyTAKnZCnzr1x76j7VvGxZBL"
	url = "https://graph.facebook.com/v2.3/1424614544776/comments?format=json&access_token=CAACEdEose0cBAGZAUGcbZCw7oHzBSwLz6fSOZARyIBXpPws1FpSMq0ud2eCZBjz0b8kgu02y7IfvT9iBIFDju1TbvEAt2G1Euc2mUCuzG9xHVGfqfYVXvWA81pafaZCaXaApVZAyGdg9MVNro32hyctZCTQTdJWe8IWZBT5ACkubPSJld2MkUp76YXYXWv4AzZADyTAKnZCnzr1x76j7VvGxZBL&limit=25&until=1408241916&__paging_token=enc_AdCvU0X1xvXrY23dW8hZAfwJUaK9CYJxAi5w1nNCFyjYB2oeKnZC372WTDDuYxKMI2iefBTtq69iYH5MBhZCHZADGd9g"
	insert_query = """INSERT INTO scratch.fb_messages (created_time, name, message)
		VALUES """

	page_count = 0
	while True:
		page_count += 1
		if page_count % 50 == 0:
			print 'Inserted %s pages' % page_count

		try:
			response = requests.get(url).json()

			messages = response.get('data')
			msg_tuples = [
				(m['created_time'], m['from']['name'], m.get('message'))
				for m in messages if m.get('message')
			]

			values_str = ','.join(cur.mogrify("%s", (tuple(row),)) for row in msg_tuples)
			cur.execute(insert_query + values_str)

			url = response.get('paging').get('next')
		except:
			tb.print_exc()
			raise

if __name__ == '__main__':
	main()
