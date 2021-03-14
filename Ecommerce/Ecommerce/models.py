'''
    Shopping Project Database
    -----------------------------------------------------------------
    Database Model For Shopping Site
    author : Nitesh Kumar Niranjan <niteshkumarniranjan@gmail.com>
'''

import datetime

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from peewee import *
from playhouse.migrate import SqliteMigrator
import uuid
import translators as ts

# Default database
DATABASE = SqliteDatabase('shop.db')
migrator = SqliteMigrator(DATABASE)


# User Table
class User(UserMixin, Model):
    """App Users Table"""
    full_name = CharField()
    email = CharField(unique=True)
    password = CharField(max_length=100)
    mobile_no = CharField()
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)


    class Meta:
        database = DATABASE
  
    @classmethod
    def create_user(cls, full_name, email, password, mobile_no, admin=False):
        try:
            cls.create(
                full_name = full_name,
                email = email,
                password = generate_password_hash(password),
                mobile_no = mobile_no,
                is_admin = admin
            )
        except IntegrityError:
            raise ValueError("User already exists")

class Category(Model):
    id = IntegerField(null=False)
    categoryName = CharField()
    categoryID = IntegerField(null=False)
    isSub = IntegerField(null=False)

    class Meta:
        database = DATABASE
    
    @classmethod
    def create_category(cls, categoryName, categoryID):
        try:
            cls.create(
                categoryName = categoryName,
                categoryID = categoryID,
                isSub = 0
            )
        except IntegrityError:
            raise ValueError("Category already exists")

    @property
    def serialize(self):
        return (self.id , self.categoryName)
    @property
    def lineformat(self):
        return {
             'id' : self.id,
             'categoryName': self.categoryName,
             'categoryID':self.categoryID,
             'isSub':self.isSub
            }

class Product(Model):
    """Products Table"""
    name = CharField()
    title = CharField()
    image_1 = CharField()
    image_2 = CharField()
    image_3 = CharField()
    count = IntegerField()
    actual_price = IntegerField()
    off_percent = IntegerField()
    buy_price = IntegerField()
    features = CharField()
    other_details = TextField()
    overview_eng = TextField()
    overview_de = TextField() 
    category_num = IntegerField(null=False)
    published_at = DateTimeField(default=datetime.datetime.now)


    class Meta:
        database = DATABASE
        order_by = ('-published_at',)
    
    @property
    def serialize(self):
        return self

    @property
    def lineformat(self):
        return {
            'name': self.name,
            'title' : self.title,
            'image_1' : self.image_1,
            'image_2' : self.image_2,
            'image_3' : self.image_3,
            'count' : self.count,
            'actual_price' : self.actual_price,
            'off_percent' : self.off_percent,
            'buy_price' : self.buy_price,
            'features' : self.features,
            'other_details' : self.other_details,
            'overview_eng' : self.overview_eng,
            'overview_de' : self.overview_de, 
            'category_num' : self.category_num
            }

    @classmethod
    def add_product(cls, name, image_1, image_2, image_3, count, actual_price, off_percent, buy_price, 
                            features, other_details, overview_eng, overview_de, category_num):
        #try:
            _title = name.replace(" ", "_").lower()
            cls.create(
                name = name, 
                title = _title,
                image_1 = image_1, 
                image_2 = image_2, 
                image_3 = image_3,
                count = count,
                actual_price = actual_price, 
                off_percent = off_percent, 
                buy_price = buy_price, 
                features = features,  
                other_details = other_details,
                overview_eng = overview_eng,
                overview_de = overview_de,
                category_num = category_num,
            )
        #except IntegrityError:
        #    raise ValueError("Some Error Happened")


class Comment(Model):
    user = ForeignKeyField(User, related_name='user_comment')
    product = ForeignKeyField(Product, related_name='products_comment')
    text = TextField()
    rating = IntegerField()
    comment_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

    @classmethod
    def add_comment(cls, user, product, text, rating):
        try:
            cls.create(
                user = user,
                product = product, 
                text = text,
                rating = rating
            )
        except IntegrityError :
            raise ValueError("Some Error Happened")

class Cart(Model):
    user_email = ForeignKeyField(User, related_name='carts')
    product_id = ForeignKeyField(Product, related_name='products')
    count = IntegerField()
    
    class Meta:
        database = DATABASE

    @classmethod
    def add_product(cls, user_email_id, product_id_id, count=1):
        try:
            cls.create(
                user_email_id=user_email_id,
                product_id_id=product_id_id,
                count=count
            )
        except IntegrityError:
            raise ValueError("Some Error Happened")

    



class BuyHistory(Model):
    """Item Buying History"""
    order_id = CharField(max_length=50, unique=True)
    product_id = ForeignKeyField(Product, related_name='product')
    buyer = ForeignKeyField(User, related_name='customer')
    product_name = CharField()
    buyer_name = CharField()
    mobile_no = IntegerField()
    payment_option = CharField()
    product_quantity = IntegerField()
    buyer_address = TextField()
    buy_time = DateTimeField(default=datetime.datetime.now)
    status = CharField()
    delivered = BooleanField()
    deliverTime = DateTimeField(null = True, default = datetime.datetime.now)


    class Meta:
        database = DATABASE
        order_by = ('buy_time',)
    
    @classmethod
    def add_history(cls, buyer, product_id, product_name, product_quantity, buyer_name, buyer_address, mobile_no, payment_option, status="Initiated", delivered=False):
        cls.create(
            order_id = str(uuid.uuid4()),
            buyer = buyer,
            product_id = product_id,
            product_name = product_name,
            product_quantity = product_quantity,
            buyer_name = buyer_name,
            buyer_address = buyer_address,
            mobile_no = mobile_no,
            payment_option = payment_option,
            status = status,
            delivered=delivered
        )


class Review(Model):
    user = CharField()
    order_id = CharField()
    text = TextField()
    comment_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE
    
    @classmethod
    def add_review(cls, user, order_id, text):
        try:
            cls.create(
                user = user,
                order_id = order_id, 
                text = text
            )
        except IntegrityError :
            raise ValueError("Some Error Happened")

class Banner(Model):
    link = CharField()

    class Meta:
        database = DATABASE

    @classmethod
    def add_banner(cls, link):
        try:
            cls.create(
                link = link,
            )
        except IntegrityError :
            raise ValueError("Some Error Happened")

class Localization(Model):
    id = IntegerField()
    search = TextField()
    searchp = TextField()
    wiasi = TextField()
    wiasidesc = TextField()
    aboutus = TextField()
    returnpolicy = TextField()
    contactus = TextField()
    account = TextField()
    signin = TextField()
    signout = TextField()
    profile = TextField()
    dashboard = TextField()
    logout = TextField()
    changepass = TextField()
    email = TextField()
    password = TextField()
    donthave = TextField()
    forgotpass = TextField()
    fillname = TextField()
    confirmpass = TextField()
    mobileno = TextField()
    allreadyhave = TextField()
    login = TextField()
    register = TextField()
    overview = TextField()
    detales = TextField()
    addreview = TextField()
    reviewcaption = TextField()
    submit = TextField()
    nocards = TextField()
    seegal = TextField()
    avail = TextField()
    notavail = TextField()
    features = TextField()
    errorlog = TextField()
    error = TextField()
    successlog = TextField()
    success = TextField()

    class Meta:
        database = DATABASE

    @classmethod
    def translate(self,element, leng):
        text = element.search + '|' + element.searchp + '|' + element.wiasi + '|' + element.wiasidesc + '|' + element.aboutus + '|' + element.returnpolicy + '|' + element.contactus + '|' + element.account + '|' + element.signin + '|' + element.signout + '|' + element.profile + '|' + element.dashboard + '|' + element.logout + '|'  + element.changepass + '|'  + element.email + '|'  + element.password + '|'  + element.donthave + '|'  + element.forgotpass + '|' + element.fillname + '|'   + element.confirmpass + '|'  + element.mobileno + '|'   + element.allreadyhave + '|'  + element.login + '|'  + element.register + '|'  + element.overview + '|'   + element.detales + '|'   + element.addreview + '|'  + element.reviewcaption + '|' + element.submit + '|' + element.nocards  + '|' + element.seegal + '|' + element.avail + '|' + element.notavail + '|' + element.features + '|' + element.errorlog + '|' + element.error + '|' + element.successlog + '|' + element.success 
        text = ts.bing(text, if_use_cn_host=False, to_language = leng)
        len = []
        len = list(text.split('|'))
        element.search = len[0]
        element.searchp = len[1]
        element.wiasi = len[2]
        element.wiasidesc = len[3]
        element.aboutus = len[4]
        element.returnpolicy = len[5]
        element.contactus = len[6]
        element.account = len[7]
        element.signin = len[8]
        element.signout = len[9]
        element.profile = len[10]
        element.dashboard = len[11]
        element.logout = len[12]
        element.changepass = len[13]
        element.email = len[14]
        element.password = len[15]
        element.donthave = len[16]
        element.forgotpass = len[17]
        element.fillname = len[18]
        element.confirmpass = len[19]
        element.mobileno = len[20]
        element.allreadyhave = len[21]
        element.login = len[22]
        element.register = len[23]
        element.overview = len[24]
        element.detales = len[25]
        element.addreview = len[26]
        element.reviewcaption = len[27]
        element.submit = len[28]
        element.nocards = len[29]
        element.seegal = len[30]
        element.avail = len[31]
        element.notavail = len[32]
        element.features = len[33]
        element.errorlog = len[34]
        element.error = len[35]
        element.successlog = len[36]
        element.success = len[37]
        return element

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Category, Product, Cart, BuyHistory, Comment, Review, Banner], safe=True)
    DATABASE.close()

