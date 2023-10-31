# Author: Joshua Kim 
# Assignment 1b
# Date: October 30, 2023 
# Description: This is a Speaker class that mimics that of a wireless speaker. It has attributes such as 
#              name, brand, mdoel, price and other attributes that manage speaker state, queueing music, 
#              applying equalizer values to control frequency outputs. A listening history to allow the speaker 
#              to provide your most listened to artists. 
#
# Inputs: Uses typing to provide type hints for method arguments and return values 
# Outputs: Can create a instance of speaker along with all methods that will compute, mutate, and retrieve data from the stored in the class

from typing import Union, List, Dict
import sys 
import pandas as pd 

class Speaker:
    """ 
    Speaker

    This is a speaker class that assumes that the speaker is wireless/bluetootha and that also has multiple methods for keeping track of
        1: battery
        2: playing/pausing 
        3: skippingb
        4: queuing music/audio activities 
        5: charging
        6: equalizer 
        7: listening history 
        8: speaker information (name, brand, model, price)
        9: connection to a device
    """

    def __init__(self, name:str, brand:str, model:str, price:float, max_battery_life_hours:float=8.0, volume: int=20, battery_percentage:float=100.0):
        """
        Constructor method 
        
        name (str): custom name for the speaker 
        brand (str): brand of the speaker 
        model (str): model of the speaker 
        price (str): the price of the speaker 
        max_battery_life_hours (float): the maximum battery life of the speaker in hours
        battery_percentage (int): initial battery percentage - defaults to 100 percent
        volume (int): initial volume of speaker - defaults to 20 
        """
        # Check that all arguments of the right type and value
        if (not isinstance(name, str) 
            or not isinstance(brand, str) 
            or not isinstance(model, str) 
            or not isinstance(price, float) 
            or max_battery_life_hours and not isinstance(max_battery_life_hours, float) 
            or volume and not isinstance(volume, int) 
            or battery_percentage and not isinstance(battery_percentage, float)):
            raise TypeError("Argument types are incorrect")
        
        # Check that all the values inputted are correct 
        elif (not name 
              or not brand 
              or not model 
              or (price < 0.0) 
              or max_battery_life_hours and max_battery_life_hours <= 0.0
              or volume and not (0 <= volume <= 100) 
              or battery_percentage and not (0.0 <= battery_percentage <= 100.0)):
            raise ValueError("Argument Values are incorrect")
        
        self._name = name 
        self._brand = brand 
        self._model = model 
        self._price = price 
        self._battery_percentage = battery_percentage
        self._max_battery_life_hours = max_battery_life_hours
        self._volume = volume

        self._currently_playing = None
        self._state = { "turned_on": False, "charging": False, "playing": False }
        self._equalizer = { "bass": 0, "mids": 0, "highs": 0 }
        self._connected_to = None

        self._queue = []
        self._listening_history = []
    
    # Accessor Methods  
    def get_name(self) -> str:
        """
        get_name() 
        
        Accessor method for getting the name of the speaker
        
        returns the name of the speaker
        """
        return self._name 
    
    def get_brand(self) -> str:
        """
        get_brand() 
        
        Accessor method for getting the brand of the speaker 
        
        returns the brand of the speaker
        """
        return self._brand
    
    def get_model(self) -> str:
        """
        get_model()
        
        Accessor method for the getting the model of the speaker 
        
        returns the model of the speaker
        """
        return self._model
    
    def get_price(self) -> float:
        """
        get_price() 
        
        Accessor method for getting the price of the speaker 
        
        returns the price of the speaker"""
        return self._price

    def get_state(self) -> Dict[str, bool]: 
        """
        get_state() 
        
        Accessor method for getting the state of the speaker 

        returns the state of the speaker as a dict: { "turned_on": bool, "charging": bool, "playing": bool, "connected": bool }
        """
        return self._state
    
    def get_max_battery_life_hours(self) -> float:
        """
        get_battery_life_hours() 
        
        Accessor method for getting the battery life of the speaker in hours 
        
        returns the battery life of the speaker in hours 
        """
        return self._max_battery_life_hours
    
    def get_connected_to(self) -> str:
        """
        get_connected_to() 
        
        Accessor method for getting the device that this speaker instance is connected to 
        
        Raises:
            InvalidSpeakerOperationException: if the speaker is not turned on 
        
        returns the currently connected to device name if there is one, None otherwise
        """
        # Check that the speaker is turned on 
        if self._check_turned_on(): 
            return self._connected_to
        else: 
            raise InvalidSpeakerOperationException("Speaker is not turned on")
        

    def get_currently_playing(self) -> Dict[str, str]: 
        """
        get_currently_playing() 
        
        Accessor method for getting the currently playing track

        Raises:
            InvalidSpeakerOperationException: if the speaker is turned off

        returns the currently selected/playing track as a dict: { "title": str, "artist": str, "genre": str }
        """
        # Check that the speaker is turned on 
        if self._check_turned_on(): 
            return self._currently_playing
        else:
            raise InvalidSpeakerOperationException("Speaker is not turned on")

    def get_volume(self) -> int: 
        """
        get_volume() 
        
        Accessor method for getting the volume of the speaker 

        Raises:
            InvalidSpeakerOperationException: if the speaker is turned off

        returns the volume set for the speaker
        """
        # Check that the speaker is turned on
        if self._check_turned_on(): 
            return self._volume 
        else: 
            raise InvalidSpeakerOperationException("Speaker is not turned on")
    
    def get_battery_percentage(self) -> float:
        """
        get_battery_percentage()
        
        Accessor method for getting the battery percentage 
        
        returns the battery percentage of the speaker
        """
        return self._battery_percentage 
    
    def get_remaining_battery_life(self) -> float:
        """
        get_remaining_battery_life 
        
        Accessor method for getting the remaining batter life of the speaker 
        formula: max_battery_life_hours * (battery_percentage/100)
        
        returns remaining battery life in hours as a float 
        """

        # Check if the speaker is turned on 
        if not self._state['turned_on']:
            raise InvalidSpeakerOperationException("Speaker is not turned on")
        return float(self._max_battery_life_hours) * (self._battery_percentage/100.0)

    def get_queue(self) -> List[Dict[str, Union[str, List[str]]]]:
        """
        get_queue() 
        
        Accessor method for getting the current queue

        Raises:
            InvalidSpeakerOperationException: if the speaker is turned off

        returns the queue of tracks, queue implemented as a python list 
        """
        # Check that the speaker is turned on 
        if self._check_turned_on(): 
            return self._queue  
        else:
            raise InvalidSpeakerOperationException("Speaker is not turned on")

    def get_equalizer(self) -> Dict[str, int]: 
        """
        get_equalizer() 
        
        Accessor method for getting the equalizer values 

        Raises:
            InvalidSpeakerOperationException: if the speaker is turned off

        returns a dict of equalizer values:  { "bass": 0, "mids": 0, "highs": 0 }
        """
        # Check that the speaker is turned on 
        if self._check_turned_on():
            return self._equalizer
        else:
            raise InvalidSpeakerOperationException("Speaker is not turned on")

    def get_most_played_artists(self, num_artists:int=1) -> List[str]:
        """
        get_most_played_artists()
        
        Accessor method for getting the most played artists 

        Args:
            num_artists: get the "num_artists" most played artists, defaults to 1

        Raises:
            InvalidSpeakerOperationException: if speaker is not turned_on 
            TypeError: if num_artists is not an integer 
            ValueError: if the value of num_artists is negative 
        
        returns the top 'num_artists' most played artists
        """
        # Check base conditions (Values and Types)
        if not isinstance(num_artists, int): 
            raise TypeError("Argument is wrong type")
        elif num_artists <= 0: 
            raise ValueError("Argument num_artists should be greater than 0")
        elif not self._check_turned_on():
            raise InvalidSpeakerOperationException("Speaker is not turned on")
        
        # Initialize dict key: frequency -> value: List[artists]
        most_frequent = {} 
        for i in range(1, len(self._get_listening_history()) + 1):
            most_frequent[i] = []

        # Get the number of occurrences of each artist in listening history 
        occurrences = {} 
        for item in self._get_listening_history(): 
            # Check if the song has a single artist
            if isinstance(item['artist'], str):
                if item['artist'] not in occurrences: 
                    occurrences[item['artist']] = 1 
                else: 
                    occurrences[item['artist']] += 1 

            # Check if the song has a list of artists (multiple artists)
            elif isinstance(item['artist'], list):

                # Loop through list of artists
                for artist in item['artist']:
                    if artist not in occurrences:
                        occurrences[artist] = 1 
                    else:
                        occurrences[artist] += 1
        
        # Create a new dict with the frequency the artist appears as the key and the artist as the value within a list
        for artist, frequency in occurrences.items(): 
            most_frequent[frequency].append(artist)

        # Loop through each number of occurrences from largest possible to smallest, and add the artist to a list 
        most_played_artists = [] 
        for i in range(len(self._listening_history), 0, -1):
            for artist in most_frequent[i]:
                most_played_artists.append(artist)
                if len(most_played_artists) == num_artists:
                    return most_played_artists
        
        # Case where num_artists is greater than number of unique artists in listening history 
        if most_played_artists: 
            return most_played_artists
        return None

    
    # Mutator Methods 
    def turn_on(self):
        """
        turn_on() 
        
        turns on the speaker 

        Raises:
            InvalidSpeakerOperationException: if the speaker is already turned on
        """
        # Check that the speaker is not turned on 
        if not self._check_turned_on(): 
            self._state['turned_on'] = True 
        else: 
            raise InvalidSpeakerOperationException("Speaker is already turned on")
    
    def turn_off(self):
        """
        turn_off() 
        
        turns off the speaker

        Raises:
            InvalidSpeakerOperationException: if the speaker is already turned off 
        """
        # Check that the speaker is turned on
        if self._check_turned_on(): 
            self._state['turned_on'] = False 
        else: 
            raise InvalidSpeakerOperationException("Speaker is already turned off")

    def connect(self, device_name:str): 
        """
        connect() 
        
        Args:
            device_name: name of device that speaker will connect to

        Raises:
            TypeError: if device_name is not of type string
            InvalidSpeakerOperationException: if speaker is not turned on
        """
        # Check that the device_name is of correct type and value 
        if not isinstance(device_name, str): 
            raise TypeError("Arugment device_name is of wrong type")
        elif not device_name.strip():
            raise ValueError("Ensure that device_name is not an empty string")
        elif not self._check_turned_on():
            raise InvalidSpeakerOperationException
        else:
            self._connected_to = device_name 

    def disconnect(self):
        """
        disconnect() 
        
        Removes the current connection if there is one
        
        Raises:
            InvalidSpeakerOperationException: if the speaker is already disconnected
            InvalidSpeakerOperationException: if the speaker is not turned on 
        """
        # Check that the speaker is turned on 
        if not self._check_turned_on(): 
            raise InvalidSpeakerOperationException("Speaker is not turned on")
        
        # Check that the speaker is connected to something 
        elif self.get_connected_to() == None:
            raise InvalidSpeakerOperationException("Can't disconnect from None")
        else: 
            self._connected_to = None 

    
    def charge(self): 
        """
        charge()
        
        charges the speaker and sets the speaker state to charging 

        Raises:
            InvalidSpeakerOperationException: if the speaker is already charging 
        """
        # Check that the speaker is not charging 
        if not self.get_state()['charging']:
            self._state['charging'] = True 
        else: 
            raise InvalidSpeakerOperationException("Speaker is already charging")
    
    def stop_charging(self):
        """
        stop_charging()
        
        stops charging the speaker

        Raises:
            InvalidSpeakerOperationException: if the speaker is already not charging 
        """
        # Check that the speaker is charging 
        if not self.get_state()['charging']:
            raise InvalidSpeakerOperationException("Speaker is already not charging")
        else: 
            self._state['charging'] = False 

    def play(self): 
        """
        play() 
        
        Plays the currently selected track if it exists, otherwise will play next song in queue 

        Raises:
            InvalidSpeakerOperationException: 
                1: if the speaker is already playing audio
                2: if no current selected song and queue is empty 
                3. if speaker is not turned on 
        """
        # Check that the speaker is not playing, and has songs in the queue and is turned on
        if (self.get_state()['playing'] 
            or (not self.get_currently_playing() and not self.get_queue()) 
            or not self._check_turned_on()):
            raise InvalidSpeakerOperationException("Speaker needs to be turned on, have songs in the queue, and not playing")
        
        # If there is no track playing but a track exists in the queue 
        elif not self.get_currently_playing() and self.get_queue(): 
            self.skip() 
        self._state['playing'] = True 

    def pause(self): 
        """
        pause() 
        
        Pauses the speaker

        Raises:
            InvalidSpeakerOperationException: if the speaker is already paused or if speaker is turned off 
        """
        # Check if the speaker is turned off or is not playing (paused)
        if not self.get_state()['playing'] or not self._check_turned_on(): 
            raise InvalidSpeakerOperationException("Speaker is already paused or is not turned on")
        else: 
            self._state['playing'] = False 
    
    def skip(self): 
        """
        skip() 
        
        Skips the currently playing track to the next song in the queue.
        This method will not mutate speaker state
        
        Raises:
            InvalidSpeakerOperationException: if no items exist in the queue or if speaker is not turned on 
        """
        # Check if speaker is turned off or queue is empty 
        if not self._check_turned_on() or not self.get_queue():
            raise InvalidSpeakerOperationException("Speaker is not turned on or speaker has no songs in queue")
        
        # Skip to the next song (does not play or pause speaker)
        else: 
            self._currently_playing = self._queue.pop(0)
            self._listening_history.append(self._currently_playing)
        
    
    def play_audio(self, title:str, artist:Union[str, List[str]], genre:str) -> None:
        """
        play_audio()
        
        plays the song/audio that is specified from the arguments.
        Speaker 'playing' set is changed to True
        
        Args (trailing whitespace will be removed, and converted to lower case):
            artist: the artist/author
            title: the title of the song/audio 
            genre: the genre of the song/audio 

        Raises:
            TypeError: if artist, title, or genre or not of type string 
            ValueError: if the genre is not in the _genres set
            InvalidSpeakerOperationException: if the speaker is not turned on 

        """
        # Check that all inputs are of correct types and values 
        if not isinstance(title, str) or not (isinstance(artist, str) or isinstance(artist, list)) or not isinstance(genre, str):
            raise TypeError("Ensure that title is a string,  artist is either a string of list and genre is a string")
        elif not title.lower().strip() or (isinstance(artist, str) and not artist.lower().strip()) or not genre.strip().lower(): 
            raise ValueError("Ensure that title, artist, and genre are not empty strings")
        elif isinstance(artist, list):

            # Convert all artist names to lowercase and strip trailing white space 
            for name in artist: 
                if not isinstance(name, str):
                    raise TypeError("Ensure that artists contains only strings as elements")
                elif not name.lower().strip(): 
                    raise ValueError("Ensure that all elements in artist are of type string")

            for i in range(len(artist)):
                artist[i] = artist[i].strip().lower()

        elif not self._check_turned_on():
            raise InvalidSpeakerOperationException("Speaker is not turned on")
        
        elif isinstance(artist, str):
            artist = artist.strip().lower()
        
        # Update state values and internal data
        self._state['playing'] = True
        self._currently_playing = { "title": title.strip().lower(), "artist": artist, "genre": genre.strip().lower() }
        self._listening_history.append({ "title": title.strip().lower(), "artist": artist, "genre": genre.strip().lower() })
     


    def queue(self, title:str, artist:Union[str, List[str]], genre:str) -> None: 
        """
        queue() 
        
        adds a track to a queue
        
        Args (trailing whitespace will be removed, and converted to lower case):
            title: name of the track, podcast etc to be queued
            artist: the name of the artist 
            genre: the genre of the track, podcast etc 
        
        Raises:
            TypeError: if the artist, title, or genre are not of type string 
            ValueError: if the genre is not in the _genre set 
            InvalidSpeakerOperationException: if speaker is not turned on 
        """
        # Check types and values 
        if not isinstance(title, str) or not isinstance(genre, str) or not (isinstance(artist, str) or isinstance(artist, list)):
            raise TypeError("Ensure that title is a string, genre is a string and artist is either a string or a list")
        
        # Check values of inputs 
        elif not title.lower().strip() or not genre.lower().strip(): 
            raise ValueError("Ensure that genre and title are not empty strings")
        
        elif isinstance(artist, str) and not artist: 
            raise ValueError("Ensure that artist is not an empty string")
        
        # Check each element in artist if artist is a list 
        elif isinstance(artist, list):
            for name in artist: 
                if not isinstance(name, str):
                    raise TypeError("Ensure that all elements of artist are strings")
                elif not name.lower().strip(): 
                    raise ValueError("Ensure that all elements of artist are not empty strings")
                
            for i in range(len(artist)):
                artist[i] = artist[i].strip().lower()

        elif not self._check_turned_on(): 
            raise InvalidSpeakerOperationException("Speaker is not turned on")
        
        elif isinstance(artist, str):
            artist = artist.strip().lower() 
        
        # Update the queue 
        self._queue.append({ "title": title.strip().lower(), "artist": artist, "genre": genre.strip().lower() })

    
    def delete_song_from_queue(self, title:str, artist:Union[str, List[str]]) -> None:
        """
        delete_song_from_queue() 
        
        deletes a song from the queue given the title and artist 
        
        Args (trailing whitespace will be removed, and converted to lower case):
            title: the title of the song/audio etc 
            artist: the name of the artist for the song/audio 
        
        Raises: 
            TypeError: if the title or artist are not of type string
            ValueError: if the specified title and artist are not found in the queue
            InvalidSpeakerOperationException: if no items exist in the queue  
        """
        # Check that the speaker is turned on and that the queue is not empty 
        if not self._state['turned_on'] or not self.get_queue():
            raise InvalidSpeakerOperationException("Speaker is not turned on or no songs are in queue")

        # Check that arguments are the correct types 
        if not isinstance(title, str) or not (isinstance(artist, str) or isinstance(artist, list)):
            raise TypeError("Ensure that title is a string, artist is either a string or a list")
        elif not title.lower().strip() or (isinstance(artist, str) and not artist.lower().strip()): 
            raise ValueError("Ensure that title and artist are not an empty string")

        # If a list of artists are given, check that each element within is a string 
        elif isinstance(artist, list):
            for name in artist:
                if not name.lower().strip(): 
                    raise ValueError("Ensure that all elements in artist are not empty strings")
                elif not isinstance(name, str):
                    raise TypeError("Ensure that all elements in artist are of type string")
            
            # strip elements of trailing white space and convert to lowercase 
            for i in range(len(artist)):
                artist[i] = artist[i].strip().lower() 
        
        # If artist is just a string, remove trailing white space and convert to lower case 
        elif isinstance(artist, str):
            artist = artist.strip().lower()
        
        title = title.strip().lower()
        
        # loop through queue and delete the song if there is a match 
        deleted = False
        for i in range(len(self._queue)):
            if self._queue[i]['title'] == title and self._queue[i]['artist'] == artist: 
                self._queue.pop(i)
                deleted = True
                break 
        
        # If no match raise a ValueError 
        if not deleted: 
            raise ValueError(f"No entry is queue matches input: { {'title': title, 'artist': artist} }")

    
    def reset_queue(self) -> None:
        """
        reset_queue() 
        
        deletes all entries in the queue 
        
        Raises: 
            InvalidSpeakerOperationException: if the speaker is not turned on 
        """
        # Check that the speaker is turned on 
        if not self._check_turned_on(): 
            raise InvalidSpeakerOperationException("Speaker is not turned on")
        else: 
            self._queue = [] 
    
    def update_information(self, name:str=None, brand:str=None, model:str=None, price:float=None) -> None: 
        """
        update_information() 

        updates the information about the speaker's name, brand, model, and price
        
        Args (trailing whitespace will be removed, and converted to lower case):
            name: updated name of the speaker 
            price: updated price of the speaker 
            brand: updated brand of the speaker 
            model: updated model of the speaker

        Raises:
            TypeError: if name, brand, or model are provided and are not of type string or if the price is provided and is not of type float
            ValueError: if price is a negative value, or if name, brand, or model are empty strings 
        """
        # Check the values and types of the arugments 
        if name == brand == model == price == None: 
            raise ValueError("No argument values passed")
        
        elif (name != None and not isinstance(name, str) 
              or brand != None and not isinstance(brand, str) 
              or model != None and not isinstance(model, str) 
              or price != None and not isinstance(price, float)):
            
            raise TypeError("Ensure that name, brand, model, and price are of correct types if arguments are passed")
        
        elif (name != None and not name.strip() 
              or brand != None and not brand.strip() 
              or model != None and not model.strip()): 
            
            raise ValueError("Ensure that all arugments are passed as not empty strings")
        
        elif price and price < 0.0: 
            raise ValueError("Ensure that price equal to or greater than $0.0")
        
        # Update the atrributes of the speaker 
        self._name = name.strip() if name else self._name
        self._brand = brand.strip() if brand else self._brand 
        self._model = model.strip() if model else self._model 
        self._price = price if price else self._price


    def set_volume(self, volume:int) -> None: 
        """
        set_volume() 
        
        set the volume of the speaker to a sepcified value 
        
        Args: 
            volume: the volume to set for the speaker as an int from 1 to 100 inclusive

        Raises:
            TypeError: if the volume is not an integer 
            ValueError: if the volume is negative or greater than 100
        """
        # Check that the speaker is turned on and type/value of the argument
        if not self._state['turned_on']:
            raise InvalidSpeakerOperationException("Speaker is not turned on")
        
        # Check that volume is the correct type (int)
        elif not isinstance(volume, int):
            raise TypeError("Ensure that volume is of type integer")
        
        # Check the value of volume
        elif not (0 <= volume <= 100): 
            raise ValueError("Ensure that the volume is between 0 and 100 inclusive")
        self._volume = volume 
    
    def set_battery_percentage(self, battery_percentage:float) -> None:
        """
        set_battery_percentage()
        
        sets the battery percentage of the speaker 
        
        Args:
            battery_percentage: the udpated battery percentage of the speaker 
        
        Raises:
            TypeError: if the type of battery_percentage is not an integer 
            ValueError: if the battery_percentage is not in between 0 and 100 inclusive 
        """
        # Check the type and value of battery_percentage 
        if not isinstance(battery_percentage, float):
            raise TypeError("Ensure that the battery_percentage is of type float")
        
        # Check value of battery_percentage
        elif not (0.0 <= battery_percentage <= 100.0): 
            raise ValueError("Ensure that the battery percentage is between 0.0 and 100.0 inclusive")
        
        self._battery_percentage = battery_percentage
    
    def set_max_battery_life_hours(self, max_battery_life_hours:float) -> None:
        """
        set_battery_life_hours()
        
        sets the maximum battery life of the speaker 
        
        Args:
            max_battery_life_hours: maximum battery life of the speaker in hours 
        
        Raises:
            TypeError: if max_battery_life_hours is not of type float 
            ValueError: if the max_battery_life_hours passed is negative
        """
        # Check that the type and values of the max_battery_life_hours is correct
        if not isinstance(max_battery_life_hours, float):
            raise TypeError("Ensure that max_battery_life_hours is of type float")
        
        # Check value of max_battery_life_hours
        elif max_battery_life_hours <= 0.0: 
            raise ValueError("Ensure that max_battery_life_hours is greater than 0.0")
        self._max_battery_life_hours = max_battery_life_hours 

    def set_equalizer(self, bass:int=None, mids:int=None, highs:int=None) -> None:
        """
        set_equalizer() 
        
        set the bass, mid, and high frequencies for the equalizer if they are provided. 
        if any of bass, mids, highs is not provided the value corresponding to will not be changed

        Args:
            bass: value for bass (low) frequencies - optional 
            mids: value for mid frequencies - optional 
            highs: value for high frequencies - optional
        
        Raises: 
            TypeError: if bass, mids, or highs are not integers
            ValueError: if the bass, mids, or highs are not between integer values of
            -100 and 100 inclusive 
        """
        # Check that the speaker is turned on 
        if not self._state['turned_on']:
            raise InvalidSpeakerOperationException("Speaker is not turned on")
        
        # Check that all arguments are of the correct types and values 
        elif (bass != None and not isinstance(bass, int)) or (mids != None and not isinstance(mids, int)) or (highs != None and not isinstance(highs, int)):
            raise TypeError("Ensure that all arguments passed are of correct type (integers)")\
            
        elif (not bass and not mids and not highs):
            raise ValueError("No arugments were passed")
        
        # Limits on the range of input for the equalizer 
        elif bass and not (-100 <= bass <= 100): 
            raise ValueError("Ensure that the value of bass is between -100 and 100 inclusive")
        
        elif mids and not (-100 <= mids <= 100):
            raise ValueError("Ensure that the value for mids is between -100 and 100 inclusive")
        
        elif highs and not (-100 <= highs <= 100):
            raise ValueError("Ensure that the value for highs is between -100 and 100 inclusive")
        
        # update the bass, mids, and highs of the equalizer 
        if bass:
            self._equalizer['bass'] = bass 
        if mids:
            self._equalizer['mids'] = mids 
        if highs:
            self._equalizer['highs'] = highs 
    

    # Private Helper Methods 
    def _set_listening_history(self, listening_history: List[Dict[str, str]]) -> None:
        """
        Private method used for assisting in testing

        mutates the listening history to the passed listening_history
        """
        self._listening_history = listening_history

    def _get_listening_history(self) -> List[Dict[str, str]]:
        """
        Private method to help test listening history 
        
        returns a list of songs that were listened to
        """
        return self._listening_history
    
    def _set_queue(self, queue: List[Union[Dict[str, str], Dict[str, List[str]]]]) -> None:
        """
        Private method to help with testing queue 
        
        mutates the queue to the list passed as an arg (queue)
        """
        self._queue = queue
    
    # NEW METHODS
    def _check_turned_on(self) -> bool: 
        """
        Private method that checks if the speaker is turned on 
        
        returns True of the speaker is turned on False otherwise
        """
        turned_on: bool = self.get_state()['turned_on']
        return turned_on

    
    def __sizeof__(self):
        size = 0 

        # Calculate size of elements of self._state
        for k, v in self._state.items():
            size += sys.getsizeof(k) + sys.getsizeof(v)

        # calculate size of elements of self._equalizer
        for k, v in self._equalizer.items():
            size += sys.getsizeof(k) + sys.getsizeof(v)


        # Calculate size of elements of self._queue 

        # Get size of each element within list 
        for i in range(len(self._queue)):
            size += sys.getsizeof(self._queue[i])

            # Get size of each key, value pair of each dictionary within the list 
            for k, v in self._queue[i].items(): 
                if isinstance(v, str):
                    size += sys.getsizeof(k) + sys.getsizeof(v)

                # key 'artist' may be a list of strings 
                elif isinstance(v, list):
                    size += sys.getsizeof(v)
                    for item in v: 
                        size += sys.getsizeof(item)


        # Calculate size of elements in self._listening_history 
        
        # Get size of each element within list 
        for i in range(len(self._listening_history)):
            size += sys.getsizeof(self._listening_history[i])

            # Get size of each key, value pair of each dictionary within the list 
            for k, v in self._listening_history[i].items(): 
                if isinstance(v, str):
                    size += sys.getsizeof(k) + sys.getsizeof(v)
                
                # key 'artist' may be a list of strings 
                elif isinstance(v, list):
                    size += sys.getsizeof(v)
                    for item in v: 
                        size += sys.getsizeof(item)

        return (size 
                + sys.getsizeof(self._name) 
                + sys.getsizeof(self._model) 
                + sys.getsizeof(self._brand) 
                + sys.getsizeof(self._price)
                + sys.getsizeof(self._volume)
                + sys.getsizeof(self._equalizer)
                + sys.getsizeof(self._connected_to)
                + sys.getsizeof(self._currently_playing)
                + sys.getsizeof(self._queue)
                + sys.getsizeof(self._state)
                + sys.getsizeof(self._battery_percentage)
                + sys.getsizeof(self._max_battery_life_hours)
                + sys.getsizeof(self._listening_history)) 




# RUNNING SPACE ANALYSIS
if __name__ == '__main__':

    INCREMENT = 100
    MAX_INPUT_SIZE = 10000
    STARTING_INPUT_SIZE = 1

    ### _name data ###
    data = {"input_size": [], "class_size": []}
    for i in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)
        speaker.update_information(name=("j" * i))
        data['input_size'].append(i)
        data['class_size'].append(sys.getsizeof(speaker))
    df = pd.DataFrame(data)
    df.to_csv('./data/_name.csv', index=False)

    ### _brand data ###
    data = {"input_size": [], "class_size": []}
    for i in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)
        speaker.update_information(brand=("j" * i))
        data['input_size'].append(i)
        data['class_size'].append(sys.getsizeof(speaker))
    df = pd.DataFrame(data)
    df.to_csv('./data/_brand.csv', index=False)

    ### _model data ###
    data = {"input_size": [], "class_size": []}
    for i in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)
        speaker.update_information(model=("j" * i))
        data['input_size'].append(i)
        data['class_size'].append(sys.getsizeof(speaker))
    df = pd.DataFrame(data)
    df.to_csv('./data/_model.csv', index=False)

    ### _connected_to data ###
    data = {"input_size": [], "class_size": []}
    for i in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)
        speaker.turn_on()
        speaker.connect(("j" * i))
        data['input_size'].append(i)
        data['class_size'].append(sys.getsizeof(speaker))
    df = pd.DataFrame(data)
    df.to_csv('./data/_connected_to.csv', index=False)


    ### _queue data ###

    ### queue with artist as a string

    # SMALLER queue with adding minimal songs (strings with 1 character)
    data = {"input_size": [], "class_size": []}
    speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)
    speaker.turn_on()
    for size in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):

        queue = [{'title': 'j', 'artist': 'j', 'genre': 'j'}]*size
        speaker._set_queue(queue=queue)
        data['input_size'].append(size)
        data['class_size'].append(sys.getsizeof(speaker))

    df = pd.DataFrame(data)
    df.to_csv('./data/_queue_minimal.csv', index=False)

    # LARGER queue with adding larger songs (strings with 100 characters)
    data = {"input_size": [], "class_size": []}
    speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)
    speaker.turn_on()
    for size in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        queue = [{'title': 'j'*100, 'artist': 'j'*100, 'genre': 'j'*100}]*size
        speaker._set_queue(queue=queue)
        data['input_size'].append(size)
        data['class_size'].append(sys.getsizeof(speaker))

    df = pd.DataFrame(data)
    df.to_csv('./data/_queue_larger.csv', index=False)       


    # -------------------------------------------------------------------------

    ### queue with artist as a list ; seeing how class grows with increase in len(artist) ###

    # SMALLER queue with internal dict key 'artist' being a list of data and minimal for other attributes
    data = {"input_size": [], "class_size": []}

    # max number of artists on a song will probably be around 10
    NUM_ARTISTS = 10
    for size in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)

        # Increase size of array of artist by a factor if 'i'
        queue = [{'title': 'j', 'artist': ['j']*NUM_ARTISTS, 'genre': 'j'}]*size
        speaker._set_queue(queue=queue)
        data['input_size'].append(size)
        data['class_size'].append(sys.getsizeof(speaker))
    
    df = pd.DataFrame(data)
    df.to_csv('./data/_queue_artist_list_minimal.csv', index=False)


    # LARGER queue. Upper bound on Realistic large size values for queue
    # String lengths are 100 and artist list length will increase
    data = {"input_size": [], "class_size": []}

    # max number of artists on a song will probably be around 10
    NUM_ARTISTS = 10

    for size in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)

        # Increase size of array of artist by a factor if 'i'
        queue = [{'title': 'j'*100, 'artist': ['j'*100]*NUM_ARTISTS, 'genre': 'j'*100}]*size
        speaker._set_queue(queue=queue)
        data['input_size'].append(size)
        data['class_size'].append(sys.getsizeof(speaker))
    
    df = pd.DataFrame(data)
    df.to_csv('./data/_queue_artist_list_larger.csv', index=False)

    # ------------------------------------------------------------------------- 

    ### listening history ### 

    ### Minimal; artist is a string ###
    data = {"input_size": [], "class_size": []}
    for size in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)

        history = [{'title': 'j', 'artist': 'j', 'genre': 'j'}]*size
        speaker._set_listening_history(listening_history=history)
        data['input_size'].append(size)
        data['class_size'].append(sys.getsizeof(speaker))
    
    df = pd.DataFrame(data)
    df.to_csv('./data/_history_minimal.csv', index=False)

    ### Larger; artist is a string ### 
    data = {"input_size": [], "class_size": []}
    for size in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)

        history = [{'title': 'j'*100, 'artist': 'j'*100, 'genre': 'j'*100}]*size
        speaker._set_listening_history(listening_history=history)
        data['input_size'].append(size)
        data['class_size'].append(sys.getsizeof(speaker))
    
    df = pd.DataFrame(data)
    df.to_csv('./data/_history_larger.csv', index=False)

    # ------------------------------------------------------------------------- 

    ### With artist list increasing in length ### (where list length, and string sizes are large)

    # SMALLER queue with internal dict key 'artist' being a list of data and minimal for other attributes
    data = {"input_size": [], "class_size": []}

    # max number of artists on a song will probably be around 10
    NUM_ARTISTS = 10
    for size in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)

        # Increase size of array of artist
        history = [{'title': 'j', 'artist': ['j']*NUM_ARTISTS, 'genre': 'j'}]*size
        speaker._set_listening_history(history)
        data['input_size'].append(size)
        data['class_size'].append(sys.getsizeof(speaker))
    
    df = pd.DataFrame(data)
    df.to_csv('./data/_history_artist_list_minimal.csv', index=False)


    # LARGER queue. Upper bound on Realistic large size values for queue
    # String lengths are 100 and artist list length will increase
    data = {"input_size": [], "class_size": []}

    # max number of artists on a song will probably be around 10
    NUM_ARTISTS = 10

    for size in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)

        # Increase size of array of artist by a factor if 'i'
        history = [{'title': 'j'*100, 'artist': ['j'*100]*NUM_ARTISTS, 'genre': 'j'*100}]*size
        speaker._set_listening_history(history)
        data['input_size'].append(size)
        data['class_size'].append(sys.getsizeof(speaker))
    
    df = pd.DataFrame(data)
    df.to_csv('./data/_history_artist_list_larger.csv', index=False)

    # ------------------------------------------------------------------------- 

    ### SOFT UPPER BOUND ON CLASS SIZE ###

    data = {"input_size": [], "class_size": []}
    # max number of artists on a song will probably be around 10
    NUM_ARTISTS = 10

    for size in range(STARTING_INPUT_SIZE, MAX_INPUT_SIZE, INCREMENT):
        speaker = Speaker(name="JJK", brand="JBL", model="Flip6", price=190.00)
        speaker.turn_on()

        history = [{'title': 'j'*100, 'artist': ['j'*100]*NUM_ARTISTS, 'genre': 'j'*100}]*size
        speaker._set_listening_history(history)

        queue = [{'title': 'j'*100, 'artist': ['j'*100]*NUM_ARTISTS, 'genre': 'j'*100}]*size
        speaker._set_queue(queue=queue)

        speaker.update_information(name=("j" * i), brand=("j" * i), model=("j" * i))
        speaker.connect("j"*size)

        data['input_size'].append(size)
        data['class_size'].append(sys.getsizeof(speaker))
    
    df = pd.DataFrame(data)
    df.to_csv('./data/_max_class_size.csv', index=False)



# Custom Class Exceptions
class InvalidSpeakerOperationException(Exception):
    def __init__(self, message: str = None):
        """
        This exception will be raised whenever an 'illegal' speaker operation is attempted 
        
        Example: charging the speaker when it is already charging
        """
        if message:
            self.message = message 
        else: 
            self.message = "Invalid speaker operation"
        super().__init__(self.message)