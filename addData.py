from datetime import datetime

from aunet.Home.models import News,AdvanceNotice,StarAssociation,CharmAssociation,AssociationTag
from aunet import db

	
# a=AdvanceNotice("<body>hello</body>","1","1","/static/1.jpg")
# b=AdvanceNotice("<body>hello</body>","1","1","/static/1.jpg")
# c=AdvanceNotice("<body>hello</body>","1","1","/static/1.jpg")
# d=AdvanceNotice("<body>hello</body>","1","1","/static/1.jpg")
# e=AdvanceNotice("<body>hello</body>","1","1","/static/1.jpg")

# db.session.add(a)
# db.session.add(b)
# db.session.add(c)
# db.session.add(d)
# db.session.add(e)

# db.session.commit()

# a1=StarAssociation("StarAssociationer","lihua","/static/1.jpg","哈哈哈")
# b1=StarAssociation("StarAUer","lihua","/static/1.jpg","哈哈哈")
# c1=StarAssociation("StarTeacher","lihua","/static/1.jpg","哈哈哈")

# db.session.add(a1)
# db.session.add(b1)
# db.session.add(c1)

# db.session.commit()

# a2=CharmAssociation("思存工作室","/static/1.jpg")
# b2=AssociationTag("五星社团",a2)

# db.session.add(a2)
# db.session.add(b2)

# db.session.commit()

# a=News("PinPai","<body>hello</body>","2","2jaja","/static/1.jpg")
# b=News("CharmHust","<body>hello</body>","2","2jaja","/static/1.jpg")
 

# db.session.add(a)
# db.session.add(b)
# db.session.commit()
#news_Category,news_Detail,news_Title,news_Outline,news_Img_Url
a=News("News","<body>hello</body>","2","hello world","/static/1.jpg")
b=News("News","<body>hello</body>","2","hello world","/static/1.jpg")
c=News("News","<body>hello</body>","2","hello world","/static/1.jpg")
d=News("News","<body>hello</body>","2","hello world","/static/1.jpg")
e=News("News","<body>hello</body>","2","hello world","/static/1.jpg")
db.session.add(a)
db.session.add(b)
db.session.add(c)
db.session.add(d)
db.session.add(e)

db.session.commit()