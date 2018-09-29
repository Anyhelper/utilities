import psycopg2 
"""
this is a script to query the aa.aa_message database structured as follows:
[('openid', 'character varying'), ('worker', 'character varying'), ('message_type', 'character varying'), ('message_content', 'text'), ('occur_time', 'timestamp without time zone'), ('id', 'uuid'), ('opercode', 'integer'), ('oid', 'integer'), ('chat_time', 'character varying'), ('username', 'character varying')]
"""

def loadQuestionFilteredBy( string ):
    """
    :string, this is the filter for the DB query
    :rtype, list of (string,)
    REQUIRED:
    - psycopg2 dependency
    - password to access DB
    """
    try:
        conn = psycopg2.connect("dbname='anyhelper' user='postgres' host='115.159.86.101' password=password")
    except Exception as e:
        print e
    cur = conn.cursor()
    try:
        cur.execute("""select message_content from aa.aa_message where message_content like '%{}%' order by chat_time""".format(string))
        res = cur.fetchall()
    except Exception as e:
        print e
    conn.commit()
    return res

