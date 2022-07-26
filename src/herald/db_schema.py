# Author Julien Le Bourg for DAOR project

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, ForeignKey, ForeignKeyConstraint, Integer, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = Base.metadata



class Abilitytypes(Base):
    __tablename__ = 'abilitytypes'

    abilitytypeid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('abilitytypes_abilitytypeid_seq'::regclass)"))
    abilitytypename = Column(String(50), nullable=False)
    customerguid = Column(UUID, primary_key=True, nullable=False)

    abilities = relationship('Abilities', back_populates='abilitytypes')


class Areaofinteresttypes(Base):
    __tablename__ = 'areaofinteresttypes'

    areaofinteresttypeid = Column(Integer, primary_key=True, server_default=text("nextval('areaofinteresttypes_areaofinteresttypeid_seq'::regclass)"))
    areaofinteresttypedesc = Column(String(50), nullable=False)


class Areasofinterest(Base):
    __tablename__ = 'areasofinterest'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    areasofinterestguid = Column(UUID, primary_key=True, nullable=False)
    mapzoneid = Column(Integer, nullable=False)
    areaofinterestname = Column(String(50), nullable=False)
    radius = Column(Float(53), nullable=False)
    areaofinteresttype = Column(Integer, nullable=False)
    x = Column(Float(53))
    y = Column(Float(53))
    z = Column(Float(53))
    rx = Column(Float(53))
    ry = Column(Float(53))
    rz = Column(Float(53))
    customdata = Column(Text)


class Charabilitybars(Base):
    __tablename__ = 'charabilitybars'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    charabilitybarid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('charabilitybars_charabilitybarid_seq'::regclass)"))
    characterid = Column(Integer, nullable=False)
    abilitybarname = Column(String(50), nullable=False, server_default=text("''::character varying"))
    maxnumberofslots = Column(Integer, nullable=False, server_default=text('1'))
    numberofunlockedslots = Column(Integer, nullable=False, server_default=text('1'))
    charabilitybarscustomjson = Column(Text)

    charabilitybarabilities = relationship('Charabilitybarabilities', back_populates='charabilitybars')


class Charinventory(Base):
    __tablename__ = 'charinventory'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    characterid = Column(Integer, primary_key=True, nullable=False)
    charinventoryid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('charinventory_charinventoryid_seq'::regclass)"))
    inventoryname = Column(String(50), nullable=False)
    inventorysize = Column(Integer, nullable=False)
    inventorywidth = Column(Integer, nullable=False, server_default=text('1'))
    inventoryheight = Column(Integer, nullable=False, server_default=text('1'))


class Charinventoryitems(Base):
    __tablename__ = 'charinventoryitems'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    charinventoryid = Column(Integer, primary_key=True, nullable=False)
    charinventoryitemid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('charinventoryitems_charinventoryitemid_seq'::regclass)"))
    itemid = Column(Integer, nullable=False)
    inslotnumber = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    numberofusesleft = Column(Integer, nullable=False, server_default=text('0'))
    condition = Column(Integer, nullable=False, server_default=text('100'))
    charinventoryitemguid = Column(UUID, nullable=False, server_default=text('gen_random_uuid()'))
    customdata = Column(Text)


class Charonmapinstance(Base):
    __tablename__ = 'charonmapinstance'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    characterid = Column(Integer, primary_key=True, nullable=False)
    mapinstanceid = Column(Integer, primary_key=True, nullable=False)


class Chatgroups(Base):
    __tablename__ = 'chatgroups'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    chatgroupid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('chatgroups_chatgroupid_seq'::regclass)"))
    chatgroupname = Column(String(50), nullable=False)


class Chatgroupusers(Base):
    __tablename__ = 'chatgroupusers'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    chatgroupid = Column(Integer, primary_key=True, nullable=False)
    characterid = Column(Integer, primary_key=True, nullable=False)


class Chatmessages(Base):
    __tablename__ = 'chatmessages'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    chatmessageid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('chatmessages_chatmessageid_seq'::regclass)"))
    sentbycharid = Column(Integer, nullable=False)
    chatmessage = Column(Text, nullable=False)
    messagedate = Column(DateTime, nullable=False, server_default=text('now()'))
    senttocharid = Column(Integer)
    chatgroupid = Column(Integer)


class Class(Base):
    __tablename__ = 'class'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    classid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('class_classid_seq'::regclass)"))
    classname = Column(String(50), nullable=False, server_default=text("''::character varying"))
    startingmapname = Column(String(50), nullable=False)
    x = Column(Float(53), nullable=False)
    y = Column(Float(53), nullable=False)
    z = Column(Float(53), nullable=False)
    perception = Column(Float(53), nullable=False)
    acrobatics = Column(Float(53), nullable=False)
    climb = Column(Float(53), nullable=False)
    stealth = Column(Float(53), nullable=False)
    rx = Column(Float(53), nullable=False)
    ry = Column(Float(53), nullable=False)
    rz = Column(Float(53), nullable=False)
    spirit = Column(Float(53), nullable=False)
    magic = Column(Float(53), nullable=False)
    teamnumber = Column(Integer, nullable=False)
    thirst = Column(Float(53), nullable=False)
    hunger = Column(Float(53), nullable=False)
    gold = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)
    characterlevel = Column(SmallInteger, nullable=False)
    gender = Column(SmallInteger, nullable=False)
    xp = Column(Integer, nullable=False)
    hitdie = Column(SmallInteger, nullable=False)
    wounds = Column(Float(53), nullable=False)
    size = Column(SmallInteger, nullable=False)
    weight = Column(Float(53), nullable=False)
    maxhealth = Column(Float(53), nullable=False)
    health = Column(Float(53), nullable=False)
    healthregenrate = Column(Float(53), nullable=False)
    maxmana = Column(Float(53), nullable=False)
    mana = Column(Float(53), nullable=False)
    manaregenrate = Column(Float(53), nullable=False)
    maxenergy = Column(Float(53), nullable=False)
    energy = Column(Float(53), nullable=False)
    energyregenrate = Column(Float(53), nullable=False)
    maxfatigue = Column(Float(53), nullable=False)
    fatigue = Column(Float(53), nullable=False)
    fatigueregenrate = Column(Float(53), nullable=False)
    maxstamina = Column(Float(53), nullable=False)
    stamina = Column(Float(53), nullable=False)
    staminaregenrate = Column(Float(53), nullable=False)
    maxendurance = Column(Float(53), nullable=False)
    endurance = Column(Float(53), nullable=False)
    enduranceregenrate = Column(Float(53), nullable=False)
    strength = Column(Float(53), nullable=False)
    dexterity = Column(Float(53), nullable=False)
    constitution = Column(Float(53), nullable=False)
    intellect = Column(Float(53), nullable=False)
    wisdom = Column(Float(53), nullable=False)
    charisma = Column(Float(53), nullable=False)
    agility = Column(Float(53), nullable=False)
    fortitude = Column(Float(53), nullable=False)
    reflex = Column(Float(53), nullable=False)
    willpower = Column(Float(53), nullable=False)
    baseattack = Column(Float(53), nullable=False)
    baseattackbonus = Column(Float(53), nullable=False)
    attackpower = Column(Float(53), nullable=False)
    attackspeed = Column(Float(53), nullable=False)
    critchance = Column(Float(53), nullable=False)
    critmultiplier = Column(Float(53), nullable=False)
    haste = Column(Float(53), nullable=False)
    spellpower = Column(Float(53), nullable=False)
    spellpenetration = Column(Float(53), nullable=False)
    defense = Column(Float(53), nullable=False)
    dodge = Column(Float(53), nullable=False)
    parry = Column(Float(53), nullable=False)
    avoidance = Column(Float(53), nullable=False)
    versatility = Column(Float(53), nullable=False)
    multishot = Column(Float(53), nullable=False)
    initiative = Column(Float(53), nullable=False)
    naturalarmor = Column(Float(53), nullable=False)
    physicalarmor = Column(Float(53), nullable=False)
    bonusarmor = Column(Float(53), nullable=False)
    forcearmor = Column(Float(53), nullable=False)
    magicarmor = Column(Float(53), nullable=False)
    resistance = Column(Float(53), nullable=False)
    reloadspeed = Column(Float(53), nullable=False)
    range = Column(Float(53), nullable=False)
    speed = Column(Float(53), nullable=False)
    silver = Column(Integer, nullable=False)
    copper = Column(Integer, nullable=False)
    freecurrency = Column(Integer, nullable=False)
    premiumcurrency = Column(Integer, nullable=False)
    fame = Column(Float(53), nullable=False)
    alignment = Column(Float(53), nullable=False)
    description = Column(Text)


class Classinventory(Base):
    __tablename__ = 'classinventory'

    classinventoryid = Column(Integer, primary_key=True, server_default=text("nextval('classinventory_classinventoryid_seq'::regclass)"))
    customerguid = Column(UUID, nullable=False)
    classid = Column(Integer, nullable=False)
    inventoryname = Column(String(50), nullable=False)
    inventorysize = Column(Integer, nullable=False)
    inventorywidth = Column(Integer, nullable=False)
    inventoryheight = Column(Integer, nullable=False)


class Customers(Base):
    __tablename__ = 'customers'

    customerguid = Column(UUID, primary_key=True, server_default=text('gen_random_uuid()'))
    customername = Column(String(50), nullable=False)
    customeremail = Column(String(255), nullable=False)
    enabledebuglogging = Column(Boolean, nullable=False, server_default=text('false'))
    enableautoloopback = Column(Boolean, nullable=False, server_default=text('true'))
    developerpaid = Column(Boolean, nullable=False, server_default=text('false'))
    stripecustomerid = Column(String(50), nullable=False, server_default=text("''::character varying"))
    supportunicode = Column(Boolean, nullable=False, server_default=text('false'))
    createdate = Column(DateTime, nullable=False, server_default=text('now()'))
    noportforwarding = Column(Boolean, nullable=False, server_default=text('false'))
    customerphone = Column(String(20))
    customernotes = Column(Text)
    publisherpaiddate = Column(DateTime)
    freetrialstarted = Column(DateTime)


class Debuglog(Base):
    __tablename__ = 'debuglog'

    debuglogid = Column(Integer, primary_key=True, server_default=text("nextval('debuglog_debuglogid_seq'::regclass)"))
    debugdate = Column(DateTime)
    debugdesc = Column(Text)
    customerguid = Column(UUID)


class Globaldata(Base):
    __tablename__ = 'globaldata'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    globaldatakey = Column(String(50), primary_key=True, nullable=False)
    globaldatavalue = Column(Text, nullable=False)


class Items(Base):
    __tablename__ = 'items'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    itemid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('items_itemid_seq'::regclass)"))
    itemtypeid = Column(Integer, nullable=False)
    itemname = Column(String(50), nullable=False)
    itemweight = Column(Numeric(18, 2), nullable=False, server_default=text('0'))
    itemcanstack = Column(Boolean, nullable=False, server_default=text('false'))
    itemstacksize = Column(SmallInteger, nullable=False, server_default=text('0'))
    itemisusable = Column(Boolean, nullable=False, server_default=text('false'))
    itemisconsumedonuse = Column(Boolean, nullable=False, server_default=text('true'))
    customdata = Column(String(2000), nullable=False, server_default=text("''::character varying"))
    defaultnumberofuses = Column(Integer, nullable=False, server_default=text('0'))
    itemvalue = Column(Integer, nullable=False, server_default=text('0'))
    itemmesh = Column(String(200), nullable=False, server_default=text("''::character varying"))
    meshtouseforpickup = Column(String(200), nullable=False, server_default=text("''::character varying"))
    texturetouseforicon = Column(String(200), nullable=False, server_default=text("''::character varying"))
    premiumcurrencyprice = Column(Integer, nullable=False, server_default=text('0'))
    freecurrencyprice = Column(Integer, nullable=False, server_default=text('0'))
    itemtier = Column(Integer, nullable=False, server_default=text('0'))
    itemdescription = Column(Text, nullable=False, server_default=text("''::text"))
    itemcode = Column(String(50), nullable=False, server_default=text("''::character varying"))
    itemduration = Column(Integer, nullable=False, server_default=text('0'))
    canbedropped = Column(Boolean, nullable=False, server_default=text('true'))
    canbedestroyed = Column(Boolean, nullable=False, server_default=text('false'))
    weaponactorclass = Column(String(200), nullable=False, server_default=text("''::character varying"))
    staticmesh = Column(String(200), nullable=False, server_default=text("''::character varying"))
    skeletalmesh = Column(String(200), nullable=False, server_default=text("''::character varying"))
    itemquality = Column(SmallInteger, nullable=False, server_default=text('0'))
    iconslotwidth = Column(Integer, nullable=False, server_default=text('1'))
    iconslotheight = Column(Integer, nullable=False, server_default=text('1'))
    itemmeshid = Column(Integer, nullable=False, server_default=text('0'))


class Itemtypes(Base):
    __tablename__ = 'itemtypes'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    itemtypeid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('itemtypes_itemtypeid_seq'::regclass)"))
    itemtypedesc = Column(String(50), nullable=False)
    useritemtype = Column(SmallInteger, nullable=False, server_default=text('0'))
    equipmenttype = Column(SmallInteger, nullable=False, server_default=text('0'))
    itemquality = Column(SmallInteger, nullable=False, server_default=text('0'))
    equipmentslottype = Column(SmallInteger, nullable=False, server_default=text('0'))


class Mapinstances(Base):
    __tablename__ = 'mapinstances'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    mapinstanceid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('mapinstances_mapinstanceid_seq'::regclass)"))
    worldserverid = Column(Integer, nullable=False)
    mapid = Column(Integer, nullable=False)
    port = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False, server_default=text('0'))
    numberofreportedplayers = Column(Integer, nullable=False, server_default=text('0'))
    createdate = Column(DateTime, nullable=False, server_default=text('now()'))
    playergroupid = Column(Integer)
    lastupdatefromserver = Column(DateTime)
    lastserveremptydate = Column(DateTime)


class Maps(Base):
    __tablename__ = 'maps'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    mapid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('maps_mapid_seq'::regclass)"))
    mapname = Column(String(50), nullable=False)
    width = Column(SmallInteger, nullable=False)
    height = Column(SmallInteger, nullable=False)
    zonename = Column(String(50), nullable=False)
    worldcompcontainsfilter = Column(String(100), nullable=False, server_default=text("''::character varying"))
    worldcomplistfilter = Column(String(200), nullable=False, server_default=text("''::character varying"))
    mapmode = Column(Integer, nullable=False, server_default=text('1'))
    softplayercap = Column(Integer, nullable=False, server_default=text('60'))
    hardplayercap = Column(Integer, nullable=False, server_default=text('80'))
    minutestoshutdownafterempty = Column(Integer, nullable=False, server_default=text('1'))
    mapdata = Column(LargeBinary)


t_owsversion = Table(
    'owsversion', metadata,
    Column('owsdbversion', String(10))
)


class Playergroupcharacters(Base):
    __tablename__ = 'playergroupcharacters'

    playergroupid = Column(Integer, primary_key=True, nullable=False)
    customerguid = Column(UUID, primary_key=True, nullable=False)
    characterid = Column(Integer, primary_key=True, nullable=False)
    dateadded = Column(DateTime, nullable=False, server_default=text('now()'))
    teamnumber = Column(Integer, nullable=False, server_default=text('0'))


class Playergrouptypes(Base):
    __tablename__ = 'playergrouptypes'

    playergrouptypeid = Column(Integer, primary_key=True)
    playergrouptypedesc = Column(String(50), nullable=False)

    playergroup = relationship('Playergroup', back_populates='playergrouptypes')


class Races(Base):
    __tablename__ = 'races'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    raceid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('races_raceid_seq'::regclass)"))
    racename = Column(String(50), nullable=False)


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        UniqueConstraint('customerguid', 'email', 'role'),
    )

    userguid = Column(UUID, primary_key=True, server_default=text('gen_random_uuid()'))
    customerguid = Column(UUID, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    passwordhash = Column(String(128), nullable=False)
    createdate = Column(DateTime, nullable=False, server_default=text('now()'))
    lastaccess = Column(DateTime, nullable=False, server_default=text('now()'))
    role = Column(String(10), nullable=False)

    characters = relationship('Characters', back_populates='users')
    usersessions = relationship('Usersessions', back_populates='users')


class Usersinqueue(Base):
    __tablename__ = 'usersinqueue'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    userguid = Column(UUID, primary_key=True, nullable=False)
    queuename = Column(String(20), primary_key=True, nullable=False)
    joindt = Column(DateTime, nullable=False)
    matchmakingscore = Column(Integer, nullable=False, server_default=text('0'))


t_vrandnumber = Table(
    'vrandnumber', metadata,
    Column('randnumber', Float(53))
)


class Worldservers(Base):
    __tablename__ = 'worldservers'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    worldserverid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('worldservers_worldserverid_seq'::regclass)"))
    serverip = Column(String(50), nullable=False)
    maxnumberofinstances = Column(Integer, nullable=False)
    port = Column(Integer, nullable=False, server_default=text('8181'))
    serverstatus = Column(SmallInteger, nullable=False, server_default=text('0'))
    internalserverip = Column(String(50), nullable=False, server_default=text("''::character varying"))
    startingmapinstanceport = Column(Integer, nullable=False, server_default=text('7778'))
    activestarttime = Column(DateTime)


class Worldsettings(Base):
    __tablename__ = 'worldsettings'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    worldsettingsid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('worldsettings_worldsettingsid_seq'::regclass)"))
    starttime = Column(BigInteger, nullable=False)


class Abilities(Base):
    __tablename__ = 'abilities'
    __table_args__ = (
        ForeignKeyConstraint(['customerguid', 'abilitytypeid'], ['abilitytypes.customerguid', 'abilitytypes.abilitytypeid']),
    )

    customerguid = Column(UUID, primary_key=True, nullable=False)
    abilityid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('abilities_abilityid_seq'::regclass)"))
    abilityname = Column(String(50), nullable=False)
    abilitytypeid = Column(Integer, nullable=False)
    texturetouseforicon = Column(String(200), nullable=False, server_default=text("''::character varying"))
    gameplayabilityclassname = Column(String(200), nullable=False, server_default=text("''::character varying"))
    class_ = Column('class', Integer)
    race = Column(Integer)
    abilitycustomjson = Column(Text)

    abilitytypes = relationship('Abilitytypes', back_populates='abilities')


class Characters(Base):
    __tablename__ = 'characters'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    characterid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('characters_characterid_seq'::regclass)"))
    email = Column(String(256), nullable=False)
    charname = Column(String(50), nullable=False)
    x = Column(Float(53), nullable=False)
    y = Column(Float(53), nullable=False)
    z = Column(Float(53), nullable=False)
    perception = Column(Float(53), nullable=False)
    acrobatics = Column(Float(53), nullable=False)
    climb = Column(Float(53), nullable=False)
    stealth = Column(Float(53), nullable=False)
    lastactivity = Column(DateTime, nullable=False, server_default=text('now()'))
    rx = Column(Float(53), nullable=False, server_default=text('0'))
    ry = Column(Float(53), nullable=False, server_default=text('0'))
    rz = Column(Float(53), nullable=False, server_default=text('0'))
    spirit = Column(Float(53), nullable=False, server_default=text('0'))
    magic = Column(Float(53), nullable=False, server_default=text('0'))
    teamnumber = Column(Integer, nullable=False, server_default=text('0'))
    thirst = Column(Float(53), nullable=False, server_default=text('0'))
    hunger = Column(Float(53), nullable=False, server_default=text('0'))
    gold = Column(Integer, nullable=False, server_default=text('0'))
    score = Column(Integer, nullable=False, server_default=text('0'))
    characterlevel = Column(SmallInteger, nullable=False, server_default=text('0'))
    gender = Column(SmallInteger, nullable=False, server_default=text('0'))
    xp = Column(Integer, nullable=False, server_default=text('0'))
    hitdie = Column(SmallInteger, nullable=False, server_default=text('0'))
    wounds = Column(Float(53), nullable=False, server_default=text('0'))
    size = Column(SmallInteger, nullable=False, server_default=text('0'))
    weight = Column(Float(53), nullable=False, server_default=text('0'))
    maxhealth = Column(Float(53), nullable=False, server_default=text('0'))
    health = Column(Float(53), nullable=False, server_default=text('0'))
    healthregenrate = Column(Float(53), nullable=False, server_default=text('0'))
    maxmana = Column(Float(53), nullable=False, server_default=text('0'))
    mana = Column(Float(53), nullable=False, server_default=text('0'))
    manaregenrate = Column(Float(53), nullable=False, server_default=text('0'))
    maxenergy = Column(Float(53), nullable=False, server_default=text('0'))
    energy = Column(Float(53), nullable=False, server_default=text('0'))
    energyregenrate = Column(Float(53), nullable=False, server_default=text('0'))
    maxfatigue = Column(Float(53), nullable=False, server_default=text('0'))
    fatigue = Column(Float(53), nullable=False, server_default=text('0'))
    fatigueregenrate = Column(Float(53), nullable=False, server_default=text('0'))
    maxstamina = Column(Float(53), nullable=False, server_default=text('0'))
    stamina = Column(Float(53), nullable=False, server_default=text('0'))
    staminaregenrate = Column(Float(53), nullable=False, server_default=text('0'))
    maxendurance = Column(Float(53), nullable=False, server_default=text('0'))
    endurance = Column(Float(53), nullable=False, server_default=text('0'))
    enduranceregenrate = Column(Float(53), nullable=False, server_default=text('0'))
    strength = Column(Float(53), nullable=False, server_default=text('0'))
    dexterity = Column(Float(53), nullable=False, server_default=text('0'))
    constitution = Column(Float(53), nullable=False, server_default=text('0'))
    intellect = Column(Float(53), nullable=False, server_default=text('0'))
    wisdom = Column(Float(53), nullable=False, server_default=text('0'))
    charisma = Column(Float(53), nullable=False, server_default=text('0'))
    agility = Column(Float(53), nullable=False, server_default=text('0'))
    fortitude = Column(Float(53), nullable=False, server_default=text('0'))
    reflex = Column(Float(53), nullable=False, server_default=text('0'))
    willpower = Column(Float(53), nullable=False, server_default=text('0'))
    baseattack = Column(Float(53), nullable=False, server_default=text('0'))
    baseattackbonus = Column(Float(53), nullable=False, server_default=text('0'))
    attackpower = Column(Float(53), nullable=False, server_default=text('0'))
    attackspeed = Column(Float(53), nullable=False, server_default=text('0'))
    critchance = Column(Float(53), nullable=False, server_default=text('0'))
    critmultiplier = Column(Float(53), nullable=False, server_default=text('0'))
    haste = Column(Float(53), nullable=False, server_default=text('0'))
    spellpower = Column(Float(53), nullable=False, server_default=text('0'))
    spellpenetration = Column(Float(53), nullable=False, server_default=text('0'))
    defense = Column(Float(53), nullable=False, server_default=text('0'))
    dodge = Column(Float(53), nullable=False, server_default=text('0'))
    parry = Column(Float(53), nullable=False, server_default=text('0'))
    avoidance = Column(Float(53), nullable=False, server_default=text('0'))
    versatility = Column(Float(53), nullable=False, server_default=text('0'))
    multishot = Column(Float(53), nullable=False, server_default=text('0'))
    initiative = Column(Float(53), nullable=False, server_default=text('0'))
    naturalarmor = Column(Float(53), nullable=False, server_default=text('0'))
    physicalarmor = Column(Float(53), nullable=False, server_default=text('0'))
    bonusarmor = Column(Float(53), nullable=False, server_default=text('0'))
    forcearmor = Column(Float(53), nullable=False, server_default=text('0'))
    magicarmor = Column(Float(53), nullable=False, server_default=text('0'))
    resistance = Column(Float(53), nullable=False, server_default=text('0'))
    reloadspeed = Column(Float(53), nullable=False, server_default=text('0'))
    range = Column(Float(53), nullable=False, server_default=text('0'))
    speed = Column(Float(53), nullable=False, server_default=text('0'))
    silver = Column(Integer, nullable=False, server_default=text('0'))
    copper = Column(Integer, nullable=False, server_default=text('0'))
    freecurrency = Column(Integer, nullable=False, server_default=text('0'))
    premiumcurrency = Column(Integer, nullable=False, server_default=text('0'))
    fame = Column(Float(53), nullable=False, server_default=text('0'))
    alignment = Column(Float(53), nullable=False, server_default=text('0'))
    defaultpawnclasspath = Column(String(200), nullable=False, server_default=text("''::character varying"))
    isinternalnetworktestuser = Column(Boolean, nullable=False, server_default=text('false'))
    classid = Column(Integer, nullable=False)
    isadmin = Column(Boolean, nullable=False, server_default=text('false'))
    ismoderator = Column(Boolean, nullable=False, server_default=text('false'))
    createdate = Column(DateTime, nullable=False, server_default=text('now()'))
    userguid = Column(ForeignKey('users.userguid'))
    mapname = Column(String(50))
    serverip = Column(String(50))
    description = Column(Text)
    basemesh = Column(String(100))

    users = relationship('Users', back_populates='characters')
    charhasabilities = relationship('Charhasabilities', back_populates='characters')
    charhasitems = relationship('Charhasitems', back_populates='characters')
    customcharacterdata = relationship('Customcharacterdata', back_populates='characters')


class Playergroup(Base):
    __tablename__ = 'playergroup'

    playergroupid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('playergroup_playergroupid_seq'::regclass)"))
    customerguid = Column(UUID, primary_key=True, nullable=False)
    playergroupname = Column(String(50), nullable=False)
    playergrouptypeid = Column(ForeignKey('playergrouptypes.playergrouptypeid'), nullable=False)
    readystate = Column(Integer, nullable=False, server_default=text('0'))
    createdate = Column(DateTime)

    playergrouptypes = relationship('Playergrouptypes', back_populates='playergroup')


class Usersessions(Base):
    __tablename__ = 'usersessions'

    customerguid = Column(UUID, primary_key=True, nullable=False)
    usersessionguid = Column(UUID, primary_key=True, nullable=False, server_default=text('gen_random_uuid()'))
    userguid = Column(ForeignKey('users.userguid'), nullable=False)
    logindate = Column(DateTime, nullable=False)
    selectedcharactername = Column(String(50))

    users = relationship('Users', back_populates='usersessions')


class Charhasabilities(Base):
    __tablename__ = 'charhasabilities'
    __table_args__ = (
        ForeignKeyConstraint(['customerguid', 'characterid'], ['characters.customerguid', 'characters.characterid']),
    )

    customerguid = Column(UUID, primary_key=True, nullable=False)
    charhasabilitiesid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('charhasabilities_charhasabilitiesid_seq'::regclass)"))
    characterid = Column(Integer, nullable=False)
    abilityid = Column(Integer, nullable=False)
    abilitylevel = Column(Integer, nullable=False, server_default=text('1'))
    charhasabilitiescustomjson = Column(Text)

    characters = relationship('Characters', back_populates='charhasabilities')
    charabilitybarabilities = relationship('Charabilitybarabilities', back_populates='charhasabilities')


class Charhasitems(Base):
    __tablename__ = 'charhasitems'
    __table_args__ = (
        ForeignKeyConstraint(['customerguid', 'characterid'], ['characters.customerguid', 'characters.characterid']),
    )

    customerguid = Column(UUID, primary_key=True, nullable=False)
    characterid = Column(Integer, primary_key=True, nullable=False)
    charhasitemid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('charhasitems_charhasitemid_seq'::regclass)"))
    itemid = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, server_default=text('1'))
    equipped = Column(Boolean, nullable=False, server_default=text('false'))

    characters = relationship('Characters', back_populates='charhasitems')


class Customcharacterdata(Base):
    __tablename__ = 'customcharacterdata'
    __table_args__ = (
        ForeignKeyConstraint(['customerguid', 'characterid'], ['characters.customerguid', 'characters.characterid']),
    )

    customerguid = Column(UUID, primary_key=True, nullable=False)
    customcharacterdataid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('customcharacterdata_customcharacterdataid_seq'::regclass)"))
    characterid = Column(Integer, nullable=False)
    customfieldname = Column(String(50), nullable=False)
    fieldvalue = Column(Text, nullable=False)

    characters = relationship('Characters', back_populates='customcharacterdata')


class Charabilitybarabilities(Base):
    __tablename__ = 'charabilitybarabilities'
    __table_args__ = (
        ForeignKeyConstraint(['customerguid', 'charabilitybarid'], ['charabilitybars.customerguid', 'charabilitybars.charabilitybarid']),
        ForeignKeyConstraint(['customerguid', 'charhasabilitiesid'], ['charhasabilities.customerguid', 'charhasabilities.charhasabilitiesid'])
    )

    customerguid = Column(UUID, primary_key=True, nullable=False)
    charabilitybarabilityid = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('charabilitybarabilities_charabilitybarabilityid_seq'::regclass)"))
    charabilitybarid = Column(Integer, nullable=False)
    charhasabilitiesid = Column(Integer, nullable=False)
    inslotnumber = Column(Integer, nullable=False, server_default=text('1'))
    charabilitybarabilitiescustomjson = Column(Text)

    charabilitybars = relationship('Charabilitybars', back_populates='charabilitybarabilities')
    charhasabilities = relationship('Charhasabilities', back_populates='charabilitybarabilities')


