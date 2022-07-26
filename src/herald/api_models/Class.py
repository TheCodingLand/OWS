from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Class(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    classid: int = Field(None, title='Classid')
    classname: str = Field(None, title='Classname')
    startingmapname: str = Field(None, title='Startingmapname')
    x: float = Field(None, title='X')
    y: float = Field(None, title='Y')
    z: float = Field(None, title='Z')
    perception: float = Field(None, title='Perception')
    acrobatics: float = Field(None, title='Acrobatics')
    climb: float = Field(None, title='Climb')
    stealth: float = Field(None, title='Stealth')
    rx: float = Field(None, title='Rx')
    ry: float = Field(None, title='Ry')
    rz: float = Field(None, title='Rz')
    spirit: float = Field(None, title='Spirit')
    magic: float = Field(None, title='Magic')
    teamnumber: int = Field(None, title='Teamnumber')
    thirst: float = Field(None, title='Thirst')
    hunger: float = Field(None, title='Hunger')
    gold: int = Field(None, title='Gold')
    score: int = Field(None, title='Score')
    characterlevel: int = Field(None, title='Characterlevel')
    gender: int = Field(None, title='Gender')
    xp: int = Field(None, title='Xp')
    hitdie: int = Field(None, title='Hitdie')
    wounds: float = Field(None, title='Wounds')
    size: int = Field(None, title='Size')
    weight: float = Field(None, title='Weight')
    maxhealth: float = Field(None, title='Maxhealth')
    health: float = Field(None, title='Health')
    healthregenrate: float = Field(None, title='Healthregenrate')
    maxmana: float = Field(None, title='Maxmana')
    mana: float = Field(None, title='Mana')
    manaregenrate: float = Field(None, title='Manaregenrate')
    maxenergy: float = Field(None, title='Maxenergy')
    energy: float = Field(None, title='Energy')
    energyregenrate: float = Field(None, title='Energyregenrate')
    maxfatigue: float = Field(None, title='Maxfatigue')
    fatigue: float = Field(None, title='Fatigue')
    fatigueregenrate: float = Field(None, title='Fatigueregenrate')
    maxstamina: float = Field(None, title='Maxstamina')
    stamina: float = Field(None, title='Stamina')
    staminaregenrate: float = Field(None, title='Staminaregenrate')
    maxendurance: float = Field(None, title='Maxendurance')
    endurance: float = Field(None, title='Endurance')
    enduranceregenrate: float = Field(None, title='Enduranceregenrate')
    strength: float = Field(None, title='Strength')
    dexterity: float = Field(None, title='Dexterity')
    constitution: float = Field(None, title='Constitution')
    intellect: float = Field(None, title='Intellect')
    wisdom: float = Field(None, title='Wisdom')
    charisma: float = Field(None, title='Charisma')
    agility: float = Field(None, title='Agility')
    fortitude: float = Field(None, title='Fortitude')
    reflex: float = Field(None, title='Reflex')
    willpower: float = Field(None, title='Willpower')
    baseattack: float = Field(None, title='Baseattack')
    baseattackbonus: float = Field(None, title='Baseattackbonus')
    attackpower: float = Field(None, title='Attackpower')
    attackspeed: float = Field(None, title='Attackspeed')
    critchance: float = Field(None, title='Critchance')
    critmultiplier: float = Field(None, title='Critmultiplier')
    haste: float = Field(None, title='Haste')
    spellpower: float = Field(None, title='Spellpower')
    spellpenetration: float = Field(None, title='Spellpenetration')
    defense: float = Field(None, title='Defense')
    dodge: float = Field(None, title='Dodge')
    parry: float = Field(None, title='Parry')
    avoidance: float = Field(None, title='Avoidance')
    versatility: float = Field(None, title='Versatility')
    multishot: float = Field(None, title='Multishot')
    initiative: float = Field(None, title='Initiative')
    naturalarmor: float = Field(None, title='Naturalarmor')
    physicalarmor: float = Field(None, title='Physicalarmor')
    bonusarmor: float = Field(None, title='Bonusarmor')
    forcearmor: float = Field(None, title='Forcearmor')
    magicarmor: float = Field(None, title='Magicarmor')
    resistance: float = Field(None, title='Resistance')
    reloadspeed: float = Field(None, title='Reloadspeed')
    range: float = Field(None, title='Range')
    speed: float = Field(None, title='Speed')
    silver: int = Field(None, title='Silver')
    copper: int = Field(None, title='Copper')
    freecurrency: int = Field(None, title='Freecurrency')
    premiumcurrency: int = Field(None, title='Premiumcurrency')
    fame: float = Field(None, title='Fame')
    alignment: float = Field(None, title='Alignment')
    description: Optional[str] = Field(None, title='Description')
