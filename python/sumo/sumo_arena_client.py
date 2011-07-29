#! /usr/bin/python

# This program is a simple example of SumoArena coding contest
# client. It handles the socket and JSON layers.
#
# You can use this code to write your own SumoArena client.
#
# All you need is to put your AI code between this kind of tags
# below in the source code :
#
#    #--------------------------------------------------------------
#    # Your code begins here
#    #--------------------------------------------------------------
#
# and
#
#    #--------------------------------------------------------------
#    # Your code ends here.
#    #--------------------------------------------------------------
#
# You may also want to change this information before joining the
# contest:

CLIENT_NAME     = 'Python Dummy Client' # <-- Put your own client name here.
AVATAR_URL      = ''                    # <-- Put a picture URL (PNG), if any.

# This client does nothing more than going to the right as fast
# as he can. It is unlikely to be the most clever strategy to
# win the contest.
#
# This code accepts command line arguments:
#
#           sumo_arena_client.py <hostname>:<port>
#
# where
#
#           <host_name> is the game server hostname (default: localhost)
#           <port_name> is the game server port (default: 9090)
#
# Good luck.

import sys

import asyncore
import socket

import json

from math import sqrt


# Command-line specified host and port may be missing.
DEFAULT_GAME_SERVER_HOST = '10.194.3.170'
DEFAULT_GAME_SERVER_PORT = 9090


class RoundStartInfo(object):

    def __init__(self, json_dict):
        self.__dict__.update(json_dict)


class Sphere(object):
    
    def __init__(self, json_dict):
        self.__dict__.update(json_dict)


class PlayingInfo(object):

    def __init__(self, json_dict):

        self.arenaRadius = json_dict["arenaRadius"]
        self.players = [Sphere(data) for data in json_dict["players"]]


class RoundStopInfo(object):

    def __init__(self, json_dict):
        self.__dict__.update(json_dict)


class Player(object):

    def on_round_start(self, startInfo):
        
        # Get all the available information.
        self.ownIndex           = startInfo.yourIndex
        self.playerCount        = startInfo.playerCount
        self.arenaInitialRadius = startInfo.arenaInitialRadius
        self.radius             = startInfo.sphereRadius
        self.maxVar             = startInfo.maxSpeedVariation
        self.currentRound       = startInfo.currentRound
        self.roundForVictory    = startInfo.roundForVictory

        print "Round is about to start."
        print "Now playing..."

    def on_play_request(self, playgroundInfo):
        
        if not playgroundInfo.players[self.ownIndex].inArena:
            # I'm out of the arena.
            return None

        result = self._choose_acceleration(playgroundInfo)

        # Check given rules.
        #
        # Assert()ions would be a little hard on us, isn't it?

        if not isinstance(result, tuple):
            print "*** Acceleration is supposed to be a (int, int) tuple."
        if not isinstance(result[0], int):
            print "*** Acceleration is supposed to be a (int, int) tuple."
        if not isinstance(result[0], int):
            print "*** Acceleration is supposed to be a (int, int) tuple."
        if not len(result) == 2:
            print "*** Acceleration is supposed to be a (int, int) tuple."

        sq_norm = result[0] * result[0] + result[1] * result[1] 
        if sq_norm > self.maxVar * self.maxVar:
            print "*** Acceleration is too big."

        return result

    def _choose_acceleration(self, playgroundInfo):
        # Your tough job starts here.
        #
        # Your are expected to return an (int, int)
        # tuple that gives (dVx, dVy) acceleration.

        # Here is the available information.
        arenaRadius = playgroundInfo.arenaRadius

        # This one is your sphere.
        #
        # Other sphere information is the same.
        myself      = playgroundInfo.players[self.ownIndex]

        # Position.
        x           = myself.x
        y           = myself.y

        # Velocity.
        vx          = myself.vx
        vy          = myself.vy

        # Other info.
        index       = myself.index      # Sphere index in players list.
        inArena     = myself.inArena    # Tell if game is over for this sphere.

        #--------------------------------------------------------------
        # Your code begins here.
        #--------------------------------------------------------------

        # Replace with more clever decision.
        #wanted_acceleration = self.maxVar, 0

				# Wanted x acceleration
				wx					= x*(-1)
	
				# Wanted y acceleration
				wy					= y*(-1)

				while ( 

        wanted_acceleration = x*(-1), y*(-1)



        #--------------------------------------------------------------
        # Your code ends here.
        #--------------------------------------------------------------

        return wanted_acceleration

    def on_round_stop(self, endInfo):
        
        # Get all the available information.
        currentRound     = endInfo.currentRound
        gameWinnerIndex  = endInfo.gameWinnerIndex
        roundWinnerIndex = endInfo.roundWinnerIndex

        # Did I win the round?
        if roundWinnerIndex == self.ownIndex:
            print "Hey, I just won this round."
        else:
            print "Well, I did not win this round."

        # Is the game over?
        if gameWinnerIndex < 0:
            print "I lost a round, but I dit not lose the game."
            return

        # If so, am I the king?
        if gameWinnerIndex == self.ownIndex:
            print "Hey, I also won this game, it seems."
        else:
            print "Kudos to the brilliant winner (not me, sadly)."


class GameClient(asyncore.dispatcher):

    def __init__(self, address, name, avatar_url=''):

        self._player = None

        # Protocol automaton data.
        self._callbacks = {
                'acknowledgeConnection':    self._on_connection_ack,
                'prepare':                  self._on_prepare,
                'play':                     self._on_play,
                'finishRound':              self._on_finish_round
            }
        self._actions = self._callbacks.keys()

        # Prepara connection information and send it ASAP.
        self._to_send = '{ "action": "connectPlayer", "parameters": {"name": "' + name + '", "avatar_url": "' + avatar_url + '"} }'
        self._received = ''

        # Connect to the server.
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(address)

    def handle_connect(self):
        # Now we are connected, we need a brain.
        self._player = Player()

    def writable(self):
        return len(self._to_send) > 0

    def handle_write(self):
        # Send waiting data.
        sent = self.send(self._to_send)
        self._to_send = self._to_send[sent:]

    def handle_read(self):

        # Read what is available
        data = self.recv(1024)
        if not data:
            return
        self._received += data

        # Parse what we received.
        valid, action, json_params = self._parse_server_request(self._received)
        if valid:
            self._callbacks[action](json_params)
        else:
            print action, self._received
        self._received = '' # FIXME Could have problem with partial requests.

    def handle_close(self):
        print "Connection closed."
        self.close()

    def handle_error(self):
        # Give uncondensed traceback.
        import traceback
        traceback.print_exc()

    def _parse_server_request(self, data):

        # Check JSON validity.
        req = None
        try:
            req = json.loads(data)
        except ValueError, ve:
            return False, 'Invalid JSON data', None

        # Check acceptable server actions.
        action = req.get('action', None)
        if not action:
            return False, 'No action in request', None
        if action not in self._actions:
            return False, 'Requested action is unknown', None

        # Get parameters.
        parameters = req.get('parameters', None)

        return True, action, parameters

    def _on_connection_ack(self, json_params):
        print "I'm connected as '%s'" % json_params["yourName"]

    def _on_prepare(self, json_params):
        info = RoundStartInfo(json_params)
        self._player.on_round_start(info)

    def _on_play(self, json_params):
        info = PlayingInfo(json_params)
        result = self._player.on_play_request(info)
        if result:
            data = {
                "action":     "updateVector",
                "parameters": {
                    "dVx": result[0],
                    "dVy": result[1]
                }
            }
            self._to_send = json.dumps(data)

    def _on_finish_round(self, json_params):
        info = RoundStopInfo(json_params)
        self._player.on_round_stop(info)


def main(argv=None):

    # Parse server host and port on command-line.
    server_host = DEFAULT_GAME_SERVER_HOST
    server_port = DEFAULT_GAME_SERVER_PORT
    if len(argv) > 1:
        args = argv[1].split(':')
        if len(args) == 1:
            server_host = argv[1]
        if len(args) == 2:
            server_host, port = args
            server_port = int(port)

    # Create and start client.
    client = GameClient(
                (server_host, server_port),
                CLIENT_NAME,
                AVATAR_URL)
    asyncore.loop()


if __name__ == "__main__":
    sys.exit( main(sys.argv) )

