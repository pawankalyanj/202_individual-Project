import psycopg2
CONNECTION = "postgres://tsdbadmin:AVNS_qdv_vgOhhiXe9T2@tsdb-206531ac-sjsu-0c73.a.timescaledb.io:16433/defaultdb?sslmode=require"
conn=None
def main():  
    conn = psycopg2.connect(CONNECTION)
    cursor = conn.cursor()
    # use the cursor to interact with your database
    cursor.execute("SELECT 'hello world'")
    print(cursor.fetchone())