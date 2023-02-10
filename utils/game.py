def reward(first, second):
    first.update(second, True )
    second.update(first, False)

def play(first, second, turn):
    
    if turn:
        first.lastAction = None
        actions = list(range(1, min(first.maxBet, first.worth, second.worth)+1))
        first.action = first.chooseAction(actions, None)    

        second.lastAction = None
        actions = list(range(first.action, min(first.maxBet, first.worth, second.worth)+1))
        actions.append(0)
        second.action = second.chooseAction(actions, first.action)

        while first.action*second.action > 0 and first.action != second.action:

            first.lastAction = first.action
            actions = list(range(second.action , min(first.maxBet, first.worth, second.worth)+1))
            actions.append(0)
            first.action = first.chooseAction(actions, second.action)

            if first.action > 0 and second.action != first.action:

                second.lastAction = second.action
                actions = list(range(first.action, min(first.maxBet, first.worth, second.worth)+1))
                actions.append(0)
                second.action = second.chooseAction(actions, first.action)

        reward(first, second)
        
    else:
        play(second, first, 1 - turn)
        
def simplePlay(first, second, turn):
    
    if turn:
        actions = list(range(1, min(first.maxBet, first.worth, second.worth)+1))
        first.action = first.chooseAction(actions, None)    

        actions = [0, first.action]
        second.action = second.chooseAction(actions, first.action)
        
        reward(first, second) 
    else:
        simplePlay(second, first, 1 - turn)