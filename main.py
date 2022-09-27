def main():
    import back    
    
    s = back.Screen((1200,700),(850,650),"logo.png","Window Caption")

    def switch_section(f,t):
        f.enabled = False
        t.enabled = True
        t.ready_static()
        s.flush()
    
    L1 = back.Section((800,600),'white',False)
    L2 = back.Section((800,600),'white',False)
    L3 = back.Section((800,600),'white',False)
    L4 = back.Section((800,600),'white',False)

    L1.add_label("First ","black","arial",36,(0,0),0)
    L1.add_label("Page","red","arial",36,(0,0))
    L1.add_label("Content","blue","arial",36,(0,0),1.2)
    L1.add_button("Go to L2","black","calibri",20,[200,300,200,40],"white","yellow","black","green",[switch_section,L1,L2])
    L1.ready_static()
    L1.ready_dynamic()
    
    L2.add_label("Second ","black","arial",48,(0,0),0)
    L2.add_label("Page","orange","arial",48,(0,0))
    L2.add_label("Content","blue","arial",48,(0,0),1.2)
    L2.add_button("Go to L3","black","calibri",20,[200,300,200,40],"white","yellow","black","green",[switch_section,L2,L3])
    L2.ready_static()
    L2.ready_dynamic()
    
    L3.add_label("Third ","red","palatinolinotype",48,(0,0),0)
    L3.add_label("Page","green","palatinolinotype",48,(0,0))
    L3.add_label("Content","black","palatinolinotype",48,(0,0),1.2)
    L3.add_button("Go to L4","black","calibri",20,[200,300,200,40],"white","yellow","black","green",[switch_section,L3,L4])
    L3.ready_static()
    L3.ready_dynamic()
    
    L4.add_button("Go to L1","black","calibri",20,[200,300,200,40],"white","yellow","black","green",[switch_section,L4,L1])
    L4.ready_static()
    L4.ready_dynamic()

    switch_section(L1,L1)

    while 1:        
        while L1.enabled:
            s.before()
            s.place_subscreen(L1.return_subscreen())
            s.after()
            s.event_handler(L1.buttons,L1.ready_dynamic)
        while L2.enabled:
            s.before()
            s.place_subscreen(L2.return_subscreen())
            s.after()
            s.event_handler(L2.buttons,L2.ready_dynamic)
        while L3.enabled:
            s.before()
            s.place_subscreen(L3.return_subscreen())
            s.after()
            s.event_handler(L3.buttons,L3.ready_dynamic)
        while L4.enabled:
            s.before()
            s.place_subscreen(L4.return_subscreen())
            s.after()
            s.event_handler(L4.buttons,L4.ready_dynamic)

if __name__ == "__main__":
    main()