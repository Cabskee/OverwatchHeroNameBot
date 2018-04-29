#!/usr/bin/env python
# -*- coding: utf-8 -*-

import praw
import settings

reddit = praw.Reddit(
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    username=settings.USERNAME,
    password=settings.PASSWORD,
    user_agent=settings.USER_AGENT
)

hero_names = {
  'Pharah': [
    'fara',
    'farah',
    'phara',
    'pharaoh',
    'pharo',
    'pharoh',
  ],
  'McCree': [
    'mcre',
    'mcree',
  ],
  'Moira': [
    'moria',
  ],
  'Brigitte': [
    'baguette',
    'bridgette',
    'brigete',
    'brigette',
    'briggete',
    'briggette',
    'briggite',
    'briggitte',
    'brigite',
  ]
}

if __name__ == '__main__':
  all_wrong_names = []

  for key in hero_names:
    for wrong_name in hero_names[key]:
      all_wrong_names.append(wrong_name)

  for comment in reddit.subreddit(settings.SUBREDDIT).stream.comments(skip_existing=True):
    if comment.author == settings.USERNAME:
      continue

    found_heroes = []
    for wrong_name in all_wrong_names:
      if wrong_name in comment.body.lower():
        for correct_hero in hero_names:
          if wrong_name in hero_names[correct_hero]:
            if correct_hero not in found_heroes:
              found_heroes.append(correct_hero)

    comment.reply('''
I believe you meant to say {}.

----

*Beep, boop. I am a bot created by /u/Cabskee. You can see my source code [here](https://github.com/Cabskee/OverwatchHeroNameBot).*
    '''.format(', '.join(['**' + hero_name + '**' for hero_name in found_heroes])))

