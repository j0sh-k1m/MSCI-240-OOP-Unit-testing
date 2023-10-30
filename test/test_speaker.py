# test_speaker
#
# Author: Joshua Kim
# Assignment 1A 
# Date: October 8, 2023
# Description: these are the test cases for the speaker class. It checks for proper usage of the class 
#              and checks for proper mutation and accessing of class data. 
# Inputs: Each unit test will have their own inputs for testing but none externally 
# Outputs: Each unit test will either Pass or Fail depending if the implementations of the methods 
#          works as intended 

import unittest
from speaker.speaker import Speaker, InvalidSpeakerOperationException

class TestSpeaker(unittest.TestCase):

    def test_constructor_typical1(self):
        """
        Input: 
            name = "jjkflip6", 
            brand = "JBL", 
            model = "Flip6", 
            price = 200.0

        Expected Output: instance of Speaker with the variables above with default values
            1: Max_battery_life_hours = 8.0 
            2: volume = 20 
            3: Battery_percentage = 100  
        """

        # Create speaker instance 
        speaker = Speaker(name="jjkflip6", brand="JBL", model="Flip6", price=200.0)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        # Check post conditions
        self.assertEquals(speaker.get_name(), "jjkflip6")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "Flip6")
        self.assertEquals(speaker.get_price(), 200.0)
        self.assertEquals(speaker.get_max_battery_life_hours(), 8.0)
        self.assertEquals(speaker.get_battery_percentage(), 100.0)
        self.assertEquals(speaker.get_volume(), 20)

    def test_constructor_typical2(self):
        """
        Input: 
            name = "jjkflip6", 
            brand = "JBL", 
            model = "Flip6", 
            price = 200.0
            max_battery_life_hours = 9.21

        Expected Output: instance of Speaker with the variables above with default values 
            1: volume = 20 
            2: Battery_percentage = 100  
        """

        # Create speaker instance 
        speaker = Speaker(name="jjkflip6", brand="JBL", model="Flip6", price=200.0, max_battery_life_hours=9.21)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        # Check post conditions 
        self.assertEquals(speaker.get_name(), "jjkflip6")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "Flip6")
        self.assertEquals(speaker.get_price(), 200.0)
        self.assertEquals(speaker.get_max_battery_life_hours(), 9.21)
        self.assertEquals(speaker.get_battery_percentage(), 100.0)
        self.assertEquals(speaker.get_volume(), 20)

    def test_constructor_typical3(self):
        """
        Input: 
            name = "jjkflip6", 
            brand = "JBL", 
            model = "Flip6", 
            price = 200.0
            max_battery_life_hours = 9.21
            volume = 10

        Expected Output: instance of Speaker with the variables above with default values 
            1: Battery_percentage = 100  
        """

        # Create speaker instance 
        speaker = Speaker(name="jjkflip6", brand="JBL", model="Flip6", price=200.0, max_battery_life_hours=9.21, volume=10)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        # Check post conditions 
        self.assertEquals(speaker.get_name(), "jjkflip6")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "Flip6")
        self.assertEquals(speaker.get_price(), 200.0)
        self.assertEquals(speaker.get_max_battery_life_hours(), 9.21)
        self.assertEquals(speaker.get_battery_percentage(), 100.0)
        self.assertEquals(speaker.get_volume(), 10)

    def test_constructor_typical4(self):
        """
        Input: 
            name = "jjkflip6", 
            brand = "JBL", 
            model = "Flip6", 
            price = 200.0
            max_battery_life_hours = 9.21
            volume = 10
            battery_percentage = 45.5

        Expected Output: instance of Speaker with the variables above
        """

        # Create speaker instance 
        speaker = Speaker(name="jjkflip6", brand="JBL", model="Flip6", price=200.0, max_battery_life_hours=9.21, battery_percentage=45.5, volume=10)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        # Check post conditions 
        self.assertEquals(speaker.get_name(), "jjkflip6")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "Flip6")
        self.assertEquals(speaker.get_price(), 200.0)
        self.assertEquals(speaker.get_max_battery_life_hours(), 9.21)
        self.assertEquals(speaker.get_battery_percentage(), 45.5)
        self.assertEquals(speaker.get_volume(), 10)

    def test_constructor_typical5(self):
        """
        Input: 
            name = "jjkflip6", 
            brand = "JBL", 
            model = "Flip6", 
            price = 200.0
            volume = 10

        Expected Output: instance of Speaker with the variables above with default values 
            1: battery_percentage = 100.0
            2: max_battery_life_hours = 8.0
        """

        # Create speaker instance 
        speaker = Speaker(name="jjkflip6", brand="JBL", model="Flip6", price=200.0, volume=10)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        # Check post conditions 
        self.assertEquals(speaker.get_name(), "jjkflip6")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "Flip6")
        self.assertEquals(speaker.get_price(), 200.0)
        self.assertEquals(speaker.get_max_battery_life_hours(), 8.0)
        self.assertEquals(speaker.get_battery_percentage(), 100.0)
        self.assertEquals(speaker.get_volume(), 10)

    def test_constructor_typical6(self): 
        """
        Input:
            name = “jjkflip6” 
            brand = “JBL”
            model = “Flip6”
            price = 200.0 
            battery_percentage = 90.0

        Expected Output: an instance of speaker with the above variables with default values 
            1: volume = 20 
            2: max_battery_life_hours = 8.0
        """

        # Create speaker instance 
        speaker = Speaker(name="jjkflip6", brand="JBL", model="Flip6", price=200.0, battery_percentage=90.0)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        # Check post conditions 
        self.assertEquals(speaker.get_name(), "jjkflip6")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "Flip6")
        self.assertEquals(speaker.get_price(), 200.0)
        self.assertEquals(speaker.get_max_battery_life_hours(), 8.0)
        self.assertEquals(speaker.get_battery_percentage(), 90.0)
        self.assertEquals(speaker.get_volume(), 20)

    def test_constructor_typical7(self):
        """
        Input:
            name = “jjkflip6” 
            brand = “JBL”
            model = “Flip6”
            price = 200.0 
            volume = 10 

        Expected Output: an instance of speaker with the above variables with default values 
            battery_percentage = 100.0 
            max_battery_life_hours = 8.0 
        """

        # Create speaker instance 
        speaker = Speaker(name="jjkflip6", brand="JBL", model="Flip6", price=200.0, volume=10)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        # Check post conditions 
        self.assertEquals(speaker.get_name(), "jjkflip6")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "Flip6")
        self.assertEquals(speaker.get_price(), 200.0)
        self.assertEquals(speaker.get_max_battery_life_hours(), 8.0)
        self.assertEquals(speaker.get_battery_percentage(), 100.0)
        self.assertEquals(speaker.get_volume(), 10)

    def test_constructor_unusual1(self):
        """
        Input:
            name = “jjkflip6” 
            brand = “JBL”
            model = “Flip6”
            price = 0.0 
            battery_percentage = 90.0
            volume = 10 
            max_battery_life_hours = 9.21

        Expected Output: an instance of speaker with the above variables 
        """

        # Create speaker instance 
        speaker = Speaker(name="jjkflip6", brand="JBL", model="Flip6", price=200.0, battery_percentage=90.0, volume=10, max_battery_life_hours=9.21)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        # Check post conditions 
        self.assertEquals(speaker.get_name(), "jjkflip6")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "Flip6")
        self.assertEquals(speaker.get_price(), 200.0)
        self.assertEquals(speaker.get_max_battery_life_hours(), 9.21)
        self.assertEquals(speaker.get_battery_percentage(), 90.0)
        self.assertEquals(speaker.get_volume(), 10)

    def test_constructor_unusual2(self):
        """
        Input: 
            name = “-1snfhui2” 
            brand = “JBL”
            model = “Flip6”
            price = 100.0
            max_battery_life_hours = 9.21
            volume = 10  
            battery_percentage = 100.0

        Excpected Output: an instance of speaker with the above values 
        """

        # Create speaker instance 
        speaker = Speaker(name="-1snfhui2", brand="JBL", model="Flip6", price=100.0, max_battery_life_hours=9.21, volume=10, battery_percentage=100.0)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        # Check post conditions 
        self.assertEquals(speaker.get_name(), "-1snfhui2")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "Flip6")
        self.assertEquals(speaker.get_price(), 100.0)
        self.assertEquals(speaker.get_max_battery_life_hours(), 9.21)
        self.assertEquals(speaker.get_volume(), 10)
        self.assertEquals(speaker.get_battery_percentage(), 100.0)

    def test_constructor_unusual3(self):
        """
        Input: 
            name = “jjkflip6” 
            brand = “&#---1”
            model = “&*()”
            price = 100.0
            max_battery_life_hours = 3.763
            volume = 69
            battery_percentage = 45.3

        Expected Output: an instance of speaker with the above variables 
        """

        # Create speaker instance 
        speaker = Speaker(name="jjkflip6", brand="JBL", model="&*()", price=100.0, max_battery_life_hours=3.763, volume=69, battery_percentage=45.3)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        # Check post conditions 
        self.assertEquals(speaker.get_name(), "jjkflip6")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "&*()")
        self.assertEquals(speaker.get_price(), 100.0)
        self.assertEquals(speaker.get_max_battery_life_hours(), 3.763)
        self.assertEquals(speaker.get_volume(), 69)
        self.assertEquals(speaker.get_battery_percentage(), 45.3)

    def test_constructor_unusual4(self):
        """
        Input:
            name = “jjkflip6” 
            brand = “JBL”
            model = “Aubnw34”
            price = 100.0
            max_battery_life_hours = 012.4
            volume = 10  
            battery_percentage = 100.0
        
        Expected Output: an instance of speaker with the above values 
        """

        # Create speaker instance 
        speaker = Speaker(name="jjkflip6", brand="JBL", model="Aubnw34", price=100.0, max_battery_life_hours=012.4, volume=10, battery_percentage=100.0)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        # Check post conditions 
        self.assertEquals(speaker.get_name(), "jjkflip6")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "Aubnw34")
        self.assertEquals(speaker.get_price(), 100.0)
        self.assertEquals(speaker.get_max_battery_life_hours(), 012.4)
        self.assertEquals(speaker.get_volume(), 10)
        self.assertEquals(speaker.get_battery_percentage(), 100.0)

    def test_constructor_error1(self): 
        """
        Input:
            name = -100
            brand = “JBL”
            model = “Flip6”
            price = 100.0
            max_battery_life_hours = 9.21
            volume = 10  
            battery_percentage = 100.0
        
        Expected Output: raised TypeError
        """
        with self.assertRaises(TypeError):
            Speaker(name=-100, brand="JBL", model="Flip6", price=100.0, max_battery_life_hours=9.21, volume=10, battery_percentage=100.0)

    def test_constructor_error2(self):
        """
        Input:
            name = “JJKFlip6”
            brand = {“hello world”}
            model = “Aubnw34”
            price = 100.0
            max_battery_life_hours = 9.21
            volume = 10  
            battery_percentage = 100.0

        Expected Output: raised TypeError 
        """
        with self.assertRaises(TypeError):
            Speaker(name="JJKFlip6", brand={"hello world"}, model="Aubnw34", price=100.0, max_battery_life_hours=9.21, volume=10, battery_percentage=100.0)

    def test_constructor_error3(self):
        """
        Input: 
            name = “JJKFlip6”
            brand = “JBL”
            model = [“hello”, -1]
            price = 100.0
            max_battery_life_hours = 9.21
            volume = 10  
            battery_percentage = 100.0
        
        Expected Output: raised TypeError 
        """
        with self.assertRaises(TypeError):
            Speaker(name="JJKFlip6", brand="JBL", model=['hello', -1], price=100.0, max_battery_life_hours=9.21, volume=10, battery_percentage=100.0)

    def test_constructor_error4(self):
        """
        Input: 
            name = “JJKFlip6”
            brand = “JBL”
            model = “Flip6”
            price = “str”
            max_battery_life_hours = 9.21
            volume = 10  
            battery_percentage = 100.0
        
        Expected Output: raised TypeError 
        """
        with self.assertRaises(TypeError):
            Speaker(name="JJKFlip6", brand="JBL", model="Flip6", price="str", max_battery_life_hours=9.21, volume=10, battery_percentage=100.0)

    def test_constructor_error5(self):
        """
        Input:
            name = “JJKFlip6”
            brand = “JBL”
            model = “Flip6”
            price = -100.0
            max_battery_life_hours = 9.21
            volume = 10  
            battery_percentage = 100.0
        
        Expected Output: raised ValueError
        """
        with self.assertRaises(ValueError):
            Speaker(name="JJKFlip6", brand="JBL", model="Flip6", price=-100.0, max_battery_life_hours=9.21, volume=10, battery_percentage=100.0)

    def test_constructor_error6(self):
        """
        Input: 
            name = “JJKFlip6”
            brand = “JBL”
            model = “Flip6”
            price = 100.77
            max_battery_life_hours = “help”
            volume = 10  
            battery_percentage = 100.0

        Expected Output: raised TypeError 
        """
        with self.assertRaises(TypeError):
            Speaker(name="JJKFlip6", brand="JBL", model="Flip6", price=100.77, max_battery_life_hours="help", volume=10, battery_percentage=100.0)

    def test_constructor_error7(self):
        """
        Input:
            name = “JJKFlip6”
            brand = “JBL”
            model = “Flip6”
            price = 100.77
            max_battery_life_hours = -100.0
            volume = 10  
            battery_percentage = 100.0
        
        Expected Output: raised ValueError 
        """
        with self.assertRaises(ValueError):
            Speaker(name="JJKFlip6", brand="JBL", model="Flip6", price=100.77, max_battery_life_hours=-100.0, volume=10, battery_percentage=100.0)

    def test_constructor_error8(self):
        """
        Input:
            name = “JJKFlip6”
            brand = “JBL”
            model = “Flip6”
            price = 100.77
            max_battery_life_hours = 2.0
            volume = 20.0
            battery_percentage = 100.0
        
        Expected Output: raised TypeError 
        """
        with self.assertRaises(TypeError):
            Speaker(name="JJKFlip6", brand="JBL", model="Flip6", price=100.77, max_battery_life_hours=2.0, volume=20.0, battery_percentage=100.0)

    def test_constructor_error9(self): 
        """
        Input:
            name = “JJKFlip6”
            brand = “JBL”
            model = “Flip6”
            price = 100.77
            max_battery_life_hours = 2.0
            volume = -5
            battery_percentage = 100.0
        
        Expected Output: raised ValueError
        """
        with self.assertRaises(ValueError):
            Speaker(name="JJKFlip6", brand="JBL", model="Flip6", price=100.77, max_battery_life_hours=2.0, volume=-5, battery_percentage=100.0)

    def test_constructor_error10(self):
        """
        Input:
            name = “JJKFlip6”
            brand = “JBL”
            model = “Flip6”
            price = 100.77
            max_battery_life_hours = 2.0
            volume = 43
            battery_percentage = “str”
        
        Expected Output: raised TypeError 
        """
        with self.assertRaises(TypeError):
            Speaker(name="JJKFlip6", brand="JBL", model="Flip6", price=100.77, max_battery_life_hours=2.0, volume=43, battery_percentage="str")

    def test_constructor_error11(self):
        """
        Input:
            name = “JJKFlip6”
            brand = “JBL”
            model = “Flip6”
            price = 100.77
            max_battery_life_hours = 2.0
            volume = 43
            battery_percentage = -10.0
        
        Expected Output: raised ValueError
        """
        with self.assertRaises(ValueError):
            Speaker(name="JJKFlip6", brand="JBL", model="Flip6", price=100.77, max_battery_life_hours=2.0, volume=43, battery_percentage=-12.0)

    def test_constructor_error12(self):
        """
        Input:
            name = “jjkflip6” 
            brand = “JBL”
            model = “Flip6”
            price = 100.0
            max_battery_life_hours = 0.0
            volume = 10  
            battery_percentage = 100.0

        Expected Output: raised ValueError
        """
        with self.assertRaises(ValueError):
            Speaker(name="JJKFlip6", brand="JBL", model="Flip6", price=100.77, max_battery_life_hours=0.0, volume=43, battery_percentage=-12.0)



    def test_get_state_typical1(self):
        """
        Testing proper mutation and accessing of the 'turned_on' state 
        """
        # Create Speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_state()['turned_on'], False)
        speaker.turn_on()
        self.assertEquals(speaker.get_state()['turned_on'], True)
        speaker.turn_off()
        self.assertEquals(speaker.get_state()['turned_on'], False)

    def test_get_state_typical2(self):
        """
        Testing proper mutation and accessing of the 'playing' state 

        speaker.play() should only work if speaker.get_state()['turned_on'] = True 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)
        
        self.assertEquals(speaker.get_state()['playing'], False)
        speaker.turn_on()
        speaker.queue(title="Lucid Dream", artist="Aespa", genre="K-pop")
        speaker.play()
        self.assertEquals(speaker.get_state()['playing'], True)
        speaker.pause()
        self.assertEquals(speaker.get_state()['playing'], False)

    def test_get_state_typical3(self):
        """
        Testing proper mutation and accessing of the 'charging' state 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_state()['charging'], False)
        speaker.charge()
        self.assertEquals(speaker.get_state()['charging'], True)
        speaker.stop_charging()
        self.assertEquals(speaker.get_state()['charging'], False)



    def test_get_max_batery_life_hours_typical1(self):
        """
        Testing proper mutation and accessing of the current battery percentage 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_max_battery_life_hours(), 8.0)
        speaker.set_max_battery_life_hours(30.2)
        self.assertEquals(speaker.get_max_battery_life_hours(), 30.2)
        speaker.set_max_battery_life_hours(0.123)
        self.assertEquals(speaker.get_max_battery_life_hours(), 0.123)



    def test_get_currently_playing_typical1(self):
        """
        Testing proper mutation and accessing of the currently playing track 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        self.assertEquals(speaker.get_currently_playing(), None)
        speaker.play_audio(title="Honeymoon Avenue", artist="Arianna Grande", genre="Rnb")
        self.assertEquals(speaker.get_currently_playing(), {"title": "honeymoon avenue", "artist": "arianna grande", "genre": "rnb"})

    def test_get_currently_playing_error1(self):
        """
        Testing the error case where the speaker is turned off 
        
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)
        self.assertRaises(InvalidSpeakerOperationException, speaker.get_currently_playing)



    def test_get_connected_to_typical1(self):
        """
        Testing the accessing of the current connection 
        
        Expected Output: connection to proper device
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        speaker.connect("josh's pixel 8")
        self.assertEquals(speaker.get_connected_to(), "josh's pixel 8")

    def test_get_connected_to_error1(self):
        """
        Testing the case where the speaker is turned off
        
        Expected Output: raised InvalidSpeakerOperationException
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)
        self.assertRaises(InvalidSpeakerOperationException, speaker.get_connected_to)



    def test_get_volume_typical1(self):
        """
        Testing proper mutation and accessing of the current volume of the speaker 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        self.assertEquals(speaker.get_volume(), 45) 
        speaker.set_volume(30)
        self.assertEquals(speaker.get_volume(), 30)
        speaker.set_volume(100)
        self.assertEquals(speaker.get_volume(), 100)

    def test_get_volume_error1(self):
        """
        Testing case where speaker is turned off
        
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)
        self.assertRaises(InvalidSpeakerOperationException, speaker.get_volume)



    def test_get_battery_percentage_typical1(self):
        """
        Testing proper mutation and accessing of the current battery percentage 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, battery_percentage=34.5)

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_battery_percentage(), 34.5)
        speaker.set_battery_percentage(20.0)
        self.assertEquals(speaker.get_battery_percentage(), 20.0)
        speaker.set_battery_percentage(95.3892)
        self.assertEquals(speaker.get_battery_percentage(), 95.3892)



    def test_get_remaining_battery_life_typical1(self):
        """
        Input: 
            max_battery_life_hours: 8.0
            battery_percentage: 98 
            
        Expected Output: 8.0 * (float(98)/100)
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, max_battery_life_hours=8.0, battery_percentage=98.0)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        self.assertEquals(speaker.get_remaining_battery_life(), 8.0 * (float(98)/100))

    def test_get_remaining_battery_life_typical2(self):
        """
        Input: 
            max_battery_life_hours: 7.27
            battery_percentage: 31
        
        Expected Output: 7.27 * (float(31)/100)
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, max_battery_life_hours=7.27, battery_percentage=31.0)
        
        self.assertIsNotNone(speaker)
        speaker.turn_on()
        self.assertEquals(speaker.get_remaining_battery_life(), 7.27 * float(31)/100)

    def test_get_remaining_battery_life_error1(self):
        """
        Testing case where speaker is turned off 
        
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)

        self.assertRaises(InvalidSpeakerOperationException, speaker.get_remaining_battery_life)



    def test_get_queue_typical1(self):
        """
        Testing proper mutation and accessing of the queue of songs,podcasts etc
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        self.assertEquals(speaker.get_queue(), [])
        speaker.queue(title="Lucid Dream", artist="Aespa", genre="k-pop")
        self.assertEquals(speaker.get_queue(), [{"title": "lucid dream", "artist": "aespa", "genre": 'k-pop'}])
        speaker.queue(title="Yatch", artist="Jay Park", genre="k-rnb")
        self.assertEquals(speaker.get_queue(), [{"title": "lucid dream", "artist": "aespa", "genre": 'k-pop'}, {"title": "yatch", "artist": "jay park", "genre": "k-rnb"}])
        speaker.delete_song_from_queue(title="Lucid Dream", artist="Aespa")
        self.assertEquals(speaker.get_queue(), [{"title": "yatch", "artist": "jay park", "genre": "k-rnb"}])

    def test_get_queue_error1(self):
        """
        Testing the case where the speaker is turned off 
        
        Expected Output: InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        # Check for raised exception 
        self.assertIsNotNone(speaker)
        self.assertRaises(InvalidSpeakerOperationException, speaker.get_queue)


    def test_get_equalizer_typical1(self):
        """
        Testing proper mutation and accessing of the equalizer 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        self.assertEquals(speaker.get_equalizer(),  { "bass": 0, "mids": 0, "highs": 0 })
        speaker.set_equalizer(bass=-50, mids=50, highs=2)
        self.assertEquals(speaker.get_equalizer(), { "bass": -50, "mids": 50, "highs": 2 })
        speaker.set_equalizer(highs=40)
        self.assertEquals(speaker.get_equalizer(), {"bass": -50, "mids": 50, "highs": 40 })

    def test_get_equalizer_error1(self):
        """
        Testing the case where the speaker is turned off 
        
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)
        self.assertRaises(InvalidSpeakerOperationException, speaker.get_equalizer)



    def test_get_most_played_artists_typical1(self):
        """
        Testing proper computation of get_most_played_artists()
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        self.assertEquals(speaker.get_most_played_artists(), None)
        listening_history = [
            {
                "title": "yatch", 
                "artist": "jay park",
                "genre": "k-rnb"
            }, 
            {
                "title": "yatch", 
                "artist": "jay park",
                "genre": "k-rnb"
            }, 
            {
                "title": "7 rings", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "positions", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "v", 
                "artist": "jay park",
                "genre": "k-rnb"
            },
            {
                "title": "all i wanna do", 
                "artist": "jay park",
                "genre": "k-rnb"
            },
        ]
        speaker._set_listening_history(listening_history=listening_history)
        self.assertEquals(speaker.get_most_played_artists(1), ["jay park"])
        self.assertEquals(speaker.get_most_played_artists(2), ["jay park", "arianna grande"])

    def test_get_most_played_artists_typical2(self):
        """
        Input: 
            num_artists = 3 (greater than number of unique artists in listening history)
            
        Excpected Output: the max number if unique artists in the listening history
        """
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        self.assertEquals(speaker.get_most_played_artists(), None)
        listening_history = [
            {
                "title": "yatch", 
                "artist": "jay park",
                "genre": "k-rnb"
            }, 
            {
                "title": "7 rings", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "positions", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "v", 
                "artist": "jay park",
                "genre": "k-rnb"
            },
            {
                "title": "all i wanna do", 
                "artist": ['jay park', 'hoody', 'loco'],
                "genre": "k-rnb"
            },
        ]
        speaker._set_listening_history(listening_history=listening_history)

        self.assertEquals(speaker.get_most_played_artists(4), ["jay park", "arianna grande", "hoody", "loco"])


    def test_get_most_played_artists_unusual1(self):
        """
        Input: 
            num_artists = 3 (greater than number of unique artists in listening history)
            
        Excpected Output: the max number if unique artists in the listening history
        """
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        self.assertEquals(speaker.get_most_played_artists(), None)
        listening_history = [
            {
                "title": "yatch", 
                "artist": "jay park",
                "genre": "k-rnb"
            }, 
            {
                "title": "yatch", 
                "artist": "jay park",
                "genre": "k-rnb"
            }, 
            {
                "title": "7 rings", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "positions", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "v", 
                "artist": "jay park",
                "genre": "k-rnb"
            },
            {
                "title": "all i wanna do", 
                "artist": "jay park",
                "genre": "k-rnb"
            },
        ]
        speaker._set_listening_history(listening_history=listening_history)

        self.assertEquals(speaker.get_most_played_artists(3), ["jay park", "arianna grande"])


    def test_get_most_played_artists_error1(self): 
        """
        Input:
            num_artists = "str"
        
        Expected Output: raised ValueError
        """
        # Create Speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        self.assertEquals(speaker.get_most_played_artists(), None)
        listening_history = [
            {
                "title": "yatch", 
                "artist": "jay park",
                "genre": "k-rnb"
            }, 
            {
                "title": "yatch", 
                "artist": "jay park",
                "genre": "k-rnb"
            }, 
            {
                "title": "7 rings", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "positions", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "v", 
                "artist": "jay park",
                "genre": "k-rnb"
            },
            {
                "title": "all i wanna do", 
                "artist": "jay park",
                "genre": "k-rnb"
            },
        ]
        speaker._set_listening_history(listening_history=listening_history)

        # Check TypeError
        with self.assertRaises(TypeError):
            speaker.get_most_played_artists("str")

    def test_get_most_played_artists_error2(self):
        """
        Input:
            num_artists = 0 
        
        Expected Output: raised ValueError
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        self.assertEquals(speaker.get_most_played_artists(), None)
        listening_history = [
            {
                "title": "yatch", 
                "artist": "jay park",
                "genre": "k-rnb"
            }, 
            {
                "title": "yatch", 
                "artist": "jay park",
                "genre": "k-rnb"
            }, 
            {
                "title": "7 rings", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "positions", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "v", 
                "artist": "jay park",
                "genre": "k-rnb"
            },
            {
                "title": "all i wanna do", 
                "artist": "jay park",
                "genre": "k-rnb"
            },
        ]
        speaker._set_listening_history(listening_history=listening_history)

        # Check for ValueError
        with self.assertRaises(ValueError):
            speaker.get_most_played_artists(0)

    def test_get_most_played_artists_error3(self):
        """
        Input:
            num_artists = 0 
        
        Expected Output: raised ValueError
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        self.assertEquals(speaker.get_most_played_artists(), None)
        listening_history = [
            {
                "title": "yatch", 
                "artist": "jay park",
                "genre": "k-rnb"
            }, 
            {
                "title": "yatch", 
                "artist": "jay park",
                "genre": "k-rnb"
            }, 
            {
                "title": "7 rings", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "positions", 
                "artist": "arianna grande",
                "genre": "rnb"
            },
            {
                "title": "v", 
                "artist": "jay park",
                "genre": "k-rnb"
            },
            {
                "title": "all i wanna do", 
                "artist": "jay park",
                "genre": "k-rnb"
            },
        ]
        speaker._set_listening_history(listening_history=listening_history)

        # Check for ValueError
        with self.assertRaises(ValueError):
            speaker.get_most_played_artists(-3)

    def test_get_most_played_artists_error4(self):
        """
        Check the case where the speaker is not turned on 
        
        Expected Output: raised InvalidSpeakerOperationException
        """
        # Create speaker instance 
        speaker = Speaker(name="Joshy", brand="Bose", model="bose123", price=115.99)

        self.assertIsNotNone(speaker)

        self.assertRaises(InvalidSpeakerOperationException, speaker.get_most_played_artists)

    # Testing Mutator Methods 
    def test_turn_on_typical1(self):
        """
        Testing the mutation of the turned_on state 
        """
        # Create speaker instance 
        speaker = Speaker(name="Joshy", brand="Bose", model="bose123", price=115.99)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertEquals(speaker.get_state()['turned_on'], True)

    def test_turn_on_error1(self):
        """
        Testing that InvalidSpeakerOperationException is raised when trying to turn on the speaker when
        it is already turned on 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)
        
        self.assertIsNotNone(speaker)
        speaker.turn_on()
        self.assertRaises(InvalidSpeakerOperationException, speaker.turn_on)



    def test_turn_off_typical1(self):
        """
        Testing the mutation of the turned_off state
        """
        # Create Speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_state()['turned_on'], False)
        speaker.turn_on()
        self.assertEquals(speaker.get_state()['turned_on'], True)
        speaker.turn_off() 
        self.assertEquals(speaker.get_state()['turned_on'], False)

    def test_turn_off_typical2(self):
        """
        Testing proper mutation of other variables 
        
        self._currently_playing -> None
        self._connected_to -> None
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)

        # Turn on speaker and set to playing and connected
        speaker.turn_on()
        self.assertEquals(speaker.get_state()['turned_on'], True)
        speaker.play_audio(title="Thirsty", artist="Aespa", genre="k-pop")
        speaker.connect('iphone')
        self.assertEquals(speaker.get_currently_playing(), {"title": "thirsty", "artist": "aespa", "genre": "k-pop"})
        self.assertEquals(speaker.get_connected_to(), "iphone")
        speaker.turn_off() 
        # Check post conditions of calling speaker.turn_off() 
        self.assertEquals(speaker.get_state()['turned_on'], False)
        with self.assertRaises(InvalidSpeakerOperationException):
            speaker.get_connected_to() 

    def test_turn_off_error1(self):
        """
        Testing that InvalidSpeakerOperationException is raised when trying to turn off the speaker 
        when the speaker is already turned off 

        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertEquals(speaker.get_state()['turned_on'], False)
        self.assertRaises(InvalidSpeakerOperationException, speaker.turn_off)



    def test_connect_typical1(self):
        """
        Testing the mutation of the connect method 
        
        Input: 
            device_name: "josh's iphone"
        
        Expected Output: connection to "josh's iphone" 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        self.assertEquals(speaker.get_connected_to(), None)
        speaker.connect("josh's iphone")
        self.assertEquals(speaker.get_connected_to(), "josh's iphone")

    def test_connect_typical2(self):
        """
        Input: 
            device_name = "Macbook pro"
        
        Input: 
            device_name = "iPad" 

        Expected Output: connection to "iPad"     
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23)

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        self.assertEquals(speaker.get_connected_to(), None)
        speaker.connect('Macbook pro')
        self.assertEquals(speaker.get_connected_to(), "Macbook pro")
        speaker.connect("iPad") 
        self.assertEquals(speaker.get_connected_to(), "iPad")

    def test_connect_error1(self):
        """
        Input: 
            device_name = ""

        Expected Output: raised ValueError    
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)
        speaker.turn_on() 

        with self.assertRaises(ValueError):
            speaker.connect("")

    def test_connect_error2(self):
        """
        Input:
            device_name: -40
        
        Excpected Output: raised TypeError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45) 

        self.assertIsNotNone(speaker)
        speaker.turn_on()

        with self.assertRaises(TypeError):
            speaker.connect(-2)

    def test_connect_error3(self):
        """
        Testing case where speaker is not turned on

        Input:
            device_name: "iphone"
        
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)
        with self.assertRaises(InvalidSpeakerOperationException):
            speaker.connect("iphone")



    def test_disconnect_typical1(self):
        """
        Input:
            device_name: "iphone"
        
        Expected Output: self._connected_to should be set to None
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        speaker.connect("iphone")
        self.assertEquals(speaker.get_connected_to(), "iphone")
        speaker.disconnect()
        self.assertEquals(speaker.get_connected_to(), None)

    def test_disconnect_error1(self):
        """
        Testing case where speaker is not turned on 
        
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)
        self.assertRaises(InvalidSpeakerOperationException, speaker.disconnect)

    def test_disconnect_error2(self):
        """
        Testing case where speaker is on but not connected to a device
        
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)
        speaker.turn_on() 
        with self.assertRaises(InvalidSpeakerOperationException):
            speaker.disconnect()


    
    def test_charge_typical1(self):
        """
        Input: 
            call speaker.charge()

        Expected Output: self._state['charging'] = True 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_state()['charging'], False)
        speaker.charge() 
        self.assertEquals(speaker.get_state()['charging'], True)

    def test_charge_error1(self):
        """
        Input: 
            call speaker.charge() 
            call speaker.charge() again 
            
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)

        speaker.charge() 
        self.assertRaises(InvalidSpeakerOperationException, speaker.charge)

    

    def test_stop_charging_typical1(self): 
        """
        Input:
            call speaker.stop_chargin() 
        
        Excpected Output: self._state['charging'] = False 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)

        speaker.charge() 
        self.assertEquals(speaker.get_state()['charging'], True)
        speaker.stop_charging() 
        self.assertEquals(speaker.get_state()['charging'], False)

    def test_stop_charging_error1(self):
        """
        Testing case where the speaker is already not charging 
        
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)
        self.assertRaises(InvalidSpeakerOperationException, speaker.stop_charging)
        speaker.charge() 
        speaker.stop_charging() 
        self.assertRaises(InvalidSpeakerOperationException, speaker.stop_charging)

    

    def test_play_typical1(self):
        """
        Input: 
            call speaker.play()
            
        Expected Output: currently playing song will resume playing, self._state['playing'] = True 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)

        # Check post conditions 
        speaker.turn_on()
        speaker.play_audio(title="Savage", artist="Aespa", genre="k-pop")
        speaker.pause() 
        self.assertEquals(speaker.get_state()['playing'], False)
        speaker.queue(title="Lucid Dream", artist="Aespa", genre="k-pop")
        speaker.play() 
        self.assertEquals(speaker.get_state()['playing'], True)

    def test_play_typical2(self):
        """
        Input: 
            speaker.queue()
            speaker.play() 
            
        Expected Output: the queued song will play and the 'playing' state will be True
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)

        # Check post behaviors 
        self.assertEquals(speaker.get_state()['playing'], False)
        self.assertEquals(speaker.get_state()['turned_on'], False)
        speaker.turn_on() 
        speaker.queue(title="Next Level", artist="Aespa", genre="k-pop")
        speaker.play() 
        self.assertEquals(speaker.get_currently_playing(), {"title": "next level", "artist": "aespa", "genre": "k-pop"})
        self.assertEquals(speaker.get_state()['playing'], True)
        self.assertEquals(speaker.get_queue(), [])

    def test_play_error1(self):
        """
        Input: 
            speaker.play() when speaker is turned off 
            
        Expected Output: raised InvalidSpeakerOperationException
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)
        self.assertRaises(InvalidSpeakerOperationException, speaker.play)

    def test_play_error2(self):
        """ 
        Input: 
            speaker.play() when speaker is already playing music 
            
        Excpected Output: raise InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        speaker.queue(title="Lucid Dream", artist="Aespa", genre="k-pop")
        speaker.play()
        self.assertEquals(speaker.get_state()['playing'], True)
        self.assertRaises(InvalidSpeakerOperationException, speaker.play)

    

    def test_pause_typical1(self):
        """
        Input: 
            speaker.turn_on() 
            speaker.play_audio() 
            speaker.pause() 
            
        Excpected Behavior: 
            1: self._state['playing'] = False 
            2: self._currently_playing is not changed
        """
        # Create speaker instance 
        speaker = Speaker(name="Jay Park", brand="Sony", model="sbn123", price=50.23, volume=45)

        self.assertIsNotNone(speaker)

        # turn on speaker and set up state
        speaker.turn_on() 
        self.assertEquals(speaker.get_state()['turned_on'], True) 
        speaker.play_audio(title="The Girls", artist="Aespa", genre="k-pop")
        self.assertEquals(speaker.get_currently_playing(), {"title": "the girls", "artist": "aespa", "genre": "k-pop"})
        # check post conditions of calling speaker.pause() 
        speaker.pause() 
        self.assertEquals(speaker.get_state()['playing'], False)
        self.assertEquals(speaker.get_currently_playing(), {"title": "the girls", "artist": "aespa", "genre": "k-pop"})

    def test_pause_error1(self):
        """
        Test the case where the speaker is not turned on 
        
        Excpected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)
        self.assertRaises(InvalidSpeakerOperationException, speaker.pause)

    def test_pause_error2(self):
        """
        Test case where speaker is already not playing audio (ie, paused)
        
        Expected Output: InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        self.assertRaises(InvalidSpeakerOperationException, speaker.pause)

    

    def test_skip_typical1(self): 
        """
        Input: 
            speaker.turn_on()
            speaker.queue()
            speaker.skip() 
        
        Expected Output: currently playing track is the first track in the queue 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        # Turn on speaker and set up state 
        speaker.turn_on() 
        self.assertEquals(speaker.get_state()['turned_on'], True)
        speaker.play_audio(title="Thirsty", artist="Aespa", genre="k-pop")
        self.assertEquals(speaker.get_currently_playing(), {"title": "thirsty", "artist": "aespa", "genre": "k-pop"})
        speaker.queue(title="Yeppi Yeppi", artist="Aespa", genre="k-pop")
        self.assertEquals(speaker.get_queue(), [{"title": "yeppi yeppi", "artist": "aespa", "genre": "k-pop"}])
        # Check post conditions/behavior after calling speaker.skip() 
        speaker.skip() 
        self.assertEquals(speaker.get_currently_playing(), {"title": "yeppi yeppi", "artist": "aespa", "genre": "k-pop"})
        self.assertEquals(speaker.get_queue(), [])
        self.assertEquals(speaker._get_listening_history(), [{"title": "thirsty", "artist": "aespa", "genre": "k-pop"}, {"title": "yeppi yeppi", "artist": "aespa", "genre": "k-pop"}])

    def test_skip_error1(self):
        """
        Test the case where the speaker is not turned on 
        
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        # check for proper rasing of exception 
        self.assertIsNotNone(speaker)
        self.assertRaises(InvalidSpeakerOperationException, speaker.skip)
        
        # check the turn on and then turn off case 
        speaker.turn_on() 
        speaker.play_audio(title="Yeppi Yeppi", artist="Aespa", genre="k-pop")
        speaker.turn_off() 
        self.assertRaises(InvalidSpeakerOperationException, speaker.skip)

    def test_skip_error2(self):
        """
        Test the case where no songs exist the in the queue 
        
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        # turn on speaker 
        speaker.turn_on() 
        # Check for raising of exception 
        with self.assertRaises(InvalidSpeakerOperationException):
            speaker.skip()



    def test_play_audio_typical1(self):
        """
        Input: 
            title = "Yeppi Yeppi"
            artist = "Aespa"
            genre = "k-pop" 

        Expected Output: proper mutation of currently playing and the 'playing' state 
        """
        # create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        # turn on speaker and set up state 
        speaker.turn_on() 
        self.assertEquals(speaker.get_state()['turned_on'], True)
        self.assertEquals(speaker.get_state()['playing'], False)
        # Check post conditions of calling speaker.play_audio() 
        speaker.play_audio(title="Yeppi Yeppi", artist="Aespa", genre="k-pop")
        self.assertEquals(speaker.get_state()['playing'], True)
        self.assertEquals(speaker.get_currently_playing(), {"title": "yeppi yeppi", "artist": "aespa", "genre": "k-pop"})

    def test_play_audio_typical2(self):
        """
        Input: 
            title: "Yatch"
            artist: ["Jay Park", "Sik-k"]
            genre: "k-rnb" 
    

        Expected Output: proper mutation of currently playing and 'playing' state
        and no mutation to the queue
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        # Check inital states of speaker 
        speaker.turn_on() 
        self.assertEquals(speaker.get_state()['turned_on'], True)
        speaker.queue(title="Knife Talk", artist=["Drake", "21 Savage"], genre="rap")
        # Check proper mutation of the currently playing track 
        speaker.play_audio(title="The Girls", artist="Aespa", genre="k-pop")
        self.assertEquals(speaker.get_queue(), [{"title": "knife talk", "artist": ['drake', '21 savage'], "genre": "rap"}])
        self.assertEquals(speaker.get_currently_playing(), {"title": "the girls", "artist": "aespa", "genre": "k-pop"})

    def test_play_audio_unusual1(self):
        """
        Input: 
            title = "  YatcH" 
            artist = "jAy pARK   "
            genre = "k -rap"
            
        Expected Output: self._currently_playing = {'title': 'yatch', 'artist': 'jay park', 'genre': 'k -rap'}
        white space removed, and all lower case characters 
        """
        # Create Speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)
        speaker.turn_on() 
        speaker.play_audio(title="  YatcH", artist="jAy pARK   ", genre="k -rap")
        self.assertEquals(speaker.get_currently_playing(), {'title': 'yatch', 'artist': 'jay park', 'genre': 'k -rap'})

    def test_play_audio_error1(self):
        """
        Test the case where the speaker is turned off 
        
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)
        with self.assertRaises(InvalidSpeakerOperationException):
            speaker.play_audio(title="Lingo", artist="Aespa", genre="k-pop")

    def test_play_audio_error2(self):
        """
        Input:
            title = -1
            artist = "Aespa"
            genre = "k-pop  

        Expected Output: raised TypeError 
        """
        # Create Speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        with self.assertRaises(TypeError):
            speaker.play_audio(title=-1, artist="Aespa", genre="k-pop")

    def test_play_audio_error3(self):
        """
        Input: 
            title = "ICU"
            artist = {}
            genre = "k-pop"
        
        Expected Output: raised TypeError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        with self.assertRaises(TypeError):
            speaker.play_audio(title="ICU", artist={}, genre="k-pop")

    def test_play_audio_error4(self):
        """
        Input: 
            title = "ICU"
            artist = "Aespa"
            genre = 8.0
        
        Expected Output: raised TypeError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertRaises(TypeError, speaker.play_audio(title="ICU", artist="Aespa", genre="8.0"))

    def test_play_audio_error5(self):
        """
        Input: 
            title = ""
            artist = "Aespa"
            genre = "k-pop"
        
        Expected Output: raised ValueError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        with self.assertRaises(ValueError):
            speaker.play_audio(title="", artist="Aespa", genre="k-pop")

    def test_play_audio_error6(self):
        """
        Input: 
            title = "ICU"
            artist = ""
            genre = "k-pop"
        
        Expected Output: raised ValueError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        with self.assertRaises(ValueError):
            speaker.play_audio(title="ICU", artist="", genre="k-pop")

    def test_play_audio_error7(self):
        """
        Input: 
            title = "ICU"
            artist = "Aespa"
            genre = ""
        
        Expected Output: raised ValueError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        with self.assertRaises(ValueError):
            speaker.play_audio(title="ICU", artist="Aespa", genre="")

    def test_play_audio_error8(self):
        """
        Input: 
            title = "ICU"
            artist = ['Aepsa', '']
            genre = "k-pop"

            title = "ICU"
            artist = ['', 'Aespa']
        
        Expected Output: raised ValueError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        with self.assertRaises(ValueError):
            speaker.play_audio(title="ICU", artist=['Aespa', ''], genre="k-pop")
        
        with self.assertRaises(ValueError):
            speaker.play_audio(title="ICU", artist=['', 'Aespa'], genre='k-pop')


    def test_queue_typical1(self):
        """
        Input: 
            title = "All I wanna do" 
            artist = ["Jay Park", "Sik-k"] 
            genre = "k-rnb"
        
        Input: 
            title = "Spicy" 
            artist = "Aespa" 
            genre = "k-pop" 
        
        Expected Output: speaker.get_queue() = [{'title': 'All I wanna do', 'artist': ['Jay Park', 'Sik-k'], 'genre': 'k-rnb'}]
        Expected Output: speaker.get_queue() = [{'title': 'All I wanna do', 'artist': ['Jay Park', 'Sik-k'], 'genre': 'k-rnb'}, {'title': 'Spicy', 'artist': 'Aespa', 'genre': 'k-pop'}]
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        speaker.queue(title="All I wanna do", artist=['Jay Park', 'Sik-k'], genre='k-rnb')
        self.assertEquals(speaker.get_queue(), [{'title': 'all i wanna do', 'artist': ['jay park', 'sik-k'], 'genre': 'k-rnb'}])
        speaker.queue(title="Spicy", artist="Aespa", genre="k-pop")
        self.assertEquals(speaker.get_queue(), [{'title': 'all i wanna do', 'artist': ['jay park', 'sik-k'], 'genre': 'k-rnb'}, {'title': 'spicy', 'artist': 'aespa', 'genre': 'k-pop'}])

    def test_queue_error1(self):
        """
        Input: 
            title = -1
            artist = "Aespa" 
            genre = "k-rnb"
        
        Expected Output: TypeError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        with self.assertRaises(TypeError):
            speaker.queue(title=-1, artist="Aespa", genre="k-rnb")

    def test_queue_error2(self):
        """
        Input: 
            title = "Thirsty"
            artist = ["Aespa", 9]
            genre = "k-rnb" 
        
        Expected Output: raised TypeError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        with self.assertRaises(TypeError):
            speaker.queue(title="Thirsty", artist=["Aepsa", 9], genre="k-rnb")

    def test_queue_error3(self):
        """
        Input:
            title = "Thirsty"
            artist = ['Aepsa', 'Jay Park'] 
            genre = {}
        
        Expected Output: raised TypeError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        with self.assertRaises(TypeError):
            speaker.queue(title="Thirty", artist=['Aespa', 'Jay Park'], genre={})

    def test_queue_error4(self):
        """
        Input: 
            title = "" 
            artist = "Aespa" 
            genre = "k-pop" 
            
        Expected Output: raised ValueError
        """
        # create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        with self.assertRaises(ValueError):
            speaker.queue(title="", artist="Aepsa", genre="k-pop")

    def test_queue_error5(self):
        """
        Input:
            title = "better things"
            artist = ["Aespa", ""]
            genre = "k-pop"
            
        Expected Output: raised ValueError 
        """
        # create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        with self.assertRaises(ValueError):
            speaker.queue(title="better things", artist=['Aepsa', ''], genre='k-pop')

    def test_queue_error6(self):
        """
        Input: 
            title = "better things"
            artist = ""
            genre = "k-pop" 
            
        Expected Output: raised ValueError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        with self.assertRaises(ValueError):
            speaker.queue(title="better things", artist="", genre="k-pop")

    def test_queue_error7(self):
        """
        Input: 
            title = 'Yeppi Yeppi' 
            artist = "Aespa" 
            genre = ""
        
        Expected Output: ValueError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        with self.assertRaises(ValueError):
            speaker.queue(title="Yeppi Yeppi", artist="Aespa", genre="")

    def test_queue_error8(self):
        """
        Test case where the speaker is not turned on 

        Input: 
            title = "Yeppi Yeppi"
            artist = "Aespa" 
            genre = "k-pop"
            
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45)

        self.assertIsNotNone(speaker)
        with self.assertRaises(InvalidSpeakerOperationException):
            speaker.queue(title="Yeppi Yeppi", artist="Aespa", genre="k-pop")

    

    def test_delete_song_from_queue_typical1(self):
        """
        Input: 
            title = "Yeppi Yeppi"
            artist = ["aespa", "jay park"]
            
        Expected Output: the specified queued song will be removed from the queue 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        speaker._set_queue([{ 'title': 'yeppi yeppi', 'artist': ['aespa', 'jay park'], 'genre': 'k-pop' }, { 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])
        self.assertEquals(speaker.get_queue(), [{ 'title': 'yeppi yeppi', 'artist': ['aespa', 'jay park'], 'genre': 'k-pop' }, { 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])
        speaker.delete_song_from_queue(title='yeppi yeppi', artist=['aespa', 'jay park'])
        self.assertEquals(speaker.get_queue(), [{ 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])

    def test_delete_song_from_queue_typical2(self):
        """
        Input: 
            title = "Yeppi Yeppi"
            artist = ["Aespa", "Jay Park "]
            
        Expected Output: the specified queued song will be removed from the queue 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        speaker._set_queue([{ 'title': 'yeppi yeppi', 'artist': ['aespa', 'jay park'], 'genre': 'k-pop' }, { 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])
        self.assertEquals(speaker.get_queue(), [{ 'title': 'yeppi yeppi', 'artist': ['aespa', 'jay park'], 'genre': 'k-pop' }, { 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])
        speaker.delete_song_from_queue(title='yeppi yeppi', artist=['Aespa', 'Jay park '])
        self.assertEquals(speaker.get_queue(), [{ 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])

    def test_delete_song_from_queue_error1(self):
        """
        when the speaker is not turned on

        Input:
            title = "ICU"
            artist = "aespa"
        
        Expected Output: raised InvalidSpeakerOperationException
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)
        with self.assertRaises(InvalidSpeakerOperationException):
            speaker.delete_song_from_queue(title="ICU", artist="aespa")

    def test_delete_song_from_queue_error2(self):
        """
        when the track specified is not in the queue but correct type

        Input:
            title = "ICU"
            artist = "aespa"
        
        Expected Output: raised ValueError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)
        speaker.turn_on()
        speaker._set_queue([{ 'title': 'yeppi yeppi', 'artist': ['aespa', 'jay park'], 'genre': 'k-pop' }, { 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])
        with self.assertRaises(ValueError):
            speaker.delete_song_from_queue(title="ICU", artist="aespa")

    def test_delete_song_from_queue_error3(self):
        """
        Input: 
            title = "ICU"
            artist = ""
        
        Expected Output: raised ValueError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker._set_queue([{ 'title': 'yeppi yeppi', 'artist': ['aespa', 'jay park'], 'genre': 'k-pop' }, { 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])

        speaker.turn_on() 
        with self.assertRaises(ValueError):
            speaker.delete_song_from_queue(title="ICU", artist="")

    def test_delete_song_from_queue_error4(self):
        """
        Input:
            title = ""
            artist = "aespa"
        
        Expected Output: raised ValueError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker._set_queue([{ 'title': 'yeppi yeppi', 'artist': ['aespa', 'jay park'], 'genre': 'k-pop' }, { 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])

        speaker.turn_on()
        with self.assertRaises(ValueError):
            speaker.delete_song_from_queue(title="", artist='aespa')

    def test_delete_song_from_queue_error5(self):
        """
        Input: 
            title = "ICU"
            artist = ['aespa', '', 'Jay park']
            
        Expected Output: raised ValueError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker._set_queue([{ 'title': 'yeppi yeppi', 'artist': ['aespa', 'jay park'], 'genre': 'k-pop' }, { 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])

        speaker.turn_on()
        with self.assertRaises(ValueError):
            speaker.delete_song_from_queue(title="ICU", artist=['aespa', '', 'Jay park'])

    def test_delete_song_from_queue_error6(self):
        """
        Input: 
            title = "ICU"
            artist = {} 
        
        Expected Output: raised TypeError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker._set_queue([{ 'title': 'yeppi yeppi', 'artist': ['aespa', 'jay park'], 'genre': 'k-pop' }, { 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])

        speaker.turn_on() 
        with self.assertRaises(TypeError):
            speaker.delete_song_from_queue(title="ICU", artist={})

    def test_delete_song_from_queue_error7(self):
        """
        Input: 
            title = 9.0
            artist = "aespa"
        
        Expected Output: raised TypeError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker._set_queue([{ 'title': 'yeppi yeppi', 'artist': ['aespa', 'jay park'], 'genre': 'k-pop' }, { 'title': 'ICU', 'artist': "aepspa", 'genre': 'k-pop'}])

        speaker.turn_on() 
        with self.assertRaises(TypeError):
            speaker.delete_song_from_queue(title=8.0, artist="aespa")

    def test_delete_song_from_queue_error8(self):
        """
        Check the case where there are no songs in the queue 

        Input:
            title = "ICU"
            artist = "jay park"

        Expected Output: raised InvalidSpeakerOperationException
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on()
        with self.assertRaises(InvalidSpeakerOperationException):
            speaker.delete_song_from_queue(title="ICU", artist='jay park')

    

    def test_update_information_typical1(self):
        """
        Input: 
            name = "JJK"
        
        Expected Output: speaker with a new name "JJK"
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_name(), "Yeppi")
        speaker.update_information(name="JJK")
        self.assertEquals(speaker.get_name(), "JJK")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "sbn123")
        self.assertEquals(speaker.get_price(), 30.67)

    def test_update_information_typical2(self):
        """
        Input:
            brand = "Bose" 
            
        Expected Output: Speaker with udpated brand 
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_brand(), "JBL")
        speaker.update_information(brand="Bose")
        self.assertEquals(speaker.get_name(), "Yeppi")
        self.assertEquals(speaker.get_brand(), "Bose")
        self.assertEquals(speaker.get_model(), "sbn123")
        self.assertEquals(speaker.get_price(), 30.67)

    def test_update_information_typical3(self):
        """
        Input:
            model = "bsn123" 
            
        Expected Output: Speaker with udpated brand 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_model(), "sbn123")
        speaker.update_information(model="bsn123")
        self.assertEquals(speaker.get_name(), "Yeppi")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "bsn123")
        self.assertEquals(speaker.get_price(), 30.67)

    def test_update_information_typical4(self):
        """
        Input:
            price = 339.99 
            
        Expected Output: Speaker with udpated brand 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_price(), 30.67)
        speaker.update_information(price=339.99)
        self.assertEquals(speaker.get_name(), "Yeppi")
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "sbn123")
        self.assertEquals(speaker.get_price(), 339.99)

    def test_update_information_typical5(self):
        """
        Input: 
            brand = "Sony"
            model = "SBNXm100
            
        Expected Output: speaker with updated information as above
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "sbn123")
        speaker.update_information(brand="Sony", model="SBNXm100")
        self.assertEquals(speaker.get_brand(), "Sony")
        self.assertEquals(speaker.get_model(), "SBNXm100")
    
    def test_update_information_typical6(self):
        """
        Input: 
            brand = "Sony"
            model = "SBNXm100
            price = 10.99
            
        Expected Output: speaker with udpated information as above
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "sbn123")
        self.assertEquals(speaker.get_price(), 30.67)
        speaker.update_information(brand="Sony", model="SBNXm100", price=10.99)
        self.assertEquals(speaker.get_brand(), "Sony")
        self.assertEquals(speaker.get_model(), "SBNXm100")
        self.assertEquals(speaker.get_price(), 10.99)


    def test_update_information_unusual1(self):
        """
        Input: 
            name = " JJK " 
            brand = "  SonY"
            model = " asdf"
        
        Expected Output: updated speaker attributes with trailing white spaces removed
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        self.assertEquals(speaker.get_brand(), "JBL")
        self.assertEquals(speaker.get_model(), "sbn123")
        self.assertEquals(speaker.get_price(), 30.67)
        speaker.update_information(name=" JJK ", brand="  SonY", model=" asdf")
        self.assertEquals(speaker.get_name(), "JJK")
        self.assertEquals(speaker.get_brand(), "SonY")
        self.assertEquals(speaker.get_model(), "asdf")

    def test_update_information_error1(self):
        """
        Input: 
            name = -1
            
        Expected Output: raised TypeError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        with self.assertRaises(TypeError):
            speaker.update_information(name=-1)

    def test_update_information_error2(self):
        """
        Input: 
            brand = [] 
            
        Expected Output: raised TypeError
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        with self.assertRaises(TypeError):
            speaker.update_information(brand=[])

    def test_update_information_error3(self):
        """
        Input:
            model = {}
            
        Expected Output: raised TypeError
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        with self.assertRaises(TypeError):
            speaker.update_information(model={})

    def test_update_information_error4(self):
        """
        Input: 
            price = "str"
        
        Expected Output: raised TypeError
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        with self.assertRaises(TypeError):
            speaker.update_information(price="str")

    def test_update_information_error5(self): 
        """
        Input: 
            name = "" 
            
        Expected Output: raised ValueError
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        with self.assertRaises(ValueError):
            speaker.update_information(name="")

    def test_update_information_error6(self):
        """
        Input: 
            brand = ""
        
        Expected Output: raised ValueError
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        with self.assertRaises(ValueError):
            speaker.update_information(brand="")

    def test_update_information_error7(self):
        """
        Input:
            model = ""
        
        Expected Output: raised ValueError 
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        with self.assertRaises(ValueError):
            speaker.update_information(model="")

    def test_update_information_error8(self):
        """
        Input:
            price = -100.0
            
        Expected Output: raised ValueError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        with self.assertRaises(ValueError):
            speaker.update_information(price=-100.0)
    
    def test_update_information_error9(self):
        """
        Input: 
            name = ""
            price = "str"
        
        Expected Output: raised TypeError
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        with self.assertRaises(TypeError):
            speaker.update_information(name="", price="str")

    def test_update_information_error10(self):
        """
        Input 
            none
            
        Expected Output: raised ValueError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)
        with self.assertRaises(ValueError):
            speaker.update_information()

    

    def test_set_volume_typical1(self):
        """
        Input: 
            volume = 3
        
        Expected Output: volume is changed to 3 
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        speaker.turn_on() 
        self.assertEquals(speaker.get_volume(), 45)
        speaker.set_volume(3)
        self.assertEquals(speaker.get_volume(), 3)

    def test_set_volume_error1(self):
        """
        Input: 
            volume = 100.0
            
        Expected Output: raised TypeError 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        speaker.turn_on() 
        with self.assertRaises(TypeError):
            speaker.set_volume(100.0)

    def test_set_volume_error2(self):
        """
        Input: 
            volume = -100 
            
        Expected Output: raised ValueError 
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        speaker.turn_on() 
        with self.assertRaises(ValueError):
            speaker.set_volume(-100)

    def test_set_volume_error3(self):
        """
        Input:
            volume = 101
            
        Expected Output: raised ValueError 
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        speaker.turn_on() 
        with self.assertRaises(ValueError): 
            speaker.set_volume(101)

    def test_set_volume_error4(self):
        """
        Test case where speaker is not turned on

        Input: 
            volume = 90
            
        Expected Output: raised InvalidSpeakerOperationException 
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        # Check post conditions
        with self.assertRaises(InvalidSpeakerOperationException):
            speaker.set_volume(90)

    

    def test_set_battery_percentage_typical1(self):
        """
        Input: 
            battery_percentage = 34.78
            
        Expected Output: battery_percentage is changed to 34.78
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        self.assertEquals(speaker.get_battery_percentage(), 100)
        speaker.set_battery_percentage(34.78)
        self.assertEquals(speaker.get_battery_percentage(), 34.78)

    def test_set_battery_percentage_error1(self):
        """
        Input: 
            battery_percentage = -34
            
        Expected Outpu: raised TypeError 
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)
        with self.assertRaises(TypeError):
            speaker.set_battery_percentage(-34)

    def test_set_battery_percentage_error2(self):
        """
        Input: 
            battery_percentage = -100.0
            
        Expected Output: raised ValueError 
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)
        with self.assertRaises(ValueError):
            speaker.set_battery_percentage(-100.0)  

    def test_set_battery_percentage_error3(self):
        """
        Input: 
            battery_percentage = 200.0
            
        Expected Output: raised ValueError
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)
        with self.assertRaises(ValueError):
            speaker.set_battery_percentage(200.0)

    


    def test_set_max_battery_life_hours_typical1(self):
        """
        Input: 
            max_battery_percentage_hours = 12.8
            
        Expected Output: max_battery_life_hours is updated to 12.8 
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)
        
        self.assertEquals(speaker.get_max_battery_life_hours(), 8.0)
        speaker.set_max_battery_life_hours(12.8)
        self.assertEquals(speaker.get_max_battery_life_hours(), 12.8)

    def test_set_max_battery_life_hours_error1(self):
        """
        Input: 
            max_battery_life_hours = "str"
            
        Expected Output: raised TypeError
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)
        with self.assertRaises(TypeError):
            speaker.set_max_battery_life_hours("str")

    def test_set_max_battery_life_hours_error2(self):
        """
        Input
            max_battery_life_hours = -100.0
            
        Expected Output: raised ValueError 
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)
        with self.assertRaises(ValueError):
            speaker.set_max_battery_life_hours(-100.0)



    def test_set_equalizer_typical1(self):
        """
        Input: 
            bass = -20
            mids = 3 
            highs = -60 
        
        Expected Output: equalizer changed to the values above 
        """
        # Create speaker instance
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertEquals(speaker.get_equalizer(), {"bass": 0, "mids": 0, "highs": 0})
        speaker.set_equalizer(bass=-20, mids=3, highs=-60)
        self.assertEquals(speaker.get_equalizer(), {"bass": -20, "mids": 3, "highs": -60})

    def test_set_equalizer_typical2(self): 
        """
        Input: 
            bass = 80 
            highs = 20 
        
        Expected Output: equalizer with the above values and mids at 0 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertEquals(speaker.get_equalizer(), {"bass": 0, "mids": 0, "highs": 0})
        speaker.set_equalizer(bass=80, highs=20)
        self.assertEquals(speaker.get_equalizer(), {"bass": 80, "mids": 0, "highs": 20})

    def test_set_equalizer_typical3(self):
        """
        Input: 
            mids = -90
            highs = 20 
        
        Expected Output: equalizer with the above values and mids at 0 
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertEquals(speaker.get_equalizer(), {"bass": 0, "mids": 0, "highs": 0})
        speaker.set_equalizer(mids=-90, highs=20)
        self.assertEquals(speaker.get_equalizer(), {"bass": 0, "mids": -90, "highs": 20})   

    def test_set_equalizer_error1(self):
        """
        Input: 
            none 
            
        Expected Output: raised ValueError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertEquals(speaker.get_equalizer(), {"bass": 0, "mids": 0, "highs": 0})
        with self.assertRaises(ValueError):
            speaker.set_equalizer()

    def test_set_equalizer_error2(self):
        """
        Input: 
            bass = "str"
            
        Expected Output: TypeError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertEquals(speaker.get_equalizer(), {"bass": 0, "mids": 0, "highs": 0})
        with self.assertRaises(TypeError):
            speaker.set_equalizer(bass="str")   

    def test_set_equalizer_error3(self):
        """
        Input: 
            mids = {}
            
        Expected Output: TypeError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertEquals(speaker.get_equalizer(), {"bass": 0, "mids": 0, "highs": 0})
        with self.assertRaises(TypeError):
            speaker.set_equalizer(mids={})

    def test_set_equalizer_error4(self):
        """
        Input: 
            highs = [] 
            
        Expected Output: raised TypeError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertEquals(speaker.get_equalizer(), {"bass": 0, "mids": 0, "highs": 0})
        with self.assertRaises(TypeError):
            speaker.set_equalizer(highs=[])

    def test_set_equalizer_error5(self):
        """
        Input: 
            bass = -101
            
        Expected Output: raised ValueError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertEquals(speaker.get_equalizer(), {"bass": 0, "mids": 0, "highs": 0})
        with self.assertRaises(ValueError):
            speaker.set_equalizer(bass=-101)

    def test_set_equalizer_error6(self):
        """
        Input: 
            mids = 200
            
        Expected Output: raised ValueError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertEquals(speaker.get_equalizer(), {"bass": 0, "mids": 0, "highs": 0})
        with self.assertRaises(ValueError):
            speaker.set_equalizer(mids=200)

    def test_set_equalizer_error7(self):
        """
        Input: 
            highs = 101
            
        Expected Output: raised ValueError
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)

        speaker.turn_on() 
        self.assertEquals(speaker.get_equalizer(), {"bass": 0, "mids": 0, "highs": 0})
        with self.assertRaises(ValueError):
            speaker.set_equalizer(highs=101)

    def test_set_equalizer_error8(self):
        """
        Test the case where the speaker is not turned on

        Input: 
            bass = -40 
            highs = -30 
            mids = 40 
        
        Expected Output: raised InvalidSpeakerOperationException
        """
        # Create speaker instance 
        speaker = Speaker(name="Yeppi", brand="JBL", model="sbn123", price=30.67, volume=45) 

        self.assertIsNotNone(speaker)
        with self.assertRaises(InvalidSpeakerOperationException):
            speaker.set_equalizer(bass=-40, highs=-30, mids=40)