import psycopg2 
def util_DropCreateTable():
    """
    this is an old utility used to create/drop tables, it can be used as an example to reuse when necessary
    REQUIRED:
    - psycopg2 as depency
    - password to access DB
    """
    try:
        conn = psycopg2.connect("dbname='anyhelper' user='postgres' host='115.159.86.101' password=password")
    except Exception as e:
        print e

    cur = conn.cursor()

    try:
        #cur.execute("""DROP TABLE aa.aa_wj_tk""")
        cur.execute("""CREATE TABLE aa.pp_comment_image (
        id UUID DEFAULT newid() PRIMARY KEY,
        comment VARCHAR(255),
        imgurl VARCHAR(255),
        service VARCHAR(255)
        );""")
    except Exception as e:
        print e

    conn.commit()

    conn.close()


def util_AlterTable():
    """
    this is an old utility used to alter tables, it can be used as an example to reuse when necessary
    REQUIRED:
    - psycopg2 as depency
    - password to access DB
    """
    try:
        conn = psycopg2.connect("dbname='anyhelper' user='postgres' host='115.159.86.101' password=password")
    except Exception as e:
        print e

    cur = conn.cursor()

    try:
       #cur.execute("""ALTER TABLE aa.pp_answers ALTER COLUMN link TYPE text""")
       #cur.execute("""ALTER TABLE aa.pp_questions RENAME COLUMN headimgurl2 TO testing""")
       #cur.execute("""ALTER TABLE aa.pp_comment ADD COLUMN link_type INTEGER DEFAULT 0""")
       #cur.execute("""ALTER TABLE aa.pp_comment ADD COLUMN verified INTEGER DEFAULT 0""")
       #cur.execute("""UPDATE aa.pp_user SET freak = freak + 1 WHERE id = '6bff2306-0fd0-44cc-bbb5-06667c831e0b'""")
       cur.execute("""ALTER TABLE aa.pp_comment_image ADD COLUMN ctime TIMESTAMP""")
       #cur.execute("""select * from aa.pp_questions order by upvotes desc,id desc limit 10 offset 0""")
       #cur.execute("""ALTER TABLE aa.pp_user RENAME COLUMN level TO contributions""")
       #cur.execute(""" SELECT * FROM aa.pp_upvote WHERE hunter_id = '6bfddf4f-9c47-4b4e-ba9f-6a987ede175c' ORDER BY otime DESC LIMIT 3""")
       #cur.execute(""" SELECT name FROM aa.pp_service WHERE hunter_id = '6bff2306-0fd0-44cc-bbb5-06667c831e0b'""")
       #cur.execute("""update aa.pp_answers set upvotes=1 where upvotes=0 """)
       #cur.execute(""" INSERT INTO aa.pp_service (name, description, ctime, comment_number, upvoters_number, hunter_id) VALUES ('UPLOAD TEST 3','descrption test', current_timestamp, 0, 6,'bd4a6f83-3ec4-4ba0-83b9-d193542ee0f1','http://cdn.anyhelper.cn/www/76835a47-83d0-411d-8800-7dcc2fc24d83c.jpg' ); """)
       #cur.execute("""select * from aa.pp_answers where question='1abfe3ef-3dde-477f-93ff-28ae5c579510'""")
       #cur.execute("""update aa.pp_questions set description = 'testing' where id='7814d5d5-228e-493f-852a-669c1e675951'""")/
       #cur.execute("""select * from aa.pp_answers where question='596ca2a6-1d90-4135-b449-303ed8d2dc47' order by upvotes desc limit 3""")
       #cur.execute("""SELECT * FROM aa.pp_user WHERE id = '6bff2306-0fd0-44cc-bbb5-06667c831e0b' OR id = '6bfddf4f-9c47-4b4e-ba9f-6a987ede175c'  OR id= 'f8d28fe3-2f22-4717-bd0d-9913309ea283' ORDER BY upvotes""")
       #cur.execute("""select * from aa.pp_user where challenge=1 order by upvotes desc""")
       #cur.execute("""SELECT tag FROM aa.pp_questions WHERE id = '38d371ff-6694-4f0d-a36c-51bab51e8ee6' """)
       #cur.execute("""INSERT INTO aa.pp_service (id,name, ctime, comment_number, upvoters_number, hunter_id, cdnurl,profilephoto,tags_name,tags, reason) VALUES ('52c13727-076f-4017-8097-fd4c4eaf9049','ying yang', current_timestamp, 0, 0,'e544cfe6-b2dd-4247-9825-4b197fba4b13','http://cdn.anyhelper.cn/www/2be4af27-abd0-419c-a700-5a6585ab9bf8.png','/2018/2be4af27-abd0-419c-a700-5a6585ab9bf8.png','Food','Food','This Shanghai authentic place allows you to bring your own stuff and spark it with a nice glass of dry Macallan 18yrs the decoration is very communist looking but its all about the vibe Very cool definitely a go to place to meet and discuss with smokers and random nice people '); """)
       #cur.execute("""select * from aa.pp_questions order by ctime desc limit 30 offset 0""")
       #cur.execute("""INSERT INTO aa.pp_user_preferences (id,user_id,cat) VALUES ('asdasd','asdasd','asdasd') """)
       #cur.execute("""select * from aa.pp_questions q1 JOIN aa.pp_question_follows q2 ON q1.id=q2.question_id WHERE q2.follower_id='ba474e0d-1902-4c8c-8898-a2daea3c2126' """)
       #cur.execute("""update aa.pp_service set description='' where description='add your description here...'""")
       #res = cur.fetchall()
    except Exception as e:
        print e

    #print res

    conn.commit()

     

