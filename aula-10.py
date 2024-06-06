

from minecraft import agent, LEFT_TURN

def on_on_chat():
    """
    This function is called when a chat event occurs.
    It turns the agent to the left.
    """
    agent.turn(LEFT_TURN)
player.on_chat("left", on_on_chat)

def on_on_chat2():
    """
    This function performs a series of actions using the Minecraft agent.
    It destroys blocks, moves in different directions, and collects iron ore if detected.
    """
    while True:
        for index in range(4):
            agent.destroy(FORWARD)
            agent.move(FORWARD, 1)
            agent.destroy(DOWN)
        agent.turn(LEFT_TURN)
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.destroy(FORWARD)
        agent.destroy(DOWN)
        agent.move(BACK, 1)
        agent.destroy(DOWN)
        agent.move(BACK, 1)
        agent.turn(RIGHT_TURN)
        agent.turn(RIGHT_TURN)
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.destroy(DOWN)
        agent.destroy(FORWARD)
        agent.destroy(DOWN)
        agent.move(BACK, 1)
        agent.turn(LEFT_TURN)
        if agent.detect(AgentDetection.BLOCK, IRON_ORE):
            agent.collect_all()
        else:
            pass
player.on_chat("dig", on_on_chat2)

def on_on_chat3():
    """
    This function handles the event when a chat message is received.
    It makes the agent turn right.
    """
    agent.turn(RIGHT_TURN)
player.on_chat("right", on_on_chat3)

def on_on_chat4():
    """
    Gives 5 pieces of cooked beef to the target player.
    """
    mobs.give(mobs.target(LOCAL_PLAYER), COOKED_BEEF, 5)
player.on_chat("food", on_on_chat4)

def on_on_chat5():
    """
    Moves the agent up by 1 block.
    """
    agent.move(UP, 1)
player.on_chat("up", on_on_chat5)

def on_on_chat6():
    """
    Moves the agent down by 1 block.
    """
    agent.move(DOWN, 1)
player.on_chat("down", on_on_chat6)

def on_on_chat7():
    """
    Teleports the agent to the player's location.
    """
    agent.teleport_to_player()
player.on_chat("agent", on_on_chat7)

gameplay.title(mobs.target(LOCAL_PLAYER), "say agent", "")