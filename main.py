def main():
    import back
    
    s = back.Screen((1200,700),(850,650),"logo.png","Window Caption")
    
    L1 = back.Section((800,600),'white',True)
    L1.add_labels(["Lorem ipsum","blue","bahnschrift",24,(0,0),0],[" dolor","red","bahnschrift",24,[0,0],0])
    L1.ready_subscreen()

    while 1:
        while L1.enabled:
            s.before()
            s.place_subscreen(L1.return_subscreen())
            s.after()
            s.event_handler()

if __name__ == "__main__":
    main()