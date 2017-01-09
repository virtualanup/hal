# -*- coding: utf-8 -*-

import re
import random

from hal.library import HalLibrary


class JokeLib(HalLibrary):

    name = "jokes"

    jokeregex = re.compile("((jokes)|(a\s+)?joke)", re.IGNORECASE)
    def init(self):
        pass

    def match(self):
        # Remove "tell" if it exists
        self.match_and_reduce(self.tell)
        if self.match_and_reduce(self.jokeregex):
            # joke matched
            self.match_and_reduce(self.punctuations)
            if len(self.command) == 0:
                self.matched = True

    def get_response(self):
        """
        Tell a joke
        """
        return [random.choice(self.jokes_collection)]


    def help_text(self, text):
        pass

    # Jokes from onelinefun.com
    jokes_collection = [
            "I hate lying people, they're always in my way to the ocean.",
            "My wife and I were happy for twenty years. Then we met.",
            "Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water.",
            "If i had a dollar for every girl that found me unattractive, they would eventually find me attractive.",
            "A recent study has found that women who carry a little extra weight live longer than the men who mention it.",
            "A recent study has found that women who carry a little extra weight live longer than the men who mention it.",
            "I'm great at multitasking. I can waste time, be unproductive, and procrastinate all at once.",
            "Just read that 4,153,237 people got married last year, not to cause any trouble but shouldn't that be an even number?",
            "I find it ironic that the colors red, white, and blue stand for freedom until they are flashing behind you.",
            "Life is like toilet paper, you're either on a roll or taking shit from some asshole.",
            "I want to die peacefully in my sleep, like my grandfather.. Not screaming and yelling like the passengers in his car.",
            "Isn't it great to live in the 21st century? Where deleting history has become more important than making it.",
            "When wearing a bikini, women reveal 90 % of their body... men are so polite they only look at the covered parts.",
            "You know that tingly little feeling you get when you like someone? That's your common sense leaving your body.",
            "My favorite mythical creature? The honest politician.",
            "Relationships are a lot like algebra. Have you ever looked at your X and wondered Y?",
            "I can totally keep secrets. It's the people I tell them to that can't.",
            "When my boss asked me who is the stupid one, me or him? I told him everyone knows he doesn't hire stupid people.",
            "Strong people don't put others down. They lift them up and slam them on the ground for maximum damage.",
            "You know you're ugly when it comes to a group picture and they hand you the camera.",
            "Is your ass jealous of the amount of shit that just came out of your mouth?",
            "Apparently I snore so loudly that it scares everyone in the car I'm driving.",
            "Politicians and diapers have one thing in common. They should both be changed regularly, and for the same reason.",
            "Alcohol is a perfect solvent: It dissolves marriages, families and careers.",
            "You're not fat, you're just... easier to see.",
            "Did you know that dolphins are so smart that within a few weeks of captivity, they can train people to stand on the very edge of the pool and throw them fish?",
            "That awkward moment when you leave a store without buying anything and all you can think is \"act natural, you're innocent\".",
            "I used to think I was indecisive, but now I'm not too sure.",
            "How do I disable the autocorrect function on my wife?",
            "If you can smile when things go wrong, you have someone in mind to blame."
            ]
