from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


class DB(object):
	"""Initialize mysql database """
	host = "nozomi.proxy.rlwy.net"
	user = "root"
	password = "eFueqEYTZzHZxYenNYfZrLzeGplLnsoW"
	db = "railway"
	table = ""

	def __init__(self, app):
		app.config["MYSQL_DATABASE_HOST"] = self.host;
		app.config["MYSQL_DATABASE_USER"] = self.user;
		app.config["MYSQL_DATABASE_PASSWORD"] = self.password;
		app.config["MYSQL_DATABASE_DB"] = self.db;
		app.config['MYSQL_DATABASE_HOST'] = 'nozomi.proxy.rlwy.net';
		app.config['MYSQL_DATABASE_PORT'] = 47310;

		self.mysql = MySQL(app, cursorclass=DictCursor)

	def cur(self):
		return self.mysql.get_db().cursor()

	def query(self, q):
		h = self.cur()
	
		if (len(self.table)>0):
			q = q.replace("@table", self.table)

		h.execute(q)

		return h

	def commit(self):
		self.query("COMMIT;")