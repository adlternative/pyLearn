from database import Database


def test_insert(something1,something2,something3,something4):
    db = Database()
    try:
        # querySql = "select * from `messages` where text='"+something+"'"
        # querySql =("select * from `messages` where text='%s'"%something)
        # chanels = db.query(querySql)
        # print(type(something3))
        preUpdateSql="update `messages`set subject=%s,sender=%s,reply_to=%s,text=%s where id =3"
        db.insert(preUpdateSql,[something1,something2,something3,something4])
        # return chanels
    except Exception as e:
        print(e)

if __name__ == '__main__':
  print("select admin from users where username = '%s'" % "'; select true; --")
# select admin from users where username = ''; select true; --'


