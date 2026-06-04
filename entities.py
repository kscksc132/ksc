import random


class Player:
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.hp = 100
        self.attack = 20
        self.defense = 5
        self.level = 1
        self.exp = 0
        self.exp_to_next = 30

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        actual = max(1, dmg - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def gain_exp(self, amount):
        self.exp += amount
        print(f"  경험치 +{amount} (현재: {self.exp}/{self.exp_to_next})")
        if self.exp >= self.exp_to_next:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= self.exp_to_next
        self.exp_to_next = int(self.exp_to_next * 1.5)
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 5
        self.defense += 2
        print(f"\n★ 레벨 업! Lv.{self.level} ★")
        print(f"  HP +20, 공격력 +5, 방어력 +2")

    def status(self):
        bar = "█" * (self.hp * 20 // self.max_hp) + "░" * (20 - self.hp * 20 // self.max_hp)
        print(f"[{self.name}] Lv.{self.level}  HP: [{bar}] {self.hp}/{self.max_hp}  ATK:{self.attack}  DEF:{self.defense}")


class Monster:
    TEMPLATES = [
        {"name": "슬라임",    "hp": 30,  "attack": 8,  "defense": 0, "exp": 10, "emoji": "🟢"},
        {"name": "고블린",    "hp": 50,  "attack": 14, "defense": 2, "exp": 18, "emoji": "👺"},
        {"name": "오크",      "hp": 80,  "attack": 20, "defense": 5, "exp": 30, "emoji": "👹"},
        {"name": "드래곤",    "hp": 150, "attack": 35, "defense": 10,"exp": 60, "emoji": "🐉"},
    ]

    def __init__(self, level=1):
        template = random.choice(self.TEMPLATES[:min(level, len(self.TEMPLATES))])
        scale = 1 + (level - 1) * 0.2
        self.name = template["name"]
        self.emoji = template["emoji"]
        self.max_hp = int(template["hp"] * scale)
        self.hp = self.max_hp
        self.attack = int(template["attack"] * scale)
        self.defense = template["defense"]
        self.exp_reward = int(template["exp"] * scale)

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        actual = max(1, dmg - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual

    def status(self):
        bar = "█" * (self.hp * 20 // self.max_hp) + "░" * (20 - self.hp * 20 // self.max_hp)
        print(f"{self.emoji} [{self.name}]  HP: [{bar}] {self.hp}/{self.max_hp}  ATK:{self.attack}")
