
define ai = Character('Айсен', color='#000000', image='aisen')
define ar = Character('Артур', color='#000000', image='artur')
define ko = Character('Коля' , color='#000000', image='kolya')
define audio.rington = "audio/rington.mp3"
define audio.zyb = "audio/zyb.mp3"
define audio.tp = "audio/toptop.mp3"

init:
    $ left2 = Position(xalign=0.2, yalign=1.1)
    $ right2 = Position(xalign=0.8, yalign=1.1)
label start:

    stop music fadeout 1
    
    scene black
    with fade
    
    "{cps=*1}{i}Утро Среды.{/i}{/cps}"
    
    scene black
    
    play audio rington
    
    pause(1)
    
    "{cps=*1}Кто вообще пишет в такую рань?{/cps}"
    "{cps=*2}{i}посмотрел на телефон...{/i}{/cps}"
    
    scene telefon
    with dissolve
    
    menu:
        "{cps=*2}Неизвестный номер отправил сообщение.{/cps}"

        "Перейти по ссылке":
            
            scene black
            with fade
            
            '{b}{i}GAMEOVER{/i}{/b}'
            'Дети, не переходите по подозрительным ссылкам!'
            
            return

        "Проигнорировать":
            
            scene black
            with fade
            
            play music zyb
            
            "{cps=8}Зубы моем. Зубы моем.\n С мылом и водою. C мылом и водою.{/cps}"
            
            stop music fadeout 1
    
            scene room
            with fade
            
            jump room
    return
label room:

    scene room
    
    menu:
        "{cps=*2}выберите персонажа{/cps}"
    
    
        "{image=images/sprite/aisen.png} Айсен":
        
            show aisen normal at right2
            with dissolve
            
            menu:
                "режим Айсен - легкий уровень сложности"
                
                "Подтвердить":
                    $ p=1                
                "Вернуться назад":
                    hide aisen
                    with dissolve
                    
                    jump room
            
        "{image=images/sprite/artur.png} Артур":
            
            show artur normal at right2
            with dissolve
            
            menu:
                "режим Артур - средний уровень сложности"
            
                    
                "Подтвердить":
                    $ p=2
                
                "Вернуться назад":
                    hide artur
                    with dissolve
                    
                    jump room
            
        "{image=images/sprite/kolya.png} Коля":
            
            show kolya normal at right2
            with dissolve
            
            menu:
                "режим Коля - уровень сложности {b}ХАРДКОР{/b}"
             
                "Подтвердить":
                    $ p=3
                
                "Вернуться назад":
                    hide kolya
                    with dissolve
                    
                    jump room
label Aisen:
    

label telefonroom:
    
    scene exitin
    with fade
    
    if p == 1:
    
        show aisen normal at right2
        with dissolve
        
        menu:
            ai "Блин, я оставил телефон."
            
            "Вурнуться":
                jump toptop
                
            "Оставить":
                menu:
                    "Точно?"
                    
                    "Вурнуться":
                            jump toptop
                       
                    "Оставить":
                        menu:
                            "Точно??"
                
                            "Вурнуться":
                                jump toptop
                   
                            "Оставить":
                                menu:
                                    "Точно???"
                
                                    "Вурнуться":
                                        jump toptop
                   
                                    "Оставить":
                                    
                                        scene black
                                        with fade
                                        
                                        "Вы провели обычный, но досмерти скучный день..."
                                        
                                        play music zyb
                                        
                                        "{cps=8}Зубы моем. Зубы моем.\n С мылом и водою. C мылом и водою.{/cps}"
                                        
                                        stop music fadeout 1

                                        return
                                        
    if p == 2:
        
        show artur normal at right2
        with dissolve
        
        menu:
            ar "Блин, я оставил телефон."
            
            "Вернуться":
                jump toptop
            "Оставить":
                ar "Я не вижу жизни без телефона, лучьше венусь."
                jump toptop
    if p == 3:
    
        show kolya normal at right2
        with dissolve
    
        menu:
            ko "Блин, я оставил телефон."
            
            "Вернуться":
                jump toptop
            "Оставить":
                ko "А нет, он в карман."
                jump toptop
    return
label toptop:

    scene black
    with fade
    
    play audio tp
    pause(5)
    
    return