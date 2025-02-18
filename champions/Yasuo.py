from champion_base import Champion
class Yasuo(Champion): # Void kế thừa từ Champion
    def __init__(self):
        super().__init__("Yasuo", "Say Bye")

    def cast_skill_q(self):
        print('q is Stell Tempest')
    def cast_skill_w(self):
        print('w is Wind Wall')
    def cast_skill_r(self):
        print('r is Sweeping Blade')
    def cast_skill_e(self):
        print(f'e is {skill}')
