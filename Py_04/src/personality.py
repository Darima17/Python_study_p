import random
import time
def turrets_generator():
    while True:
        personality_traits = [random.randint(0, 100) for i in range(5)]
        if sum(personality_traits) == 100:
            turret = type(
                'Turret', (object, ),
                dict(shoot=lambda self: print('Shooting'),
                     search=lambda self: print('Searching'),
                     talk=lambda self: print('Talking'),
                     neuroticism=personality_traits[0],
                     openness=personality_traits[1],
                     conscientiousness=personality_traits[2],
                     extraversion=personality_traits[3],
                     agreeableness=personality_traits[4])
            )
            yield turret

if __name__ == '__main__':
    turret_g = turrets_generator()
    print(type(turret_g))
    print(next(turret_g))
    for turret in turret_g:
        print('Information about the turret:')
        print('Neuroticism:', turret.neuroticism, 'Openness:', turret.openness,
              'Conscientiousness:', turret.conscientiousness,
              'Extraversion:', turret.extraversion, 'Agreeableness:',
              turret.agreeableness)
        turret.shoot(turret)
        turret.search(turret)
        turret.talk(turret)
        time.sleep(3)
