import cx_Oracle 
import jaydebeapi



lib_dir = "/Users/wannagohome/instantclient_19_8/"
wallet_location = "/Users/wannagohome/instantclient_19_8/network/admin/Wallet_seonyu.zip"

cx_Oracle.init_oracle_client(lib_dir)
username='ADMIN'
password = '@@Drunken0878'
jdbc_driver_loc = "/Library/Java/Extensions/ojdbc8/ojdbc8.jar"

#  jdbc:oracle:thin:@데이터베이스 이름_medium?TNS_ADMIN=/전자지갑경로/Wallet_데이터베이스 이름/
jdbc ='jdbc:oracle:thin:@seonyu_high?TNS_ADMIN=//Users/wannagohome/instantclient_19_8/network/admin/Wallet_seonyu'

jdbc_class ="oracle.jdbc.driver.OracleDriver"

conn = jaydebeapi.connect(jdbc_class,jdbc,[username, password],jdbc_driver_loc)


cs = conn.cursor()

sql ='select * from moka'
cs.execute(sql)
print(cs.fetchall())

cs.close()
conn.close()