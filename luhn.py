
import PySimpleGUI as sg
# import os
# import sys


def myfunction():
    text = sg.PopupGetText('Please enter your 16-digit credit card number', )
    try:
        int_text = int(text)
    except ValueError:
        sg.Popup('No valid input. Please enter a valid card number!')
        myfunction()
        
    
    a = int(str(int_text)[::-1])  # tipono ti lista anapoda

    res = [int(x) for x in str(a)]

    b = res
    c = []

    for i in b[1::2]:  # tipono ti lista ana dio
        c.append(i)
            #     print(i)

    z = []
    for i in c:
        z.append(i*2)  # tipono ti lista ana dio pollaplasioasmeni epi dio

    new_list = []
    new_list2 = []
    for i in z:
        if i > 9:
                new_list.append(i)  # afairo tamegala apo ti z
        if i < 9:
            new_list2.append(i)  # afairo ta mikra apo ti z

    new_list3 = []
    for i in new_list:
        ena = i % 10
        dio = i/10
        i = ena+dio
        new_list3.append(int(i))  # apo ti lista new_list to athroisma ton megalon


    new_list4 = new_list2+new_list3


    d = []
    for i in b[0::2]:
        d.append(i)

    new_list5 = new_list4+d

    sinolo = 0
    for i in new_list5:
        sinolo = sinolo+i

    if sinolo % 10 == 0:
        a=1
        sg.Popup('The account number is possibly valid')
        exit()
    else:
        a=0
        sg.Popup('You entered wrong number')
            
        while a==0:
            text2 = sg.PopupGetText('Do you want to try again?\n (y/n)' )
            if text2=='y':
                myfunction()
            elif text2 =='n':
                exit()
            if text2!='y'or 'n':
                sg.Popup('No valid answer')
                text2 = sg.PopupGetText('Do you want to try again?\n (yy/nn)')
                if text2=='y':
                    myfunction()
                elif text2 =='n':
                    exit()
                    # if text2!='yy'or 'nn':
                    #     exit()
                
myfunction()


        

    