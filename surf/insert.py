from datetime import date

from database import User, RolesUsers, Role, User, Room, Event, Blog, Checkout, Contact, db_session, init_db, Base, engine, db_session
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore, roles_required


# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = db_session()

user_datastore = SQLAlchemySessionUserDatastore(session,
										User, Role)

#user = User(email='aaa@aaa.aa', password='passpass')
user = User(username='ayman', email='sss@sss.ss', password='passpass')
user1 = User(username='anas',email='svv@sss.ss', password='passpass')

user2 = User(username='ahmad',email='sezs@sss.ss', password='passpass')
user3 = User(username='said',email='vvv@sss.dd', password='passpass')

session.add(user)
session.add(user1)
session.add(user2)
session.add(user3)

print("Users Done :)")

######################

cnt1 = Contact(name='wassim', mail='pspp@sss.ss', sub='I want to check in ..', msg='qsdjqksldqsdkqsdlkqsdqsd')
cnt2 = Contact(name='ayman', mail='ksss@sss.ss', sub='I want your help ..', msg='qsdjqksldqsdkqsdlkqsdqsd')
cnt3 = Contact(name='wassim', mail='b6hh@sss.ss', sub='can you help me ..', msg='qsdjqksldqsdkqsdlkqsdqsd')
cnt4 = Contact(name='asaad', mail='abidd@sss.ss', sub='best sales in surf', msg='qsdjqksldqsdkqsdlkqsdqsd')

session.add(cnt1)
session.add(cnt2)
session.add(cnt3)
session.add(cnt4)
print("Contacts Done :)")

##########################################################"""

post1 = Blog(title='Best day with surf hotel fammily', body='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', tags='qqskldqlksdjklqsdj', img_off='klqjdlkqjskdqsldk')
post2 = Blog(title='Surf time in imsouan', body='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', tags='qqskldqlksdjklqsdj', img_off='klqjdlkqjskdqsldk')
post3 = Blog(title='Tamraght summer vlog', body='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', tags='qqskldqlksdjklqsdj', img_off='klqjdlkqjskdqsldk')
post4 = Blog(title='Night party with surf hotel family', body='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', tags='qqskldqlksdjklqsdj', img_off='klqjdlkqjskdqsldk')



session.add(post1)
session.add(post2)
session.add(post3)
session.add(post4)

print("Posts Done :)")


##############################################################

act1 = Event(title='Birthday of the  surf hotel', description='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', home_img='that just for test', tags='qsjhjdqsdq')
act2 = Event(title='Event test33333', description='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', home_img='that just for test', tags='qsjhjdqsdqddd')
act3 = Event(title='Event trial version test', description='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', home_img='that just for test', tags='qsjhjdssqsdq')
act4 = Event(title='Best places of tamraght', description='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', home_img='that just for test', tags='qsjhjdqsdqde')

session.add(act1)
session.add(act2)
session.add(act3)
session.add(act4)
print("Events Done :)")


##########################################################################################

ch1 = Checkout(fullname='Reda adriano', email='ddd@.ddd.dd', city='angola', state='loop', phone='9767554887', zipcode='98hhzae', addr='zeiozrez')
ch2 = Checkout(fullname='Salman kaa', email='sss@.sss.dd', city='ghana', state='dakar', phone='9767554887', zipcode='98hhzae', addr='zeiozrez')
ch3 = Checkout(fullname='Naoufel ali', email='ooo@.ooo.dd', city='france', state='paris', phone='9767554887', zipcode='98hhzae', addr='zeiozrez')
ch4 = Checkout(fullname='Samir kamal', email='xxx@.xxx.dd', city='turkey', state='istanbul', phone='9767554887', zipcode='98hhzae', addr='zeiozrez')


session.add(ch1)
session.add(ch2)
session.add(ch3)
session.add(ch4)
print("Checkouts Done :)")



###################################

r1 = Room(title='Junior Suit', description='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', price='400', mode='CLOSED', home_img='http://127.0.0.1:5000/static/img/room/r2/Room-1_1.jpg', img1_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_1.jpg', img2_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_1.jpg', img3_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_1.jpg', capacity='5')
r2 = Room(title='Sinior Suit', description='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', price='700', mode='CLOSED', home_img='http://127.0.0.1:5000/static/img/room/r2/Room-1_3.jpg', img1_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_3.jpg', img2_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_3.jpg', img3_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_3.jpg', capacity='8')
r3 = Room(title='Extra large Suit', description='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', price='160', mode='OPENED', home_img='http://127.0.0.1:5000/static/img/room/r2/Room-1_1.jpg', img1_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_1.jpg', img2_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_1.jpg', img3_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_1.jpg', capacity='5')
r4 = Room(title='Simple bad', description='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', price='87', mode='OPENED', home_img='http://127.0.0.1:5000/static/img/room/r2/Room-1_2.jpg', img1_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_2.jpg', img2_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_2.jpg', img3_url='http://127.0.0.1:5000/static/img/room/r2/Room-1_2.jpg', capacity='2')


session.add(r1)
session.add(r2)
session.add(r3)
session.add(r4)
print("Rooms Done :)")

session.commit()

session.close()

print("The Unitest Worky Seccussfly :)")

print("All Is Done ! :)")