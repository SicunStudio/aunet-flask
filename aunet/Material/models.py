#--coding:UTF-8--
from .. import db
        
class Base(object):
    '''the base of all the apply tables'''
    id = db.Column(db.INT,primary_key = True)
    apply_time = db.Column(db.TIMESTAMP)
    approve_time = db.Column(db.TIMESTAMP,nullable = True)
    result = db.Column(db.CHAR(1),default = '0',nullable = False)
    applicant = db.Column(db.String(10),nullable = False)
    advice = db.Column(db.String(20))
    pre_verify = db.Column(db.String(20))
    is_print = db.Column(db.CHAR(1))
    filename = db.Column(db.VARCHAR(50))

    association = db.Column(db.String(10),nullable = False)
    tel = db.Column(db.String(15))
    date = db.Column(db.DATE)
    site = db.Column(db.String(10))


    
class Base1(object):
    '''the base of east4,outdoor,sacenter,special'''
    activity = db.Column(db.String(15))
    number = db.Column(db.SMALLINT)
    sponsor = db.Column(db.TEXT)
    opinion = db.Column(db.String(10))
    content = db.Column(db.TEXT)
    resp_person = db.Column(db.String(10),nullable = False)
    time = db.Column(db.String(5))

class East4(db.Model,Base,Base1):
    '''model of east4'''
    __tablename__ = 'material_east4'
    site = None


class Outdoor(db.Model,Base,Base1):
    '''model of outdoor'''
    __tablename__ = 'material_outdoor'
    

class Sacenter(db.Model,Base,Base1):
    '''model of student activity center'''
    __tablename__ = 'material_sacenter'
    is_query = db.Column(db.CHAR(1))
    site_type = db.Column(db.CHAR(1))

class Special(db.Model,Base,Base1):
    '''model of special'''
    __tablename__ = 'material_special'
    is_query = db.Column(db.CHAR(1))


class Colorprint(db.Model,Base):
    '''model of colorprint'''
    __tablename__ = 'material_colorprint'
    is_sponsor = db.Column(db.CHAR(1))
    remark = db.Column(db.TEXT)
    time = db.Column(db.String(5))
    content = db.Column(db.TEXT)
    resp_person = db.Column(db.String(10),nullable = False)

class Sports(db.Model,Base):
    '''model of sports'''
    __tablename__ = 'material_sports'
    school_id = db.Column(db.String(10))
    remark = db.Column(db.TEXT)
    time = db.Column(db.String(5))
    resp_person = db.Column(db.String(10),nullable = False)
    department = db.Column(db.String(15))
    content = db.Column(db.TEXT)


class Materials(db.Model,Base):
    '''model of material'''
    __tablename__ = 'material_material'
    resp_person = db.Column(db.String(10),nullable = False)
    activity = db.Column(db.String(15))
    opinion = db.Column(db.String(20))
    projector_date = db.Column(db.DATE)
    projector_num = db.Column(db.SMALLINT)
    chair_date = db.Column(db.DATE)
    electricity_num = db.Column(db.SMALLINT)
    desk_num = db.Column(db.SMALLINT)
    chair_num = db.Column(db.SMALLINT)
    trans_desk_num = db.Column(db.SMALLINT)
    trans_chair_num = db.Column(db.SMALLINT)


class Teachingbuilding(db.Model,Base):
    '''model of teachingbuilding'''
    __tablename__ = 'material_teachingbuilding'
    content = db.Column(db.TEXT())
    activity = db.Column(db.String(15))
    signature = db.Column(db.String(10))
    capacity = db.Column(db.SMALLINT)
    number = db.Column(db.SMALLINT)
    week = db.Column(db.String(5))
    person_type = db.Column(db.CHAR(5))
    function = db.Column(db.CHAR(5))
    phone = db.Column(db.String(15))
    section = db.Column(db.CHAR(5))
    activity_type = db.Column(db.CHAR(1))
    host = db.Column(db.String(10))
    unit = db.Column(db.String(20))
    title = db.Column(db.String(10))
    resp_person = db.Column(db.String(10),nullable = False)